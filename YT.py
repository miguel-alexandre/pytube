from pytube import YouTube

try:
 print("PyYoutube Downloader by Miguel")
 url = input("Insira o endereço da url  ")
 yt = YouTube(url)

 print("Título: ",yt.title)
 print("Tamanho do video: ",yt.length)

 stream = yt.streams.get_highest_resolution()


 print("Downloading...")
 stream.download()
 print("Download completo!!")
except Exception as e:
     print("Erro:",e)
