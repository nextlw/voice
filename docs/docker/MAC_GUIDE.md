# Docker para Mac M1/M2 (ARM64)

Este guia explica como rodar o Voice Chat AI localmente no seu Mac M1/M2 usando Docker nativo ARM64.

## 📱 Arquivos Específicos para Mac

Para rodar nativamente no Mac ARM64, foram criados arquivos específicos:

- `Dockerfile.mac` - Dockerfile otimizado para ARM64
- `requirements_mac.txt` - Dependências sem PyAudio pré-compilado
- `build-for-mac.sh` - Script de build nativo

## 🚀 Como Usar

### Build Rápido (Nativo ARM64)

```bash
# Dar permissão ao script
chmod +x build-for-mac.sh

# Construir imagem nativa para Mac
./build-for-mac.sh
```

Este build será **MUITO mais rápido** (2-5 minutos) pois roda nativamente sem emulação.

### Rodar o Container

```bash
# Com arquivo .env
docker run -d \
  -p 8000:8000 \
  --env-file .env \
  --name voice-chat-mac \
  voice-chat-ai-mac:latest

# Acessar em
http://localhost:8000
```

## 🎯 Diferenças entre as Versões

### Dockerfile.mac (ARM64 Nativo)
- ✅ Build rápido (2-5 min)
- ✅ Performance nativa no Mac
- ✅ PyAudio compilado do código-fonte
- ❌ Não funciona no Render.com
- 🎯 Para desenvolvimento local

### Dockerfile.cpu (AMD64 para Render)
- ❌ Build lento no Mac (10-20 min com emulação)
- ❌ Performance reduzida no Mac (emulação)
- ✅ PyAudio via wheels pré-compiladas
- ✅ Funciona no Render.com
- 🎯 Para produção/deploy

## 🔧 Solução do PyAudio

O problema do PyAudio no ARM64 foi resolvido de duas formas:

1. **Para Mac (Dockerfile.mac)**:
   - Instala `python3-pyaudio` via apt
   - Compila PyAudio do código-fonte: `pip install pyaudio --no-binary :all:`
   - Funciona nativamente em ARM64

2. **Para Render (Dockerfile.cpu)**:
   - Força build para `linux/amd64`
   - Usa wheels pré-compiladas do PyAudio
   - Requer emulação no Mac durante o build

## 📝 Comandos Úteis

```bash
# Ver logs do container
docker logs -f voice-chat-mac

# Parar container
docker stop voice-chat-mac

# Remover container
docker rm voice-chat-mac

# Limpar imagens antigas
docker image prune -a
```

## ⚠️ Notas Importantes

1. **Uso Local vs Produção**:
   - Use `Dockerfile.mac` para desenvolvimento local
   - Use `Dockerfile.cpu` para deploy no Render

2. **Performance**:
   - Build nativo é 5-10x mais rápido
   - Execução nativa tem melhor performance

3. **Compatibilidade**:
   - Imagem ARM64 não funciona em servidores x86_64
   - Sempre use `build-for-render.sh` para deploy

## 🐛 Troubleshooting

### Container não inicia
```bash
# Verificar logs
docker logs voice-chat-mac

# Verificar se a porta está em uso
lsof -i :8000
```

### Erro de áudio
- Normal em Docker, áudio é redirecionado para null
- Aplicação funciona normalmente via API

### Build falha
```bash
# Limpar cache do Docker
docker system prune -a

# Tentar novamente
./build-for-mac.sh
```

## 📊 Comparação de Tempo de Build

| Método | Tempo | Uso |
|--------|-------|-----|
| `build-for-mac.sh` (ARM64 nativo) | 2-5 min | Desenvolvimento local |
| `build-for-render.sh` (AMD64 emulado) | 10-20 min | Deploy no Render |
| Build direto no Render | 5-10 min | CI/CD automático |

## 🔗 Links Úteis

- [Docker Desktop for Mac](https://docs.docker.com/desktop/mac/install/)
- [Docker Multi-arch](https://docs.docker.com/build/building/multi-platform/)
- [PyAudio Documentation](https://people.csail.mit.edu/hubert/pyaudio/)