# SoundSynthesizer
A project that lets the user play with audios. 
import sys
import os
import tkinter as tk

root = tk.Tk()
root.geometry('1000x1000')
root.configure(bg='indigo')
tk.Label(root,
         text="\n"

         )
tk.Label(root,
         text="\n Welcome \n to the \n Sound Synthesizer",
         fg="fuchsia",
         bg="indigo",
         font="Helvetica 30 bold").pack(side='top')
tk.Label(root,
         text="\n"

         )
tk.Label(root,
         text="\nGroup number 33\n",
         fg="hotpink",
         bg="indigo",
         font="Helvetica 16 bold").pack(side='top')
tk.Label(root,
         text="Drashti Soni         - AU1940058 \nMeghna Kanade  - AU1940134 \nJeenal Shah        - AU1940156 \nHinanshi Suthar  - AU1940266\n",
         fg="lightpink",
         bg="indigo",
         font="Helvetica 10 bold").pack(side='top')
"""
tk.Label(root,
          text="Start synthasizing your sound files \n\n Select any option",
          fg = "antiquewhite",
		 bg = "indigo",
		 font = "Helvetica 16 bold").pack(side = 'top')
"""
flash_delay = 500  # msec between colour change
flash_colours = ('black', 'antiquewhite')  # Two colours to swap between


def flashColour(object, colour_index):
    object.config(foreground=flash_colours[colour_index])
    root.after(flash_delay, flashColour, object, 1 - colour_index)


my_label = tk.Label(root,
                    text="Start synthasizing your sound files \n\n Select any option",
                    font="Helvetica 16 bold",
                    bg="indigo",
                    foreground=flash_colours[0])

my_label.pack()

flashColour(my_label, 0)

tk.Label(root,
         text="\n ",
         fg="black",
         bg="indigo",
         font="Helvetica 10 bold").pack(side='top')


def Resampling():
    os.system('Resample.py')


def ChangePitch():
    os.system('ChangePitch.py')


def ChangeVolume():
    os.system('ChangeVol.py')


def ConcatinateSignals():
    os.system('AddingSignals.py')


def OverlaySignals():
    os.system('OverlaySignals.py')


b1 = tk.Button(root, text="Resampling", fg="black", bg="white", font="Helvetica 10 bold", pady=10, command=Resampling)

b1.pack()
b2 = tk.Button(root, text="Change Pitch", fg="black", bg="white", font="Helvetica 10 bold", pady=10,
               command=ChangePitch)

b2.pack()
b3 = tk.Button(root, text="Change Volume", fg="black", bg="white", font="Helvetica 10 bold", pady=10,
               command=ChangeVolume)

b3.pack()
b4 = tk.Button(root, text="Concatenate two Audio Signals", fg="black", bg="white", font="Helvetica 10 bold", pady=10,
               command=ConcatinateSignals)

b4.pack()
b5 = tk.Button(root, text="Overlay", fg="black", bg="white", font="Helvetica 10 bold", pady=10, command=OverlaySignals)

b5.pack()
root.mainloop()
