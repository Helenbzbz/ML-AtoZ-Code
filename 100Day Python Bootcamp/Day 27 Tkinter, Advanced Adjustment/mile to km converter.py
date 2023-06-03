from tkinter import *

window = Tk()
window.geometry("250x130")
window.config()
window.title("Mile to Km Converter")

entry = 0

# Entry
entry_box = Entry(width = 7)

# Label
miles_label = Label(text = "Miles")
equal_label = Label(text = "is equal to")
Km_label = Label(text = "Km")
entry_answer = Label(text = f"{entry}")

# Calculate Button
def button_fuction():
    entry = entry_box.get()
    entry_answer["text"] = float(entry)*1.609344
    entry_answer.config(text = round((float(entry)*1.609344), 2))

calculate_button = Button(text = "Calculate", command= button_fuction)

# Placement
entry_box.place(x = 95, y = 20)
miles_label.place(x = 180, y = 20)
equal_label.place(x = 20, y = 50)
entry_answer.place(x = 130, y = 50)
Km_label.place(x = 185, y = 50)
calculate_button.place(x = 90, y = 75)

window.mainloop()