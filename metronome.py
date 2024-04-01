import pygame
import tkinter as tk


# Add missing variable increment_by
increment_by = 0

# Add missing variable increment_every
increment_every = 0

# Initialize pygame
pygame.init()

# Set the path to the sound file
sound_file = "C:/Users/Admin/Python Projects/metronome/env/snare.wav"

# Load the sound file
sound = pygame.mixer.Sound(sound_file)

# Create a flag to control the metronome
running = False

# Create a flag to control the increment
incrementing = False

# Create a new Tkinter window
window = tk.Tk()

# Create a BPM display
bpm_var = tk.IntVar(value=60)
bpm_display = tk.Label(window, textvariable=bpm_var,font=("Helvetica", 16),fg="blue")
bpm_display.pack()

# Create a BPM slider
bpm_scale = tk.Scale(window, from_=20, to=400, orient=tk.HORIZONTAL, variable=bpm_var, state='normal', showvalue=False)
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

# Create the increment function
def increment_bpm():
    if incrementing and bpm_var.get() < 400:
        bpm_var.set(bpm_var.get() + increment_by)
        window.after(increment_every * 1000, increment_bpm)

# Create the increment window
def open_increment_window():
    increment_window = tk.Toplevel(window)
    increment_window.title("Increment BPM")

    increment_by_label = tk.Label(increment_window, text="Increment current tempo by")
    increment_by_label.pack()

    increment_by_entry = tk.Entry(increment_window)
    increment_by_entry.pack()

    increment_every_label = tk.Label(increment_window, text="beats every")
    increment_every_label.pack()

    increment_every_entry = tk.Entry(increment_window)
    increment_every_entry.pack()

    increment_seconds_label = tk.Label(increment_window, text="seconds.")
    increment_seconds_label.pack()

    ok_button = tk.Button(increment_window, text="OK", command=lambda: [globals().update(increment_by=int(increment_by_entry.get()), increment_every=int(increment_every_entry.get()), incrementing=True), increment_window.destroy(), increment_bpm()])
    ok_button.pack()

# Create the Increment button
increment_button = tk.Button(window, text="Increment by", command=open_increment_window)
increment_button.pack()

# Create the Start button
start_button = tk.Button(window, text="Start", command=lambda: [globals().update(running=True), bpm_scale.config(state='normal'), metronome()])
start_button.pack()

# Create the Stop button
stop_button = tk.Button(window, text="Stop", command=lambda: [globals().update(running=False, incrementing=False), bpm_scale.config(state='normal')])
stop_button.pack()

# Start the Tkinter event loop
window.mainloop()

# Clean up pygame
pygame.quit()