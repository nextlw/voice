# 📜 Scripts

Diretório centralizado para todos os scripts do projeto Voice Chat AI.

## 📁 Estrutura

```
scripts/
├── docker/             # Scripts relacionados ao Docker
│   ├── build-local.sh  # Build para Mac ARM64
│   ├── build-render.sh # Build para Render.com
│   └── startup_docker.py # Script Python para Docker
│
├── startup/            # Scripts de inicialização
│   ├── run_server.sh   # Iniciar servidor principal
│   └── start_server.sh # Script alternativo de start
│
└── README.md          # Este arquivo
```

## 🐳 Scripts Docker

### build-local.sh
Build otimizado para Mac M1/M2 (ARM64 nativo).

```bash
./scripts/docker/build-local.sh [image-name] [tag]
```

**Características:**
- Build rápido (2-5 min)
- ARM64 nativo
- PyAudio compilado do fonte
- Para desenvolvimento local

### build-render.sh
Build para deploy no Render.com (linux/amd64).

```bash
./scripts/docker/build-render.sh [image-name] [tag]
```

**Características:**
- Compatível com Render.com
- Plataforma linux/amd64
- Build lento no Mac (emulação)
- Para produção

### startup_docker.py
Script Python auxiliar para configuração Docker.

```bash
python scripts/docker/startup_docker.py
```

## 🚀 Scripts de Inicialização

### run_server.sh
Script principal para iniciar o servidor.

```bash
./scripts/startup/run_server.sh
```

**Funcionalidades:**
- Ativa ambiente virtual
- Configura variáveis de ambiente
- Inicia servidor Uvicorn
- Logs detalhados

### start_server.sh
Script alternativo/simplificado para iniciar servidor.

```bash
./scripts/startup/start_server.sh
```

## 💡 Uso Rápido

### Desenvolvimento Local (Mac)
```bash
# Build Docker
./scripts/docker/build-local.sh

# OU iniciar servidor diretamente
./scripts/startup/run_server.sh
```

### Deploy Render
```bash
# Build para Render
./scripts/docker/build-render.sh

# Push para Docker Hub
docker push voice-chat-ai-render:latest
```

## 🔧 Permissões

Garantir que os scripts tenham permissão de execução:

```bash
# Docker scripts
chmod +x scripts/docker/*.sh

# Startup scripts
chmod +x scripts/startup/*.sh
```

## 📝 Convenções

### Nomenclatura
- Scripts de build: `build-*.sh`
- Scripts de start: `start_*.sh` ou `run_*.sh`
- Scripts auxiliares: `*_helper.py` ou `*_utils.sh`

### Estrutura dos Scripts
1. Shebang apropriado (`#!/bin/bash` ou `#!/usr/bin/env python3`)
2. Comentário descritivo no topo
3. Configuração de erro (`set -e` para bash)
4. Variáveis no topo
5. Funções auxiliares
6. Lógica principal
7. Tratamento de erros

## 🐛 Troubleshooting

### Script não executa
```bash
# Verificar permissões
ls -la scripts/docker/*.sh

# Adicionar permissão
chmod +x scripts/docker/build-local.sh
```

### Erro de caminho
```bash
# Executar da raiz do projeto
cd /path/to/voice-chat-ai
./scripts/docker/build-local.sh
```

### Docker não encontrado
```bash
# Verificar Docker
docker --version

# Iniciar Docker Desktop (Mac)
open -a Docker
```

## 🔗 Documentação Relacionada

- [Docker README](../docker/README.md)
- [Guia de Deployment](../docs/deployment/RENDER.md)
- [Guia Mac](../docs/docker/MAC_GUIDE.md)
- [README Principal](../README.md)

## 📚 Scripts Futuros

Sugestões para novos scripts:
- `test.sh` - Rodar testes automatizados
- `clean.sh` - Limpar cache e arquivos temporários
- `backup.sh` - Backup de configurações
- `deploy.sh` - Automatizar deploy completo
- `setup.sh` - Configuração inicial do projeto

---

*Última atualização: Agosto 2024*