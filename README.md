# FaiR
Simple Image Face detection using OpenCV


## Detection Modes

### Manual Input (jpg/png)
Uses PySimpleGUI to manually prompt a file to the user and make a new file in the data/output folder. 
This file will always be named "manual_output" and will be replaced each time a new one generates. To convert multiple files it's better to use the Automatic Iteration mode.

To run this, execute the run_manual.py script.

You can customize the shape by changing the input from the auto() method from 'circle' to 'rectangle'.

### Automatic Iteration (jpg/png)
This mode iterates through every file in the data/input path and outputs a copy of every image in data/output. Formatting is {filename}_output

To use this mode, execute the run_auto.py script.

You can customize the shape by changing the input from the auto() method from 'circle' to 'rectangle'.
