from pythonosc.dispatcher import Dispatcher
from pythonosc import osc_server
from threading import Thread

# ports to listen on
PORTS = [9000, 9002, 9004, 9006, 9100]

def handle_message(address, *args):
    print(f"[RECEIVED] {address} {args}")

if __name__ == '__main__':
    for port in PORTS:
        disp = Dispatcher()
        disp.map('/chatbox/input', handle_message)
        server = osc_server.ThreadingOSCUDPServer(('0.0.0.0', port), disp)
        print(f"Listening OSC on 0.0.0.0:{port}")
        Thread(target=server.serve_forever, daemon=True).start()
    input("Press Enter to exit.")