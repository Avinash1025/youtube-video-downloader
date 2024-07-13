from pytube import YouTube

link = input("Enter the Video Link here -> ")
ytube = YouTube(link)
print(f'video Tittle -> {ytube.title}')
stream = ytube.streams.filter(progressive=True)

video = list(enumerate(stream))

for i in video:
    print(i)

print("--------------------------------------------------------------------------------------------------------")
index = int(input("Give the index of the disered stream -->"))

stream[index].download()
print("success")




