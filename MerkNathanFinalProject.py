# Final Project: Kevin's Confections App
# Made by Nathan Merk
# Version 1.0, released May 10, 2024.


# Importing needed functions from breezypythongui, and tkinter.
from breezypythongui1 import EasyFrame
from breezypythongui1 import EasyRadiobuttonGroup
import tkinter
from tkinter import PhotoImage
from tkinter.font import Font
# Creating the global "order" variable, which 
order = {}
# Constant cost of all items.
ITEM_COST = {"Cone" : 2.99, "Sundae" : 3.29, "Topping" : 0.59, "Extra Scoop" : 2.49}

# The homeWindow class, which acts as the home screen for the app. 
class homeWindow(EasyFrame):
    
    # This is called once when homeWindow is called.
    def __init__(self):
        # Instantiates the window and frame that the widgets of homeWindow exist in.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Home", width = 600, height = 400, background = "#ffde59")
        # This creates the label that guides people entering the site.
        self.homeLabel = self.addLabel(text = "Welcome to the online home of Kevin's Creamy Confections, \n where you can order online to skip the line! To place \n your order, simply press the pick up or dine in options, \n depending on which one you want to do. Or, browse the menu \n to see some of our tasty creations!", row = 1, column = 0, sticky = "")
        self.homeLabel["background"] = "#ffde59"
        # This creates the logo image for the home window.
        self.imageLabel = self.addLabel(text = "", row = 0, column = 0, sticky = tkinter.N)
        self.brandImage = PhotoImage(file = "KevinLogo.png")
        self.imageLabel["image"] = self.brandImage
        self.imageLabel["background"] = "#ffde59"
        # This adds the caption for the image, and styles it.
        self.imageText = self.addLabel(text = "Kevin's Logo", row = 0, column = 0, sticky = tkinter.S)
        self.imageText["foreground"] = "blue"
        self.imageText["background"] = "#ffde59"
        font = Font(family = "Verdana", slant = "italic", size = 10)
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
        # Creates the global variable "order" which stores the order.
        global order
        order = {"orderType" : "Pick Up Order"}
        # This closes the homeWindow window.
        self.grid_forget()
        # This opens the orderWindow window by giving it the mainloop.
        orderWindow().mainloop()
        
    # This tells the program that the user is dining in, and takes them to the order screen.
    def dineInOrder(self):
        # Creates the global variable "order" which stores the order.
        global order
        order = {"orderType" : "Dine In Order"}
        # This closes the homeWindow window.
        self.grid_forget()
        # This opens the orderWindow window by giving it the mainloop.
        orderWindow().mainloop()
        
