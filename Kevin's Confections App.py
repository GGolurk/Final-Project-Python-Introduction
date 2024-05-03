# Final Project: Kevin's Confections App
# Made by Nathan Merk
# In progress! If anything is missing it's probably because it doesn't exist yet.
# For peer reviewers: If something is missing, feel free to comment on it.

''' This uses breezypythongui to function, I added a '1' at the end to
    differentiate it from identical files in other programs. This will
    probably change before I finish with this project, because it looks
    kinda bad. ''' 

# Importing needed functions from breezypythongui, and tkinter.
from breezypythongui1 import EasyFrame
from breezypythongui1 import EasyRadiobuttonGroup
import tkinter
from tkinter import PhotoImage
from tkinter.font import Font


# The homeWindow class, which acts as the home screen for the app. 
class homeWindow(EasyFrame):
    
    # This is called once when homeWindow is called.
    def __init__(self):
        EasyFrame.__init__(self, title = "Kevin's Confections App: Home", width = 600, height = 400)
        # This creates the label that guides people entering the site.
        self.homeLabel = self.addLabel(text = "Welcome to the online home of Kevin's Creamy Confections, \n where you can order online to skip the line! To place \n your order, simply press the pick up or dine in options, \n depending on which one you want to do. Or, browse the menu \n to see some of our tasty creations!", row = 1, column = 0, sticky = "")
        # Don't mind the Grindel, he's just the image I had on hand. This will be replaced with a self-made brand image.
        # This adds the image (which is a whole lot bigger than I expected)
        self.imageLabel = self.addLabel(text = "", row = 0, column = 0)
        self.brandImage = PhotoImage(file = "Grindel.png")
        self.imageLabel["image"] = self.brandImage
        # This adds the caption for the image, and styles it.
        self.imageText = self.addLabel(text = "Grindel (for now)", row = 0, column = 0, sticky = tkinter.E)
        self.imageText["foreground"] = "blue"
        font = Font(family = "Verdana", slant = "italic")
        self.imageText["font"] = font
        # This adds a button which calls the function openMenu.
        self.menuButton = self.addButton(text = "Menu", row = 2, column = 0, command = self.openMenu)
        self.menuButton.grid(sticky = tkinter.E)
        # This adds a button which calls the function pickUpOrder.
        self.pickUpButton = self.addButton(text = "Pick up", row = 2, column = 0, command = self.pickUpOrder)
        self.pickUpButton.grid(sticky = tkinter.W)
        # This adds a button which calls the function dineInOrder.
        self.dineInButton = self.addButton(text = "Dine in", row = 2, column = 0, command = self.dineInOrder)

    # This opens the menuWindow window, and closes the homeWindow window.
    def openMenu(self):
        # This closes the homeWindow window.
        self.grid_forget()
        # This opens the menuWindow window by giving it the mainloop. 
        menuWindow().mainloop()

    # This tells the program that the user is ordering pick up, and takes them to the order screen.
    def pickUpOrder(self):
        # This closes the homeWindow window.
        self.grid_forget()
        # This opens the orderWindow window by giving it the mainloop.
        orderWindow().mainloop()
        
    # This tells the program that the user is dining in, and takes them to the order screen.
    def dineInOrder(self):
        # This closes the homeWindow window.
        self.grid_forget()
        # This opens the orderWindow window by giving it the mainloop.
        orderWindow().mainloop()
        
# The menuWindow class, which acts as the menu screen for the app.
class menuWindow(EasyFrame):
    
    # This function is called with menuWindow is called.
    def __init__(self):
        # The frame of the menu window.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Menu", width = 400, height = 300)
        # This adds a button which calls the class function exitMenu.
        self.exitMenuButton = self.addButton(text = "Back", row = 1, column = 0, command = self.exitMenu)
        # This adds a text area which contains the menu.
        self.menuTextArea = self.addTextArea(text = "Kevin's Creamy Confections - Menu: \n \n Confection Types: \n  Cone \n  Sundae \n \nConfection Size: \n  One Scoop \n  Two Scoops \n  Three Scoops \n \nToppings: \n  Nuts \n  Chocolate \n  Strawberry Syrup \n  Pineapple Syrup \n  Whipped Cream \n  Sprinkles \n  Sugar Cookies \n  Bananas \n  Chery on Top \n", row = 0, column = 0, width = 1, height = 1)
        # This disables the menu, stopping it from being edited by the user.
        self.menuTextArea.config(state = "disabled")

    # This tells the program to close the menuWindow window and open the homeWindow window.
    def exitMenu(self):
        # This closes the menuWindow window.
        self.grid_forget()
        # The mainloop which runs the window is passed to homeWindow, closing menuWindow.
        homeWindow().mainloop()

