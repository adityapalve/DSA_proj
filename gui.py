from tkinter import *
from tkinter import ttk
import random
# from quicksort import quick_sort
# from mergesort import merge_sort

#variables
#selected_alg = StringVar()
data = []

#function
def drawData(data, colorArray,canvas):
    canvas.delete("all")
    c_height = 380
    c_width = 600
    x_width = c_width / (len(data) + 1)
    offset = 30
    spacing = 10
    normalizedData = [ i / max(data) for i in data]
    for i, height in enumerate(normalizedData):
        #top left
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 340
        #bottom right
        x1 = (i + 1) * x_width + offset
        y1 = c_height

        canvas.create_rectangle(x0, y0, x1, y1, fill=colorArray[i])
        canvas.create_text(x0+2, y0, anchor=SW, text=str(data[i]))

    root.update_idletasks()


def Generate():
    global data

    minVal = int(minEntry.get())
    maxVal = int(maxEntry.get())
    size = int(sizeEntry.get())

    data = []
    for _ in range(size):
        data.append(random.randrange(minVal, maxVal+1))

    drawData(data, ['red' for x in range(len(data))]) #['red', 'red' ,....]

def StartAlgorithm():
    global data
    if not data: return
    quick_sort(data, 0, len(data)-1, drawData, speedScale.get())

    merge_sort(data, drawData, speedScale.get())

    drawData(data, ['green' for x in range(len(data))])


root = Tk()
root.title('mergesort')
# root.maxsize(900, 600)
root.config(bg='light blue')
root.resizable("True","True")
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=3)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1, weight=1)

#frame / base lauout

UI_frame = Frame(root, bg='grey')
UI_frame.grid(row=0, column=0, padx=10, pady=5,columnspan=2, sticky="nsew" )
UI_frame.grid_rowconfigure(0, weight=1)
UI_frame.grid_rowconfigure(1, weight=1)
UI_frame.grid_columnconfigure(0,weight=1)
UI_frame.grid_columnconfigure(1,weight=1)
UI_frame.grid_columnconfigure(2,weight=1)


merge_canv = Canvas(root, bg='light pink')
merge_canv.grid(row=1, column=0, padx=10, pady=5,sticky="nsew")
quick_canv = Canvas(root, bg='light pink')
quick_canv.grid(row=1, column=1, padx=10, pady=5,sticky="nsew"  )

#User Interface Area
#Row[0]
# Label(UI_frame, text="Algorithm: ", bg='grey').grid(row=0, column=0, padx=5, pady=5, sticky=W)
# algMenu = ttk.Combobox(UI_frame, textvariable=selected_alg, values=['Bubble Sort', 'Quick Sort', 'Merge Sort'])
# algMenu.grid(row=0, column=1, padx=5, pady=5)
# algMenu.current(0)

speedScale = Scale(UI_frame, from_=0.1, to=5.0, length=200, digits=2, resolution=0.2, orient=HORIZONTAL, label="Select Speed [s]")
speedScale.grid(row=0, column=2, padx=5, pady=5)
Button(UI_frame, text="Start", command=StartAlgorithm, bg='red').grid(row=0, column=3, padx=5, pady=5)

#Row[1]
sizeEntry = Scale(UI_frame, from_=3, to=25, resolution=1, orient=HORIZONTAL, label="Data Size")
sizeEntry.grid(row=1, column=0, padx=5, pady=5)

minEntry = Scale(UI_frame, from_=0, to=10, resolution=1, orient=HORIZONTAL, label="Min Value")
minEntry.grid(row=1, column=1, padx=5, pady=5)

maxEntry = Scale(UI_frame, from_=10, to=100, resolution=1, orient=HORIZONTAL, label="Max Value")
maxEntry.grid(row=1, column=2, padx=5, pady=5)

Button(UI_frame, text="Generate", command=Generate, bg='white').grid(row=1, column=3, padx=5, pady=5)

root.mainloop()
