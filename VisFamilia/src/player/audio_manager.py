import sounddevice as sd
from typing import List
from player.settings_manager import SettingsManager

class AudioManager:
    """Enumerate and select audio I/O devices."""
    def __init__(self, settings: SettingsManager) -> None:
        self.settings = settings

    def list_input_devices(self) -> List[str]:
        devices = sd.query_devices()
        return [d['name'] for d in devices if d['max_input_channels'] > 0]

    def list_output_devices(self) -> List[str]:
        devices = sd.query_devices()
        return [d['name'] for d in devices if d['max_output_channels'] > 0]