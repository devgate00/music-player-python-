from tkinter.constants import RIGHT
import pygame #used to create video games
from PIL import ImageTk, Image
import tkinter as tkr #used to develop GUI
from tkinter.filedialog import askdirectory #it's used for selecting dir 
import os #it permits to interact with the operating system


# create the window of our muisc player and write the prompt 
# command for music seelction 

music_player = tkr.Tk()
music_player.title("Music player By Code with nanami ")
music_player.geometry("550x450")


def loadrelimages(relativepath):

    directory_path = os.path.dirname(__file__)
    file_path = os.path.join(directory_path, relativepath)
    img = ImageTk.PhotoImage(Image.open(file_path.replace('\\',"/")))  
    return img

background_image= loadrelimages('logo.png')

# create a dir that prompts teh user to choose the folder where the 
#music files are listed 

directory =askdirectory()
os.chdir(directory)#allows to change the current dir 

song_list = os.listdir() # returns the list of files song 

# we'll create a variable called play_list  to disply the items 
# for the user 

play_list = tkr.Listbox(music_player,font="Helvetica 12 bold", fg="white",bg= "#ED5564" ,selectmode=tkr.SINGLE, justify=RIGHT)

    pos= 0
    play_list.insert(pos, item)
    pos+1

# we'll use pygame for loading and playing songs 
pygame.init()
pygame.mixer.init()

#let's write functions to control the music player 

def play():
    pygame.mixer.music.load(play_list.get(tkr.ACTIVE))
    var.set(play_list.get(tkr.ACTIVE))
    pygame.mixer.music.play()

def stop():

    pygame.mixer.music.stop()

def pause():
    pygame.mixer.music.pause()

def unpause():
    pygame.mixer.music.unpause()



# we'll create buttons for the interface 
Button1 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold ", text="PLAY", command=play, bg="#AC92EB", fg= "white")
Button2 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="STOP", command=stop, bg="#4FC1E8", fg="white")
Button3 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="PAUSE", command=pause, bg="#A0D568", fg="white")
Button4 = tkr.Button(music_player, width=5, height=3, font="Helvetica 12 bold", text="UNPAUSE", command=unpause, bg="#FFCE54", fg="white")
# let's create a variable that permit to see the song runninng
#on the top of the app

var = tkr.StringVar()
song_title = tkr.Label(music_player, font="Helvetica 12 bold",fg="black",textvariable=var)


#arrange our buttons 

song_title.pack()
Button1.pack(fill="x")
Button2.pack(fill="x")
Button3.pack(fill="x")
Button4.pack(fill="x")

play_list.pack(fill="both",expand="yes")

music_player.mainloop()  # to run the APP
