from tkinter import *
#
# create empty window
root = Tk()

# window management
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

#widget
button_input_1 = Button(topFrame, text="Get PDF 1", fg="blue")
button_input_2 = Button(topFrame, text="Get PDF 2", fg="red")
button_output = Button(topFrame, text="Output")
button_merge = Button(bottomFrame, text="merge", fg="green")

# display button
button_input_1.pack(side=LEFT)
button_input_2.pack(side=LEFT)
button_output.pack(side=LEFT)
button_merge.pack(side=BOTTOM)

# keep window open
root.mainloop()