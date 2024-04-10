import pygame
import tkinter as tk

# Initialize pygame
pygame.init()

# Set the path to the sound file
sound_file = "C:/Users/Admin/Python Projects/metronome/env/snare.wav"

# Load the sound file
sound = pygame.mixer.Sound(sound_file)

# Create a new Tkinter window
window = tk.Tk()

# Create a BPM display
bpm_var = tk.IntVar(value=60)
bpm_display = tk.Label(window, textvariable=bpm_var,font=("Courier", 16),fg="green")

# Function to increment BPM
def increment_bpm():
    bpm_var.set(min(bpm_var.get() + 1, 400))

# Function to decrement BPM
def decrement_bpm():
    bpm_var.set(max(bpm_var.get() - 1, 20))

# Create increment and decrement buttons
increment_button = tk.Button(window, text=">", command=increment_bpm,relief="raised",bg="lightgreen")
decrement_button = tk.Button(window, text="<", command=decrement_bpm,relief="raised",bg="pink")

# Create a BPM slider
bpm_scale = tk.Scale(window, from_=20, to=400, orient=tk.HORIZONTAL, variable=bpm_var, state='normal', showvalue=False)

# Create a canvas for the animation
canvas = tk.Canvas(window, width=50, height=50)
# canvas.pack()

# Create a circle on the canvas
circle = canvas.create_oval(10, 10, 40, 40, outline='black', fill='gray50', state='hidden',activefill='red',activewidth=2)

# Create a flag to control the metronome
running = False

# Create a flag to control the increment
incrementing = False

# Add missing variable increment_by
increment_by = 0

# Add missing variable increment_every
increment_every = 0

def metronome():
    """Update the metronome function to use the BPM"""
    if running:
        # Play the sound
        sound.play()

        # Show the circle
        canvas.itemconfig(circle, state='normal')

        # Schedule the circle to be hidden after a short delay
        window.after(200, lambda: canvas.itemconfig(circle, state='hidden'))

        # Schedule the next beat
        window.after(int(60000 / bpm_var.get()), metronome)

def increment_bpm():
    """Create the increment function"""
    if incrementing and bpm_var.get() < 400:
        bpm_var.set(bpm_var.get() + increment_by)
        window.after(increment_every * 1000, increment_bpm)

def open_increment_window():
    """Create the increment window"""
    increment_window = tk.Toplevel(window)
    increment_window.title("Increment BPM")

    increment_by_label = tk.Label(increment_window, text="Increment current tempo by")
    increment_by_label.grid(row=0, column=0)

    increment_by_entry = tk.Entry(increment_window)
    increment_by_entry.grid(row=0, column=1)

    increment_every_label = tk.Label(increment_window, text="beats every")
    increment_every_label.grid(row=0, column=2)

    increment_every_entry = tk.Entry(increment_window)
    increment_every_entry.grid(row=0, column=3)

    increment_seconds_label = tk.Label(increment_window, text="seconds.")
    increment_seconds_label.grid(row=0, column=4)

    def on_ok():
        increment_by_str = increment_by_entry.get()
        increment_every_str = increment_every_entry.get()

        if increment_by_str and increment_every_str:
            globals().update(increment_by=int(increment_by_str), increment_every=int(increment_every_str), incrementing=True)
            increment_bpm()
        else:
            globals().update(incrementing=False)

        increment_window.destroy()

    ok_button = tk.Button(increment_window, text="OK", command=on_ok)
    ok_button.grid(row=1, column=0, columnspan=3)

# Arrange the decrement button, slider, increment button, and canvas using grid
bpm_display.grid(row=0, column=0, columnspan=3) # BPM display grid
decrement_button.grid(row=1, column=0)
bpm_scale.grid(row=1, column=1)
increment_button.grid(row=1, column=2)
canvas.grid(row=2, column=0, columnspan=3)

# Create the Increment, Start and Stop buttons
increment_button = tk.Button(window, text="Increment by", command=open_increment_window)

start_button = tk.Button(window, text="Start", command=lambda: [globals().update(running=True), bpm_scale.config(state='normal'), metronome()])

stop_button = tk.Button(window, text="Stop", command=lambda: [globals().update(running=False, incrementing=False), bpm_scale.config(state='normal')])

# Button placements
increment_button.grid(row=3, column=0)
start_button.grid(row=3, column=1)
stop_button.grid(row=3, column=2)

# Start the Tkinter event loop
window.mainloop()

# Clean up pygame
pygame.quit()