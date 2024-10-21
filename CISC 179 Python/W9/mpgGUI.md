# MPG GUI 

``` python
from tkinter import *

# function that calculates MPG
def calculateMpg():
    miles = float(milesEntry.get())
    gallons = float(gallonsEntry.get())
    mpgLabel.config(text=f"MPG: {miles / gallons:.2f}")

# main GUI window
root = Tk()
root.title("MPG Calculator")

# entry widgets and labels
Label(root, text="Miles:").grid(row=0, column=0)
milesEntry = Entry(root)
milesEntry.grid(row=0, column=1)

Label(root, text="Gallons:").grid(row=1, column=0)
gallonsEntry = Entry(root)
gallonsEntry.grid(row=1, column=1)

# calculate button
Button(root, text="Calculate MPG", command=calculateMpg).grid(row=2, columnspan=2)

# result label
mpgLabel = Label(root, text="MPG: ")
mpgLabel.grid(row=3, columnspan=2)

# run application
root.mainloop()
``` 
