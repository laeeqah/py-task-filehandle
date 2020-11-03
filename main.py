from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Text File")
window.config(bg = "light blue")
frame = Frame(window)

#The layout of text files
head = Label(window, text = "My weekend activities", font = 200)
head.pack(side = LEFT)
head.place(x = 50, y = 10)

# Your input
input_text = Text(window, width = 40, height = 10)
input_text. pack(side = LEFT)
input_text.place(x = 50,y = 35)

#function for create
def clicked():
    with open("my_weekend_activities.txt", "w") as docs:
        for i in range(1):
            docs.write("Went sky diving. Ate out at a a restraurant. Played games. Went to the malls. Went to family. \n") #writing in what i want it to display in the txt

                                
create_btn = Button(window, text = "Create",command = clicked)
create_btn.pack(side = LEFT)
create_btn.place(x = 50, y = 220)

#function for displaying the file
def display():
    with open("my_weekend_activities.txt","r") as docs:
        input_text.insert(INSERT,docs.read())# will insert the text that in docs into the text widget.
    
display_btn = Button(window, text = "Display", command = display)
display_btn.pack()
display_btn.place(x = 120, y = 220)


# function for append data
def append():
    with open("my_weekend_activities.txt","a") as data:
        data.write(str(input_text.get('1.0', END))) #If you click the Append Data button and type in the text widget and then click display it will appear in the doc and widget



appen_btn = Button(window, text = "Append Data", command = append)
appen_btn.pack()
appen_btn.place(x = 197, y = 220)

#function for clear button
def clear_all():
    input_text.delete("1.0","end") # Will clear the text widget
    
clear_btn =Button(window, text = "Clear", command = clear_all)
clear_btn.pack()
clear_btn.place(x = 310, y = 220)

#the exit function
def exit():
    window.destroy() # It will exit out of the window

ext_btn = Button(window, text = "Exit", command = exit)
ext_btn.pack()
ext_btn.place(x = 375 , y = 220)

window.mainloop()