# The orderWindow class, which acts as the screeen for when you are ordering something.
class orderWindow(EasyFrame):

    # This runs when orderWindow is triggered.
    def __init__(self):
        # This creates the frame for the orderWindow window.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Order", width = 600, height = 400)
        # This creates a button for confirming your order, which triggers the confirmOrder function.
        self.confirmOrderButton = self.addButton(text = "Confirm", row = 4, column = 0, command = self.confirmOrder)
        # This creates a button for returning home, which triggers the exitOrder functino.
        self.exitOrderButton = self.addButton(text = "Back", row = 4, column = 1, command = self.exitOrder)
        # This is a label which asks the user, cone or sundae?
        self.confectionTypeLabel = self.addLabel(text = "Cone or sundae?", row = 0, column = 0, sticky = "")
        # This creates a radio button group for selecting either cones or sundaes.
        self.confectionTypeRadio = self.addRadiobuttonGroup(row = 1, column = 0)
        # These lines creates radio buttons for the radio button group.
        self.cone = self.confectionTypeRadio.addRadiobutton(text = "Cone")
        self.sundae = self.confectionTypeRadio.addRadiobutton(text = "Sundae")
        # This selects the cone radio button, so that only one button is selected.
        self.confectionTypeRadio.setSelectedButton(self.cone)
        # This creates a label which asks for the size of your confection.
        self.confectionSizeLabel = self.addLabel(text = "How many scoops?", row = 0, column = 1, sticky = "")
        # This creates a radio button grounp for the number of scoops needed.
        self.confectionSizeRadio = self.addRadiobuttonGroup(row = 1, column = 1)
        # These are the radio buttons for scoop size.
        self.single = self.confectionSizeRadio.addRadiobutton(text = "One Scoop")
        self.double = self.confectionSizeRadio.addRadiobutton(text = "Two Scoops")
        self.triple = self.confectionSizeRadio.addRadiobutton(text = "Three Scoops")
        # This selects the single scoop size, as the default selects all radio buttons.
        self.confectionSizeRadio.setSelectedButton(self.single)
        # This creates a label that lists the next 10 check buttons as for toppings.
        self.toppingLabel = self.addLabel(text = "Toppings", row = 2, column = 0, sticky = "")
        # These are ten check buttons which each correspond to one topping (or none). 
        self.noTopping = self.addCheckbutton(text = "None", row = 2, column = 1, sticky = tkinter.SW)
        self.nuts = self.addCheckbutton(text = "Nuts", row = 2, column = 1, sticky = tkinter.SE)
        self.chocolate = self.addCheckbutton(text = "Chocolate", row = 3, column = 0, sticky = tkinter.NW)
        self.strawberrySyrup = self.addCheckbutton(text = "Strawberry Syrup", row = 3, column = 0, sticky = tkinter.NE)
        self.pineappleSyrup = self.addCheckbutton(text = "Pineapple Syrup", row = 3, column = 0, sticky = tkinter.SW)
        self.whippedCream = self.addCheckbutton(text = "Whipped Cream", row = 3, column = 0, sticky = tkinter.SE)
        self.sprinkles = self.addCheckbutton(text = "Sprinkles", row = 3, column = 1, sticky = tkinter.NW)
        self.sugarCookies = self.addCheckbutton(text = "Sugar Cookies", row = 3, column = 1, sticky = tkinter.NE)
        self.bananas = self.addCheckbutton(text = "Bananas", row = 3, column = 1, sticky = tkinter.SW)
        self.cherryTop = self.addCheckbutton(text = "Cherry on Top", row = 3, column = 1, sticky = tkinter.SE)
        # Selects "None" by default.
        self.noTopping.select()

    # This function exits the orderWindow window and returns to the homeWindow.
    def exitOrder(self):
        # This closes the orderWindow window.
        self.grid_forget()
        # Thiw opens the homeWindow window by giving it the mainloop.
        homeWindow().mainloop()

    # This function exits the orderWindow window and places you in the thanksWindow window.
    def confirmOrder(self):
        # This closes the orderWindow window.
        self.grid_forget()
        # This opens the tanksWindow window by giving it the mainloop.
        thanksWindow().mainloop()
        '''If this was an actual thing, I would save the order in this
           function and send it to be used elsewhere.'''
    
# The thanksWindow class, which acts as the "thank you!" screen after you order.
class thanksWindow(EasyFrame):

    # This is triggered when thanksWindow is created.
    def __init__(self):
        # This creates the frame for the thanksWindow window.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Thanks!", width = 400, height = 300)
        # This button sends you back home after thanking you.
        self.returnButton = self.addButton(text = "Return Home", row = 2, column = 0, command = self.returnHome)
        # This adds an image thanking you for being here. Right now it's another Grindel pic.
        self.thanksImage = self.addLabel(text = "", row = 0, column = 0)
        self.image = PhotoImage(file = "Grindel 2.png")
        self.thanksImage["image"] = self.image
        # This adds a caption to the image, and styles it. Right now it's a bit cramped, but once I move the giant freaking Grindel I will have more than enough room.
        self.thanksCaption = self.addLabel(text = "Thanks! (Grindel)", row = 1, column = 0)
        self.thanksCaption["foreground"] = "blue"
        font = Font(family = "Verdana", slant = "italic")
        self.thanksCaption["font"] = font

    # This function closes the thanksWindow window and opens the homeWindow window.
    def returnHome(self):
        # This closes the thanksWindow window.
        self.grid_forget()
        # This opens the homeWindow window by giving it the mainloop.
        homeWindow().mainloop()

# The main() function, which runs at the start of the program.
def main():
    # Calls the homeWindow class, opening the home window.
    homeWindow().mainloop()

# Calls the main() function, starting the program.
if __name__ == "__main__":
    main()
