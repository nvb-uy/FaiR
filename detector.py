# Facial Detection using OpenCV and PySimpleGUI
# By gingernikki

import PySimpleGUI as UI
import cv2
import os

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

# Detect faces using cv2 and draw a rectangle around them
def detectfaces(filepath):
    img = cv2.imread(filepath)
    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Load the face detector dataset
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    # Detect faces in the image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Draw rectangle around the faces
    for (x,y,w,h) in faces:
        cv2.circle(img, (x+w//2, y+h//2), w//2, (255,255,255), 3)

    # Return the image
    return img

# Display an image with PySimpleGUI

def showimage(img):
    # Show the image
    cv2.imshow('img', img)
    # set size of the window to a fraction of the size of the image and rescale the image

    
    # Wait for a key press
    cv2.waitKey(0)
    # Destroy the window
    cv2.destroyAllWindows()

def manual():
    # Get file manually
    imgPath = selectfilewindow();
    # Detect faces
    finalImage = detectfaces(imgPath);
    # Show the image
    showimage(finalImage);
    # Save the image to a file in the output folder
    # Default output file name and type
    fileName = "manual_output"
    fileType = imgPath.split('.')[-1]
    # Get the file type of imgPath
    # Save the image
    cv2.imwrite('data/output/'+fileName + '.' + fileType, finalImage)

def auto():
    # for each file in the input folder (data/input)
        for file in os.listdir('data/input'):
            # Get file manually
            cPath = file
            # Detect faces
            finalImage = detectfaces(cPath);
            # Show the image
            showimage(finalImage);
            # Save the image to a file in the output folder
            # Default output file name and type
            fileName = file.name+"_output"
            fileType = cPath.split('.')[-1]
            # Get the file type of imgPath
            # Save the image
            cv2.imwrite('data/output/'+fileName + '.' + fileType, finalImage)