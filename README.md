# Metronome

A simple metronome application built with Python.

## Features

- Adjustable beats per minute (BPM) from 20 to 400
- Visual and auditory cues for each beat
- Ability to increment BPM over time (see below)

### Increment BPM Functionality

The metronome includes a feature to increment the BPM over time. This is done by setting an increment value and a time interval. The BPM will increase by the increment value every time the time interval passes. This feature can be accessed by clicking the "Increment by" button, which opens a new window where you can set the increment value and time interval.

## Requirements

- Python 3+
- Tkinter
- Pygame

## Usage

1. Clone this repository.
2. Navigate to the directory containing `metronome.py`.
3. Run `python metronome.py`.

## Controls

- Use the slider to adjust the BPM.
- Use the "<" and ">" buttons to decrease or increase the BPM by 1.
- Use the "Increment by" button to open a window where you can set the metronome to automatically increase the BPM by a certain amount every few seconds.
- Use the "Start" button to start the metronome.
- Use the "Stop" button to stop the metronome.

