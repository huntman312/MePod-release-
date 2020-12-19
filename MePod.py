from tkinter import *
from tkinter import ttk
import os
from ast import literal_eval
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
import datetime
from reportlab.lib import colors
from reportlab.platypus import TableStyle
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib.pagesizes import letter
import sys
import tkinter.font as tkfont
import re


counter = 0

system = sys.platform
path = os.getcwd()


def date_of_order():
    d = datetime.datetime.today()
    return str(d.month) + "-" + str(d.day) + "-" + str(d.year)


# tkinter window
root = Tk()

root.title("MePod v1.30")
root.iconbitmap(path + '/EXE builder/icon.ico')

root.geometry("800x350")

my_notbook = ttk.Notebook(root)
my_notbook.pack()
my_frame1 = Frame(my_notbook, width=800, height=350)
my_frame2 = Frame(my_notbook, width=800, height=350)

my_frame1.pack(fill="both", expand=1)
my_frame2.pack(fill="both", expand=1)

my_notbook.add(my_frame1, text="Order Maker")
my_notbook.add(my_frame2, text="Add To Database")


### tool database ###


def toolDataBase():
    b = brand.get()
    m = re.sub('[/!@#$.]', '', model.get())
    filePath = path + "/" + "TOOL_DATABASE" + \
        "/" + b + "/" + m + ".txt"
    finalPath = str(filePath)

    with open(finalPath, "r") as toolTextFile:
        toolDict = toolTextFile.read()
        return literal_eval(toolDict)
### end tool database ###


def modelList(*args):
    sel = brand.get()
    if sel == 'MAX':
        ListB = ['CN55', 'CN70', 'CN70PAL', 'CN80', 'CN100', 'CN445R3',
                 'CN550S', 'CN565D', 'CN890F2', 'SN890CH3/34', 'TA551B/16-11']
    elif sel == 'TECH':
        ListB = ['PCN55M.1', 'PCN670SA.1']
    elif sel == 'OMER':
        ListB = ['B14.763 BF']
    elif sel == 'BEA':
        ListB = ['W15-358C']
    elif sel == 'BOSTITCH':
        ListB = ['438S2R-1']
    elif sel == 'SENCO':
        ListB = ['SCN65XP', 'SLP20XP']
    elif sel == 'SPOTNAILS':
        ListB = ['RC1016']
    comboboxB.config(values=ListB)


ListA = ['MAX', 'TECH', 'OMER', 'BEA', 'BOSTITCH', 'SENCO', 'SPOTNAILS']
ListB = []


shipToLabel = Label(my_frame1, text="Where to ship?", bg="#e7a6a6")
shipToLabel.grid(row=0, column=0)

shipTo = StringVar()
shipToEntry = ttk.Entry(my_frame1, textvariable=shipTo)

shipToEntry.grid(row=0, column=1)


billToLabel = Label(my_frame1, text="Customer to bill?", bg="#e7a6a6")
billToLabel.grid(row=0, column=3)

billTo = StringVar()
billToEntry = ttk.Entry(my_frame1, textvariable=billTo)
billToEntry.grid(row=0, column=4)


brandLabel = Label(my_frame1, text="Tool Brand?", bg="#e7a6a6")
brandLabel.grid(row=1, column=0)

brand = StringVar()
comboboxA = ttk.Combobox(my_frame1, textvariable=brand, values=ListA)
comboboxA.bind("<<ComboboxSelected>>", modelList)
comboboxA.grid(row=1, column=1)


modelLabel = Label(my_frame1, text="Tool model?", bg="#e7a6a6")
modelLabel.grid(row=1, column=3)

model = StringVar()
comboboxB = ttk.Combobox(my_frame1, textvariable=model, values=ListB)
comboboxB.grid(row=1, column=4)


schemLabel = Label(my_frame1, text="Shematic Number?", bg="#a9eca7")
schemLabel.grid(row=5, column=3)

blank1Label = Label(my_frame1, text=" ")
blank1Label.grid(row=2, column=3)

findLabel = Label(my_frame1, text="Pull From Database", bg="#a9eca7")
findLabel.grid(row=3, column=3)

schemNum = StringVar()
schemEntry = Entry(my_frame1, textvariable=schemNum)
schemEntry.grid(row=5, column=4)

finalPartsList = [["TOOL", "QUANTITY", "PART#", "DESCRIPTION"]]


ammountLabel = Label(my_frame1, text="Enter Quantitiy", bg="#e7a6a6")
ammountLabel.grid(row=5, column=0)

amountTo = StringVar()
amountToEntry = ttk.Entry(my_frame1, textvariable=amountTo)
amountToEntry.grid(row=5, column=1)

blankLabel = Label(my_frame1, text=" ")
blankLabel.grid(row=6, column=0)

customLabel = Label(my_frame1, text="Add Custom Part Entry", bg="#a7acec")
customLabel.grid(row=7, column=0)


def selectClick():
    global counter
    partList = toolDataBase()
    sel = schemNum.get().upper()
    list1 = []
    list1.append(brand.get() + " " + model.get())
    list1.append(amountTo.get())
    temp = list(partList[sel])
    for x in temp:
        list1.append(x)
    finalPartsList.append(list1)
    w = ttk.Combobox(my_frame1, values=finalPartsList, width=120)
    w.grid(row=12, column=0, columnspan=7)
    counter = counter + 1
    x = counter
    w.current(x)
    return 0


