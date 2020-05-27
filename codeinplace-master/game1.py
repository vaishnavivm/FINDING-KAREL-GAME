import tkinter as tk
from PIL import ImageTk, Image

CANVAS_WIDTH = 800
CANVAS_HEIGHT = 600
def main():
    # Create canvas
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'FIND KAREL')
    # image = tk.PhotoImage(file="images/study02.jpg")
    # Create image, resize it to canvas dimension and put on canvas
    create_image(canvas, "images/study02.jpg")

    # canvas.delete("all")
    # create_image(canvas, "images/study01.jpg")
    # cluePanel = tk.Label(canvas, text = "Hello from Vaishnavi!")
    # cluePanel.pack()
    # Wait
    canvas.mainloop()








def create_image(canvas, imagePath):
    # Loads the image, resizes it to the canvas dimensions
    img = Image.open(imagePath)
    img = img.resize((CANVAS_WIDTH, CANVAS_HEIGHT), Image.ANTIALIAS)
    photoImg = ImageTk.PhotoImage(img)
    canvas.create_image((480, 258, photoImg, tk.NW))
    # panel = tk.Label(canvas, image=photoImg)
    # panel.image = photoImg
    # panel.pack(side="bottom", fill="both", expand="yes")


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



if __name__ == '__main__':
    main()
