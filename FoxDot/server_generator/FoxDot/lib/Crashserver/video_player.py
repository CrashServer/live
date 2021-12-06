# A copier dans FoxDot\lib\

from ..OSC3 import *
from ..ServerManager import Server


ipreceiver = "192.168.0.18"

class FilterOSCClient(OSCClient):
        def send(self, message, *args):
                if "video" in str(message.message):
                        OSCClient.send(self, message, *args)

def OSCVideo(video_adress):
        my_client = FilterOSCClient()
        my_client.connect((video_adress, 12345))
        Server.forward = my_client

OSCVideo(ipreceiver)