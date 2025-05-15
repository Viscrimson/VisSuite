from typing import Any
from player.settings_manager import SettingsManager

class AudioFilter:
    """Apply voice-activity detection to audio chunks."""
    def __init__(self, settings: SettingsManager) -> None:
        self.settings = settings

    def filter_voice(self, audio_chunk: Any) -> Any:
        """Return only voice segments."""
        raise NotImplementedError("audio filtering not implemented yet")