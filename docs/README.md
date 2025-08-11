# 📚 Documentação Voice Chat AI

Bem-vindo à documentação completa do Voice Chat AI!

## 📁 Estrutura da Documentação

```
docs/
├── README.md           # Este arquivo (índice)
├── games.md           # Documentação dos jogos
├── stories.md         # Documentação das histórias
├── docker/            # Documentação Docker
│   ├── INSTRUCTIONS.md # Instruções gerais Docker
│   └── MAC_GUIDE.md   # Guia específico para Mac M1/M2
└── deployment/        # Guias de deployment
    └── RENDER.md      # Deploy no Render.com
```

## 🚀 Guias Rápidos

### Desenvolvimento Local

1. **[Guia Mac M1/M2](docker/MAC_GUIDE.md)** - Configure Docker no seu Mac ARM64
2. **[Instruções Docker](docker/INSTRUCTIONS.md)** - Comandos e configurações Docker

### Deployment

1. **[Deploy no Render](deployment/RENDER.md)** - Como fazer deploy no Render.com

### Funcionalidades

1. **[Jogos](games.md)** - 15+ jogos interativos com IA
2. **[Histórias](stories.md)** - Aventuras narrativas imersivas

## 🗂️ Arquivos de Configuração

Os arquivos de configuração estão em `/config`:

- `docker-compose.yml` - Configuração Docker Compose
- `environment.yml` - Ambiente Conda

## 🐳 Docker

Todos os arquivos Docker estão em `/docker`:

- `Dockerfile.local` - Para desenvolvimento local (ARM64)
- `Dockerfile.render` - Para deploy no Render (AMD64)
- `build-local.sh` - Script de build local
- `build-render.sh` - Script de build para Render
- `requirements_local.txt` - Dependências locais
- `requirements_render.txt` - Dependências para Render

## 🔗 Links Úteis

### Interno
- [README Principal](../README.md)
- [Docker README](../docker/README.md)

### Externo
- [Render.com](https://render.com)
- [Docker Hub](https://hub.docker.com)
- [PyPI](https://pypi.org)

## 📝 Convenções

### Nomes de Imagens Docker
- **Local**: `voice-chat-ai-local:latest`
- **Render**: `voice-chat-ai-render:latest`

### Estrutura de Pastas
```
voice-chat-ai/
├── app/              # Código da aplicação
├── characters/       # Personagens de IA
├── config/          # Arquivos de configuração
├── docker/          # Configurações Docker
├── docs/            # Documentação
└── outputs/         # Arquivos de saída
```

## 🎯 Início Rápido

### Para Desenvolvimento Local (Mac)
```bash
cd voice-chat-ai
./docker/build-local.sh
docker run -d -p 8000:8000 --env-file .env voice-chat-ai-local:latest
```

### Para Deploy no Render
```bash
cd voice-chat-ai
./docker/build-render.sh
docker push voice-chat-ai-render:latest
```

## 📮 Suporte

Para questões ou problemas:
1. Verifique a documentação relevante
2. Consulte os logs: `docker logs <container-name>`
3. Abra uma issue no GitHub

---

*Última atualização: Agosto 2024*