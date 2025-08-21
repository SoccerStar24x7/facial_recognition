import cv2
import os

def makeProfile():
    pass




def loadProfile()









def main():
    new_old = input("Do you already have a profile with us? ")

    if "y" in new_old.lower():
        loadProfile()

    elif "n" in new_old.lower():
        makeProfile()

    else:
        print("alright")
        exit()