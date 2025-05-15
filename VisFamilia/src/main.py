import asyncio
from pathlib import Path
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtWidgets import QApplication

from player.settings_manager import SettingsManager
from player.audio_manager import AudioManager
from player.audio_capture import AudioCapture
from player.audio_filter import AudioFilter
from player.transcription import Transcription
from player.ui_controller import UIController
from ai.core.squad import SquadManager
from tts.tts_adapter import TTSAdapter
from osc.osc_manager import OSCManager

# High DPI policy
QGuiApplication.setHighDpiScaleFactorRoundingPolicy(
    Qt.HighDpiScaleFactorRoundingPolicy.PassThrough
)


def main() -> None:
    # Initialize Qt
    app = QApplication([])

    # Load config
    settings = SettingsManager(Path('config/settings.ini'))

    # Player pipeline
    audio_mgr     = AudioManager(settings)
    capture       = AudioCapture(settings)
    filter_       = AudioFilter(settings)
    transcription = Transcription(settings)
    osc_mgr       = OSCManager(settings)
    tts           = TTSAdapter(settings)
    ui            = UIController(settings, tts, audio_mgr, transcription)

    # AI squad
    squad = SquadManager([
        'config/lyra.ini', 'config/xyla.ini',
        'config/ayda.ini', 'config/tyfa.ini'
    ])

    # Run UI and AI concurrently
    loop = asyncio.get_event_loop()
    loop.create_task(loop.run_in_executor(None, squad.run))
    ui.run()
    app.exec()


if __name__ == '__main__':
    main()