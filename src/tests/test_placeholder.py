from tts.tts_adapter import TTSAdapter
from player.settings_manager import SettingsManager
from pathlib import Path

settings = SettingsManager(Path('config/settings.ini'))
tts = TTSAdapter(settings)
filepath = tts.synthesize("Hello from VisSquad!", "char1")
print("Audio file at:", filepath)