# The menuWindow class, which acts as the menu screen for the app.
class menuWindow(EasyFrame):
    
    # This function is called with menuWindow is called.
    def __init__(self):
        # The frame of the menu window.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Menu", width = 400, height = 300, background = "#ffde59")
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
        EasyFrame.__init__(self, title = "Kevin's Confections App: Order", width = 600, height = 400, background = "#ffde59")
        # This creates a button for confirming your order, which triggers the confirmOrder function.
        self.confirmOrderButton = self.addButton(text = "Confirm", row = 4, column = 0, command = self.confirmOrder)
        # This creates a button for returning home, which triggers the exitOrder functino.
        self.exitOrderButton = self.addButton(text = "Back", row = 4, column = 1, command = self.exitOrder)
        # This is a label which asks the user, cone or sundae?
        self.confectionTypeLabel = self.addLabel(text = "Cone or sundae?", row = 0, column = 0, sticky = "")
        self.confectionTypeLabel["background"] = "#ffde59"
        # This creates a radio button group for selecting either cones or sundaes.
        self.confectionTypeRadio = self.addRadiobuttonGroup(row = 1, column = 0)
        # These lines creates radio buttons for the radio button group.
        self.cone = self.confectionTypeRadio.addRadiobutton(text = "Cone")
        self.sundae = self.confectionTypeRadio.addRadiobutton(text = "Sundae")
        # This selects the cone radio button, so that only one button is selected.
        self.confectionTypeRadio.setSelectedButton(self.cone)
        # This creates a label which asks for the size of your confection.
        self.confectionSizeLabel = self.addLabel(text = "How many scoops?", row = 0, column = 1, sticky = "")
        self.confectionSizeLabel["background"] = "#ffde59"
        # This creates a spinbox for the size of your confection.
        self.confectionSizeBox = tkinter.Spinbox(self, from_ = 1, to = 3, width = 10)
        self.confectionSizeBox.config(state = "readonly", justify = "center")
        self.confectionSizeBox.grid(row = 1, column = 1)
        # This creates a label that lists the next 10 check buttons as for toppings.
        self.toppingLabel = self.addLabel(text = "Toppings", row = 2, column = 0, sticky = "")
        self.toppingLabel["background"] = "#ffde59"
        # These are ten check buttons which each correspond to one topping (or none).
        # The noTopping button triggers the noneButton function.
        self.noTopping = self.addCheckbutton(text = "None", row = 2, column = 1, sticky = tkinter.SW, command = self.noneButton)
        # All other check buttons trigger the selectTopping function.
        self.nuts = self.addCheckbutton(text = "Nuts", row = 2, column = 1, sticky = tkinter.SE, command = self.selectTopping)
        self.chocolate = self.addCheckbutton(text = "Chocolate", row = 3, column = 0, sticky = tkinter.NW, command = self.selectTopping)
        self.strawberrySyrup = self.addCheckbutton(text = "Strawberry Syrup", row = 3, column = 0, sticky = tkinter.NE, command = self.selectTopping)
        self.pineappleSyrup = self.addCheckbutton(text = "Pineapple Syrup", row = 3, column = 0, sticky = tkinter.SW, command = self.selectTopping)
        self.whippedCream = self.addCheckbutton(text = "Whipped Cream", row = 3, column = 0, sticky = tkinter.SE, command = self.selectTopping)
        self.sprinkles = self.addCheckbutton(text = "Sprinkles", row = 3, column = 1, sticky = tkinter.NW, command = self.selectTopping)
        self.sugarCookies = self.addCheckbutton(text = "Sugar Cookies", row = 3, column = 1, sticky = tkinter.NE, command = self.selectTopping)
        self.bananas = self.addCheckbutton(text = "Bananas", row = 3, column = 1, sticky = tkinter.SW, command = self.selectTopping)
        self.cherryTop = self.addCheckbutton(text = "Cherry on Top", row = 3, column = 1, sticky = tkinter.SE, command = self.selectTopping)
        # Selects "None" by default.
        self.noTopping.select()
        # Disables "None" so that at least one button will be active at all times.
        self.noTopping.config(state = 'disabled')

    # This function exits the orderWindow window and returns to the homeWindow.
    def exitOrder(self):
        # This closes the orderWindow window.
        self.grid_forget()
        # Thiw opens the homeWindow window by giving it the mainloop.
        homeWindow().mainloop()

    # This function exits the orderWindow window and places you in the thanksWindow window.
    # It also stores your order, and calculates the price.
    def confirmOrder(self):

        # Creates a local cost storing variable.
        totalCost = 0;
        # Adds either a cone or sundae to the order.
        if self.confectionTypeRadio.getSelectedButton() == self.cone:
            order["confectionType"] = "Cone" + "%40s" % str(ITEM_COST["Cone"])
            totalCost += ITEM_COST["Cone"]
        else:
            order["confectionType"] = "Sundae" + "%38s" % str(ITEM_COST["Sundae"])
            totalCost += ITEM_COST["Sundae"]
        # Adds one extra scoop if there are two scoops, and two extra if there are three scoops.
        if self.confectionSizeBox.get() > str(1):
            order["Scoop 2"] = "Second Scoop" + "%32s" % str(ITEM_COST["Extra Scoop"])
            totalCost += ITEM_COST["Extra Scoop"]
            if self.confectionSizeBox.get() > str(2):
                order["Scoop 3"] = "Third Scoop" + "%33s" % str(ITEM_COST["Extra Scoop"])
                totalCost += ITEM_COST["Extra Scoop"]
        # Adds all topings to the order.
        if self.noTopping.isChecked == False:
            if self.nuts.isChecked():
                order["Topping 1"] = "Nuts" + "%40s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.chocolate.isChecked():
                order["Topping 2"] = "Chocolate" + "%35s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.strawberrySyrup.isChecked():
                order["Topping 3"] = "Strawberry Syrup" + "%28s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.pineappleSyrup.isChecked():
                order["Topping 4"] = "Pineapple Syrup" + "%29s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.whippedCream.isChecked():
                order["Topping 5"] = "Whipped Cream" + "%31s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.sprinkles.isChecked():
                order["Topping 6"] = "Sprinkles" + "%35s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.sugarCookies.isChecked():
                order["Topping 7"] = "Sugar Cookies" + "%31s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.bananas.isChecked():
                order["Topping 8"] = "Bananas" + "%37s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
            if self.cherryTop.isChecked():
                order["Topping 9"] = "Cherry On Top" + "%31s" % str(ITEM_COST["Topping"])
                totalCost += ITEM_COST["Topping"]
        # Adds the total cost to the order variable.
        totalCost = "%0.2f" % totalCost
        order["totalCost"] = "Total cost: " + "%32s" % str(totalCost)
            
        # This closes the orderWindow window.
        self.grid_forget()
        # This opens the confirmOrderWindow window by giving it the mainloop.
        confirmOrderWindow().mainloop()

    # Deselects the "None" button if any toppings are selected.
    def selectTopping(self):
        # Deselects the "None" button.
        self.noTopping.deselect()
        # Enables the none button.
        self.noTopping.config(state = 'normal')

    # Deselects all toppings when "None" is selected.
    def noneButton(self):
        # Deselects all topping buttons.
        self.nuts.deselect()
        self.chocolate.deselect()
        self.strawberrySyrup.deselect()
        self.pineappleSyrup.deselect()
        self.whippedCream.deselect()
        self.sprinkles.deselect()
        self.sugarCookies.deselect()
        self.bananas.deselect()
        self.cherryTop.deselect()
        # Disables the none button so it will remain selected.
        self.noTopping.config(state = 'disabled')

