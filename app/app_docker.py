"""
Wrapper module for Docker environment - handles conditional imports
"""
import os
import sys

# Check environment variables before importing
FASTER_WHISPER_LOCAL = os.getenv("FASTER_WHISPER_LOCAL", "false").lower() == "true"
TTS_PROVIDER = os.getenv('TTS_PROVIDER', 'openai')

# Mock the modules if not needed
if not FASTER_WHISPER_LOCAL:
    sys.modules['faster_whisper'] = type(sys)('faster_whisper')
    sys.modules['faster_whisper'].WhisperModel = None

if TTS_PROVIDER != 'xtts':
    sys.modules['TTS'] = type(sys)('TTS')
    sys.modules['TTS.api'] = type(sys)('TTS.api')
    sys.modules['TTS.api'].TTS = None

# Now import the actual app
from app import *