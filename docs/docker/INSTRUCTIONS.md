# Instruções para Docker - Voice Chat AI

## Arquivos Criados

Criei os seguintes arquivos para facilitar o uso com Docker:

### 1. Dockerfile.simple
- Dockerfile otimizado usando Python 3.10-slim
- Configurado para usar PulseAudio
- Instala todas as dependências do sistema necessárias

### 2. docker-compose-new.yml
- Configuração do docker-compose pronta para uso
- Suporta diferentes sistemas (macOS, Windows WSL2, Linux nativo)
- Monta volumes necessários para áudio e arquivos

### 3. requirements_docker.txt
- Lista mínima de dependências Python para o Docker
- Remove dependências problemáticas que requerem compilação complexa

## Como Usar

### 1. Build da Imagem

```bash
# Build usando o Dockerfile simplificado
docker build -t voice-chat-ai:latest -f Dockerfile.simple .
```

### 2. Executar com Docker Compose

```bash
# Iniciar o container
docker-compose -f docker-compose-new.yml up -d

# Ver logs
docker-compose -f docker-compose-new.yml logs -f

# Parar o container
docker-compose -f docker-compose-new.yml down
```

### 3. Executar com Docker Run (Alternativa)

```bash
# Para macOS/Linux
docker run -d \
  --name voice-chat-ai \
  -p 8000:8000 \
  --env-file .env \
  -v ./outputs:/app/outputs \
  -v ./characters:/app/characters \
  voice-chat-ai:latest

# Para Windows WSL2
docker run -d ^
  --name voice-chat-ai ^
  -p 8000:8000 ^
  --env-file .env ^
  -v %cd%\outputs:/app/outputs ^
  -v %cd%\characters:/app/characters ^
  voice-chat-ai:latest
```

## Acessar a Aplicação

Após iniciar o container, acesse:
- http://localhost:8000

## Observações Importantes

### Credenciais
- As credenciais estão no arquivo `.env`
- **IMPORTANTE**: Verifique e atualize suas API keys antes de usar

### Limitações do Docker
- A versão Docker usa requisitos mínimos para evitar problemas de build
- Algumas funcionalidades que dependem de bibliotecas complexas podem não estar disponíveis:
  - XTTS local (coqui-tts)
  - Faster Whisper local
  - Spacy para processamento de linguagem

### Para Funcionalidade Completa
Se você precisar de todas as funcionalidades, recomendo:
1. Usar o ambiente conda local (elias_voice_assistant)
2. Ou ajustar o Dockerfile para incluir as dependências necessárias

## Ambiente Conda (Alternativa Recomendada)

Se preferir usar o ambiente conda diretamente:

```bash
# Criar ambiente
conda env create -f environment.yml

# Ativar ambiente
conda activate elias_voice_assistant

# Executar aplicação
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Suporte

Se encontrar problemas:
1. Verifique os logs: `docker logs voice-chat-ai`
2. Certifique-se de que as portas não estão em uso
3. Verifique se o Docker tem recursos suficientes alocados