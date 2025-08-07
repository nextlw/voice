# 🐳 Docker Scripts

Scripts para construção e gerenciamento de imagens Docker.

## 📜 Scripts Disponíveis

### build-local.sh
Constrói imagem Docker otimizada para Mac M1/M2 (ARM64).

**Uso:**
```bash
./scripts/docker/build-local.sh [image-name] [tag]

# Exemplo
./scripts/docker/build-local.sh voice-chat-ai-local latest
```

**Características:**
- ✅ Build nativo ARM64 (rápido: 2-5 min)
- ✅ PyAudio compilado do código-fonte
- ✅ Otimizado para desenvolvimento local
- ❌ Não funciona no Render.com

### build-render.sh
Constrói imagem Docker para deploy no Render.com (linux/amd64).

**Uso:**
```bash
./scripts/docker/build-render.sh [image-name] [tag]

# Exemplo
./scripts/docker/build-render.sh voice-chat-ai-render latest
```

**Características:**
- ✅ Compatível com Render.com
- ✅ Plataforma linux/amd64
- ⚠️ Build lento no Mac (10-20 min - emulação)
- ✅ PyAudio via wheels pré-compiladas

### startup_docker.py
Script Python auxiliar para configurações Docker.

**Uso:**
```bash
python scripts/docker/startup_docker.py
```

**Funcionalidades:**
- Verificação de ambiente Docker
- Configuração de variáveis
- Validação de imagens
- Helpers para containers

## 🎯 Qual Script Usar?

| Situação | Script | Tempo Build (Mac) |
|----------|--------|-------------------|
| Desenvolvimento local | `build-local.sh` | 2-5 min |
| Deploy no Render | `build-render.sh` | 10-20 min |
| CI/CD GitHub Actions | `build-render.sh` | 5-10 min |

## 🔧 Configuração

### Docker Buildx (para Render)
```bash
# Criar builder multi-plataforma
docker buildx create --name multiplatform --use

# Verificar
docker buildx ls
```

### Variáveis de Ambiente
```bash
# Para build local (opcional)
export DOCKER_DEFAULT_PLATFORM=linux/arm64

# Para build Render (opcional)
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

## 📦 Imagens Geradas

### Local (ARM64)
- **Nome**: `voice-chat-ai-local:latest`
- **Tamanho**: ~1.9GB
- **Plataforma**: linux/arm64

### Render (AMD64)
- **Nome**: `voice-chat-ai-render:latest`
- **Tamanho**: ~550MB
- **Plataforma**: linux/amd64

## 🚀 Workflow Completo

### Desenvolvimento Local
```bash
# 1. Build
./scripts/docker/build-local.sh

# 2. Run
docker run -d -p 8000:8000 --env-file .env \
  --name voice-chat-local voice-chat-ai-local:latest

# 3. Logs
docker logs -f voice-chat-local

# 4. Stop
docker stop voice-chat-local && docker rm voice-chat-local
```

### Deploy Render
```bash
# 1. Build
./scripts/docker/build-render.sh

# 2. Tag
docker tag voice-chat-ai-render:latest \
  seu-usuario/voice-chat-ai:latest

# 3. Push
docker push seu-usuario/voice-chat-ai:latest

# 4. Deploy no Render
# Use a URL: docker.io/seu-usuario/voice-chat-ai:latest
```

## 🐛 Troubleshooting

### Build falha
```bash
# Limpar cache Docker
docker system prune -a

# Rebuild sem cache
docker build --no-cache ...
```

### Emulação lenta (Mac)
```bash
# Verificar se usando buildx
docker buildx version

# Verificar plataforma
docker buildx imagetools inspect <image>
```

### Erro de espaço
```bash
# Limpar imagens não usadas
docker image prune -a

# Ver espaço usado
docker system df
```

## 📝 Notas Importantes

1. **Sempre executar da raiz do projeto**
2. **Ter o arquivo .env configurado**
3. **Docker Desktop deve estar rodando**
4. **Para Render, usar sempre linux/amd64**

## 🔗 Links Relacionados

- [Docker README](../../docker/README.md)
- [Dockerfiles](../../docker/)
- [Guia de Deployment](../../docs/deployment/RENDER.md)
- [Guia Mac](../../docs/docker/MAC_GUIDE.md)