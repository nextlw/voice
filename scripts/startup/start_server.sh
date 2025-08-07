#!/bin/bash

# Inicializar conda
source /opt/anaconda3/etc/profile.d/conda.sh

# Ativar o ambiente voice_seu_elias
conda activate voice_seu_elias

# Mudar para o diretório do projeto
cd /Users/williamduarte/voice-chat-ai

# Executar o servidor
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload