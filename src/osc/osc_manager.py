from pythonosc.udp_client import SimpleUDPClient
import ipaddress
import logging
from player.settings_manager import SettingsManager

logger = logging.getLogger(__name__)

class OSCManager:
    """Send OSC messages to VRChat chatbox."""
    def __init__(self, settings: SettingsManager) -> None:
        self.settings = settings

    def send_message(self, character: str, text: str) -> None:
        """Send `/chatbox/input` with [text, True, False] to character's OSC port."""
        ip   = self.settings.get('OSC', f'{character}_ip', fallback=None)
        port = self.settings.get('OSC', f'{character}_port', fallback=None)
        try:
            if not ip or not port:
                raise ValueError("Missing OSC config for %s" % character)
            ipaddress.ip_address(ip)
            client = SimpleUDPClient(ip, int(port))
            client.send_message('/chatbox/input', [text, True, False])
            logger.info("OSC sent to %s:%s -> %s", ip, port, text)
        except Exception as e:
            logger.error("OSC send failed for %s: %s", character, e)