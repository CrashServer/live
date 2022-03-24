from OSC3 import *
from tkinter import *
from tkinter import ttk
from threading import *

class ServerGui(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.ipPanel = "localhost"
		self.width=200
		self.height=1000
		self.geometry(f"{self.width}x{self.height}")
		self.title("CrashServer Panel")
		
		self.labelcs = Label(self, text="// CrashServer //")
		self.labelcs.pack(fill="both", expand="yes")
		
		self.frameBpm = LabelFrame(self, text="Bpm : ", padx=10, pady=0)
		self.frameBpm.pack(fill="both", expand="yes")
		self.labelBpm = Label(self.frameBpm, text ="000", font=("Inconsolatas", 17))
		self.labelBpm.pack()
		
		self.frameBeat = LabelFrame(self, text="Beat : ", padx=10, pady=5)
		self.frameBeat.pack(fill="both", expand="yes")
		self.labelBeat4 = Label(self.frameBeat, text ="0/4", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat4.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat8 = Label(self.frameBeat, text ="0/8", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat8.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat16 = Label(self.frameBeat, text ="0/16", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat16.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat32 = Label(self.frameBeat, text ="0/32", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat32.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat64 = Label(self.frameBeat, text ="0/64", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat64.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat128 = Label(self.frameBeat, text ="0/128", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat128.pack(fill="both", expand="yes") ### Joke Aahahahah
		
		
		self.framePlayer = LabelFrame(self, text="Players : ", padx=10, pady=5,  font=("Inconsolatas", 12))
		self.framePlayer.pack(fill="both", expand="yes")
		self.labelPlayer = Label(self.framePlayer, text ="none")
		self.labelPlayer.pack(fill="both", expand="yes")
		
		self.frameHelp = LabelFrame(self, text="Help : ", padx=0, pady=0,  font=("Inconsolatas", 12))
		self.frameHelp.pack(fill="both", expand="yes")
		self.labelHelp = Text(self.frameHelp, wrap=WORD)
		self.scrollbar = ttk.Scrollbar(self.frameHelp, orient='vertical', command=self.labelHelp.yview)
		self.scrollbar.pack(side=RIGHT, fill=Y)
		self.labelHelp.pack(side=LEFT, fill=Y)
		self.labelHelp.config(yscrollcommand=self.scrollbar.set)

		self.oscserver = OSCServer((self.ipPanel,2000))
		self.oscBpm = 0
		self.oscBeat = 0
		self.oscPlayer = []
		
		self.thread = Thread(target = self.start)
		self.thread.daemon = True
		self.thread.start()

	def receiveBpm(self, address, tags, contents, source):
	    self.oscBpm = contents[0]
	    self.labelBpm.config(text=f"{self.oscBpm}")

	def receiveBeat(self, address, tags, contents, source):
	    self.oscBeat = contents[0]
	    self.labelBeat4.config(text=f"{int(self.oscBeat%4)+1}/4")
	    self.labelBeat8.config(text=f"{int(self.oscBeat%8)+1}/8")
	    self.labelBeat16.config(text=f"{int(self.oscBeat%16)+1}/16")
	    self.labelBeat32.config(text=f"{int(self.oscBeat%32)+1}/32")
	    self.labelBeat64.config(text=f"{int(self.oscBeat%64)+1}/64")
	    self.labelBeat128.config(text=f"{int(self.oscBeat%128)+1}/128")

	def receivePlayer(self, address, tags, contents, source):
		self.oscPlayer = contents
		oscString = str('\n'.join(self.oscPlayer))
		self.labelPlayer.config(text=oscString)

	def receiveHelp(self, address, tags, contents, source):
		oscHelp = str(contents[0])
		#self.labelHelp.config(text=oscHelp)
		self.labelHelp.delete(1.0, END)
		self.labelHelp.insert(END, oscHelp)
	    
	def start(self):
		print("Server listening...")
		self.oscserver.addMsgHandler("/panel/bpm", self.receiveBpm)
		self.oscserver.addMsgHandler("/panel/beat", self.receiveBeat)
		self.oscserver.addMsgHandler("/panel/player", self.receivePlayer)
		self.oscserver.addMsgHandler("/panel/help", self.receiveHelp)
		self.oscserver.serve_forever()

if __name__ == "__main__":
	ServerGui().mainloop()
