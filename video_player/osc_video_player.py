#!/usr/bin/env python3
"""
OSC Video Player
pre-requis: install python-mpv
Lancer avec : python3 osc_video_player.py /chemin/vers/video.mp4

Dans FoxDot:

from .Crashserver.video_player import *
OSCVideo("192.168.1.42")
v0 >> video(vidpos=90, dur=4, rate=2)

"""

import sys
import threading
import time

try:
    import mpv
except ImportError:
    print("Error: pip install python-mpv")
    sys.exit(1)

try:
    from OSC3 import ThreadingOSCServer
except ImportError:
    print("Error: OSC3 not found")
    sys.exit(1)

class SimpleOSCVideoPlayer:
    def __init__(self, video_path=None):
        self.player = mpv.MPV(
            input_default_bindings=True,
            input_vo_keyboard=True,
            keep_open='yes',
            loop='inf',
        )
        
        if video_path:
            print(f"Loading: {video_path}")
            self.player.play(video_path)
            time.sleep(1)
    
    def osc_handler(self, addr, tags, data, client_address):
        # if len(data) < 9:
        #     return
        
        vidpos = float(data[1])
        speed = float(data[2])
        
        try:
            self.player.seek(vidpos, reference='absolute-percent')
        except:
            pass
        
        try:
            # speed_map = {0: 0.0, 1: 1.0, 2: 2.0, 3: 0.5, 4: 4.0, 5: 0.25}
            # speed = speed_map.get(speed, 1.0)
            
            if speed == 0:
                self.player.pause = True
            else:
                self.player.pause = False
                self.player.speed = speed
        except:
            pass
    
    def run(self, port=11111):
        server = ThreadingOSCServer(("0.0.0.0", port))
        server.addMsgHandler("/video", self.osc_handler)
        
        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()
        
        print(f"OSC listening on port {port}")
        
        try:
            while True:
                time.sleep(0.1)
        except KeyboardInterrupt:
            server.close()
            self.player.terminate()

if __name__ == "__main__":
    video = sys.argv[1] if len(sys.argv) > 1 else None
    player = SimpleOSCVideoPlayer(video)
    player.run()
