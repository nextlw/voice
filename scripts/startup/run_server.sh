#!/bin/bash

# Ativar o ambiente conda correto
eval "$(conda shell.bash hook)"
conda activate elias_voice_assistant

# Verificar se o ambiente foi ativado
echo "Ambiente ativo: $CONDA_DEFAULT_ENV"
echo "Python: $(which python)"
echo "Uvicorn: $(which uvicorn)"

# Navegar para o diretório do projeto
cd /Users/williamduarte/voice-chat-ai

# Executar o servidor usando python -m para evitar problemas com o shebang
python -m uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload