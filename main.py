from pytube import YouTube

#Provide Link
link = input("Enter the link: ")
yt = YouTube(link)

#Video Title
print("Title: ", yt.title)

#Number of views
print("Number of views: ",yt.views)

#Video Length
print("Length of video: ",yt.length,"seconds")

#Video Description
print("Description: ",yt.description)

#Video Rating
print("Ratings: ",yt.rating)

#Get the highest resolution possible
#ys = yt.streams.get_highest_resolution()

#or

#Select video quality
print(yt.streams.filter(progressive=True))
res = input("Enter the itag number of your desired video quality: ")
ys = yt.streams.get_by_itag(res)

#Input Download Location
download_location = input("Where would you like to download this video? ")

#Start Download
print("Downloading video to " + download_location)
ys.download(download_location)
print("Download complete!")