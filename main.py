from tkinter import *
from pygame import mixer
from tkinter import filedialog
root = Tk()
root.title('music player')
root.geometry('600x600')
mixer.init()
# creating playlist
playlist = Listbox(root, bg="black", fg="white", width=60, selectbackground="gray", selectforeground="white")
playlist.pack(pady=20)
#menu
#create menu
my_menu = Menu(root)
root.config(menu=my_menu)
#menu song function declaration:
def delete_song():
    playlist.delete(ANCHOR)
    #stop music if its playing
    mixer.music.stop()

def add_song():
    song= filedialog.askopenfilename(initialdir=r'C:/Users/Aman', title="Choose a song", filetypes= (("mp3 Files", "*.mp3"),))
    playlist.insert(END, song)
#menu options
#add songs
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
add_song_menu.add_command(label="Add one song", command=add_song)
#delete song from menu:
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete a song", command=delete_song)

#btn functions:
#back
def back():
    next= playlist.curselection()
    #add one to current song
    next = next[0]-1
    song = playlist.get(next)
    mixer.music.load(song)
    mixer.music.play(loops=0)
    #clear active selection bar from playlist
    playlist.selection_clear(0, END)
    # pass on active selection bar from playlist
    playlist.activate(next)
    #set actuve bar to next song
    playlist.selection_set(next, last=None)

#forward
def forward():
    next = playlist.curselection()
    #add one to current song
    next = next[0]+1
    song = playlist.get(next)
    mixer.music.load(song)
    mixer.music.play(loops=0)
    #clear active selection bar from playlist
    playlist.selection_clear(0, END)
    # pass on active selection bar from playlist
    playlist.activate(next)
    #set actuve bar to next song
    playlist.selection_set(next, last=None)
#play
def play():
    song = playlist.get(ACTIVE)
    mixer.music.load(song)
    mixer.music.play(loops=0)
#pause'
global paused
paused = False
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        mixer.music.unpause()
        paused = False
    else:
        mixer.music.pause()
        paused = True


#btns position
controls_frame = Frame(root)
controls_frame.pack()
#btns def:
back_btn = Button(controls_frame, text="Back", bg="black", fg="white", command=back)
forward_btn = Button(controls_frame, text="Forward", bg="black", fg="white", command=forward)
play_btn = Button(controls_frame, text="Play", bg="black", fg="white", command=play)
pause_btn = Button(controls_frame, text="Pause", bg="black", fg="white", command=lambda: pause(paused))
#tbn grid:
back_btn.grid(row=0, column=0, padx=10)
forward_btn.grid(row=0, column=2, padx=10)
play_btn.grid(row=0, column=4, padx=10)

root.mainloop()

pause_btn.grid(row=0, column=6, padx=10)