import cv2
import os

def makeProfile():
    print()
    # confirmation = input("Hello! Welcome to the makeProfile Portal. Can we access your camera to start the facial recognition process (y/n)? ")
    confirmation = input("maam can we use the camera")

    """
    if confirmation == "y":
        print("Camera status: Allowed")
        print()
    
    elif confirmation == "n":
        print("I really don't care.")
        print("Camera status: Allowed")
        print()
    """

    # google method:
    print("thanks. im using the camera")
    print()

    stream = cv2.VideoCapture(0)
    if not stream.isOpened():
        print("sum wrong w yo cam. fix that shi before running ts")

    while True:
        ret, frame = stream.read()  # Capture frame-by-frame
        if not ret:
            print("Error: Could not read frame")
            break

        cv2.imshow('Camera Feed', frame)  # Display the frame

        if cv2.waitKey(1) & 0xFF == ord('q'):  # Exit on 'q' key
            break

    




















def loadProfile():
    pass
















































def main():
    new_old = input("Do you already have a profile with us? ")

    if "y" in new_old.lower():
        loadProfile()

    elif "n" in new_old.lower():
        makeProfile()

    else:
        print("alright")
        exit()

makeProfile()