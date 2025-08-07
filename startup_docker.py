#!/usr/bin/env python3
"""
Docker startup script that patches imports before starting the app
"""
import os
import sys

# Set environment variables if not set
os.environ.setdefault('FASTER_WHISPER_LOCAL', 'false')
os.environ.setdefault('TTS_PROVIDER', 'openai')

# Create mock modules for missing dependencies
class MockModule:
    def __init__(self, name):
        self.name = name
    def __getattr__(self, item):
        return lambda *args, **kwargs: None

# Mock the problematic imports
if os.getenv('FASTER_WHISPER_LOCAL', 'false').lower() != 'true':
    sys.modules['faster_whisper'] = MockModule('faster_whisper')
    
if os.getenv('TTS_PROVIDER', 'openai') != 'xtts':
    sys.modules['TTS'] = MockModule('TTS')
    sys.modules['TTS.api'] = MockModule('TTS.api')

# Mock spacy if not available
try:
    import spacy
except ImportError:
    sys.modules['spacy'] = MockModule('spacy')

# Mock coqui-tts dependencies
for module in ['coqpit', 'coqui_tts_trainer', 'gruut', 'monotonic_alignment_search']:
    if module not in sys.modules:
        sys.modules[module] = MockModule(module)

# Now start the actual application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000)