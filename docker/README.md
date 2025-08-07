# 🐳 Docker Configuration

Este diretório contém todas as configurações Docker para o Voice Chat AI.

## 📁 Estrutura de Arquivos

```
docker/
├── Dockerfile.local        # Para Mac M1/M2 (ARM64 nativo)
├── Dockerfile.render       # Para Render.com (linux/amd64)
├── requirements_local.txt  # Dependências para build local
├── requirements_render.txt # Dependências para Render
├── build-local.sh         # Script para build local
├── build-render.sh        # Script para build Render
└── README.md              # Este arquivo
```

## 🎯 Qual usar?

### Desenvolvimento Local (Mac M1/M2)
```bash
cd voice-chat-ai
./docker/build-local.sh
```
- ✅ Build rápido (2-5 min)
- ✅ Performance nativa
- ✅ Nome da imagem: `voice-chat-ai-local:latest`

### Deploy no Render.com
```bash
cd voice-chat-ai
./docker/build-render.sh
```
- ✅ Compatível com Render.com
- ⚠️ Build lento no Mac (10-20 min - emulação)
- ✅ Nome da imagem: `voice-chat-ai-render:latest`

## 🚀 Comandos Rápidos

### Build e Run Local
```bash
# Build
./docker/build-local.sh

# Run
docker run -d -p 8000:8000 --env-file .env --name voice-chat-local voice-chat-ai-local:latest

# Logs
docker logs -f voice-chat-local

# Stop
docker stop voice-chat-local && docker rm voice-chat-local
```

### Build para Render
```bash
# Build
./docker/build-render.sh

# Tag e Push
docker tag voice-chat-ai-render:latest seu-usuario/voice-chat-ai:latest
docker push seu-usuario/voice-chat-ai:latest
```

## 🧹 Limpeza

### Remover containers
```bash
# Parar e remover container local
docker stop voice-chat-local && docker rm voice-chat-local

# Parar e remover container de teste
docker stop voice-chat-test && docker rm voice-chat-test
```

### Remover imagens
```bash
# Remover imagem local
docker rmi voice-chat-ai-local:latest

# Remover imagem render
docker rmi voice-chat-ai-render:latest

# Remover imagens antigas
docker rmi voice-chat-ai-mac:latest
docker rmi voice-chat-ai-cpu:latest
```

### Limpeza completa
```bash
# Remove todas as imagens não utilizadas
docker image prune -a

# Remove containers parados, networks não usadas, imagens e cache
docker system prune -a
```

## 📊 Diferenças entre Versões

| Aspecto | Local (ARM64) | Render (AMD64) |
|---------|---------------|----------------|
| **Dockerfile** | Dockerfile.local | Dockerfile.render |
| **Requirements** | requirements_local.txt | requirements_render.txt |
| **Build Script** | build-local.sh | build-render.sh |
| **Imagem** | voice-chat-ai-local | voice-chat-ai-render |
| **Plataforma** | linux/arm64 (nativo) | linux/amd64 (emulado) |
| **Tempo Build Mac** | 2-5 min | 10-20 min |
| **PyAudio** | Compilado do fonte | Wheels pré-compiladas |
| **Uso** | Desenvolvimento | Produção |

## ⚠️ Notas Importantes

1. **Sempre use o script correto** para cada situação
2. **Não misture imagens** - local não funciona no Render
3. **O build para Render é lento** no Mac devido à emulação
4. **Mantenha .env atualizado** com suas API keys

## 🔍 Verificação

### Verificar imagens existentes
```bash
docker images | grep voice-chat
```

### Verificar containers rodando
```bash
docker ps | grep voice-chat
```

### Verificar arquitetura da imagem
```bash
docker inspect voice-chat-ai-local:latest | grep Architecture
docker inspect voice-chat-ai-render:latest | grep Architecture
```

## 📚 Documentação Adicional

- [RENDER.md](../docs/deployment/RENDER.md) - Guia completo para Render
- [MAC_GUIDE.md](../docs/docker/MAC_GUIDE.md) - Guia para Mac M1/M2
- [README.md](../README.md) - Documentação principal do projeto