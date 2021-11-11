from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import random
from quicksort import quick_sort
from mergesort import merge_sort
import threading
#variables
#selected_alg = StringVar()
dataM = []
dataQ = []
#function
# def drawData(data, colorArray,canvas):
#     threading.Thread(target=drawDatax,args=(data, colorArray,canvas,)).start()
def drawData(data, colorArray,canvas):
    canvas.delete("all")
    c_height = canvas.winfo_height()
    c_width = canvas.winfo_width()

    x_width = c_width /(len(data) + 1)

    spacing = x_width/2
    offset = spacing/2
    ypad=6
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - ypad - height * (c_height/(max(normalizedData)+0.1))
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height -ypad

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global dataM
    global dataQ
    dataM = []
    dataQ=[]
    custInput=userIn.get("1.0",END)
    if len(custInput) !=1:
        resp=messagebox.askquestion("Generate","This is your input {0}. Are you Sure?".format(custInput))
        if resp=="yes":
            data=[int(x) for x in custInput.split(",")]
            for i in data:
                dataM.append(i)
                dataQ.append(i)
        if resp=="no":
            resp2=messagebox.askquestion("Generate","Would you like to auto generate a random number?")
            if resp2=="yes":
                minVal = int(minEntry.get())
                maxVal = int(maxEntry.get())
                size = int(sizeEntry.get())

                for _ in range(size):
                    val=random.randrange(minVal, maxVal+1)
                    dataM.append(val)
                    dataQ.append(val)
            if resp2=="no":
                return
    if len(custInput)==1:
        minVal = int(minEntry.get())
        maxVal = int(maxEntry.get())
        size = int(sizeEntry.get())

        for _ in range(size):
            val=random.randrange(minVal, maxVal+1)
            dataM.append(val)
            dataQ.append(val)

    drawData(dataM, ['red' for x in range(len(dataM))],merge_canv) #['red', 'red' ,....]
    drawData(dataQ, ['red' for x in range(len(dataQ))],quick_canv) #['red', 'red' ,....]


def StartAlgorithm():
    global dataM
    global dataQ
    if (not dataM or not dataQ): return
    quick_sort(dataQ, 0, len(dataQ)-1, drawData, speedScale.get(),quick_canv)
    drawData(dataQ, ['green' for x in range(len(dataQ))],quick_canv)
    comps=merge_sort(dataM, drawData, speedScale.get(),merge_canv)
    drawData(dataM, ['green' for x in range(len(dataM))],merge_canv)
    messagebox.showinfo(title="runtime and No of comparisons",message="no of comp is {0}".format(comps))

root = Tk()
root.title('mergesort')
# root.maxsize(900, 600)
root.config(bg='light blue')
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1, weight=1)

#frame / base lauout

UI_frame = Frame(root,width= 600,height=200, bg='grey')
UI_frame.grid(row=0, column=0, padx=300, pady=5,columnspan=2,sticky="nsew")
UI_frame.grid_rowconfigure(0, weight=1)
UI_frame.grid_rowconfigure(1, weight=1)
UI_frame.grid_columnconfigure(0,weight=1)
UI_frame.grid_columnconfigure(1,weight=1)
UI_frame.grid_columnconfigure(2,weight=1)


merge_canv = Canvas(root,bg='light pink')
merge_canv.grid(row=1, column=0, padx=10, pady=5,ipady=10,sticky="nsew")
quick_canv = Canvas(root, bg='light pink')
quick_canv.grid(row=1, column=1, padx=10, pady=5,ipady=5,sticky="nsew"  )

#User Interface Area
#Row[0]
# Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
# algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
# algMenu.grid(row=0, column=1, padx=5, pady=5)
# algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5,sticky="nsew")
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=40, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5,sticky="nsew")

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5,sticky="nsew")

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5,sticky="nsew")

userIn = Text(UI_frame,bg='white',width=10,height=0.1)
userIn.insert('1.0', 'Insert data in single line')
userIn.grid(row=0, column=0 ,columnspan=2,padx=5, pady=5,sticky="nsew")
Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
