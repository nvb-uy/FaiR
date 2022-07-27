# Facial Detection using OpenCV and PySimpleGUI
# By gingernikki

## IMPORTS

import PySimpleGUI as UI
import cv2
import os

## GUI STUFF

def selectfilewindow():
    UI.theme('SystemDefault');
    # Default filename text
    filename = 'Select a file to analyze...'
    # Background color of the window
    UI.SetOptions(background_color = '#dbdbdb');
    layout = [
        [UI.FileBrowse('Browse', key='filepath', file_types=(('Image Files', '*.jpg'), ('Image Files', '*.png')), button_color=('black', 'white'), size=8, pad=((0,4),(0,0))), UI.Text(filename, size=20, font=('Helvetica', 8), justification='center')],
        # "Recognize" button in white color
        [UI.Button('Recognize', key='recognize', button_color=('black', 'white'), size=25)],
    ]
    while True:
        # Listen for events
        event, values = UI.Window(title='Facial Detection', layout=layout, finalize=True).read()
        # On the "Recognize" button click
        if event == 'recognize':
            # Return the filepath
            return values['filepath']
        break

def draw(style, fcol, thick, img, w, h, y, x):
    if style == 'rectangle':
        cv2.rectangle(img, (x,y), (x+w,y+h), (fcol, fcol, fcol), thick)
        cv2.putText(img, "Face", (x,y-20), cv2.FONT_HERSHEY_SIMPLEX, 1, (fcol, fcol, fcol), thick)
    elif style == 'circle':
        cv2.circle(img, (x+w//2, y+h//2), w//2, (fcol, fcol, fcol), thick)
        cv2.putText(img, "Face", (x-5,y+25), cv2.FONT_HERSHEY_SIMPLEX, 1, (fcol, fcol, fcol), thick)

## OPENCV STUFF

# Detect faces using cv2 and draw a rectangle around them
def detectfaces(filepath, drawtype):
    img = cv2.imread(filepath)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Load the face detector dataset
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    if drawtype == "circle":
        for (x,y,w,h) in faces:
            draw('circle', 0, 14, img, w, h, y, x); draw('rectangle', 255, 6, img, w, h, y, x)
    elif drawtype == "rectangle":
        for (x,y,w,h) in faces:
            draw('rectangle', 0, 14, img, w, h, y, x); draw('rectangle', 255, 6, img, w, h, y, x)

    # Return the image
    if len(faces) == 0:
        print("Error: No faces detected in the image", filepath)
    else:
        return img

# Display an image with PySimpleGUI

def showimage(img):
    # Show the image
    cv2.imshow('img', img)
    # Wait for a key press
    cv2.waitKey(0)
    # Destroy the window
    cv2.destroyAllWindows()

## RUN MODES

def manual(drawtype):
    # Get file manually
    imgPath = selectfilewindow();
    # Detect faces
    finalImage = detectfaces(imgPath, drawtype);
    # Show the image
    showimage(finalImage);
    # Save the image to a file in the output folder
    # Default output file name and type
    fileName = "manual_output"
    # Get the file type of imgPath
    fileType = imgPath.split('.')[-1]
    # Save the image
    cv2.imwrite('data/output/'+fileName + '.' + fileType, finalImage)

def auto(drawtype):
    # for each file in the input folder (data/input)
        for file in os.listdir('data/input'):
            cPath = 'data/input/' + file
            # Detect faces
            finalImage = detectfaces(cPath, drawtype);
            # Save the image to a file in the output folder
            # Default output file name and type
            fileName = cPath.split('.')[0].split('/')[-1]+"_output"
            fileType = cPath.split('.')[-1]
            # Get the file type of imgPath
            # Save the image
            cv2.imwrite('data/output/'+fileName + '.' + fileType, finalImage)