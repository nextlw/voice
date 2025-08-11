# ⚙️ Configurações

Este diretório contém todos os arquivos de configuração do projeto.

## 📁 Arquivos

### docker-compose.yml
Configuração para rodar o projeto com Docker Compose. Inclui:
- Configurações de volume para áudio
- Variáveis de ambiente
- Mapeamento de portas
- Opções para diferentes sistemas (WSL2, Mac, Linux)

**Uso:**
```bash
cd config
docker-compose up -d
```

### environment.yml
Ambiente Conda com todas as dependências do projeto. Inclui:
- Python 3.10
- PyTorch e bibliotecas relacionadas
- Dependências de áudio e speech
- APIs e frameworks web

**Uso:**
```bash
conda env create -f config/environment.yml
conda activate elias_voice_assistant
```

## 🔧 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto com base no `.env.sample`:

```bash
cp .env.sample .env
# Edite o .env com suas API keys
```

## 🐳 Docker vs Conda

### Use Docker quando:
- Quiser isolamento completo
- Fazer deploy em produção
- Não quiser instalar dependências localmente

### Use Conda quando:
- Desenvolver localmente
- Precisar de debug mais fácil
- Querer acesso direto ao código

## 📝 Notas

- O `docker-compose.yml` está configurado para usar a imagem do Docker Hub
- Para build local, use os scripts em `/docker`
- O `environment.yml` é usado principalmente para desenvolvimento sem Docker

## 🔗 Documentação Relacionada

- [Docker README](../docker/README.md)
- [Guia de Deployment](../docs/deployment/RENDER.md)
- [Guia Mac](../docs/docker/MAC_GUIDE.md)