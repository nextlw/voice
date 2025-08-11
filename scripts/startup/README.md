# 🚀 Scripts de Inicialização

Scripts para iniciar o servidor Voice Chat AI em diferentes modos.

## 📜 Scripts Disponíveis

### run_server.sh
Script principal com configuração completa.

**Características:**
- Ativa ambiente virtual automaticamente
- Carrega variáveis de ambiente (.env)
- Configurações de debug
- Logs detalhados
- Verificação de dependências

**Uso:**
```bash
./scripts/startup/run_server.sh
```

### start_server.sh
Script simplificado para início rápido.

**Características:**
- Início direto do servidor
- Configuração mínima
- Ideal para produção
- Menos verbose

**Uso:**
```bash
./scripts/startup/start_server.sh
```

## ⚙️ Configuração

### Variáveis de Ambiente
Os scripts procuram por `.env` na raiz do projeto:
```bash
cp .env.sample .env
# Editar .env com suas configurações
```

### Porta Padrão
- **Porta**: 8000
- **Host**: 0.0.0.0 (todas as interfaces)
- **URL**: http://localhost:8000

### Customização
Edite os scripts para mudar:
- Porta: `--port 8000`
- Host: `--host 0.0.0.0`
- Workers: `--workers 1`
- Reload: `--reload` (desenvolvimento)

## 🔍 Troubleshooting

### Servidor não inicia
```bash
# Verificar Python
python --version

# Verificar dependências
pip list | grep uvicorn

# Instalar dependências
pip install -r requirements.txt
```

### Porta em uso
```bash
# Verificar porta 8000
lsof -i :8000

# Matar processo
kill -9 <PID>
```

### Permissão negada
```bash
chmod +x scripts/startup/*.sh
```

## 📝 Logs

Os scripts geram logs em:
- Console (stdout/stderr)
- Arquivo: `logs/server.log` (se configurado)

Para logs detalhados:
```bash
export DEBUG=true
./scripts/startup/run_server.sh
```

## 🔗 Links Úteis

- [README Principal](../../README.md)
- [Documentação](../../docs/README.md)
- [Docker Scripts](../docker/)