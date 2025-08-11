# Deploy no Render.com

Este guia explica como fazer o deploy do Voice Chat AI no Render.com usando Docker.

## Problema com Arquiteturas

Se você está desenvolvendo em um Mac M1/M2 (ARM64), precisa construir a imagem Docker para a arquitetura `linux/amd64` que o Render.com utiliza.

## Solução

### Método 1: Usando o Script de Build (Recomendado)

Use o script `build-for-render.sh` que automatiza o processo:

```bash
# Dar permissão de execução
chmod +x build-for-render.sh

# Construir a imagem
./build-for-render.sh voice-chat-ai-render latest
```

### Método 2: Build Manual

```bash
# Criar builder para multi-plataforma (apenas uma vez)
docker buildx create --name multiplatform --use

# Construir para linux/amd64
docker buildx build --platform linux/amd64 -t voice-chat-ai-cpu:latest -f Dockerfile.cpu --load .
```

### Método 3: Configurar Plataforma Padrão

Adicione ao seu `.bashrc` ou `.zshrc`:

```bash
export DOCKER_DEFAULT_PLATFORM=linux/amd64
```

Depois construa normalmente:

```bash
docker build -t voice-chat-ai-cpu -f Dockerfile.cpu .
```

## Deploy no Render

### 1. Push para Docker Hub

```bash
# Fazer login no Docker Hub
docker login

# Tag da imagem
docker tag voice-chat-ai-cpu:latest seu-usuario/voice-chat-ai:latest

# Push para o Docker Hub
docker push seu-usuario/voice-chat-ai:latest
```

### 2. Configurar no Render

1. Crie um novo **Web Service** no Render
2. Escolha **Deploy an existing image from a registry**
3. Use a URL da imagem: `docker.io/seu-usuario/voice-chat-ai:latest`
4. Configure as variáveis de ambiente no painel do Render:
   - Todas as variáveis do arquivo `.env`
   - Especialmente as API keys necessárias

### 3. Configurações Importantes

- **Instance Type**: Escolha pelo menos "Starter" para ter recursos suficientes
- **Health Check Path**: `/` ou `/health` se você implementar
- **Port**: 8000
- **Docker Command**: Deixe em branco (usa o CMD do Dockerfile)

## Notas Importantes

### PyAudio e Dependências

- O PyAudio 0.2.14 tem wheels pré-compiladas para `linux/amd64`
- Não há wheels para ARM64, por isso o erro ao construir localmente no Mac
- Ao construir para `linux/amd64`, o pip consegue instalar normalmente

### Performance

- O build para `linux/amd64` em máquinas ARM64 usa emulação QEMU
- Isso torna o build mais lento (pode levar 10-20 minutos)
- Uma vez construída, a imagem funciona normalmente no Render

### Alternativas

Se o build estiver muito lento:

1. **Use GitHub Actions** para construir a imagem
2. **Use Docker Hub Automated Builds**
3. **Configure um CI/CD** que construa em arquitetura x86_64

## Teste Local

Para testar a imagem localmente (rodará com emulação em ARM64):

```bash
docker run -d \
  -p 8000:8000 \
  --env-file .env \
  --platform linux/amd64 \
  voice-chat-ai-cpu:latest
```

## Troubleshooting

### Erro "no matching distribution found for PyAudio"

- Certifique-se de estar construindo para `linux/amd64`
- Use o script `build-for-render.sh` ou `--platform linux/amd64`

### Build muito lento

- Normal em máquinas ARM64 devido à emulação
- Considere usar CI/CD para construir a imagem

### Erro de memória no Render

- Aumente o tipo de instância no Render
- Otimize o uso de memória no código

## Recursos

- [Docker Multi-platform builds](https://docs.docker.com/build/building/multi-platform/)
- [Render Docker documentation](https://render.com/docs/docker)
- [Docker Hub](https://hub.docker.com/)