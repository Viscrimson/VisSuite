import asyncio
import time
from pathlib import Path
import edge_tts
import logging
from typing import Optional
from player.settings_manager import SettingsManager

logger = logging.getLogger(__name__)

class TTSAdapter:
    """EdgeTTS-based synthesizer with caching."""
    def __init__(self, settings: SettingsManager) -> None:
        self.settings = settings
        self.cache_dir = Path('audio_cache')
        self.cache_dir.mkdir(exist_ok=True)

    def synthesize(self, text: str, character: str) -> Optional[Path]:
        """
        Synthesize text for character, save MP3, return Path or None.
        """
        engine = self.settings.get('TTS', 'engine', fallback='EdgeTTS')
        if engine != 'EdgeTTS':
            raise NotImplementedError(f"Only EdgeTTS supported, got {engine}")

        voice = self.settings.get(character, 'voice_EdgeTTS') or self.settings.get('TTS', 'voice_EdgeTTS', fallback=None)
        if not voice:
            logger.error("No EdgeTTS voice configured for %s", character)
            return None

        filename = self.cache_dir / f"{character}_{int(time.time())}.mp3"
        communicator = edge_tts.Communicator(voice=voice)
        try:
            asyncio.run(communicator.save(text, str(filename)))
            logger.info("Generated TTS for %s: %s", character, filename)
            return filename
        except Exception as e:
            logger.error("EdgeTTS synthesis failed: %s", e)
            return None