schemButton = Button(
    my_frame1, text="  Add Part  ", command=selectClick)
schemButton.grid(row=5, column=6, columnspan=2)

tableLabel = Label(my_frame1, text=" ")
tableLabel.grid(row=10, column=0, columnspan=7)

tableLabel = Label(my_frame1, text="Current Parts List")
tableLabel.grid(row=11, column=0)

w = ttk.Combobox(my_frame1, values=finalPartsList, width=120)
w.grid(row=12, column=0, columnspan=7)
w.current(counter)


def delLast():
    global counter
    if counter == 0:
        return 0
    else:
        del finalPartsList[-1]
        w = ttk.Combobox(my_frame1, values=finalPartsList, width=120)
        w.grid(row=12, column=0, columnspan=7)
        counter = counter - 1
        x = counter
        w.current(x)


delButton = Button(
    my_frame1, text="  Delete Last Entry  ", command=delLast)
delButton.grid(row=13, column=0, columnspan=4)


partNumLabel = Label(my_frame1, text="Part #", bg="#a7acec")
partNumLabel.grid(row=8, column=1)

custPartNum = StringVar()
partNumEntry = Entry(my_frame1, textvariable=custPartNum)
partNumEntry.grid(row=9, column=1)

desLabel = Label(my_frame1, text="Part Description", bg="#a7acec")
desLabel.grid(row=8, column=2)

custDes = StringVar()
desEntry = Entry(my_frame1, textvariable=custDes, width=50)
desEntry.grid(row=9, column=2, columnspan=4)


def addCus():
    global counter
    partList = toolDataBase()
    list1 = []
    list1.append(brand.get().upper() + " " + model.get().upper())
    list1.append(amountTo.get())
    list1.append(custPartNum.get().upper())
    list1.append(custDes.get().upper())
    finalPartsList.append(list1)
    w = ttk.Combobox(my_frame1, values=finalPartsList, width=120)
    w.grid(row=12, column=0, columnspan=7)
    counter = counter + 1
    x = counter
    w.current(x)
    return 0


addCusButton = Button(
    my_frame1, text="Add Custom Entry", command=addCus)
addCusButton.grid(row=9, column=6)


def schemFetch():
    modelFix = re.sub('[/!@#$.]', '', model.get())
    filename = os.getcwd() + '/Schematics/' + brand.get() + modelFix + '.pdf'
    os.startfile(filename)
    return 0


schemButton = Button(
    my_frame1, text="Show Schematic", command=schemFetch)
schemButton.grid(row=1, column=6)


# makes pdf with info nested list, data nested list and pdf name


def pdfMaker():
    # stuffx = a
    # print(type(stuffx))
    customer = billToEntry.get().upper()
    shipTo = shipToEntry.get().upper()
    dateOfOrder = date_of_order()
    pdfName = "parts order (" + customer + ") " + dateOfOrder + ".pdf"
    info = [["BILL: ", customer], ["SHIP: ", shipTo], ["DATE: ", dateOfOrder]]
    data = finalPartsList

    save_path = path + "/orders to be sent/" + pdfName

    pdf = SimpleDocTemplate(save_path, pagesize=letter)

    InFo = Table(info)
    table = Table(data)

    # add style

    style = TableStyle([
        ('BACKGROUND', (0, 0), (3, 0), colors.black),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),

        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),

        ('FONTNAME', (0, 0), (-1, 0), 'Courier-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),

        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),

        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    ])
    table.setStyle(style)

    # 2) Alternate backgroud color
    rowNumb = len(data)
    for i in range(1, rowNumb):
        if i % 2 == 0:
            bc = colors.burlywood
        else:
            bc = colors.beige

        ts = TableStyle(
            [('BACKGROUND', (0, i), (-1, i), bc)]
        )
        table.setStyle(ts)

    # 3) Add borders
    ts = TableStyle(
        [
            ('BOX', (0, 0), (-1, -1), 2, colors.black),

            # ('LINEBEFORE', (4, 1), (4, -1), 2, colors.red),
            # ('LINEABOVE', (0, 1), (-1, 1), 2, colors.green),

            ('GRID', (0, 1), (-1, -1), 2, colors.black),
        ]
    )
    table.setStyle(ts)

    elems = []
    elems.append(InFo)
    elems.append(table)

    pdf.build(elems)

# button click


def mainClick():
    # customer = billToEntry.get().upper()
    # shipTo = shipToEntry.get().upper()
    # dateOfOrder = date_of_order()
    # pdfName = "parts order (" + customer + ") " + dateOfOrder + ".pdf"
    # info = [["BILL: ", customer], ["SHIP: ", shipTo], ["DATE: ", dateOfOrder]]
    # data = [["TOOL", "QUANTITY", "PART#", "DESCRIPTION"]]

    pdfMaker()


button = Button(
    my_frame1, text="                CREATE PDF              ", command=mainClick)
button.grid(row=13, column=5, columnspan=2)


blankLabe2 = Label(my_frame1, text=" ")
blankLabe2.grid(row=14, column=7)

root.mainloop()
