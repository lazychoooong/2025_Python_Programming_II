from  tkinter import *

root = Tk()

button = Button(root, text="버튼을 클릭하세요")
button.pack()
button["fg"] = "yellow"
button["bg"] = "green"

root.mainloop()