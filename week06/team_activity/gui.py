# Copyright 2024, Sandro Ribeiro. All rights reserved.

import tkinter as tk
from tkinter import Frame, Label, Button, Entry
from values_entry import FloatEntry


def main():
    # Create the Tk root object.
    root = tk.Tk()
    root.geometry("400x120")

    # Create the main window. In tkinter,
    # a window is also called a frame.
    frm_main = Frame(root)
    frm_main.master.title("Body Mass Index (BMI)")
    frm_main.pack(padx=4, pady=3, fill=tk.BOTH, expand=1)

    # Configurar grid no frame pai
    frm_main.grid_columnconfigure(0, weight=1)
    frm_main.grid_columnconfigure(1, weight=1)
    frm_main.grid_columnconfigure(2, weight=1)
    frm_main.grid_columnconfigure(3, weight=7)

    # Call the populate_main_window function, which will add
    # labels, text entry boxes, and buttons to the main window.
    populate_main_window(frm_main)

    # Start the tkinter loop that processes user events
    # such as key presses and mouse button clicks.
    root.mainloop()


# The controls in a graphical user interface (GUI) are called widgets,
# and each widget is an object. Because a GUI has many widgets and
# each widget is an object, the code to make a GUI usually has many
# variables to store the many objects. Because there are so many
# variable names, programmers often adopt a naming convention to help
# a programmer keep track of all the variables. One popular naming
# convention is to type a three letter prefix in front of the names
# of all variables that store GUI widgets, according to this list:
#
# frm: a frame (window) widget
# lbl: a label widget that displays text for the user to see
# ent: an entry widget where a user will type text or numbers
# btn: a button widget that the user will click


def superscript(number):
    superscripts = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(number).translate(superscripts)

def populate_main_window(frm_main):
    """Populate the main window of this program. In other words, put
    the labels, text entry boxes, and buttons into the main window.

    Parameter
        frm_main: the main frame (window)
    Return: nothing
    """
    # Create a label that displays "Weight:"
    lbl_weight = Label(frm_main, text="Weight:")

    # Create an float entry box where the user will enter her weight.
    ent_weight = FloatEntry(frm_main, width=8)

    # Create a label that displays "libs"
    lbl_weight_units = Label(frm_main, text="kg")

    # Create a label that displays "Weight:"
    lbl_height = Label(frm_main, text="Height:")

    # Create an integer entry box where the user will enter her age.
    ent_height = FloatEntry(frm_main, width=8)

    # Create a label that displays "years"
    lbl_height_units = Label(frm_main, text=f"m")

    # Create a label that displays "Rates:"
    lbl_bmi = Label(frm_main, text="BMI: ")
    lbl_ans_bmi = Label(frm_main, text="")

    # Create labels that will display the results.
    lbl_bmi_units = Label(frm_main, text=f"kg/m{superscript(2)}")

    # Create labels that display messages to users
    lbl_message = Label(frm_main, 
                        text="", 
                        width=30, 
                        height=3, 
                        wraplength=200, 
                        justify="center",  
                        padx=2, 
                        pady=2,
                        borderwidth=0.5, 
                        relief="solid"
                        )

    # Create the Clear button.
    btn_clear = Button(frm_main, text="Clear", width=10)

    # Layout all the labels, entry boxes, and buttons in a grid.
    lbl_weight.grid(        row=0, column=0, padx=3, pady=3, sticky="w")
    ent_weight.grid(        row=0, column=1, padx=3, pady=3)
    lbl_weight_units.grid(  row=0, column=2, padx=3, pady=3, sticky="w")

    lbl_height.grid(        row=1, column=0, padx=3, pady=3, sticky="w")
    ent_height.grid(        row=1, column=1, padx=3, pady=3)
    lbl_height_units.grid(  row=1, column=2, padx=3, pady=3, sticky="w")

    lbl_bmi.grid(           row=2, column=0, padx=3, pady=3, sticky="w")
    lbl_ans_bmi.grid(       row=2, column=1, padx=3, pady=3)
    lbl_bmi_units.grid(     row=2, column=2, padx=5, pady=3, sticky="w")

    lbl_message.grid(       row=0, column=3, rowspan=3, padx=5, pady=5, sticky="ns")

    btn_clear.grid(         row=3, column=0, padx=3, pady=3, columnspan=8)

    # This function will be called each time the user releases a key.
    def calculate(event):
        """Compute and display the user's slowest
        and fastest beneficial heart rates.
        """
        try:
            try:
                # Get the user's weight.
                weight = ent_weight.get()
                if weight <= 0:
                    raise ValueError("weight must be positive")
            except ValueError:
                lbl_message.config(text="Please enter a valid Weight")
                return
            
            try:
                # Get the user's height.
                height = ent_height.get()

                if height <= 0:
                    raise ValueError("Height must be positive.")
            except ValueError:
                    lbl_message.config(text="Please enter a valid height")
                    return

            # Compute the user's bmi.
            ans_bmi = (weight / (height ** 2))

            # Display the bmi for the user to see.
            lbl_ans_bmi.config(text=f"{ans_bmi:.2f}")

        except ValueError:
                # When the user deletes all the digits 
                # in the weight or height entry box, 
                # clear the bmi label.
                lbl_bmi.config(text="")
    
        if ans_bmi < 18.5: 
            lbl_message.config(text="Your BMI shows you're underweight. Consider consulting a healthcare provider to ensure proper nutrition")
            
        if ans_bmi >= 18.5 and ans_bmi <= 25: 
            lbl_message.config(text="Your BMI is normal. Keep maintaining a healthy lifestyle")
            
        if ans_bmi > 25 and ans_bmi <= 30: 
            lbl_message.config(text="Your BMI indicates you're overweight, Small lifestyle changes can make a big difference")
            
        if ans_bmi > 30 and ans_bmi <= 35: 
            lbl_message.config(text="Your BMI indicates Obesity Grade I. Consider seeking guidance to improve your health")
            
        if ans_bmi > 35 and ans_bmi <= 40: 
            lbl_message.config(text="Your BMI indicates Obesity Grade II.Support from a healthcare provider can help")
        if ans_bmi > 40: 
            lbl_message.config(text="Your BMI shows Obesity Grade III. Professional guidance can help you take positive steps")

    # This function will be called each time
    # the user presses the "Clear" button.
    def clear():
        """Clear all the inputs and outputs."""
        btn_clear.focus()
        ent_weight.clear()
        ent_height.clear()
        lbl_ans_bmi.config(text="")
        lbl_message.config(text="")
        ent_weight.focus()

    # Binds the calculate function to the height 
    # value input by the user so that the computer 
    # calls the calculate function when the user 
    # clicks enter on the keyboard
    ent_height.bind("<Return>", calculate)

    # Bind the clear function to the clear button so
    # that the computer will call the clear function
    # when the user clicks the clear button
    btn_clear.config(command=clear)

    # Give the enter change focus to the height.
    def focus_change(event):
        if ent_weight.get() > 0: 
            ent_height.focus()
        else:
            lbl_message.config(text="Please enter a valid weight.")

    ent_weight.bind("<Return>", focus_change)

# If this file is executed like this:
# > python heart_rate.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.
if __name__ == "__main__":
    main()

