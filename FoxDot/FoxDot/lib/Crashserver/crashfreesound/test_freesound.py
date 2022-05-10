import freesound

client = freesound.FreesoundClient()
client.set_token("7IaFlEGP8YbTHRznLTuglsQn8wcrmP3Dz0s3TqgN")

results = client.text_search(query="dubstep",fields="id,name,previews")

for sound in results:
    sound.retrieve_preview(".",sound.name+".mp3")
    print(sound.name)