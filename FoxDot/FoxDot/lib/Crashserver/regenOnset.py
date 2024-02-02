import librosa
import numpy
def regenOnset():
    onsetDict = {}
    for it in os.scandir(FOXDOT_LOOP):
        if it.is_dir():
            for f in os.listdir(it.path):
                if f.endswith(".wav"):
                    x, sr = librosa.load(os.path.join(it, f))
                    onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
                    onsetList = onset_frames.tolist()
                    onsetTime = librosa.frames_to_time(onset_frames)
                    onsetTime = numpy.append(onsetTime, librosa.get_duration(x))
                    onsetDur = []
                    for i,t in enumerate(onsetTime):
                        try:
                            onsetDur.append(round(onsetTime[i+1]-onsetTime[i],3))
                        except:
                            pass
                    onsetDict[os.path.join(f)] = [onsetList, onsetDur]
    with open(os.path.join(FOXDOT_LOOP, "onsetDict.py"), "w") as f:
        json.dump(onsetDict, f)
        print("job done....")
