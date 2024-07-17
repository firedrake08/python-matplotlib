import matplotlib.pyplot as matplot
import tkinter as tk
from peopledata import people
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

filteredpeople = people
canvas = None
canvas_widget = None

def filterPeople(peoplefilter):
    global filteredpeople
    if peoplefilter=='all':
        filteredpeople = people
    else:
        filteredpeople = list(filter(lambda person:person['gender']==peoplefilter,people))
    createGraph()

window = tk.Tk()
buttonFrame = tk.Frame(window)
buttonFrame.pack()

allBtn = tk.Button(buttonFrame,text="All",command=lambda:filterPeople('all'))
allBtn.grid(row=0,column=0)
maleBtn = tk.Button(buttonFrame,text="Male",command=lambda:filterPeople('male'))
maleBtn.grid(row=0,column=1)
femaleBtn = tk.Button(buttonFrame,text="Female",command=lambda:filterPeople('female'))
femaleBtn.grid(row=0,column=2)

canvas = tk.Canvas(window)
canvas.pack()

def createGraph():
    global filteredpeople
    global canvas
    global canvas_widget
    if(canvas_widget):
        canvas_widget.get_tk_widget().destroy()


    names = [person["firstname"] for person in filteredpeople]
    salaries = [person["salary"] for person in filteredpeople]
    matplot.clf()
    matplot.bar(names,salaries,color="red")
    matplot.xlabel("Name")
    matplot.ylabel("Salary")

    fig = matplot.gcf()
    canvas_widget = FigureCanvasTkAgg(fig, master=canvas)
    canvas_widget.draw()
    canvas_widget.get_tk_widget().pack()


createGraph()


def closewindow():
    matplot.close("all")
    window.destroy()

window.protocol("WM_DELETE_WINDOW", closewindow)

window.mainloop()
