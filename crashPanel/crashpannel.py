from OSC3 import *
from tkinter import *
from tkinter import ttk
from threading import *

class ServerGui(Tk):
	def __init__(self):
		Tk.__init__(self)
		self.ipPanel = "0.0.0.0"
		self.width=200
		self.height=1000
		self.geometry(f"{self.width}x{self.height}")
		self.title("CrashServer Panel")
		img = PhotoImage(file="crashpanel.png")
		self.iconphoto(True, img)
		
		self.labelcs = Label(self, text="// CrashPanel //")
		self.labelcs.pack(fill="both", expand="yes")
		
		self.serverInfo = LabelFrame(self, text="Server Info", padx=10, pady=5)
		self.serverInfo.pack()

		self.frameBpm = LabelFrame(self.serverInfo, text="Bpm: ", padx=5, pady=0)
		self.frameBpm.pack(side=LEFT, fill="both", expand="no")
		self.labelBpm = Label(self.frameBpm, text ="000", font=("Inconsolatas", 15))
		self.labelBpm.pack()
		
		self.frameScale = LabelFrame(self.serverInfo, text="Scale: ", padx=5, pady=0)
		self.frameScale.pack(side=LEFT, fill="both", expand="no")
		self.labelScale = Label(self.frameScale, text ="Major", font=("Inconsolatas", 15))
		self.labelScale.pack()

		self.frameRoot = LabelFrame(self.serverInfo, text="Root: ", padx=5, pady=0)
		self.frameRoot.pack(side=LEFT, fill="both", expand="no")
		self.labelRoot = Label(self.frameRoot, text ="4", font=("Inconsolatas", 15))
		self.labelRoot.pack()
		
		self.frameChrono = LabelFrame(self, text="Crashometre : ", padx=10, pady=0)
		self.frameChrono.pack(fill="both", expand="yes")
		self.labelChrono = Label(self.frameChrono, text ="00:00", font=("Inconsolatas", 15))
		self.labelChrono.pack()

		self.frameVideo = LabelFrame(self, text="Video : ", padx=10, pady=0)
		self.frameVideo.pack(fill="both", expand="yes")
		self.labelVideo = Label(self.frameVideo, text ="Grp 00 || 00/00 - 100%", font=("Inconsolatas", 12))
		self.labelVideo.pack()

		self.frameBeat = LabelFrame(self, text="Beat : ", padx=10, pady=5)
		self.frameBeat.pack(fill="both", expand="yes")
		self.labelBeat8 = Label(self.frameBeat, text ="0/8", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat8.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat16 = Label(self.frameBeat, text ="0/16", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat16.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat32 = Label(self.frameBeat, text ="0/32", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat32.pack(fill="both", expand="yes") ### Joke Aahahahah
		self.labelBeat64 = Label(self.frameBeat, text ="0/64", padx=10, pady=0, font=("Inconsolatas", 15), relief=SUNKEN)
		self.labelBeat64.pack(fill="both", expand="yes") ### Joke Aahahahah
		
		self.framePdj = LabelFrame(self, text="Le Plat du jour est :", padx=10, pady=0,  font=("Inconsolatas", 12))
		self.framePdj.pack(fill="both", expand="yes")
		self.labelPdj = Text(self.framePdj, wrap=WORD, height=3)
		self.labelPdj.pack(fill=X, expand="yes")
		
		self.framePlayer = LabelFrame(self, text="Players : ", padx=10, pady=5,  font=("Inconsolatas", 12))
		self.framePlayer.pack(fill="both", expand="yes")
		self.labelPlayer = Listbox(self.framePlayer)
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
		self.oscScale = "Major"
		self.oscRoot = 0
		self.oscBeat = 0
		self.oscPlayer = []
		
		self.regMinute = re.compile(r'>\s*(\d+)\s*:\s*') ## find minutes in active player

		self.thread = Thread(target = self.start)
		self.thread.daemon = True
		self.thread.start()

	def receiveBpm(self, address, tags, contents, source):
		self.oscBpm = contents[0]
		self.labelBpm.config(text=f"{self.oscBpm}")
	
	def receiveScale(self, address, tags, contents, source):
		self.oscScale = contents[0]
		self.labelScale.config(text=f"{self.oscScale}")

	def receiveRoot(self, address, tags, contents, source):
		self.oscRoot = contents[0]
		self.labelRoot.config(text=f"{self.oscRoot}")

	def receiveBeat(self, address, tags, contents, source):
		self.oscBeat = contents[0]
		self.labelBeat8.config(text=f"{int(self.oscBeat%8)+1}/8")
		self.labelBeat16.config(text=f"{int(self.oscBeat%16)+1}/16")
		self.labelBeat32.config(text=f"{int(self.oscBeat%32)+1}/32")
		self.labelBeat64.config(text=f"{int(self.oscBeat%64)+1}/64")

	def receivePlayer(self, address, tags, contents, source):
		# self.oscPlayer = contents
		self.labelPlayer.delete(0, END)
		if (len(contents) > 0):
			for i in range(len(contents)):
				match = int(self.regMinute.search(contents[i]).group(1))
				if (match >= 5): ### color if player > 5 minutes
					fg = "white"
					bg = "black"
				if (match >= 4): ### color if player > 4 minutes
					fg = "white"
					bg = "red3"
				if (match >= 3): ### color if player > 3 minutes
					fg = "white"
					bg = "firebrick2"
				elif (match >= 2): ### color if player > 1 minutes
					fg = "black"
					bg = "gold"
				elif (match >= 1): ### color if player > 1 minutes
					fg = "black"
					bg = "spring green"
				else: 
					fg = "black"
					bg = "PaleGreen1" 
				self.labelPlayer.insert(END, contents[i])
				self.labelPlayer.itemconfig(i, foreground = fg, background = bg)
		#oscString = str('\n'.join(self.oscPlayer))
		#self.labelPlayer.config(text=oscString)

	def receiveHelp(self, address, tags, contents, source):
		oscHelp = str(contents[0])
		self.labelHelp.delete(1.0, END)
		self.labelHelp.insert(END, oscHelp)

	def receivePdj(self, address, tags, contents, source):
		intitule = str(contents[0])
		plat = str(contents[1])
		self.framePdj.config(text=f'{intitule} du jour')
		self.labelPdj.delete(1.0, END)
		self.labelPdj.insert(END, plat, ("centered",))
		self.labelPdj.tag_configure("centered", justify='center')

	def receiveChrono(self, address, tags, contents, source):
		timeCrash = float(contents[0])
		mins = timeCrash // 60
		sec = timeCrash % 60
		hours = mins // 60
		mins = mins % 60
		self.labelChrono.config(text=f"{int(hours):02d}:{int(mins):02d}:{int(sec):02d}")		
		
	def receiveVideo(self, address, tags, contents, source):
		group = int(contents[0])
		video = int(contents[1])
		total = int(contents[2])
		integrity = 100-int(contents[3])
		if (video == total):
			self.labelVideo.config(bg="red3", fg="white")
		else:
			self.labelVideo.config(bg="#d9d9d9", fg="black")
		self.labelVideo.config(text=f"Grp {group} || {video}/{total} - {integrity}%")

	def start(self):
		print("Server listening...")
		self.oscserver.addMsgHandler("/panel/bpm", self.receiveBpm)
		self.oscserver.addMsgHandler("/panel/scale", self.receiveScale)
		self.oscserver.addMsgHandler("/panel/root", self.receiveRoot)
		self.oscserver.addMsgHandler("/panel/beat", self.receiveBeat)
		self.oscserver.addMsgHandler("/panel/player", self.receivePlayer)
		self.oscserver.addMsgHandler("/panel/help", self.receiveHelp)
		self.oscserver.addMsgHandler("/panel/pdj", self.receivePdj)
		self.oscserver.addMsgHandler("/panel/chrono", self.receiveChrono)
		self.oscserver.addMsgHandler("/panel/video", self.receiveVideo)
		self.oscserver.serve_forever()

if __name__ == "__main__":
	ServerGui().mainloop()
