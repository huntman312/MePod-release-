from tkinter.constants import COMMAND, END
import platform
import sys
import re
import os
from ast import literal_eval
from typing_extensions import IntVar
from reportlab.platypus import SimpleDocTemplate
# from reportlab.platypus.paraparser import check_text
from reportlab.platypus.tables import Table
import datetime
from reportlab.lib import colors
from reportlab.platypus import TableStyle
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.tables import Table
from reportlab.lib.pagesizes import letter
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import BooleanVar, ttk
from tkinter import *

py3 = True
path = os.getcwd()
finalPartsList = [["TOOL", "QUANTITY", "PART#", "DESCRIPTION"]]
system = sys.platform


# start support


def set_Tk_var():
    global combobox
    combobox = tk.StringVar()
    global che81
    che81 = tk.IntVar()


def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
# end support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    set_Tk_var()
    top = Toplevel1(root)
    init(root, top)
    root.mainloop()


w = None


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    # rt = root
    root = rt
    w = tk.Toplevel(root)
    set_Tk_var()
    top = Toplevel1(w)
    init(w, top, *args, **kwargs)
    return (w, top)


def destroy_Toplevel1():
    global w
    w.destroy()
    w = None


class Toplevel1:

    def __init__(self, top=None):

        def shipList():
            setFilePath = path + "/" + "settings.txt"
            filePath = str(setFilePath)
            setfile = open(filePath, "r")
            customerList = setfile.read()
            finalList = customerList.split(",")

            return finalList

        def billList():
            billList = shipList()
            del billList[0]
            return billList

        def hideTab(event):
            self.PNotebook2.hide(self.PNotebook2_t3)

        def dataAddcus():
            dbrand = self.brandCombobox.get().upper()
            dmodel = self.modelCombobox.get().upper()
            key = self.cusSchemNum.get().upper()
            dpart = self.cusPartNum.get().upper()
            ddesc = self.cusDescription.get().upper()
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

        def DBspeed(*args):
            vw = self.DBScrolledlistbox.yview()
            dbrand = self.DBBrandTCombobox.get().upper()
            dmodel = self.DBModelTCombobox.get().upper()
            temp1 = self.DBSpeedEntry.get().upper()
            listTemp = temp1.split(" ")
            list1 = []
            list2 = []
            counter = 0
            for x in listTemp:
                if counter <= 1:
                    list1.append(x)
                    counter += 1
                else:
                    list2.append(x + " ")
            str1 = ""
            str1 = str1.join(list2)
            list1.append(str1.rstrip())
            key = list1[0]
            dpart = list1[1]
            ddesc = list1[2]
            dir1 = dbrand
            check = dmodel.replace('/', '@')
            addValues = [key, dpart, ddesc]
            list1 = []
            for x in self.DBScrolledlistbox.get(0, END):
                list1.append(list(x))
            index = -1
            for x in list1:
                if x[0] == key:
                    index = list1.index(x)
            if index >= 0:
                list1.pop(index)
                self.DBScrolledlistbox.delete(index)
                list1.insert(index, addValues)
                self.DBScrolledlistbox.insert(index, addValues)
            else:
                self.DBScrolledlistbox.insert(END, addValues)
                list1.append(addValues)

            finalDict = {}
            for x in list1:
                finalDict[x[0]] = x[1], x[2]

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
                toolFile.write(str(finalDict))
            else:
                toolFile = open(finalPath, "r")
                oldDict = toolFile.read()
                toolFile = open(finalPath, "w")
                toolFile.write(str(finalDict))
            self.DBSchemEntry.delete(0, END)
            self.DBPartEntry.delete(0, END)
            self.DBDesEntry.delete(0, END)
            self.DBScrolledlistbox.yview_scroll(1, "pages")

        def DBdataAddcus():
            vw = self.DBScrolledlistbox.yview()
            dbrand = self.DBBrandTCombobox.get().upper()
            dmodel = self.DBModelTCombobox.get().upper()
            key = self.DBSchemEntry.get().upper()
            dpart = self.DBPartEntry.get().upper()
            ddesc = self.DBDesEntry.get().upper()
            dir1 = dbrand
            check = dmodel.replace('/', '@')
            addValues = [key, dpart, ddesc]
            list1 = []
            for x in self.DBScrolledlistbox.get(0, END):
                list1.append(list(x))
            index = -1
            for x in list1:
                if x[0] == key:
                    index = list1.index(x)
            if index >= 0:
                list1.pop(index)
                self.DBScrolledlistbox.delete(index)
                list1.insert(index, addValues)
                self.DBScrolledlistbox.insert(index, addValues)
                self.DBScrolledlistbox.yview_moveto(0)
                self.DBScrolledlistbox.yview_scroll(index, "units")
            else:
                self.DBScrolledlistbox.insert(END, addValues)
                list1.append(addValues)
                self.DBScrolledlistbox.yview_moveto(1)

            finalDict = {}
            for x in list1:
                finalDict[x[0]] = x[1], x[2]

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
                toolFile.write(str(finalDict))
            else:
                toolFile = open(finalPath, "r")
                oldDict = toolFile.read()
                toolFile = open(finalPath, "w")
                toolFile.write(str(finalDict))
            self.DBSchemEntry.delete(0, END)
            self.DBPartEntry.delete(0, END)
            self.DBDesEntry.delete(0, END)

        def DBAdd(event):
            DBdataAddcus()

        def DBGrabInfo(event):
            self.TNotebook1.select(self.TNotebook1_t1)
            w = event.widget
            self.DBSchemEntry.delete(0, END)
            self.DBPartEntry.delete(0, END)
            self.DBDesEntry.delete(0, END)
            index = int(w.curselection()[0])
            value = w.get(index)
            item = list(value)
            self.DBSchemEntry.insert(END, item[0])
            self.DBPartEntry.insert(END, item[1])
            self.DBDesEntry.insert(END, item[2])

        def addCusB(*args):
            addCus()

        def addCus():
            shemNum = self.cusSchemNum.get()
            partNum = self.cusPartNum.get()
            des = self.cusDescription.get()
            tool = self.brandCombobox.get() + " " + self.modelCombobox.get()
            found = False
            for x in finalPartsList:
                if partNum == x[2]:
                    found = True
                    index2 = finalPartsList.index(x)
                    count = int(x[1]) + 1
            if found == True:
                finalPartsList.pop(index2)
                self.finalListbox.delete(index2)
                cusList = [tool, str(count),  partNum, des]
                finalPartsList.insert(index2, cusList)
                self.finalListbox.insert(index2, cusList)
            else:
                count = 1
                cusList = [tool, str(count),  partNum, des]
                finalPartsList.append(cusList)
                self.finalListbox.insert(END, cusList)
            if self.cb.get() == True:
                print("adding")
                dataAddcus()

        def date_of_order():
            d = datetime.datetime.today()
            return str(d.month) + "-" + str(d.day) + "-" + str(d.year)

        def pdfMaker():
            # stuffx = a
            # print(type(stuffx))
            customer = self.billCombobox.get().upper()
            shipTo = self.shipCombobox.get().upper()
            dateOfOrder = date_of_order()
            pdfName = "parts order (" + customer + ") " + dateOfOrder + ".pdf"
            info = [["BILL: ", customer], [
                "SHIP: ", shipTo], ["DATE: ", dateOfOrder]]
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

        def clearAllFields():
            self.partSearchEntry.delete(0, END)
            self.modelCombobox.delete(0, END)
            self.brandCombobox.delete(0, END)
            self.shipCombobox.delete(0, END)
            self.billCombobox.delete(0, END)
            self.availablePartsListBox.delete(0, END)
            self.cusSchemNum.delete(0, END)
            self.cusPartNum.delete(0, END)
            self.cusDescription.delete(0, END)
            self.finalListbox.delete(1, END)
            del finalPartsList[1:]
            shipList()

        def editSelection(event):
            self.hiddenEntry.delete(0, END)
            self.QEntry.delete(0, END)
            self.PNotebook2.select(self.PNotebook2_t3)
            w = event.widget
            index = int(w.curselection()[0])
            list1 = finalPartsList[index]
            count = int(list1[1])
            self.QEntry.insert(END, count)
            self.hiddenEntry.insert(END, index)

        def edSel():
            self.hiddenEntry.delete(0, END)
            self.QEntry.delete(0, END)
            self.PNotebook2.select(self.PNotebook2_t3)
            tup = self.finalListbox.curselection()
            index = tup[0]
            list1 = finalPartsList[index]
            count = int(list1[1])
            self.QEntry.insert(END, count)
            self.hiddenEntry.insert(END, index)

        def editPart():
            index = int(self.hiddenEntry.get())
            newCount = self.QEntry.get()
            if index > 0:
                list1 = finalPartsList[index]
                list1.pop(1)
                list1.insert(1, str(newCount))
                finalPartsList.pop(index)
                self.finalListbox.delete(index)
                finalPartsList.insert(index, list1)
                self.finalListbox.insert(index, list1)
                self.finalListbox.SelectedIndex = index

        def editPartB(*args):
            editPart()

        def deleteFromList():
            self.QEntry.delete(0, END)
            tup = self.finalListbox.curselection()
            index = tup[0]
            if index > 0:
                finalPartsList.pop(index)
                self.finalListbox.delete(index)
                self.hiddenEntry.delete(0, END)
                self.QEntry.insert(END, 0)
            self.PNotebook2.hide(self.PNotebook2_t3)

        def removeFromList():
            self.QEntry.delete(0, END)
            index = self.hiddenEntry.get()
            if index > 0:
                finalPartsList.pop(index)
                self.finalListbox.delete(index)
                self.hiddenEntry.delete(0, END)
                self.QEntry.insert(END, 0)

        def getBrands():
            return(os.listdir(str(path + "/" + "TOOL_DATABASE")))

        def DBgetBrands():
            return(os.listdir(str(path + "/" + "TOOL_DATABASE")))

        def selectFromList(event):
            w = event.widget
            index = int(w.curselection()[0])
            value = w.get(index)
            item = list(value)
            if self.brandCombobox.get() == "OMER" or self.brandCombobox.get() == "SENCO":
                for x in finalPartsList:
                    if item[0] == x[2]:
                        index1 = finalPartsList.index(x)
                        count = int(x[1]) + 1
                        finalPartsList.remove(x)
                        self.finalListbox.delete(index1)
                        item.insert(0, str(count))
                        tool = self.brandCombobox.get() + " " + self.modelCombobox.get()
                        item.insert(0, tool)
                        if self.brandCombobox.get() == "OMER" or self.brandCombobox.get() == "SENCO":
                            finalPartsList.insert(index1, item)
                            self.finalListbox.insert(index1, item)
                            self.finalListbox.yview_moveto(0)
                            self.finalListbox.yview_scroll(index1, "units")
                        else:
                            item.pop(2)
                            finalPartsList.insert(index1, item)
                            self.finalListbox.insert(index1, item)
                            self.finalListbox.yview_moveto(0)
                            self.finalListbox.yview_scroll(index1, "units")
                        isThere = True
                        break
                    else:
                        isThere = False
            else:
                for x in finalPartsList:
                    if item[1] == x[2]:
                        index1 = finalPartsList.index(x)
                        count = int(x[1]) + 1
                        finalPartsList.remove(x)
                        self.finalListbox.delete(index1)
                        item.insert(0, str(count))
                        tool = self.brandCombobox.get() + " " + self.modelCombobox.get()
                        item.insert(0, tool)
                        if self.brandCombobox.get() == "OMER" or self.brandCombobox.get() == "SENCO":
                            finalPartsList.insert(index1, item)
                            self.finalListbox.insert(index1, item)
                            self.finalListbox.yview_moveto(0)
                            self.finalListbox.yview_scroll(index1, "units")
                        else:
                            item.pop(2)
                            finalPartsList.insert(index1, item)
                            self.finalListbox.insert(index1, item)
                            self.finalListbox.yview_moveto(0)
                            self.finalListbox.yview_scroll(index1, "units")
                            isThere = True
                        break
                    else:
                        isThere = False

            if isThere == False:
                count = 1
                item.insert(0, str(count))
                tool = self.brandCombobox.get() + " " + self.modelCombobox.get()
                item.insert(0, tool)
                if self.brandCombobox.get() == "OMER" or self.brandCombobox.get() == "SENCO":
                    finalPartsList.append(item)
                    self.finalListbox.insert(END, item)
                    self.finalListbox.yview_moveto(1)
                else:
                    item.pop(2)
                    finalPartsList.append(item)
                    self.finalListbox.insert(END, item)
                    self.finalListbox.yview_moveto(1)

        def modelList(event):
            self.modelCombobox.delete(0, "end")
            w = event.widget
            sel = w.get()
            List1 = os.listdir(path + "/TOOL_DATABASE/" + sel)
            List2 = []
            for x in List1:
                a = x.replace("@", "/")
                List2.append(a)

            ListB = List2
            self.modelCombobox.configure(values=ListB)

        ListA = os.listdir(str(path + "/" + "TOOL_DATABASE"))
        ListB = []

        def DBmodelList(event):
            self.DBModelTCombobox.delete(0, "end")
            w = event.widget
            sel = w.get()
            List1 = os.listdir(path + "/TOOL_DATABASE/" + sel)
            List2 = []
            for x in List1:
                a = x.replace("@", "/")
                List2.append(a)

            ListD = List2
            self.DBModelTCombobox.configure(values=ListD)

        ListC = os.listdir(str(path + "/" + "TOOL_DATABASE"))
        ListD = []

        def callback(var):
            check = self.partSearchEntry.get().upper()
            list4 = []
            b = self.brandCombobox.get()
            m = re.sub('[/]', '@', self.modelCombobox.get())
            filePath = path + "/" + "TOOL_DATABASE" + "/" + b + "/" + m
            finalPath = str(filePath)

            with open(finalPath, "r") as toolTextFile:
                toolDict = toolTextFile.read()
                dict = literal_eval(toolDict)
            for i in (dict):
                values = list(dict[i])
                values.insert(0, i)
                list4.append(values)
            if check == "":

                toolDataBase(1)
            else:
                self.availablePartsListBox.delete(0, END)
                res = []

                for x in list4:
                    test1 = x[0]
                    test2 = x[1]
                    test3 = x[2]
                    if test1.startswith(check) or test2.startswith(check) or test3.startswith(check):
                        res.append(x)
                if self.brandCombobox.get() == "OMER" or self.brandCombobox.get() == "SENCO":
                    for i in res:
                        i.pop(0)
                        self.availablePartsListBox.insert(END, i)
                else:
                    for i in res:
                        self.availablePartsListBox.insert(END, i)

        def schemFetch():
            modelFix = re.sub('[/!@#$.]', '', self.modelCombobox.get())
            filename = os.getcwd() + '/Schematics/' + \
                self.brandCombobox.get() + modelFix + '.pdf'
            os.startfile(filename)
            return 0

        def toolDataBase(event):

            self.availablePartsListBox.delete(0, END)
            b = self.brandCombobox.get()
            m = re.sub('[/]', '@', self.modelCombobox.get())
            filePath = path + "/" + "TOOL_DATABASE" + "/" + b + "/" + m
            finalPath = str(filePath)

            with open(finalPath, "r") as toolTextFile:
                toolDict = toolTextFile.read()
                dict = literal_eval(toolDict)

            for i in (dict):
                if self.brandCombobox.get() == "OMER" or self.brandCombobox.get() == "SENCO":
                    values = list(dict[i])
                    self.availablePartsListBox.insert(END, values)
                else:
                    values = list(dict[i])
                    values.insert(0, i)
                    self.availablePartsListBox.insert(END, values)

        def DBtoolDataBase(event):

            self.DBScrolledlistbox.delete(0, END)
            b = self.DBBrandTCombobox.get()
            m = re.sub('[/]', '@', self.DBModelTCombobox.get())
            filePath = path + "/" + "TOOL_DATABASE" + "/" + b + "/" + m
            finalPath = str(filePath)

            with open(finalPath, "r") as toolTextFile:
                toolDict = toolTextFile.read()
                dict = literal_eval(toolDict)

            for i in (dict):
                values = list(dict[i])
                values.insert(0, i)
                self.DBScrolledlistbox.insert(END, values)

        def doPopUp(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()

        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
            self.style.configure('.', background=_bgcolor)
            self.style.configure('.', foreground=_fgcolor)
            self.style.configure('.', font="TkDefaultFont")
            self.style.map('.', background=[
                ('selected', _compcolor), ('active', _ana2color)])

            top.geometry("564x474+848+353")
            top.minsize(120, 1)
            top.maxsize(5564, 1901)
            top.resizable(1,  1)
            top.title("New Toplevel")
            top.configure(background="#d9d9d9")
            top.configure(highlightbackground="#d9d9d9")
            top.configure(highlightcolor="black")
            top.title("MePod v3.00 -ALPHA")
            top.iconbitmap(str(path + '/EXE builder/icon.ico'))

        global _images
        _images = (

            tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

            tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

            tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
                                  ("active", "pressed",
                                   "!disabled", "img_closepressed"),
                                  ("active", "alternate", "!disabled",
                                   "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                                {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
             {"sticky": "nswe",
              "children": [
                  ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                                                "left", "sticky": ''}),
                                    ("ClosetabNotebook.close", {"side":
                                                                "left", "sticky": ''}), ]})]})]})])
        m = Menu(root, tearoff=0)
        m.add_command(label="Edit", command=edSel)
        m.add_command(label="Delete", command=deleteFromList)

        PNOTEBOOK = "ClosetabNotebook"

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=[
                       ('selected', _compcolor), ('active', _ana2color)])
        self.PNotebook1 = ttk.Notebook(top)
        self.PNotebook1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.PNotebook1.configure(style=PNOTEBOOK)
        self.PNotebook1_t2 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t2, padding=3)
        self.PNotebook1.tab(0, text="Parts Order",
                            compound="left", underline="-1",)
        self.PNotebook1_t2.configure(background="#d9d9d9")
        self.PNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t2.configure(highlightcolor="black")
        self.PNotebook1_t1 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        self.PNotebook1.tab(1, text="Data Base",
                            compound="left", underline="-1",)
        self.PNotebook1_t1.configure(background="#d9d9d9")
        self.PNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t1.configure(highlightcolor="black")
        self.PNotebook1_t3 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t3, padding=3)
        self.PNotebook1.tab(2, text="Email", compound="none", underline="-1",)
        self.PNotebook1_t3.configure(background="#d9d9d9")
        self.PNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t3.configure(highlightcolor="black")
        self.PNotebook1_t4 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t4, padding=3)
        self.PNotebook1.tab(3, text="Settings",
                            compound="none", underline="-1",)
        self.PNotebook1_t4.configure(background="#d9d9d9")
        self.PNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t4.configure(highlightcolor="black")
        self.PNotebook1.bind('<1>', hideTab)

        self.TLabelframe1 = ttk.Labelframe(self.PNotebook1_t2)
        self.TLabelframe1.place(relx=0.513, rely=0.353,
                                relheight=0.542, relwidth=0.461)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''Current Selected Parts''')

        self.finalListbox = ScrolledListBox(self.TLabelframe1)
        self.finalListbox.place(
            relx=0.0, rely=0.082, relheight=0.905, relwidth=1.004, bordermode='ignore')
        self.finalListbox.configure(background="white")
        self.finalListbox.configure(cursor="hand2")
        self.finalListbox.configure(disabledforeground="#a3a3a3")
        self.finalListbox.configure(font="TkFixedFont")
        self.finalListbox.configure(foreground="black")
        self.finalListbox.configure(highlightbackground="#d9d9d9")
        self.finalListbox.configure(highlightcolor="#d9d9d9")
        self.finalListbox.configure(selectbackground="blue")
        self.finalListbox.configure(selectforeground="white")
        self.finalListbox.bind('<Double-1>', doPopUp)
        self.finalListbox.bind('<Delete>', deleteFromList)
        self.finalListbox.bind('<Return>', editSelection)

        for values in (finalPartsList):
            self.finalListbox.insert(END, values)

        self.TLabelframe3 = ttk.Labelframe(self.PNotebook1_t2)
        self.TLabelframe3.place(relx=0.018, rely=0.022,
                                relheight=0.261, relwidth=0.477)
        self.TLabelframe3.configure(relief='')
        self.TLabelframe3.configure(text='''Tool Select''')

        self.brandCombobox = ttk.Combobox(self.TLabelframe3)
        self.brandCombobox.place(
            relx=0.041, rely=0.35, relheight=0.205, relwidth=0.929, bordermode='ignore')
        self.brandCombobox.configure(takefocus="")
        self.brandCombobox.configure(values=getBrands())
        self.brandCombobox.bind("<<ComboboxSelected>>", modelList)

        self.Label1 = tk.Label(self.TLabelframe3)
        self.Label1.place(relx=0.041, rely=0.179, height=13,
                          width=60, bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Brand:''')

        self.Label2 = tk.Label(self.TLabelframe3)
        self.Label2.place(relx=0.041, rely=0.615, height=14,
                          width=60, bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Model:''')

        self.modelCombobox = ttk.Combobox(self.TLabelframe3)
        self.modelCombobox.place(
            relx=0.041, rely=0.795, relheight=0.205, relwidth=0.929, bordermode='ignore')
        # self.modelCombobox.configure(textvariable=)
        self.modelCombobox.configure(takefocus="")
        self.modelCombobox.configure(values=ListB)
        self.modelCombobox.bind("<<ComboboxSelected>>", toolDataBase)

        self.Button2 = tk.Button(self.TLabelframe3)
        self.Button2.place(relx=0.554, rely=0.0, height=34,
                           width=107, bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Open Schematic''')
        self.Button2.configure(command=schemFetch)

        self.TLabelframe4 = ttk.Labelframe(self.PNotebook1_t2)
        self.TLabelframe4.place(relx=0.518, rely=0.022,
                                relheight=0.254, relwidth=0.477)
        self.TLabelframe4.configure(relief='')
        self.TLabelframe4.configure(text='''Shipping and Biiling''')

        self.TLabel1 = ttk.Label(self.TLabelframe4)
        self.TLabel1.place(relx=0.052, rely=0.149, height=15,
                           width=77, bordermode='ignore')
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Ship To:''')

        self.TLabel2 = ttk.Label(self.TLabelframe4)
        self.TLabel2.place(relx=0.037, rely=0.614, height=16,
                           width=64, bordermode='ignore')
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Bill To:''')

        self.ClearButton = tk.Button(self.TLabelframe4)
        self.ClearButton.place(relx=0.655, rely=0.0,
                               height=24, width=77, bordermode='ignore')
        self.ClearButton.configure(activebackground="#ececec")
        self.ClearButton.configure(activeforeground="#000000")
        self.ClearButton.configure(background="#d9d9d9")
        self.ClearButton.configure(disabledforeground="#a3a3a3")
        self.ClearButton.configure(foreground="#000000")
        self.ClearButton.configure(highlightbackground="#d9d9d9")
        self.ClearButton.configure(highlightcolor="black")
        self.ClearButton.configure(pady="0")
        self.ClearButton.configure(text='''Clear All''')
        self.ClearButton.configure(command=clearAllFields)

        self.shipCombobox = ttk.Combobox(self.TLabelframe4)
        self.shipCombobox.place(
            relx=0.037, rely=0.351, relheight=0.211, relwidth=0.929, bordermode='ignore')
        self.shipCombobox.configure(values=shipList())
        self.shipCombobox.configure(takefocus="")

        self.billCombobox = ttk.Combobox(self.TLabelframe4)
        self.billCombobox.place(
            relx=0.037, rely=0.789, relheight=0.211, relwidth=0.929, bordermode='ignore')
        self.billCombobox.configure(values=billList())
        self.billCombobox.configure(takefocus="")

        self.PNotebook2 = ttk.Notebook(self.PNotebook1_t2)
        self.PNotebook2.place(relx=0.0, rely=0.301,
                              relheight=0.688, relwidth=0.502)
        self.PNotebook2.configure(style=PNOTEBOOK)
        self.PNotebook2_t2 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t2, padding=3)
        self.PNotebook2.tab(0, text="Available Parts",
                            compound="left", underline="-1", )
        self.PNotebook2_t2.configure(background="#d9d9d9")
        self.PNotebook2_t2.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t2.configure(highlightcolor="black")
        self.PNotebook2_t1 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t1, padding=3)
        self.PNotebook2.tab(1, text="Custom Parts",
                            compound="left", underline="-1", )
        self.PNotebook2_t1.configure(background="#d9d9d9")
        self.PNotebook2_t1.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t1.configure(highlightcolor="black")
        self.PNotebook2_t3 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t3, padding=3)
        self.PNotebook2.tab(2, text="Edit", compound="none", underline="-1",)
        self.PNotebook2_t3.configure(background="#d9d9d9")
        self.PNotebook2_t3.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t3.configure(highlightcolor="black")
        self.PNotebook2.hide(self.PNotebook2_t3)
        self.PNotebook2.bind('<1>', hideTab)

        self.availablePartsListBox = ScrolledListBox(self.PNotebook2_t2)
        self.availablePartsListBox.place(
            relx=0.0, rely=0.174, relheight=0.837, relwidth=0.968)
        self.availablePartsListBox.configure(background="white")
        self.availablePartsListBox.configure(cursor="hand2")
        self.availablePartsListBox.configure(disabledforeground="#a3a3a3")
        self.availablePartsListBox.configure(font="TkFixedFont")
        self.availablePartsListBox.configure(foreground="black")
        self.availablePartsListBox.configure(highlightbackground="#d9d9d9")
        self.availablePartsListBox.configure(highlightcolor="#d9d9d9")
        self.availablePartsListBox.configure(selectbackground="blue")
        self.availablePartsListBox.configure(selectforeground="white")
        self.availablePartsListBox.bind('<Double-1>', selectFromList)
        self.availablePartsListBox.bind('<Return>', selectFromList)

        var = tk.StringVar()
        var.trace("w", lambda name, index, mode, var=var: callback(var))

        self.partSearchEntry = ttk.Entry(self.PNotebook2_t2)
        self.partSearchEntry.place(
            relx=0.036, rely=0.074, relheight=0.074, relwidth=0.924)
        self.partSearchEntry.configure(takefocus="")
        self.partSearchEntry.configure(cursor="ibeam")
        self.partSearchEntry.configure(textvariable=var)

        self.TLabel3 = ttk.Label(self.PNotebook2_t2)
        self.TLabel3.place(relx=0.036, rely=0.0, height=20, width=64)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Part Search''')

        self.Label3 = tk.Label(self.PNotebook2_t1)
        self.Label3.place(relx=0.0, rely=0.071, height=20, width=113)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Schematic Number:''')

        self.cusSchemNum = tk.Entry(self.PNotebook2_t1)
        self.cusSchemNum.place(relx=0.43, rely=0.071,
                               height=20, relwidth=0.556)
        self.cusSchemNum.configure(background="white")
        self.cusSchemNum.configure(disabledforeground="#a3a3a3")
        self.cusSchemNum.configure(font="TkFixedFont")
        self.cusSchemNum.configure(foreground="#000000")
        self.cusSchemNum.configure(highlightbackground="#d9d9d9")
        self.cusSchemNum.configure(highlightcolor="black")
        self.cusSchemNum.configure(insertbackground="black")
        self.cusSchemNum.configure(selectbackground="blue")
        self.cusSchemNum.configure(selectforeground="white")

        self.Label4 = tk.Label(self.PNotebook2_t1)
        self.Label4.place(relx=0.0, rely=0.209, height=21, width=83)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Part Number:''')

        self.cusPartNum = tk.Entry(self.PNotebook2_t1)
        self.cusPartNum.place(relx=0.43, rely=0.209, height=20, relwidth=0.556)
        self.cusPartNum.configure(background="white")
        self.cusPartNum.configure(disabledforeground="#a3a3a3")
        self.cusPartNum.configure(font="TkFixedFont")
        self.cusPartNum.configure(foreground="#000000")
        self.cusPartNum.configure(highlightbackground="#d9d9d9")
        self.cusPartNum.configure(highlightcolor="black")
        self.cusPartNum.configure(insertbackground="black")
        self.cusPartNum.configure(selectbackground="blue")
        self.cusPartNum.configure(selectforeground="white")

        self.Label5 = tk.Label(self.PNotebook2_t1)
        self.Label5.place(relx=0.0, rely=0.351, height=20, width=73)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Description:''')

        self.cusDescription = tk.Entry(self.PNotebook2_t1)
        self.cusDescription.place(
            relx=0.036, rely=0.454, height=20, relwidth=0.953)
        self.cusDescription.configure(background="white")
        self.cusDescription.configure(disabledforeground="#a3a3a3")
        self.cusDescription.configure(font="TkFixedFont")
        self.cusDescription.configure(foreground="#000000")
        self.cusDescription.configure(highlightbackground="#d9d9d9")
        self.cusDescription.configure(highlightcolor="black")
        self.cusDescription.configure(insertbackground="black")
        self.cusDescription.configure(selectbackground="blue")
        self.cusDescription.configure(selectforeground="white")
        self.cusDescription.bind("<Return>", addCusB)

        self.Button1 = tk.Button(self.PNotebook2_t1)
        self.Button1.place(relx=0.606, rely=0.56, height=114, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Part''')
        self.Button1.configure(command=addCus)

        self.Label6 = tk.Label(self.PNotebook2_t3)
        self.Label6.place(relx=0.65, rely=0.142, height=11, width=64)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Quantitiy:''')

        self.QEntry = tk.Entry(self.PNotebook2_t3)
        self.QEntry.place(relx=0.686, rely=0.213, height=20, relwidth=0.303)
        self.QEntry.configure(background="white")
        self.QEntry.configure(disabledforeground="#a3a3a3")
        self.QEntry.configure(font="TkFixedFont")
        self.QEntry.configure(foreground="#000000")
        self.QEntry.configure(highlightbackground="#d9d9d9")
        self.QEntry.configure(highlightcolor="black")
        self.QEntry.configure(insertbackground="black")
        self.QEntry.configure(selectbackground="blue")
        self.QEntry.configure(selectforeground="white")
        self.QEntry.bind('<Return>', editPartB)

        self.updateButton = tk.Button(self.PNotebook2_t3)
        self.updateButton.place(relx=0.722, rely=0.319, height=74, width=67)
        self.updateButton.configure(activebackground="#ececec")
        self.updateButton.configure(activeforeground="#000000")
        self.updateButton.configure(background="#d9d9d9")
        self.updateButton.configure(disabledforeground="#a3a3a3")
        self.updateButton.configure(foreground="#000000")
        self.updateButton.configure(highlightbackground="#d9d9d9")
        self.updateButton.configure(highlightcolor="black")
        self.updateButton.configure(pady="0")
        self.updateButton.configure(text='''Update''')
        self.updateButton.configure(command=editPart)

        self.removeButton = tk.Button(self.PNotebook2_t3)
        self.removeButton.place(relx=0.036, rely=0.638, height=94, width=107)
        self.removeButton.configure(activebackground="#ececec")
        self.removeButton.configure(activeforeground="#000000")
        self.removeButton.configure(background="#d9d9d9")
        self.removeButton.configure(disabledforeground="#a3a3a3")
        self.removeButton.configure(foreground="#000000")
        self.removeButton.configure(highlightbackground="#d9d9d9")
        self.removeButton.configure(highlightcolor="black")
        self.removeButton.configure(pady="0")
        self.removeButton.configure(text='''Remove''')
        self.removeButton.configure(command=removeFromList)

        self.cb = BooleanVar()

        self.Checkbutton1 = tk.Checkbutton(self.PNotebook2_t1)
        self.Checkbutton1.place(relx=0.036, rely=0.908,
                                relheight=0.089, relwidth=0.433)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Add To Database''')
        self.Checkbutton1.configure(variable=che81)
        self.Checkbutton1.configure(variable=self.cb)

        self.TSeparator1 = ttk.Separator(self.PNotebook1_t2)
        self.TSeparator1.place(relx=0.504, rely=0.0,  relheight=0.987)
        self.TSeparator1.configure(orient="vertical")

        self.TSeparator2 = ttk.Separator(self.PNotebook1_t2)
        self.TSeparator2.place(relx=0.0, rely=0.0,  relwidth=0.989)

        self.TSeparator3 = ttk.Separator(self.PNotebook1_t2)
        self.TSeparator3.place(relx=-0.002, rely=0.301,  relwidth=1.007)

        self.pdfButton = tk.Button(self.PNotebook1_t2)
        self.pdfButton.place(relx=0.53, rely=0.904, height=34, width=247)
        self.pdfButton.configure(activebackground="#ececec")
        self.pdfButton.configure(activeforeground="#000000")
        self.pdfButton.configure(background="#d9d9d9")
        self.pdfButton.configure(disabledforeground="#a3a3a3")
        self.pdfButton.configure(foreground="#000000")
        self.pdfButton.configure(highlightbackground="#d9d9d9")
        self.pdfButton.configure(highlightcolor="black")
        self.pdfButton.configure(pady="0")
        self.pdfButton.configure(text='''Save To PDF''')
        self.pdfButton.configure(command=pdfMaker)

        self.PNotebook1_t2_1 = tk.Frame(self.PNotebook1_t1)
        self.PNotebook1_t2_1.place(
            relx=0.0, rely=0.0, relheight=0.002, relwidth=0.002)
        self.PNotebook1_t2_1.configure(background="#d9d9d9")
        self.PNotebook1_t2_1.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t2_1.configure(highlightcolor="black")

        self.TLabelframe1_1 = ttk.Labelframe(self.PNotebook1_t2_1)
        self.TLabelframe1_1.place(
            relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TLabelframe1_1.configure(relief='')
        self.TLabelframe1_1.configure(text='''Current Selected Parts''')

        self.TLabelframe3_1 = ttk.Labelframe(self.PNotebook1_t2_1)
        self.TLabelframe3_1.place(
            relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TLabelframe3_1.configure(relief='')
        self.TLabelframe3_1.configure(text='''Tool Select''')

        self.Label1_1 = tk.Label(self.TLabelframe3_1)
        self.Label1_1.place(relx=0.0, rely=0.0, height=1,
                            width=1, bordermode='ignore')
        self.Label1_1.configure(activebackground="#f9f9f9")
        self.Label1_1.configure(activeforeground="black")
        self.Label1_1.configure(background="#d9d9d9")
        self.Label1_1.configure(disabledforeground="#a3a3a3")
        self.Label1_1.configure(foreground="#000000")
        self.Label1_1.configure(highlightbackground="#d9d9d9")
        self.Label1_1.configure(highlightcolor="black")
        self.Label1_1.configure(text='''Brand:''')

        self.Label2_1 = tk.Label(self.TLabelframe3_1)
        self.Label2_1.place(relx=0.0, rely=1.0, height=1,
                            width=1, bordermode='ignore')
        self.Label2_1.configure(activebackground="#f9f9f9")
        self.Label2_1.configure(activeforeground="black")
        self.Label2_1.configure(background="#d9d9d9")
        self.Label2_1.configure(disabledforeground="#a3a3a3")
        self.Label2_1.configure(foreground="#000000")
        self.Label2_1.configure(highlightbackground="#d9d9d9")
        self.Label2_1.configure(highlightcolor="black")
        self.Label2_1.configure(text='''Model:''')

        self.Button2_1 = tk.Button(self.TLabelframe3_1)
        self.Button2_1.place(relx=1.0, rely=0.0, height=34,
                             width=107, bordermode='ignore')
        self.Button2_1.configure(activebackground="#ececec")
        self.Button2_1.configure(activeforeground="#000000")
        self.Button2_1.configure(background="#d9d9d9")
        self.Button2_1.configure(disabledforeground="#a3a3a3")
        self.Button2_1.configure(foreground="#000000")
        self.Button2_1.configure(highlightbackground="#d9d9d9")
        self.Button2_1.configure(highlightcolor="black")
        self.Button2_1.configure(pady="0")
        self.Button2_1.configure(text='''Open Schematic''')

        self.TLabelframe4_1 = ttk.Labelframe(self.PNotebook1_t2_1)
        self.TLabelframe4_1.place(
            relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TLabelframe4_1.configure(relief='')
        self.TLabelframe4_1.configure(text='''Shipping and Biiling''')

        self.TLabel1_1 = ttk.Label(self.TLabelframe4_1)
        self.TLabel1_1.place(relx=0.0, rely=0.0, height=1,
                             width=1, bordermode='ignore')
        self.TLabel1_1.configure(background="#d9d9d9")
        self.TLabel1_1.configure(foreground="#000000")
        self.TLabel1_1.configure(relief="flat")
        self.TLabel1_1.configure(anchor='w')
        self.TLabel1_1.configure(justify='left')
        self.TLabel1_1.configure(text='''Ship To:''')

        self.TLabel2_1 = ttk.Label(self.TLabelframe4_1)
        self.TLabel2_1.place(relx=0.0, rely=1.0, height=1,
                             width=1, bordermode='ignore')
        self.TLabel2_1.configure(background="#d9d9d9")
        self.TLabel2_1.configure(foreground="#000000")
        self.TLabel2_1.configure(relief="flat")
        self.TLabel2_1.configure(anchor='w')
        self.TLabel2_1.configure(justify='left')
        self.TLabel2_1.configure(text='''Bill To:''')

        self.ClearButton_1 = tk.Button(self.TLabelframe4_1)
        self.ClearButton_1.place(
            relx=1.0, rely=0.0, height=24, width=87, bordermode='ignore')
        self.ClearButton_1.configure(activebackground="#ececec")
        self.ClearButton_1.configure(activeforeground="#000000")
        self.ClearButton_1.configure(background="#d9d9d9")
        self.ClearButton_1.configure(disabledforeground="#a3a3a3")
        self.ClearButton_1.configure(foreground="#000000")
        self.ClearButton_1.configure(highlightbackground="#d9d9d9")
        self.ClearButton_1.configure(highlightcolor="black")
        self.ClearButton_1.configure(pady="0")
        self.ClearButton_1.configure(text='''Clear All''')

        self.hiddenEntry = tk.Entry(self.PNotebook2_t3)
        self.hiddenEntry.place(relx=0.83, rely=0.035,
                               height=20, relwidth=0.123)
        self.hiddenEntry.configure(background="#d7d7d7")
        self.hiddenEntry.configure(cursor="arrow")
        self.hiddenEntry.configure(disabledbackground="#d7d7d7")
        self.hiddenEntry.configure(disabledforeground="#d7d7d7")
        self.hiddenEntry.configure(font="-family {Arial} -size 12")
        self.hiddenEntry.configure(foreground="#d7d7d7")
        self.hiddenEntry.configure(highlightbackground="#d7d7d7")
        self.hiddenEntry.configure(highlightcolor="#d7d7d7")
        self.hiddenEntry.configure(insertbackground="#d7d7d7")
        self.hiddenEntry.configure(readonlybackground="#d7d7d7")
        self.hiddenEntry.configure(relief="flat")
        self.hiddenEntry.configure(selectbackground="#d7d7d7")
        self.hiddenEntry.configure(selectforeground="#d7d7d7")

        self.PNotebook2_1 = ttk.Notebook(self.PNotebook1_t2_1)
        self.PNotebook2_1.place(
            relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.PNotebook2_1.configure(style=PNOTEBOOK)

        self.DBBrandTCombobox = ttk.Combobox(self.PNotebook1_t1)
        self.DBBrandTCombobox.place(
            relx=0.018, rely=0.067, relheight=0.047, relwidth=0.255)
        self.DBBrandTCombobox.configure(takefocus="")
        self.DBBrandTCombobox.configure(values=DBgetBrands())
        self.DBBrandTCombobox.bind("<<ComboboxSelected>>", DBmodelList)

        self.DBModelTCombobox = ttk.Combobox(self.PNotebook1_t1)
        self.DBModelTCombobox.place(
            relx=0.304, rely=0.067, relheight=0.047, relwidth=0.255)
        self.DBModelTCombobox.configure(takefocus="")
        self.DBModelTCombobox.bind("<<ComboboxSelected>>", DBtoolDataBase)
        self.DBModelTCombobox.bind('<Return>', DBtoolDataBase)

        self.DBTLabel1 = ttk.Label(self.PNotebook1_t1)
        self.DBTLabel1.place(relx=0.018, rely=0.022, height=19, width=45)
        self.DBTLabel1.configure(background="#d9d9d9")
        self.DBTLabel1.configure(foreground="#000000")
        self.DBTLabel1.configure(font="TkDefaultFont")
        self.DBTLabel1.configure(relief="flat")
        self.DBTLabel1.configure(anchor='w')
        self.DBTLabel1.configure(justify='left')
        self.DBTLabel1.configure(text='''Brand:''')

        self.DBTLabel2 = ttk.Label(self.PNotebook1_t1)
        self.DBTLabel2.place(relx=0.304, rely=0.022, height=19, width=46)
        self.DBTLabel2.configure(background="#d9d9d9")
        self.DBTLabel2.configure(foreground="#000000")
        self.DBTLabel2.configure(font="TkDefaultFont")
        self.DBTLabel2.configure(relief="flat")
        self.DBTLabel2.configure(anchor='w')
        self.DBTLabel2.configure(justify='left')
        self.DBTLabel2.configure(text='''Model:''')

        self.TNotebook1 = ttk.Notebook(self.PNotebook1_t1)
        self.TNotebook1.place(relx=0.0, rely=0.134,
                              relheight=0.304, relwidth=1.007)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Simple Entry",
                            compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Speed Entry",
                            compound="left", underline="-1",)
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.DBTLabel3 = ttk.Label(self.TNotebook1_t1)
        self.DBTLabel3.place(relx=0.0, rely=0.182, height=20, width=115)
        self.DBTLabel3.configure(background="#d9d9d9")
        self.DBTLabel3.configure(foreground="#000000")
        self.DBTLabel3.configure(font="TkDefaultFont")
        self.DBTLabel3.configure(relief="flat")
        self.DBTLabel3.configure(anchor='w')
        self.DBTLabel3.configure(justify='left')
        self.DBTLabel3.configure(text='''Shematic Number:''')

        self.DBTLabel4 = ttk.Label(self.TNotebook1_t1)
        self.DBTLabel4.place(relx=0.268, rely=0.145, height=29, width=85)
        self.DBTLabel4.configure(background="#d9d9d9")
        self.DBTLabel4.configure(foreground="#000000")
        self.DBTLabel4.configure(font="TkDefaultFont")
        self.DBTLabel4.configure(relief="flat")
        self.DBTLabel4.configure(anchor='w')
        self.DBTLabel4.configure(justify='left')
        self.DBTLabel4.configure(text='''Part Number:''')

        self.DBTLabel5 = ttk.Label(self.TNotebook1_t1)
        self.DBTLabel5.place(relx=0.0, rely=0.545, height=23, width=76)
        self.DBTLabel5.configure(background="#d9d9d9")
        self.DBTLabel5.configure(foreground="#000000")
        self.DBTLabel5.configure(font="TkDefaultFont")
        self.DBTLabel5.configure(relief="flat")
        self.DBTLabel5.configure(anchor='w')
        self.DBTLabel5.configure(justify='left')
        self.DBTLabel5.configure(text='''Description:''')

        self.DBSchemEntry = ttk.Entry(self.TNotebook1_t1)
        self.DBSchemEntry.place(relx=0.0, rely=0.364,
                                relheight=0.191, relwidth=0.225)
        self.DBSchemEntry.configure(takefocus="")
        self.DBSchemEntry.configure(cursor="ibeam")

        self.DBPartEntry = ttk.Entry(self.TNotebook1_t1)
        self.DBPartEntry.place(relx=0.25, rely=0.364,
                               relheight=0.191, relwidth=0.225)
        self.DBPartEntry.configure(takefocus="")
        self.DBPartEntry.configure(cursor="ibeam")

        self.DBDesEntry = ttk.Entry(self.TNotebook1_t1)
        self.DBDesEntry.place(relx=0.0, rely=0.727,
                              relheight=0.191, relwidth=0.993)
        self.DBDesEntry.configure(takefocus="")
        self.DBDesEntry.configure(cursor="ibeam")
        self.DBDesEntry.bind('<Return>', DBAdd)

        self.DBAddBuuton = ttk.Button(self.TNotebook1_t1)
        self.DBAddBuuton.place(relx=0.518, rely=0.273, height=35, width=196)
        self.DBAddBuuton.configure(takefocus="")
        self.DBAddBuuton.configure(text='''ADD/UPDATE''')
        self.DBAddBuuton.configure(command=DBdataAddcus)

        self.DBSpeedEntry = ttk.Entry(self.TNotebook1_t2)
        self.DBSpeedEntry.place(relx=0.018, rely=0.573,
                                relheight=0.191, relwidth=0.957)
        self.DBSpeedEntry.configure(takefocus="")
        self.DBSpeedEntry.configure(cursor="ibeam")
        self.DBSpeedEntry.bind("<Return>", DBspeed)

        self.DBTLabel6 = ttk.Label(self.TNotebook1_t2)
        self.DBTLabel6.place(relx=0.089, rely=0.0, height=30, width=135)
        self.DBTLabel6.configure(background="#d9d9d9")
        self.DBTLabel6.configure(foreground="#000000")
        self.DBTLabel6.configure(font="TkDefaultFont")
        self.DBTLabel6.configure(relief="flat")
        self.DBTLabel6.configure(anchor='w')
        self.DBTLabel6.configure(justify='left')
        self.DBTLabel6.configure(text='''syntax for speed entry is''')

        self.DBTLabel7 = ttk.Label(self.TNotebook1_t2)
        self.DBTLabel7.place(relx=0.018, rely=0.282, height=30, width=315)
        self.DBTLabel7.configure(background="#d9d9d9")
        self.DBTLabel7.configure(foreground="#000000")
        self.DBTLabel7.configure(font="TkDefaultFont")
        self.DBTLabel7.configure(relief="flat")
        self.DBTLabel7.configure(anchor='w')
        self.DBTLabel7.configure(justify='left')
        self.DBTLabel7.configure(
            text='''ShematicNumber   PartNumber   Description''')

        self.DBTLabel8 = ttk.Label(self.TNotebook1_t2)
        self.DBTLabel8.place(relx=0.643, rely=0.145, height=30, width=186)
        self.DBTLabel8.configure(background="#d9d9d9")
        self.DBTLabel8.configure(foreground="#ff0000")
        self.DBTLabel8.configure(font="TkDefaultFont")
        self.DBTLabel8.configure(relief="flat")
        self.DBTLabel8.configure(anchor='w')
        self.DBTLabel8.configure(justify='left')
        self.DBTLabel8.configure(text='''*must be seperated by one space*''')

        self.DBScrolledlistbox = ScrolledListBox(self.PNotebook1_t1)
        self.DBScrolledlistbox.place(
            relx=0.0, rely=0.446, relheight=0.547, relwidth=1.002)
        self.DBScrolledlistbox.configure(background="white")
        self.DBScrolledlistbox.configure(cursor="hand2")
        self.DBScrolledlistbox.configure(disabledforeground="#a3a3a3")
        self.DBScrolledlistbox.configure(font="TkFixedFont")
        self.DBScrolledlistbox.configure(foreground="black")
        self.DBScrolledlistbox.configure(highlightbackground="#d9d9d9")
        self.DBScrolledlistbox.configure(highlightcolor="#d9d9d9")
        self.DBScrolledlistbox.configure(selectbackground="blue")
        self.DBScrolledlistbox.configure(selectforeground="white")
        self.DBScrolledlistbox.bind('<Double-1>', DBGrabInfo)

        self.DBRefreshButton = ttk.Button(self.PNotebook1_t1)
        self.DBRefreshButton.place(relx=0.821, rely=0.045, height=35, width=86)
        self.DBRefreshButton.configure(takefocus="")
        self.DBRefreshButton.configure(text='''Refresh''')

# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.


def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index


def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
        return
    element = widget.identify(event.x, event.y)
    index = widget.index("@%d,%d" % (event.x, event.y))
    if "close" in element and widget._active == index:
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None


def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

# The following code is added to facilitate the Scrolled widgets you specified.


class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical',
                                command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @ staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind(
            '<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped


class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @ _create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

    def size_(self):
        sz = tk.Listbox.size(self)
        return sz


def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>',
                       lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))


def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')


def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')


def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')


if __name__ == '__main__':
    vp_start_gui()
