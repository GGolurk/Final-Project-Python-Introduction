# Final Project: Kevin's Confections App
# Made by Nathan Merk
# In progress! If anything is missing it's probably because it doesn't exist yet.

''' This uses breezypythongui to function, I added a '1' at the end to
    differentiate it from identical files in other programs. This will
    probably change before I finish with this project, because it looks
    kinda bad. ''' 

# Importing needed functions from breezypythongui.
from breezypythongui1 import EasyFrame
from breezypythongui1 import EasyRadiobuttonGroup


# The homeWindow class, which acts as the home screen for the app. 
class homeWindow(EasyFrame):
    
    # This is called once when homeWindow is called.
    def __init__(self):
        EasyFrame.__init__(self, title = "Kevin's Confections App: Home", width = 600, height = 400)
        # Add image here
        # This adds a button which calls the function openMenu.
        self.menuButton = self.addButton(text = "Menu", row = 0, column = 3, command = self.openMenu)
        # This adds a button which calls the function pickUpOrder.
        self.pickUpButton = self.addButton(text = "Pick up", row = 0, column = 0, command = self.pickUpOrder)
        # This adds a button which calls the function dineInOrder.
        self.dineInButton = self.addButton(text = "Dine in", row = 0, column = 1, command = self.dineInOrder)

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
        self.exitMenuButton = self.addButton(text = "Back", row = 0, column = 0, command = self.exitMenu)

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
        self.confirmOrderButton = self.addButton(text = "Confirm", row = 0, column = 0, command = self.confirmOrder)
        # This creates a button for returning home, which triggers the exitOrder functino.
        self.exitOrderButton = self.addButton(text = "Back", row = 0, column = 1, command = self.exitOrder)
        # This creates a radio button group for selecting either cones or sundaes.
        self.confectionTypeRadio = self.addRadiobuttonGroup(row = 1, column = 0, rowspan = 2, columnspan = 1)
        # These lines creates radio buttons for the radio button group.
        self.cone = self.confectionTypeRadio.addRadiobutton(text = "Cone")
        self.sundae = self.confectionTypeRadio.addRadiobutton(text = "Sundae")
        # This selects the cone radio button.
        self.confectionTypeRadio.setSelectedButton(self.cone)

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
        self.returnButton = self.addButton(text = "Return Home", row = 0, column = 0, command = self.returnHome)

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
