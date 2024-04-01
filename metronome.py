import pygame
import tkinter as tk
from threading import Thread

# Initialize pygame
pygame.init()

# Set the path to the sound file
sound_file = "C:/Users/Admin/Python Projects/metronome/env/snare.wav"

# Load the sound file
sound = pygame.mixer.Sound(sound_file)

# Create a flag to control the metronome
running = False

# Create a new Tkinter window
window = tk.Tk()

# Create a BPM display
bpm_var = tk.IntVar(value=60)
bpm_display = tk.Label(window, textvariable=bpm_var,font=("Helvetica", 16),fg="blue")
bpm_display.pack()

# Create a BPM slider
bpm_scale = tk.Scale(window, from_=40, to=300, orient=tk.HORIZONTAL, variable=bpm_var, state='normal', showvalue=False)
bpm_scale.pack()

# Create a canvas for the animation
canvas = tk.Canvas(window, width=50, height=50)
canvas.pack()

# Create a circle on the canvas
circle = canvas.create_oval(10, 10, 40, 40, outline='black', fill='black', state='hidden')

# Update the metronome function to use the BPM
def metronome():
    if running:
        # Play the sound
        sound.play()

        # Show the circle
        canvas.itemconfig(circle, state='normal')

        # Schedule the circle to be hidden after a short delay
        window.after(200, lambda: canvas.itemconfig(circle, state='hidden'))

        # Schedule the next beat
        window.after(int(60000 / bpm_var.get()), metronome)


# Create the Start button# Modify the Start button command
start_button = tk.Button(window, text="Start", command=lambda: [globals().update(running=True), bpm_scale.config(state='normal'), metronome()])
start_button.pack()

# Create the Stop button
stop_button = tk.Button(window, text="Stop", command=lambda: [globals().update(running=False), bpm_scale.config(state='normal')])
stop_button.pack()

# Start the Tkinter event loop
window.mainloop()

# Clean up pygame
pygame.quit()