# The confirmWindow class, which confirms your order and tells you the price.
class confirmOrderWindow(EasyFrame):

    # This runs when confirmOrderWindow is loaded.
    def __init__(self):
        # Creates the window and frame for confirmOrderWindow.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Confirm Order", width = 400, height = 300, background = "#ffde59")
        # Adds a label asking you to confirm your label.
        self.confirmLabel = self.addLabel(text = "Confirm order:", row = 0, column = 0, sticky = '')
        self.confirmLabel["background"] = "#ffde59"
        # Creates a local variable which turns the order dictionary into a string.
        orderString = ""
        for key in order:
            orderString = orderString + str(order[key]) + "\n"
        # Creates a text area to display the order.
        self.orderDisplay = self.addTextArea(text = orderString, row = 1, column = 0, width = 1, height = 1)
        self.orderDisplay.config(state = "disabled")
        # Creates a button to confirm your order, and calls the "finishOrder" function.
        self.confirmButton = self.addButton(text = "Confirm", row = 2, column = 0, command = self.finishOrder)
        self.confirmButton.grid(sticky = tkinter.W)
        # Creates a button to return to the order menu, which calls the "backToOrder" function.
        self.backButton = self.addButton(text = "Back", row = 2, column = 0, command = self.backToOrder)
        self.backButton.grid(sticky = tkinter.E)

    # Closes the current window, and starts the thanksWindow window.
    def finishOrder(self):
        self.grid_forget()
        thanksWindow().mainloop()
        # If this was actually a real thing, this is where I would save the order data.

    # Returns to the orderWindow window and resets the order variable.
    def backToOrder(self):
        # Resets the order variable.
        global order
        if order["orderType"] == "Pick Up":
            order = {"orderType" : "Pick Up"}
        else:
            order = {"orderType" : "Dine In"}
        # Returns to the orderWindow window.
        self.grid_forget()
        orderWindow().mainloop()
        
# The thanksWindow class, which acts as the "thank you!" screen after you order.
class thanksWindow(EasyFrame):

    # This is triggered when thanksWindow is created.
    def __init__(self):
        # This creates the frame for the thanksWindow window.
        EasyFrame.__init__(self, title = "Kevin's Confections App: Thanks!", width = 400, height = 400, background = "#ffde59")
        # This button sends you back home after thanking you.
        self.returnButton = self.addButton(text = "Return Home", row = 2, column = 0, command = self.returnHome)
        # This adds an image thanking you for being here. Right now it's another Grindel pic.
        self.thanksImage = self.addLabel(text = "", row = 0, column = 0, sticky = '')
        self.image = PhotoImage(file = "Thank You!.png")
        self.thanksImage["image"] = self.image
        self.thanksImage["background"] = "#ffde59"
        # This adds a caption to the image, and styles it. Right now it's a bit cramped, but once I move the giant freaking Grindel I will have more than enough room.
        self.thanksCaption = self.addLabel(text = "Thank you for ordering!", row = 1, column = 0, sticky = tkinter.S)
        self.thanksCaption["foreground"] = "blue"
        self.thanksCaption["background"] = "#ffde59"
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
