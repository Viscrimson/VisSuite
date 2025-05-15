import configparser
from pathlib import Path
from typing import Optional

class SettingsManager:
    """Load, migrate, and persist configuration via INI files."""
    def __init__(self, path: Path) -> None:
        self.path = path
        self.config = configparser.ConfigParser()
        self.load()

    def load(self) -> None:
        if not self.path.exists() or self.path.stat().st_size == 0:
            self.create_defaults()
        else:
            self.config.read(self.path)
        self.migrate()
        self.save()

    def create_defaults(self) -> None:
        self.config['Audio'] = { ... }
        self.config['OSC']   = { ... }
        self.config['TTS']   = { 'engine': 'EdgeTTS' }
        self.config['Names'] = { ... }
        self.config['Defaults'] = { 'default_character': 'char1', 'tts_engine': 'EdgeTTS' }

    def migrate(self) -> None:
        # TODO: add missing sections without overwriting
        pass

    def save(self) -> None:
        with self.path.open('w') as f:
            self.config.write(f)

    def get(self, section: str, option: str, fallback: Optional[str]=None) -> Optional[str]:
        return self.config.get(section, option, fallback=fallback)

    def set(self, section: str, option: str, value: str) -> None:
        if section not in self.config:
            self.config[section] = {}
        self.config[section][option] = value
        self.save()