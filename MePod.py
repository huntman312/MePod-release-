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

root.title("MePod v1.35")
root.iconbitmap(str(path + '/EXE builder/icon.ico'))

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
    m = re.sub('[/]', '@', model.get())
    filePath = path + "/" + "TOOL_DATABASE" + \
        "/" + b + "/" + m
    finalPath = str(filePath)

    with open(finalPath, "r") as toolTextFile:
        toolDict = toolTextFile.read()
        return literal_eval(toolDict)
### end tool database ###


def modelList(*args):
    sel = brand.get()
    List1 = os.listdir(path + "/TOOL_DATABASE/" + sel)
    List2 = []
    for x in List1:
        a = x.replace("@", "/")
        List2.append(a)

    ListB = List2
    comboboxB.config(values=ListB)


ListA = os.listdir(str(path + "/" + "TOOL_DATABASE"))
ListB = []


# add to database button setup

def dataAdd():
    dbrand = addbrand.get().upper()
    dmodel = addmodel.get().upper()
    key = addschemNum.get().upper()
    dpart = addPartNum.get().upper()
    ddesc = adddesentry.get().upper()
    dir1 = dbrand
    check = dmodel.replace('/', '@')
    if not os.path.exists(path + "/" + "TOOL_DATABASE" + "/" + dir1):
        os.mkdir(path + "/" + "TOOL_DATABASE" + "/" + dir1)
        file1 = os.path.join(path + "/" + "TOOL_DATABASE" +
                             "/" + dir1, check)
    else:
        file1 = os.path.join(path + "/" + "TOOL_DATABASE" +
                             "/" + dir1, check)
    finalPath = file1
    if os.path.isfile(finalPath) == False:
        toolFile = open(finalPath, "w")
        toolDict = {}
        toolDict[key] = dpart, ddesc
        toolFile.write(str(toolDict))
    else:
        toolFile = open(finalPath, "r")
        oldDict = toolFile.read()
        newDict = {}
        newDict[key] = dpart, ddesc
        strToDict = literal_eval(oldDict)
        finalDict = {**strToDict, **newDict}
        toolFile = open(finalPath, "w")
        toolFile.write(str(finalDict))


brandLabel2 = Label(my_frame2, text="Tool Brand?")
brandLabel2.grid(row=0, column=0)

addbrand = StringVar()
modelentryA2 = ttk.Entry(my_frame2, textvariable=addbrand)
modelentryA2.grid(row=0, column=1)


modelLabel2 = Label(my_frame2, text="Tool model?")
modelLabel2.grid(row=0, column=3)

addmodel = StringVar()
modelentryB2 = ttk.Entry(my_frame2, textvariable=addmodel)
modelentryB2.grid(row=0, column=4)

schemLabel = Label(my_frame2, text="Shematic Number?")
schemLabel.grid(row=1, column=0)

addschemNum = StringVar()
schemEntry2 = Entry(my_frame2, textvariable=addschemNum)
schemEntry2.grid(row=1, column=1)

addPart = Label(my_frame2, text="Part Number?")
addPart.grid(row=1, column=3)

addPartNum = StringVar()
PartNum2 = Entry(my_frame2, textvariable=addPartNum)
PartNum2.grid(row=1, column=4)

adddesc = Label(my_frame2, text="Description?")
adddesc.grid(row=2, column=0)

adddesentry = StringVar()
adddes2 = Entry(my_frame2, textvariable=adddesentry, width=55)
adddes2.grid(row=2, column=1, columnspan=4)


addButton = Button(
    my_frame2, text="  Add To Database  ", command=dataAdd)
addButton.grid(row=2, column=6, columnspan=2)


# order tab
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


schemLabel = Label(my_frame1, text="Shematic Number?", bg="#e7a6a6")
schemLabel.grid(row=5, column=3)

blank1Label = Label(my_frame1, text=" ")
blank1Label.grid(row=2, column=3)

findLabel = Label(my_frame1, text="Pull From Database", bg="#e7a6a6")
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


warn1 = Label(my_frame1, text="All RED fields required!")
warn1.grid(row=4, column=6)

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


def dataAddcus():
    dbrand = brand.get().upper()
    dmodel = model.get().upper()
    key = schemNum.get().upper()
    dpart = custPartNum.get().upper()
    ddesc = custDes.get().upper()
    dir1 = dbrand
    check = dmodel.replace('/', '@')
    if not os.path.exists(path + "/" + "TOOL_DATABASE" + "/" + dir1):
        os.mkdir(path + "/" + "TOOL_DATABASE" + "/" + dir1)
        file1 = os.path.join(path + "/" + "TOOL_DATABASE" +
                             "/" + dir1, check)
    else:
        file1 = os.path.join(path + "/" + "TOOL_DATABASE" +
                             "/" + dir1, check)
    finalPath = file1
    if os.path.isfile(finalPath) == False:
        toolFile = open(finalPath, "w")
        toolDict = {}
        toolDict[key] = dpart, ddesc
        toolFile.write(str(toolDict))
    else:
        toolFile = open(finalPath, "r")
        oldDict = toolFile.read()
        newDict = {}
        newDict[key] = dpart, ddesc
        strToDict = literal_eval(oldDict)
        finalDict = {**strToDict, **newDict}
        toolFile = open(finalPath, "w")
        toolFile.write(str(finalDict))


def addCus():
    global counter
    #partList = toolDataBase()
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
    dataAddcus()
    return 0


warn2 = Label(my_frame1, text="All RED and BLUE fields required!")
warn2.grid(row=8, column=6)

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
