"""
Elai Bridge - Integração do Voice Chat AI com o Elai via Nexcode API
"""
import asyncio
import json
import logging
import websockets
from typing import Optional, Dict, Any
from datetime import datetime
import aiohttp

# ANSI colors
PINK = '\033[95m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
NEON_GREEN = '\033[92m'
RESET_COLOR = '\033[0m'

logger = logging.getLogger(__name__)

class ElaiVoiceAgent:
    """
    Agente de voz que conecta o Voice Chat AI com o Elai
    através do Nexcode API Voice Bridge
    """
    
    def __init__(self, nexcode_url: str = "ws://localhost:3002"):
        self.nexcode_url = nexcode_url
        self.ws_connection: Optional[websockets.WebSocketClientProtocol] = None
        self.session_id: Optional[str] = None
        self.is_connected = False
        self.current_task_id: Optional[str] = None
        self.status_callback = None
        
    async def connect(self):
        """Conecta ao Nexcode API Voice Bridge"""
        try:
            self.ws_connection = await websockets.connect(f"{self.nexcode_url}/ws/voice")
            self.is_connected = True
            
            # Aguarda mensagem de boas-vindas
            welcome = await self.ws_connection.recv()
            welcome_data = json.loads(welcome)
            self.session_id = welcome_data.get('sessionId')
            
            print(f"{NEON_GREEN}Conectado ao Elai Voice Bridge!{RESET_COLOR}")
            print(f"Session ID: {self.session_id}")
            
            # Inicia listener de mensagens
            asyncio.create_task(self._message_listener())
            
            return True
            
        except Exception as e:
            logger.error(f"Erro ao conectar ao Voice Bridge: {e}")
            self.is_connected = False
            return False
    
    async def disconnect(self):
        """Desconecta do Voice Bridge"""
        if self.ws_connection:
            await self.ws_connection.close()
            self.is_connected = False
            print(f"{YELLOW}Desconectado do Voice Bridge{RESET_COLOR}")
    
    async def _message_listener(self):
        """Escuta mensagens do Voice Bridge"""
        try:
            while self.is_connected and self.ws_connection:
                message = await self.ws_connection.recv()
                data = json.loads(message)
                
                if data['type'] == 'status_update':
                    await self._handle_status_update(data)
                elif data['type'] == 'speak_response':
                    await self._handle_speak_response(data)
                elif data['type'] == 'command_received':
                    print(f"{CYAN}Comando recebido pelo Elai: {data['command']}{RESET_COLOR}")
                elif data['type'] == 'error':
                    print(f"{PINK}Erro: {data['message']}{RESET_COLOR}")
                    
        except websockets.exceptions.ConnectionClosed:
            print(f"{YELLOW}Conexão com Voice Bridge fechada{RESET_COLOR}")
            self.is_connected = False
        except Exception as e:
            logger.error(f"Erro no listener: {e}")
    
    async def _handle_status_update(self, data: Dict[str, Any]):
        """Processa atualizações de status"""
        status = data.get('status')
        message = data.get('message', '')
        
        print(f"{YELLOW}[Status] {message}{RESET_COLOR}")
        
        # Se houver callback de status, chama
        if self.status_callback:
            await self.status_callback(status, message)
    
    async def _handle_speak_response(self, data: Dict[str, Any]):
        """Processa resposta para síntese de voz"""
        text = data.get('text', '')
        
        # Importa a função de TTS do voice-chat-ai
        try:
            from app import process_and_play
            # Usa o arquivo de áudio do personagem atual
            await process_and_play(text, None)
        except Exception as e:
            logger.error(f"Erro ao sintetizar voz: {e}")
    
    async def send_voice_command(self, transcription: str) -> Optional[str]:
        """Envia comando de voz transcrito para o Elai"""
        if not self.is_connected:
            print(f"{PINK}Não conectado ao Voice Bridge{RESET_COLOR}")
            return None
        
        try:
            # Envia comando
            await self.ws_connection.send(json.dumps({
                'type': 'voice_command',
                'text': transcription,
                'timestamp': datetime.now().isoformat()
            }))
            
            print(f"{CYAN}Comando enviado: {transcription}{RESET_COLOR}")
            
            # Aguarda confirmação
            response = await asyncio.wait_for(self.ws_connection.recv(), timeout=5.0)
            data = json.loads(response)
            
            if data['type'] == 'command_received':
                self.current_task_id = data.get('taskId')
                return self.current_task_id
                
        except asyncio.TimeoutError:
            print(f"{PINK}Timeout ao enviar comando{RESET_COLOR}")
        except Exception as e:
            logger.error(f"Erro ao enviar comando: {e}")
            
        return None
    
    async def check_task_status(self) -> Optional[Dict[str, Any]]:
        """Verifica status da tarefa atual via REST API"""
        if not self.current_task_id:
            return None
        
        try:
            async with aiohttp.ClientSession() as session:
                url = f"http://localhost:3002/api/voice/task/{self.current_task_id}"
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
        except Exception as e:
            logger.error(f"Erro ao verificar status: {e}")
            
        return None
    
    def set_status_callback(self, callback):
        """Define callback para atualizações de status"""
        self.status_callback = callback


class ElaiConversationHandler:
    """
    Handler para conversação integrada com Elai
    """
    
    def __init__(self):
        self.agent = ElaiVoiceAgent()
        self.is_active = False
        
    async def start(self):
        """Inicia a conversação integrada"""
        # Conecta ao Voice Bridge
        connected = await self.agent.connect()
        if not connected:
            print(f"{PINK}Falha ao conectar ao Elai. Verifique se o Voice Bridge está rodando.{RESET_COLOR}")
            return False
        
        self.is_active = True
        
        # Define callback de status que fornece feedback contextual
        async def status_feedback(status: str, message: str):
            # Usa TTS para dar feedback
            if status == 'using_tool':
                from app import process_and_play
                await process_and_play(f"Aguarde, estou {message}", None)
        
        self.agent.set_status_callback(status_feedback)
        
        print(f"{NEON_GREEN}Modo Elai ativado! Fale seus comandos.{RESET_COLOR}")
        return True
    
    async def process_transcription(self, transcription: str) -> str:
        """Processa transcrição enviando para Elai"""
        if not self.is_active:
            return "Modo Elai não está ativo."
        
        # Envia comando para Elai
        task_id = await self.agent.send_voice_command(transcription)
        
        if not task_id:
            return "Erro ao processar comando."
        
        # Aguarda resposta (o Voice Bridge enviará via WebSocket)
        # A resposta será falada automaticamente via _handle_speak_response
        return "Processando..."
    
    async def stop(self):
        """Para a conversação integrada"""
        if self.agent:
            await self.agent.disconnect()
        self.is_active = False
        print(f"{YELLOW}Modo Elai desativado.{RESET_COLOR}")


# Instância global do handler
elai_handler = ElaiConversationHandler()

async def start_elai_mode():
    """Inicia o modo Elai"""
    return await elai_handler.start()

async def stop_elai_mode():
    """Para o modo Elai"""
    await elai_handler.stop()

async def process_elai_command(transcription: str):
    """Processa comando no modo Elai"""
    return await elai_handler.process_transcription(transcription)

# Função para verificar se o Voice Bridge está disponível
async def check_voice_bridge_health():
    """Verifica se o Voice Bridge está rodando"""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get("http://localhost:3002/health") as response:
                if response.status == 200:
                    data = await response.json()
                    return data.get('status') == 'ok'
    except:
        pass
    return False