import tkinter as tk
import time
from PIL import ImageTk, Image

"""FINDING KAREL GAME
The player needs to find Karel with the clues provided by Karel.
The player needs to click on the object that matches the clue. 
The player has three chances to click on the right object for the whole game. 
If the player clicks wrong objects three times, the game exits and the player has to start over. 
"""
#creating a canvas from tkinter; taken for Chris' checkerboard game
def make_canvas(width, height, title=None):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    objects = {}
    top = tk.Tk()
    top.minsize(width=width, height=height)
    if title:
        top.title(title)
    canvas = tk.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # add this so (0, 0) works correctly
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    return canvas


CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600

#defines correct object's clue coordinates: first four for the first image, second four for image 2 and so on.
#(x1,y1) - Left top and (x2,y2) - Right bottom for each of the clue
CLUE_COORDS = [0,0,800,600,86,140,145,216,153,338,197,377,2,262,801,375,19,255,135,462,0,0,800,600]

#GAMESTATE is dictionary to save current state of the player.
#numlife is the lives or tries a player has
#currentClue is the clue for each image which increments when player chooses the right object
#errorPage is displayed on choosing the wrong object
GAMESTATE = {'numLife' : 3, 'currentClue' : 0, 'errorPage': False}

#Create canvas
canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'FINDING KAREL')

def main():
    # Create image, resize it to canvas dimension and put on canvas
    create_image(canvas, "images/home.jpg")
    canvas.update()

    # adding a mouse click callback; this will get invoked for any click on canvas
    canvas.bind("<Button-1>", mouse_click)
    canvas.pack()

    canvas.mainloop()

"""function mouse_click checks the coordinates of the clues and 
moves the next page or the error page based on the player's mouse click"""
def mouse_click(event):
    if GAMESTATE['errorPage'] == True : #sets the GAMESTATE[errorPage] back to True and displays the current clue page
        if GAMESTATE['numLife'] <=0 :   #if numlife (lives left is less than or equal to 0, exit the game)
            exit()
        else:
            GAMESTATE['errorPage'] = False
            set_image() #Set the current clue back on the canvas
    else:
        if GAMESTATE['currentClue'] == 0 : #if currentClue=0, displays the first image and the coordinates from the first four elements in the list
            x1 = CLUE_COORDS[0]
            y1 = CLUE_COORDS[1]
            x2 = CLUE_COORDS[2]
            y2 = CLUE_COORDS[3]
        if GAMESTATE['currentClue'] == 1 : #if currentClue=1, displays the first image and the coordinates from the 2nd set of four elements in the list
            x1 = CLUE_COORDS[4]
            y1 = CLUE_COORDS[5]
            x2 = CLUE_COORDS[6]
            y2 = CLUE_COORDS[7]
        elif GAMESTATE['currentClue'] == 2 : #if currentClue=2, displays the first image and the coordinates from the 3rd set of four elements in the list
            x1 = CLUE_COORDS[8]
            y1 = CLUE_COORDS[9]
            x2 = CLUE_COORDS[10]
            y2 = CLUE_COORDS[11]
        elif GAMESTATE['currentClue'] == 3 : #if currentClue=3, displays the first image and the coordinates from the 4th set of four elements in the list
            x1 = CLUE_COORDS[12]
            y1 = CLUE_COORDS[13]
            x2 = CLUE_COORDS[14]
            y2 = CLUE_COORDS[15]
        elif GAMESTATE['currentClue'] == 4 :#if currentClue=4, displays the first image and the coordinates from the 5th set of four elements in the list
            x1 = CLUE_COORDS[16]
            y1 = CLUE_COORDS[17]
            x2 = CLUE_COORDS[18]
            y2 = CLUE_COORDS[19]
        elif GAMESTATE['currentClue'] == 5 : #if currentClue=5, displays the first image and the coordinates from the last four elements in the list
            x1 = CLUE_COORDS[20]
            y1 = CLUE_COORDS[21]
            x2 = CLUE_COORDS[22]
            y2 = CLUE_COORDS[23]


        #checks if the selected object falls within the (x1,y1) and (x2,y2) coordinates
        if ((event.x > x1 and event.y > y1) and (event.x < x2 and event.y < y2)):
            print("Yay! You got it!")
            GAMESTATE['currentClue'] += 1  #if currect object selected, increments the currentClue to 1
            canvas.delete("all")
            if GAMESTATE['currentClue'] != 6 and GAMESTATE['currentClue'] != 1:
                create_image(canvas, "images/awesome.jpg") #creates the image if the clues are correct and when the clues are not the first(Intro Screen) and last (ie. 1 and 6)
                canvas.update()
                time.sleep(0.5) #sustains the image for 0.5s)
            set_image()


        else:
            GAMESTATE['numLife'] -= 1  # Reduce the remaining lives
            GAMESTATE['errorPage'] = True # Set the error Page flag and display the number of remaining tries
            if GAMESTATE['numLife'] <= 0:
                create_image(canvas, "images/Sorry.jpg") #displays this image if the player finishes three wrong tries
                canvas.update()


            elif GAMESTATE['numLife'] == 2:
                create_image(canvas, "images/oops.jpg") # If the user has 2 more tries left
                canvas.update()

            elif GAMESTATE['numLife'] == 1:
                create_image(canvas, "images/oops1.jpg") #1 more try left
                canvas.update()

                print("Try again! you have remaining lives - ", GAMESTATE['numLife'])

    # displays on terminal the coordinates of mouse click (for reference)
    print("clicked at", event.x, event.y)

"""Sets an image to nextClueImagePath based on the increment of current clue"""
def set_image():
    if GAMESTATE['currentClue'] == 0:
        nextClueImagePath = 'images/home.png'
    if GAMESTATE['currentClue'] == 1:
        nextClueImagePath = 'images/STUDY.png'
    if GAMESTATE['currentClue'] == 2:
        nextClueImagePath = 'images/BEDROOM.png'
    elif GAMESTATE['currentClue'] == 3:
        nextClueImagePath = 'images/Garden.png'
    elif GAMESTATE['currentClue'] == 4:
        nextClueImagePath = 'images/Kitchen.png'
    elif GAMESTATE['currentClue'] == 5:
        nextClueImagePath = 'images/bakerkarel0.jpg'
    elif GAMESTATE['currentClue'] == 6:
        exit()
    create_image(canvas, nextClueImagePath)


def create_image(canvas, imagePath):
    # Loads the image, resizes it to the canvas dimensions
    img = Image.open(imagePath)
    img = img.resize((CANVAS_WIDTH, CANVAS_HEIGHT), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(img)
    canvas.image = photoImg
    canvas.create_image(0,0,anchor =tk.NW, image = photoImg )


if __name__ == '__main__':
    main()
