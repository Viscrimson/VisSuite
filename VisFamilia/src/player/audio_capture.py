import sounddevice as sd
from typing import Callable, Any
from player.settings_manager import SettingsManager

class AudioCapture:
    """Capture raw audio stream from selected device."""
    def __init__(self, settings: SettingsManager) -> None:
        self.settings = settings

    def start_stream(self, callback: Callable[[Any], None]) -> None:
        """Open input stream and pass audio chunks to callback."""
        raise NotImplementedError("audio capture not implemented yet")