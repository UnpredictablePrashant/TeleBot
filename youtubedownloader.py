from pytube import YouTube
 
#where to save
SAVE_PATH = "audio/" #to_do
 
#link of the video to be downloaded
link="https://www.youtube.com/watch?v=xWOoBJUqlbI"
 
try:
    #object creation using YouTube which was imported in the beginning
    yt = YouTube(link)
except:
    print("Connection Error") #to handle exception
 
#filters out all the files with "mp4" extension
#mp4files = yt.streams.filter('mp4')
 
#yt.set_filename('GeeksforGeeks Video') #to set the name of the file
 
#get the video with the extension and resolution passed in the get() function
#d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
try:
    #downloading the video
    yt.streams.filter(only_audio=True, file_extension='mp3').order_by('resolution').desc().first().download(SAVE_PATH)
    print('Task Completed!')
except:
    print("Some Error!")


