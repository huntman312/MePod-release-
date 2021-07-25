from tkinter.constants import COMMAND, END
import platform
import sys
import re
import os
import time
import subprocess
from ast import literal_eval
from typing_extensions import IntVar
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus.paragraph import textTransformFrags
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
import pyautogui
import collections
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import shutil
py3 = True
FILEBROWSER_PATH = os.path.join(os.getenv('WINDIR'), 'explorer.exe')
path = os.getcwd() + "/Dat"
Epath = os.getcwd() + "/Dat/orders to be sent"
finalPartsList = [["TOOL", "QUANTITY", "PART#", "DESCRIPTION"]]
system = sys.platform
DBList = []
BOList = []
CUSTOMER_LIST = []
credlist = []
themes = ['LIGHT', 'DARK', 'GREEN', 'BLUE', 'PINK', 'LIGHT GREEN']
foreground = "white"
background = "#404040"
selected = "#808080"
buttonbackground = "#3f3f3f"
comboboxback = "#808080"


fsetFilePath = path + "/" + "vis"
ffilePath = str(fsetFilePath)
fsetfile = open(ffilePath, "r")
fList = fsetfile.read()
themeList = fList.split(",")
try:
    int(themeList[0])
    size = themeList[0]
    font = "-size " + size
except ValueError:
    font = "-size 10"
    themeList.insert(0, "10")
try:
    themeselect = themeList[1]
except IndexError:
    themeselect = ''

if themeselect == "DARK":
    foreground = "white"
    background = "#404040"
    selected = "#808080"
    buttonbackground = "#3f3f3f"
    comboboxback = "#808080"
elif themeselect == "GREEN":
    foreground = "red"
    background = "#002f00"
    selected = "#002200"
    buttonbackground = "#005100"
    comboboxback = "#005100"
elif themeselect == "BLUE":
    foreground = "#ffd6c1"
    background = "#5757fd"
    selected = "#1d1dfc"
    buttonbackground = "#005100"
    comboboxback = "#5757fd"
elif themeselect == "PINK":
    foreground = "black"
    background = "#ffdfe0"
    selected = "#ffb3b3"
    buttonbackground = "#3f3f3f"
    comboboxback = "#ffdfe0"
elif themeselect == "LIGHT GREEN":
    foreground = "black"
    background = "#e2ffe1"
    selected = "#b3ffb0"
    buttonbackground = "#3f3f3f"
    comboboxback = "#e2ffe1"
else:
    foreground = "black"
    background = "white"
    selected = "#ffb3b3"
    buttonbackground = "#3f3f3f"
    comboboxback = "white"


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
        setFilePath = path + "/" + "settings"
        filePath = str(setFilePath)
        setfile = open(filePath, "r")
        customerList = setfile.read()
        CUSTOMER_LIST = customerList.split(",")

        csetFilePath = path + "/" + "cred"
        cfilePath = str(csetFilePath)
        csetfile = open(cfilePath, "r")
        cList = csetfile.read()
        credlist = cList.split(",")

        self.special = 0

        def openExplorer():
            Opath = os.path.normpath(os.getcwd())
            subprocess.run([FILEBROWSER_PATH, Opath])

        def veiworder2():
            index = self.EScrolledlistbox2.curselection()[0]
            file_name = self.EScrolledlistbox2.get(index)
            file_path = Epath + "/" + file_name
            os.startfile(file_path)
            self.special = 0

        def veiwOrder():
            index = self.EScrolledlistbox1.curselection()[0]
            file_name = self.EScrolledlistbox1.get(index)
            file_path = Epath + "/" + file_name
            os.startfile(file_path)
            self.special = 0

        def orderDel():
            index = self.EScrolledlistbox1.curselection()[0]
            file_path = Epath + "/" + self.EScrolledlistbox1.get(index)
            os.remove(file_path)
            tpath = path + "/" + "MASTER/temp/" + \
                self.EScrolledlistbox1.get(index)[13:]
            fpath = tpath[:-15]
            os.remove(fpath)
            self.EScrolledlistbox1.delete(index)
            self.special = 0

        def savecred():
            user = self.EEntry1.get()
            PASS = self.EEntry2.get()
            if self.ecb.get() == True:
                str1 = ""
                list1 = []
                list1.append("1")
                list1.append(user)
                list1.append(PASS)
                for x in list1:
                    str1 += x
                    str1 += ","
                finalstr = str1[:-1]
                setFile = open(path + "/" + "cred", "w")
                n = setFile.write(finalstr)
                setFile.close()
            else:
                os.remove(path + "/" + "cred")
                str1 = "0"
                setFile = open(path + "/" + "cred", "w")
                n = setFile.write(str1)
                setFile.close()

        def movefiles():
            for i in self.EScrolledlistbox2.get(0, END):
                shutil.move(path + "/temp/" + i, path + "/sent/" + i)
            self.EScrolledlistbox2.delete(0, END)

        def premove():
            for i in self.EScrolledlistbox2.get(0, END):
                shutil.move(Epath + "/" + i, path + "/temp/" + i)

        def selectpdf(event):
            if self.special == 0:
                try:
                    index = self.EScrolledlistbox1.curselection()[0]
                    self.EScrolledlistbox2.insert(
                        END, self.EScrolledlistbox1.get(index))
                    self.EScrolledlistbox1.delete(index)
                except IndexError:
                    return 0

        def unselectpdf(event):
            if self.special == 0:
                try:
                    index = self.EScrolledlistbox2.curselection()[0]
                    self.EScrolledlistbox1.insert(
                        END, self.EScrolledlistbox2.get(index))
                    self.EScrolledlistbox2.delete(index)
                except IndexError:
                    return 0

        def saveFinalMaster():
            finalList = list(os.listdir(path + "/MASTER/final"))
            tempList = []
            for i in self.EScrolledlistbox2.get(0, END):
                tempList.append(i[13:-15])
            for tmpCus in tempList:
                isThere = False
                for x in finalList:
                    if x == tmpCus:
                        isThere = True
                        break
                if isThere == False:
                    shutil.move(path + "/MASTER/temp/" + tmpCus,
                                path + "/MASTER/final/" + tmpCus)
                else:
                    tempDict = {}
                    finalPath = path + "/MASTER/final/" + tmpCus
                    tempPath = path + "/MASTER/temp/" + tmpCus
                    with open(finalPath, "r") as toolTextFile:
                        Dict1 = toolTextFile.read()
                        olddict = literal_eval(Dict1)
                    with open(tempPath, "r") as toolTextFile:
                        Dict2 = toolTextFile.read()
                        newdict = literal_eval(Dict2)
                    for x in (newdict):
                        values = list(newdict[x])
                        values.insert(0, x)
                        if x in olddict.keys():
                            list1 = list(olddict.get(x))
                            newCount = int(values[2]) + int(list1[1])
                            list1.pop(1)
                            list1.insert(1, str(newCount))
                            tempDict[values[0]
                                     ] = list1[0], list1[1], list1[2], list1[3]
                            olddict.pop(x)
                        else:
                            tempDict[values[0]
                                     ] = values[1], values[2], values[3], values[4]
                    finalDict = {**tempDict, **olddict}
                    toolFile = open(finalPath, "w")
                    toolFile.write(str(finalDict))
                    toolFile.close()
                    toolTextFile.close()
                    os.remove(path + "/MASTER/temp/" + tmpCus)

        def collect_mail_info():
            premove()
            saveFinalMaster()
            user = self.EEntry1.get()
            PASS = self.EEntry2.get()
            send_list = list(self.EEntry3.get().split(","))
            subject = self.EEntry4.get()
            body = self.EScrolledtext.get("1.0", END)
            list2 = os.listdir(str(path + "/temp/"))
            send_mail_gmail(user, PASS, send_list, subject, body, list2)
            savecred()

        def send_mail_gmail(user, PASS, send_list, subject="", body="", list2=None):
            s = smtplib.SMTP('smtp.gmail.com:587')
            s.starttls()
            try:
                s.login(user, PASS)
                # s.set_debuglevel(1)
                msg = MIMEMultipart()
                sender = user
                recipients = send_list
                msg['Subject'] = subject
                msg['From'] = sender
                msg['To'] = ", ".join(recipients)
                if list2 is not None:
                    for file_path in list2:
                        final_path = path + "/temp/" + file_path
                        try:
                            with open(final_path, "rb") as fp:
                                part = MIMEBase('application', "octet-stream")
                                part.set_payload((fp).read())
                                # Encoding payload is necessary if encoded (compressed) file has to be attached.
                                encoders.encode_base64(part)
                                part.add_header(
                                    'Content-Disposition', "attachment; filename= %s" % os.path.basename(file_path))
                                msg.attach(part)
                            msg.attach(MIMEText(body, 'html'))
                            fail = False

                        except:
                            self.EMessage.configure(foreground="#f5010a")
                            self.EMessage.configure(
                                text='''FAILED_error_code:3''')
                            fail = True
                else:
                    self.EMessage.configure(foreground="#f5010a")
                    self.EMessage.configure(text='''FAILED_error_code:0''')
                    fail = True
                if fail == False:
                    s.sendmail(sender, recipients, msg.as_string())
                    self.EMessage.configure(highlightbackground=background)
                    self.EMessage.configure(text='''sent_successful''')
                    movefiles()
            except:
                self.EMessage.configure(foreground="#f5010a")
                self.EMessage.configure(text='''invalid login crudentials''')

        def keySearch(key):
            counter = 0
            while counter == 0:
                for x in customerList:
                    if x.startswith(key):
                        counter = + customerList.index(x)
            print(counter)

        def keyPressL(*ARGS):
            keySearch("L")

        def addCustomerToListB(*args):
            addCustomerToList()

        def addCustomerToList():
            value = self.SetCustEntry.get().upper()
            isThere = False
            for x in self.SetScrolledlistbox.get(0, END):
                if x == value:
                    isThere = True
            if isThere == False:
                self.SetScrolledlistbox.insert(END, value)
            self.SetCustEntry.delete(0, END)

        def setDelCust():
            self.SetScrolledlistbox.delete(
                self.SetScrolledlistbox.curselection()[0])

        def setSave():
            str1 = ""
            list1 = []
            list2 = []
            name = self.SetNameEntry.get().upper()
            list1.append(name + '\'S HOUSE')
            for x in self.SetScrolledlistbox.get(0, END):
                list2.append(x)

            list2.sort()
            fList = list1 + list2
            CUSTOMER_LIST = fList
            for x in fList:
                str1 += x
                str1 += ","
            finalstr = str1[:-1]
            setFile = open(path + "/" + "settings", "w")
            n = setFile.write(finalstr)
            setFile.close()

            str2 = ""
            if self.FontCombobox1.get() == "":
                str2 += themeList[0]
                str2 += ","
            else:
                str2 += self.FontCombobox1.get()
                str2 += ","
            if self.ThemeCombobox2.get() == "":
                str2 += themeList[1]
                str2 += ","
            else:
                str2 += self.ThemeCombobox2.get()
                str2 += ","
            ffinalstr = str2[:-1]
            setFile = open(path + "/" + "vis", "w")
            n = setFile.write(ffinalstr)
            setFile.close()
            root.destroy()

        def setting():
            totalList = shipList()
            name = str(totalList[0])
            nameOnly = name[:-8]
            totalList.pop(0)
            for i in totalList:
                self.SetScrolledlistbox.insert(END, i)
            return nameOnly

        def BOBack():
            self.TNotebook2.select(self.TNotebook2_t2)

        def BOedSel(event):
            if self.special == 0:
                w = event.widget
                try:
                    index = int(w.curselection()[0])
                    self.TNotebook2.select(self.TNotebook2_t1)
                    selected = list(self.BOScrolledlistbox.get(index))
                    self.BOMessage.configure(text=str(selected))
                    actualIndex = BOList.index(selected)
                    self.hiddenEntry.insert(END, actualIndex)
                    self.BOQuantEntry.delete(0, END)
                except IndexError:
                    return 0

        def BOupdateB(*args):
            BOupdate()

        def BOdel():
            index = self.BOScrolledlistbox.curselection()[0]
            self.BOScrolledlistbox.delete(index)
            dict1 = {}
            for x in self.BOScrolledlistbox.get(0, END):
                dict1[x[0]] = x[1], x[2], x[3], x[4]
            os.remove(path + "/" + "MASTER/final/" + self.BOCombobox1.get())
            finalPath = os.path.join(
                path + "/" + "MASTER/final", self.BOCombobox1.get())
            toolFile = open(finalPath, "w")
            toolFile.write(str(dict1))

        def BOupdate():
            getBO(1)
            item = list(self.BOScrolledlistbox.get(
                int(self.hiddenEntry.get())))
            oldcount = item.pop(2)
            newcount = int(oldcount) - int(self.BOQuantEntry.get())
            if newcount <= 0:
                self.BOScrolledlistbox.delete(int(self.hiddenEntry.get()))
                BOList.pop(int(self.hiddenEntry.get()))
            else:
                item.insert(2, str(newcount))
                self.BOScrolledlistbox.delete(int(self.hiddenEntry.get()))
                BOList.pop(int(self.hiddenEntry.get()))
                self.BOScrolledlistbox.insert(
                    int(self.hiddenEntry.get()), item)
                BOList.insert(int(self.hiddenEntry.get()), item)
            self.hiddenEntry.delete(0, END)
            dict1 = {}
            for x in self.BOScrolledlistbox.get(0, END):
                dict1[x[0]] = x[1], x[2], x[3], x[4]
            os.remove(path + "/MASTER/final/" + self.BOCombobox1.get())
            finalPath = os.path.join(
                path + "/MASTER/final", self.BOCombobox1.get())
            toolFile = open(finalPath, "w")
            toolFile.write(str(dict1))

        def getBO(event):
            self.BOEntry1.delete(0, END)
            BOList.clear()
            self.TNotebook2.select(self.TNotebook2_t2)
            self.BOScrolledlistbox.delete(0, END)
            cust = self.BOCombobox1.get()
            filePath = path + "/" + "MASTER/final/" + cust
            finalPath = str(filePath)
            try:
                with open(finalPath, "r") as toolTextFile:
                    toolDict = toolTextFile.read()
                    dict = literal_eval(toolDict)
                for i in (dict):
                    values = list(dict[i])
                    values.insert(0, i)
                    self.BOScrolledlistbox.insert(END, values)
                    BOList.append(values)
            except PermissionError:
                return 0

        def BOCustomerGet():
            return(os.listdir(str(path + "/" + "MASTER/final")))

        def shipList():
            setFilePath = path + "/" + "settings"
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
            try:
                index = int(w.curselection()[0])
                value = w.get(index)
                item = list(value)
                self.DBSchemEntry.insert(END, item[0])
                self.DBPartEntry.insert(END, item[1])
                self.DBDesEntry.insert(END, item[2])
            except IndexError:
                    return 0

        def DBdeleteFromList():
            index = self.DBScrolledlistbox.curselection()[0]
            DBList.pop(index)
            self.DBScrolledlistbox.delete(index)
            brand = self.DBBrandTCombobox.get()
            m = re.sub('[/]', '@', self.DBModelTCombobox.get())
            finalPath = os.path.join(
                path + "/" + "TOOL_DATABASE" + "/" + brand, m)
            finalDict = {}
            for x in DBList:
                finalDict[x[0]] = x[1], x[2]

            toolFile = open(finalPath, "w")
            toolFile.write(str(finalDict))

        def addCusB(*args):
            addCus()

        def addCus():
            shemNum = self.cusSchemNum.get().upper()
            partNum = self.cusPartNum.get().upper()
            des = self.cusDescription.get().upper()
            tool = self.brandCombobox.get().upper() + " " + self.modelCombobox.get().upper()
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

        def dateemailstr():
            date = date_of_order()
            return "parts order " + date

        def saveToMaster(customer1, data, date):
            customer = customer1.lstrip()
            filePath = path + "/" + "MASTER/temp/" + customer
            toolDict = {}
            if os.path.isfile(filePath) == True:
                os.remove(filePath)
                for x in data:
                    key = x[2]
                    tool = x[0]
                    desc = x[3]
                    quant = x[1]
                    if key != "PART#":
                        toolFile = open(filePath, "w")
                        toolDict[key] = tool, quant, desc, date
                        toolFile.write(str(toolDict))
            else:
                for x in data:
                    key = x[2]
                    tool = x[0]
                    desc = x[3]
                    quant = x[1]
                    if key != "PART#":
                        toolFile = open(filePath, "w")
                        toolDict[key] = tool, quant, desc, date
                        toolFile.write(str(toolDict))

            toolFile.close()

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

            if os.path.isfile(save_path) == False:
                self.EScrolledlistbox1.insert(END, pdfName)

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
            saveToMaster(customer, data, dateOfOrder)

        def BOPDF():
            # stuffx = a
            # print(type(stuffx))
            customer = self.BOCombobox1.get().upper()
            dateOfOrder = date_of_order()
            pdfName = dateOfOrder + "(" + customer + ")Parts Waiting.pdf"
            info = [["BACK", "ORDER"], [
                "Customer: ", customer], ["DATE: ", dateOfOrder]]
            dataList = BOList
            data = []
            for i in dataList:
                i.pop(3)
                data.append(i)

            header = ["Part Number", "Tool", "Amount Owed", "Last Ordered"]
            data.insert(0, header)

            dirPath = os.path.expanduser("~/Desktop")
            check = os.path.exists(dirPath)

            if check == False:
                dirPath = os.path.expanduser("~/OneDrive/Desktop")

            save_path = dirPath + "/" + pdfName

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
                    bc = colors.aquamarine
                else:
                    bc = colors.lavender

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

                    ('GRID', (0, 1), (-1, -1), 2, colors.maroon),
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
            index = self.finalListbox.curselection()[0]
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
            try:
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
                    tool = self.brandCombobox.get().upper() + " " + self.modelCombobox.get().upper()
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
            except IndexError:
                    return 0

        def modelList(event):
            self.availablePartsListBox.delete(0, END)
            self.modelCombobox.delete(0, "end")
            sel = self.brandCombobox.get()
            try:
                List1 = os.listdir(path + "/TOOL_DATABASE/" + sel)
                List2 = []
                for x in List1:
                    a = x.replace("@", "/")
                    List2.append(a)

                ListB = List2
                self.modelCombobox.configure(values=ListB)
            except FileNotFoundError:
                return 0

        ListA = os.listdir(str(path + "/" + "TOOL_DATABASE"))
        ListB = []

        def DBmodelList(event):
            self.DBScrolledlistbox.delete(0, END)
            self.DBModelTCombobox.delete(0, "end")
            sel = self.DBBrandTCombobox.get()
            try:
                List1 = os.listdir(path + "/TOOL_DATABASE/" + sel)
                List2 = []
                for x in List1:
                    a = x.replace("@", "/")
                    List2.append(a)

                ListD = List2
                self.DBModelTCombobox.configure(values=ListD)
            except FileNotFoundError:
                return 0

        ListC = os.listdir(str(path + "/" + "TOOL_DATABASE"))
        ListD = []

        def callback(var):
            check = self.partSearchEntry.get().upper()
            list4 = []
            b = self.brandCombobox.get()
            m = re.sub('[/]', '@', self.modelCombobox.get())
            filePath = path + "/" + "TOOL_DATABASE" + "/" + b + "/" + m
            finalPath = str(filePath)
            try:
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
            except PermissionError:
                return 0

        def callback1(var):
            check = self.BOEntry1.get().upper()
            list1 = []
            for x in self.BOScrolledlistbox.get(0, END):
                list1.append(x)
            if check == '':
                getBO(1)

            else:
                res = []
                for x in list1:
                    test1 = x[0]
                    test2 = x[1]
                    test3 = x[4]
                    if test1.startswith(check) or test2.startswith(check) or test3.startswith(check):
                        res.append(x)
                self.BOScrolledlistbox.delete(0, END)
                for x in res:
                    self.BOScrolledlistbox.insert(END, x)

        def schemFetch():
            modelFix = re.sub('[/!@#$.]', '', self.modelCombobox.get())
            filename = path + '/Schematics/' + \
                self.brandCombobox.get() + modelFix + '.pdf'
            os.startfile(filename)
            return 0

        def toolDataBase(event):
            self.partSearchEntry.delete(0, END)
            self.availablePartsListBox.delete(0, END)
            b = self.brandCombobox.get()
            m = re.sub('[/]', '@', self.modelCombobox.get())
            filePath = path + "/" + "TOOL_DATABASE" + "/" + b + "/" + m
            finalPath = str(filePath)
            try:
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
            except FileNotFoundError:
                return 0
            except PermissionError:
                return 0

        def DBtoolDataBaseB():
            DBtoolDataBase(1)

        def DBtoolDataBase(event):
            DBList.clear()
            self.DBScrolledlistbox.delete(0, END)
            b = self.DBBrandTCombobox.get()
            brand = self.DBBrandTCombobox.get()
            m = re.sub('[/]', '@', self.DBModelTCombobox.get())
            filePath = path + "/" + "TOOL_DATABASE" + "/" + b + "/" + m
            finalPath = str(filePath)
            tempList = []
            intList = []
            strList = []
            somesortedIntList = []
            try:
                with open(finalPath, "r") as toolTextFile:
                    toolDict = toolTextFile.read()
                    dict = literal_eval(toolDict)

                for i in (dict):
                    values = list(dict[i])
                    values.insert(0, i)
                    tempList.append(values)

                for x in tempList:
                    try:
                        int1 = int(x[0])
                        x.pop(0)
                        x.insert(0, int1)
                        intList.append(x)
                    except ValueError:
                        strList.append(x)

                intList.sort(key=lambda x: x[0])
                strList.sort(key=lambda x: x[0])

                for x in intList:
                    str1 = str(x[0])
                    x.pop(0)
                    x.insert(0, str1)
                    somesortedIntList.append(x)

                if not somesortedIntList == [] and not strList == []:
                    someList = somesortedIntList + strList
                if strList == [] and not somesortedIntList == []:
                    someList = somesortedIntList
                if not strList == [] and somesortedIntList == []:
                    someList = strList
                if somesortedIntList == [] and strList == []:
                    someList = tempList

                for i in someList:
                    DBList.append(i)
                    self.DBScrolledlistbox.insert(END, i)

                finalPath = os.path.join(
                    path + "/" + "TOOL_DATABASE" + "/" + brand, m)
                finalDict = {}
                for x in DBList:
                    finalDict[x[0]] = x[1], x[2]

                toolFile = open(finalPath, "w")
                toolFile.write(str(finalDict))
            except PermissionError:
                return 0
            except FileNotFoundError:
                return 0

        def doclick(*args):
            pyautogui.tripleClick()

        def doclickS(*args):
            self.special += 1
            pyautogui.tripleClick()

        def doPopUp(event):
            try:
                m1.tk_popup(event.x_root, event.y_root)
            finally:
                m1.grab_release()

        def DBdoPopUp(event):
            try:
                m2.tk_popup(event.x_root, event.y_root)
            finally:
                m2.grab_release()

        def setdoPopUp(event):
            try:
                m3.tk_popup(event.x_root, event.y_root)
            finally:
                m3.grab_release()

        def EMdoPopUp(event):
            try:
                m4.tk_popup(event.x_root, event.y_root)
            finally:
                self.special = 0
                m4.grab_release()

        def EM2doPopUp(event):
            try:
                m5.tk_popup(event.x_root, event.y_root)
            finally:
                self.special = 0
                m5.grab_release()

        def BOdoPopUp(event):
            try:
                m6.tk_popup(event.x_root, event.y_root)
            finally:
                self.special = 0
                m6.grab_release()

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
            self.style.configure('.', background=background)
            self.style.configure('.', foreground=foreground)
            self.style.configure('.', font=font)
            self.style.map('.', background=[
                           ('selected', selected), ('active', selected)])
            self.style.map('TNotebook.Tab', background=[
                           ('selected', selected), ('active', selected)])
            self.style.configure(
                ".", fieldbackground=comboboxback, background=background)
            self.style.configure(
                "TNotebook.Tab", background=background, foreground=background)

            top.geometry("850x550+848+353")
            top.minsize(850, 550)
            top.maxsize(5564, 1901)
            top.resizable(1,  1)
            top.title("New Toplevel")
            top.configure(background=background)
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
        m1 = Menu(root, tearoff=0)
        m1.add_command(label="Edit", command=edSel)
        m1.add_command(label="Delete", command=deleteFromList)

        m2 = Menu(root, tearoff=0)
        m2.add_command(label="Delete", command=DBdeleteFromList)

        m3 = Menu(root, tearoff=0)
        m3.add_command(label="Delete", command=setDelCust)

        m4 = Menu(root, tearoff=0)
        m4.add_command(label="View", command=veiwOrder)
        m4.add_command(label="Delete", command=orderDel)

        m5 = Menu(root, tearoff=0)
        m5.add_command(label="View", command=veiworder2)

        m6 = Menu(root, tearoff=0)
        m6.add_command(label="Remove", command=BOdel)

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
        self.PNotebook1_t2.configure(background=background)
        self.PNotebook1_t2.configure(highlightbackground=background)
        self.PNotebook1_t2.configure(highlightcolor="black")
        self.PNotebook1_t1 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1, padding=3)
        self.PNotebook1.tab(1, text="Data Base",
                            compound="left", underline="-1",)
        self.PNotebook1_t1.configure(background=background)
        self.PNotebook1_t1.configure(highlightbackground=background)
        self.PNotebook1_t1.configure(highlightcolor="black")
        self.PNotebook1_t3 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t3, padding=3)
        self.PNotebook1.tab(2, text="Email", compound="none", underline="-1",)
        self.PNotebook1_t3.configure(background=background)
        self.PNotebook1_t3.configure(highlightbackground=background)
        self.PNotebook1_t3.configure(highlightcolor="black")
        self.PNotebook1_t5 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t5, padding=3)
        self.PNotebook1.tab(3, text="Back Order",
                            compound="none", underline="-1",)
        self.PNotebook1_t5.configure(background=background)
        self.PNotebook1_t5.configure(highlightbackground=background)
        self.PNotebook1_t5.configure(highlightcolor="black")
        self.PNotebook1_t4 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t4, padding=3)
        self.PNotebook1.tab(4, text="Settings",
                            compound="none", underline="-1",)
        self.PNotebook1_t4.configure(background=background)
        self.PNotebook1_t4.configure(highlightbackground=background)
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
        self.finalListbox.configure(background=background)
        self.finalListbox.configure(cursor="hand2")
        self.finalListbox.configure(disabledforeground="#a3a3a3")
        self.finalListbox.configure(font=font)
        self.finalListbox.configure(foreground=foreground)
        self.finalListbox.configure(highlightbackground=background)
        self.finalListbox.configure(highlightcolor="#d9d9d9")
        self.finalListbox.configure(selectbackground="blue")
        self.finalListbox.configure(selectforeground="white")
        self.finalListbox.bind('<3>', doclick)
        self.finalListbox.bind('<Delete>', deleteFromList)
        self.finalListbox.bind('<Return>', editSelection)
        self.finalListbox.bind('<Triple-1>', doPopUp)

        for values in (finalPartsList):
            self.finalListbox.insert(END, values)

        self.TLabelframe3 = ttk.Labelframe(self.PNotebook1_t2)
        self.TLabelframe3.place(relx=0.018, rely=0.022,
                                relheight=0.261, relwidth=0.477)
        self.TLabelframe3.configure(relief='')
        self.TLabelframe3.configure(text='''Tool Select''')

        var3 = tk.StringVar()
        var3.trace("w", lambda name, index, mode, var=var3: modelList(var))

        self.brandCombobox = ttk.Combobox(self.TLabelframe3)
        self.brandCombobox.place(
            relx=0.041, rely=0.35, relheight=0.205, relwidth=0.929, bordermode='ignore')
        self.brandCombobox.configure(takefocus="")
        self.brandCombobox.configure(font=font, textvariable=var3)
        self.brandCombobox.configure(values=getBrands())
        self.brandCombobox.bind("<<ComboboxSelected>>", modelList)

        self.Label1 = tk.Label(self.TLabelframe3)
        self.Label1.place(relx=0.041, rely=0.179, height=15,
                          width=60, bordermode='ignore')
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=background)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground=foreground)
        self.Label1.configure(highlightbackground=background)
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Brand:''', font=font)

        self.Label2 = tk.Label(self.TLabelframe3)
        self.Label2.place(relx=0.041, rely=0.615, height=15,
                          width=60, bordermode='ignore')
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background=background)
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground=foreground)
        self.Label2.configure(highlightbackground=background)
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''Model:''', font=font)

        var4 = tk.StringVar()
        var4.trace("w", lambda name, index, mode, var=var4: toolDataBase(var))

        self.modelCombobox = ttk.Combobox(self.TLabelframe3)
        self.modelCombobox.place(
            relx=0.041, rely=0.795, relheight=0.205, relwidth=0.929, bordermode='ignore')
        self.modelCombobox.configure(textvariable=var4)
        self.modelCombobox.configure(takefocus="")
        self.modelCombobox.configure(values=ListB, font=font)
        self.modelCombobox.bind("<<ComboboxSelected>>", toolDataBase)

        self.Button2 = tk.Button(self.TLabelframe3)
        self.Button2.place(relx=0.350, rely=0.0, height=34,
                           width=160, bordermode='ignore')
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground=foreground)
        self.Button2.configure(background=background)
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground=foreground)
        self.Button2.configure(highlightbackground=background)
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Open Schematic''', font=font)
        self.Button2.configure(command=schemFetch)

        self.TLabelframe4 = ttk.Labelframe(self.PNotebook1_t2)
        self.TLabelframe4.place(relx=0.518, rely=0.022,
                                relheight=0.254, relwidth=0.477)
        self.TLabelframe4.configure(relief='')
        self.TLabelframe4.configure(text='''Shipping and Biiling''')

        self.TLabel1 = ttk.Label(self.TLabelframe4)
        self.TLabel1.place(relx=0.052, rely=0.149, height=25,
                           width=77, bordermode='ignore')
        self.TLabel1.configure(background=background)
        self.TLabel1.configure(foreground=foreground)
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Ship To:''', font=font)

        self.TLabel2 = ttk.Label(self.TLabelframe4)
        self.TLabel2.place(relx=0.037, rely=0.614, height=25,
                           width=64, bordermode='ignore')
        self.TLabel2.configure(background=background)
        self.TLabel2.configure(foreground=foreground)
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''Bill To:''', font=font)

        self.ClearButton = tk.Button(self.TLabelframe4)
        self.ClearButton.place(relx=0.655, rely=0.0,
                               height=30, width=90, bordermode='ignore')
        self.ClearButton.configure(activebackground="#ececec")
        self.ClearButton.configure(activeforeground=foreground)
        self.ClearButton.configure(background=background)
        self.ClearButton.configure(disabledforeground="#a3a3a3")
        self.ClearButton.configure(foreground=foreground)
        self.ClearButton.configure(highlightbackground=background)
        self.ClearButton.configure(highlightcolor="black")
        self.ClearButton.configure(pady="0")
        self.ClearButton.configure(text='''Clear All''', font=font)
        self.ClearButton.configure(command=clearAllFields)

        self.shipCombobox = ttk.Combobox(self.TLabelframe4)
        self.shipCombobox.place(
            relx=0.037, rely=0.351, relheight=0.211, relwidth=0.929, bordermode='ignore')
        self.shipCombobox.configure(
            values=shipList(), font=font, foreground="black")
        self.shipCombobox.configure(takefocus="")
        self.shipCombobox.bind("L", keyPressL)
        self.shipCombobox.configure(state='readonly')

        self.billCombobox = ttk.Combobox(self.TLabelframe4)
        self.billCombobox.place(
            relx=0.037, rely=0.789, relheight=0.211, relwidth=0.929, bordermode='ignore')
        self.billCombobox.configure(state='readonly')
        self.billCombobox.configure(
            values=billList(), font=font, foreground="black")
        self.billCombobox.configure(takefocus="")

        self.PNotebook2 = ttk.Notebook(self.PNotebook1_t2)
        self.PNotebook2.place(relx=0.0, rely=0.301,
                              relheight=0.688, relwidth=0.502)
        self.PNotebook2.configure(style=PNOTEBOOK)
        self.PNotebook2_t2 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t2, padding=3)
        self.PNotebook2.tab(0, text="Available Parts",
                            compound="left", underline="-1", )
        self.PNotebook2_t2.configure(background=background)
        self.PNotebook2_t2.configure(highlightbackground=background)
        self.PNotebook2_t2.configure(highlightcolor="black")
        self.PNotebook2_t1 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t1, padding=3)
        self.PNotebook2.tab(1, text="Custom Parts",
                            compound="left", underline="-1", )
        self.PNotebook2_t1.configure(background=background)
        self.PNotebook2_t1.configure(highlightbackground=background)
        self.PNotebook2_t1.configure(highlightcolor="black")
        self.PNotebook2_t3 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t3, padding=3)
        self.PNotebook2.tab(2, text="Edit", compound="none", underline="-1",)
        self.PNotebook2_t3.configure(background=background)
        self.PNotebook2_t3.configure(highlightbackground=background)
        self.PNotebook2_t3.configure(highlightcolor="black")
        self.PNotebook2.hide(self.PNotebook2_t3)
        self.PNotebook2.bind('<1>', hideTab)

        self.availablePartsListBox = ScrolledListBox(self.PNotebook2_t2)
        self.availablePartsListBox.place(
            relx=0.0, rely=0.174, relheight=0.837, relwidth=0.968)
        self.availablePartsListBox.configure(background=background)
        self.availablePartsListBox.configure(cursor="hand2")
        self.availablePartsListBox.configure(disabledforeground="#a3a3a3")
        self.availablePartsListBox.configure(font=font)
        self.availablePartsListBox.configure(foreground=foreground)
        self.availablePartsListBox.configure(highlightbackground=background)
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
        self.partSearchEntry.configure(textvariable=var, font=font)

        self.TLabel3 = ttk.Label(self.PNotebook2_t2)
        self.TLabel3.place(relx=0.036, rely=0.0, height=23, width=150)
        self.TLabel3.configure(background=background)
        self.TLabel3.configure(foreground=foreground)
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''Part Search:''', font=font)

        self.Label3 = tk.Label(self.PNotebook2_t1)
        self.Label3.place(relx=0.0, rely=0.071, height=20, width=180)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background=background)
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground=foreground)
        self.Label3.configure(highlightbackground=background)
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''Schematic Number:''', font=font)

        self.cusSchemNum = tk.Entry(self.PNotebook2_t1)
        self.cusSchemNum.place(relx=0.43, rely=0.071,
                               height=20, relwidth=0.556)
        self.cusSchemNum.configure(background=background)
        self.cusSchemNum.configure(disabledforeground="#a3a3a3")
        self.cusSchemNum.configure(font=font)
        self.cusSchemNum.configure(foreground=foreground)
        self.cusSchemNum.configure(highlightbackground=background)
        self.cusSchemNum.configure(highlightcolor="black")
        self.cusSchemNum.configure(insertbackground="black")
        self.cusSchemNum.configure(selectbackground="blue")
        self.cusSchemNum.configure(selectforeground="white")

        self.Label4 = tk.Label(self.PNotebook2_t1)
        self.Label4.place(relx=0.0, rely=0.209, height=21, width=150)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background=background)
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground=foreground)
        self.Label4.configure(highlightbackground=background)
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Part Number:''', font=font)

        self.cusPartNum = tk.Entry(self.PNotebook2_t1)
        self.cusPartNum.place(relx=0.43, rely=0.209, height=20, relwidth=0.556)
        self.cusPartNum.configure(background=background)
        self.cusPartNum.configure(disabledforeground="#a3a3a3")
        self.cusPartNum.configure(font=font)
        self.cusPartNum.configure(foreground=foreground)
        self.cusPartNum.configure(highlightbackground=background)
        self.cusPartNum.configure(highlightcolor="black")
        self.cusPartNum.configure(insertbackground="black")
        self.cusPartNum.configure(selectbackground="blue")
        self.cusPartNum.configure(selectforeground="white")

        self.Label5 = tk.Label(self.PNotebook2_t1)
        self.Label5.place(relx=0.0, rely=0.351, height=20, width=130)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background=background)
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground=foreground)
        self.Label5.configure(highlightbackground=background)
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''Description:''', font=font)

        self.cusDescription = tk.Entry(self.PNotebook2_t1)
        self.cusDescription.place(
            relx=0.036, rely=0.454, height=20, relwidth=0.953)
        self.cusDescription.configure(background=background)
        self.cusDescription.configure(disabledforeground="#a3a3a3")
        self.cusDescription.configure(font=font)
        self.cusDescription.configure(foreground=foreground)
        self.cusDescription.configure(highlightbackground=background)
        self.cusDescription.configure(highlightcolor="black")
        self.cusDescription.configure(insertbackground="black")
        self.cusDescription.configure(selectbackground="blue")
        self.cusDescription.configure(selectforeground="white")
        self.cusDescription.bind("<Return>", addCusB)

        self.Button1 = tk.Button(self.PNotebook2_t1)
        self.Button1.place(relx=0.606, rely=0.56, height=114, width=107)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground=foreground)
        self.Button1.configure(background=background)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground=foreground)
        self.Button1.configure(highlightbackground=background)
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Add Part''')
        self.Button1.configure(command=addCus)

        self.Label6 = tk.Label(self.PNotebook2_t3)
        self.Label6.place(relx=0.69, rely=0.142, height=18, width=80)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background=background)
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground=foreground)
        self.Label6.configure(highlightbackground=background)
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Quantitiy:''', font=font)

        self.QEntry = tk.Entry(self.PNotebook2_t3)
        self.QEntry.place(relx=0.686, rely=0.213, height=20, relwidth=0.303)
        self.QEntry.configure(background=background)
        self.QEntry.configure(disabledforeground="#a3a3a3")
        self.QEntry.configure(font=font)
        self.QEntry.configure(foreground=foreground)
        self.QEntry.configure(highlightbackground=background)
        self.QEntry.configure(highlightcolor="black")
        self.QEntry.configure(insertbackground="black")
        self.QEntry.configure(selectbackground="blue")
        self.QEntry.configure(selectforeground="white")
        self.QEntry.bind('<Return>', editPartB)

        self.updateButton = tk.Button(self.PNotebook2_t3)
        self.updateButton.place(relx=0.722, rely=0.319, height=70, width=90)
        self.updateButton.configure(activebackground="#ececec")
        self.updateButton.configure(activeforeground=foreground)
        self.updateButton.configure(background=background)
        self.updateButton.configure(disabledforeground="#a3a3a3")
        self.updateButton.configure(foreground=foreground)
        self.updateButton.configure(highlightbackground=background)
        self.updateButton.configure(highlightcolor="black")
        self.updateButton.configure(pady="0")
        self.updateButton.configure(text='''Update''', font=font)
        self.updateButton.configure(command=editPart)

        self.removeButton = tk.Button(self.PNotebook2_t3)
        self.removeButton.place(relx=0.036, rely=0.638, height=94, width=107)
        self.removeButton.configure(activebackground="#ececec")
        self.removeButton.configure(activeforeground=foreground)
        self.removeButton.configure(background=background)
        self.removeButton.configure(disabledforeground="#a3a3a3")
        self.removeButton.configure(foreground=foreground)
        self.removeButton.configure(highlightbackground=background)
        self.removeButton.configure(highlightcolor="black")
        self.removeButton.configure(pady="0")
        self.removeButton.configure(text='''Remove''', font=font)
        self.removeButton.configure(command=removeFromList)

        self.cb = BooleanVar()

        self.Checkbutton1 = tk.Checkbutton(self.PNotebook2_t1)
        self.Checkbutton1.place(relx=0.036, rely=0.908,
                                relheight=0.089, relwidth=0.433)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground=foreground)
        self.Checkbutton1.configure(background=background)
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground='black')
        self.Checkbutton1.configure(highlightbackground=background)
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Add To Database''', font=font)
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
        self.pdfButton.configure(activeforeground=foreground)
        self.pdfButton.configure(background=background)
        self.pdfButton.configure(disabledforeground="#a3a3a3")
        self.pdfButton.configure(foreground=foreground)
        self.pdfButton.configure(highlightbackground=background)
        self.pdfButton.configure(highlightcolor="black")
        self.pdfButton.configure(pady="0")
        self.pdfButton.configure(text='''Save To PDF''', font=font)
        self.pdfButton.configure(command=pdfMaker)

        self.PNotebook1_t2_1 = tk.Frame(self.PNotebook1_t1)
        self.PNotebook1_t2_1.place(
            relx=0.0, rely=0.0, relheight=0.002, relwidth=0.002)
        self.PNotebook1_t2_1.configure(background=background)
        self.PNotebook1_t2_1.configure(highlightbackground=background)
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

        self.TLabelframe4_1 = ttk.Labelframe(self.PNotebook1_t2_1)
        self.TLabelframe4_1.place(
            relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)
        self.TLabelframe4_1.configure(relief='')
        self.TLabelframe4_1.configure(text='''Shipping and Biiling''')

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

        var5 = tk.StringVar()
        var5.trace("w", lambda name, index, mode, var=var5: DBmodelList(var))

        self.DBBrandTCombobox = ttk.Combobox(self.PNotebook1_t1)
        self.DBBrandTCombobox.place(
            relx=0.018, rely=0.067, relheight=0.047, relwidth=0.255)
        self.DBBrandTCombobox.configure(takefocus="", textvariable=var5)
        self.DBBrandTCombobox.configure(values=DBgetBrands(), font=font)
        #self.DBBrandTCombobox.bind("<<ComboboxSelected>>", DBmodelList)

        var6 = tk.StringVar()
        var6.trace("w", lambda name, index, mode, var=var6: DBtoolDataBase(var))

        self.DBModelTCombobox = ttk.Combobox(self.PNotebook1_t1)
        self.DBModelTCombobox.place(
            relx=0.304, rely=0.067, relheight=0.047, relwidth=0.255)
        self.DBModelTCombobox.configure(takefocus="", font=font, textvariable=var6)
        #self.DBModelTCombobox.bind("<<ComboboxSelected>>", DBtoolDataBase)
        self.DBModelTCombobox.bind('<Return>', DBtoolDataBase)

        self.DBTLabel1 = ttk.Label(self.PNotebook1_t1)
        self.DBTLabel1.place(relx=0.018, rely=0.022, height=23, width=80)
        self.DBTLabel1.configure(background=background)
        self.DBTLabel1.configure(foreground=foreground)
        self.DBTLabel1.configure(font="TkDefaultFont")
        self.DBTLabel1.configure(relief="flat")
        self.DBTLabel1.configure(anchor='w')
        self.DBTLabel1.configure(justify='left')
        self.DBTLabel1.configure(text='''Brand:''', font=font)

        self.DBTLabel2 = ttk.Label(self.PNotebook1_t1)
        self.DBTLabel2.place(relx=0.304, rely=0.022, height=23, width=80)
        self.DBTLabel2.configure(background=background)
        self.DBTLabel2.configure(foreground=foreground)
        self.DBTLabel2.configure(font="TkDefaultFont")
        self.DBTLabel2.configure(relief="flat")
        self.DBTLabel2.configure(anchor='w')
        self.DBTLabel2.configure(justify='left')
        self.DBTLabel2.configure(text='''Model:''', font=font)

        self.TNotebook1 = ttk.Notebook(self.PNotebook1_t1)
        self.TNotebook1.place(relx=0.0, rely=0.134,
                              relheight=0.304, relwidth=1.007)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(0, text="Simple Entry",
                            compound="left", underline="-1", )
        self.TNotebook1_t1.configure(background=background)
        self.TNotebook1_t1.configure(highlightbackground=background)
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(1, text="Speed Entry",
                            compound="left", underline="-1",)
        self.TNotebook1_t2.configure(background=background)
        self.TNotebook1_t2.configure(highlightbackground=background)
        self.TNotebook1_t2.configure(highlightcolor="black")

        self.DBTLabel3 = ttk.Label(self.TNotebook1_t1)
        self.DBTLabel3.place(relx=0.0, rely=0.182, height=23, width=175)
        self.DBTLabel3.configure(background=background)
        self.DBTLabel3.configure(foreground=foreground)
        self.DBTLabel3.configure(font="TkDefaultFont")
        self.DBTLabel3.configure(relief="flat")
        self.DBTLabel3.configure(anchor='w')
        self.DBTLabel3.configure(justify='left')
        self.DBTLabel3.configure(text='''Schematic Number:''', font=font)

        self.DBTLabel4 = ttk.Label(self.TNotebook1_t1)
        self.DBTLabel4.place(relx=0.250, rely=0.145, height=24, width=175)
        self.DBTLabel4.configure(background=background)
        self.DBTLabel4.configure(foreground=foreground)
        self.DBTLabel4.configure(font="TkDefaultFont")
        self.DBTLabel4.configure(relief="flat")
        self.DBTLabel4.configure(anchor='w')
        self.DBTLabel4.configure(justify='left')
        self.DBTLabel4.configure(text='''Part Number:''', font=font)

        self.DBTLabel5 = ttk.Label(self.TNotebook1_t1)
        self.DBTLabel5.place(relx=0.0, rely=0.545, height=23, width=125)
        self.DBTLabel5.configure(background=background)
        self.DBTLabel5.configure(foreground=foreground)
        self.DBTLabel5.configure(font="TkDefaultFont")
        self.DBTLabel5.configure(relief="flat")
        self.DBTLabel5.configure(anchor='w')
        self.DBTLabel5.configure(justify='left')
        self.DBTLabel5.configure(text='''Description:''', font=font)

        self.DBSchemEntry = ttk.Entry(self.TNotebook1_t1)
        self.DBSchemEntry.place(relx=0.0, rely=0.364,
                                relheight=0.191, relwidth=0.225)
        self.DBSchemEntry.configure(takefocus="")
        self.DBSchemEntry.configure(cursor="ibeam", font=font)

        self.DBPartEntry = ttk.Entry(self.TNotebook1_t1)
        self.DBPartEntry.place(relx=0.25, rely=0.364,
                               relheight=0.191, relwidth=0.225)
        self.DBPartEntry.configure(takefocus="")
        self.DBPartEntry.configure(cursor="ibeam", font=font)

        self.DBDesEntry = ttk.Entry(self.TNotebook1_t1)
        self.DBDesEntry.place(relx=0.0, rely=0.727,
                              relheight=0.191, relwidth=0.993)
        self.DBDesEntry.configure(takefocus="")
        self.DBDesEntry.configure(cursor="ibeam", font=font)
        self.DBDesEntry.bind('<Return>', DBAdd)

        self.DBAddBuuton = tk.Button(self.TNotebook1_t1)
        self.DBAddBuuton.place(relx=0.518, rely=0.273, height=35, width=196)
        self.DBAddBuuton.configure(
            takefocus="", font=font, background=background, foreground=foreground)
        self.DBAddBuuton.configure(text='''ADD/UPDATE''')
        self.DBAddBuuton.configure(command=DBdataAddcus)

        self.DBSpeedEntry = tk.Entry(self.TNotebook1_t2)
        self.DBSpeedEntry.place(relx=0.018, rely=0.573,
                                relheight=0.191, relwidth=0.957)
        self.DBSpeedEntry.configure(
            takefocus="", font=font, background=comboboxback, foreground=foreground)
        self.DBSpeedEntry.configure(cursor="ibeam")
        self.DBSpeedEntry.bind("<Return>", DBspeed)

        self.DBTLabel6 = ttk.Label(self.TNotebook1_t2)
        self.DBTLabel6.place(relx=0.089, rely=0.0, height=30, width=200)
        self.DBTLabel6.configure(background=background)
        self.DBTLabel6.configure(foreground=foreground)
        self.DBTLabel6.configure(relief="flat")
        self.DBTLabel6.configure(anchor='w')
        self.DBTLabel6.configure(justify='left')
        self.DBTLabel6.configure(
            text='''syntax for speed entry is''', font=font)

        self.DBTLabel7 = ttk.Label(self.TNotebook1_t2)
        self.DBTLabel7.place(relx=0.018, rely=0.282, height=30, width=450)
        self.DBTLabel7.configure(background=background)
        self.DBTLabel7.configure(foreground=foreground)
        self.DBTLabel7.configure(relief="flat")
        self.DBTLabel7.configure(anchor='w')
        self.DBTLabel7.configure(justify='left')
        self.DBTLabel7.configure(
            text='''SchematicNumber   PartNumber   Description''', font=font)

        self.DBTLabel8 = ttk.Label(self.TNotebook1_t2)
        self.DBTLabel8.place(relx=0.6, rely=0.145, height=30, width=300)
        self.DBTLabel8.configure(background=background)
        self.DBTLabel8.configure(foreground="#ff0000")
        self.DBTLabel8.configure(font=font)
        self.DBTLabel8.configure(relief="flat")
        self.DBTLabel8.configure(anchor='w')
        self.DBTLabel8.configure(justify='left')
        self.DBTLabel8.configure(text='''*must be seperated by one space*''')

        self.DBScrolledlistbox = ScrolledListBox(self.PNotebook1_t1)
        self.DBScrolledlistbox.place(
            relx=0.0, rely=0.446, relheight=0.547, relwidth=1.002)
        self.DBScrolledlistbox.configure(background=background)
        self.DBScrolledlistbox.configure(cursor="hand2")
        self.DBScrolledlistbox.configure(disabledforeground="#a3a3a3")
        self.DBScrolledlistbox.configure(font=font)
        self.DBScrolledlistbox.configure(
            background=background, foreground=foreground)
        self.DBScrolledlistbox.configure(highlightbackground=background)
        self.DBScrolledlistbox.configure(highlightcolor="#d9d9d9")
        self.DBScrolledlistbox.configure(selectbackground="blue")
        self.DBScrolledlistbox.configure(selectforeground="white")
        self.DBScrolledlistbox.bind('<Double-1>', DBGrabInfo)
        self.DBScrolledlistbox.bind('<3>', doclick)
        self.DBScrolledlistbox.bind('<Triple-1>', DBdoPopUp)

        self.DBSortButton = tk.Button(self.PNotebook1_t1)
        self.DBSortButton.place(relx=0.679, rely=0.042, height=35, width=96)
        self.DBSortButton.configure(takefocus="")
        self.DBSortButton.configure(
            text='''Sort List''', font=font, background=background, foreground=foreground)
        self.DBSortButton.configure(command=DBtoolDataBaseB)

        self.BOCombobox1 = ttk.Combobox(self.PNotebook1_t5)
        self.BOCombobox1.place(relx=0.589, rely=0.063,
                               relheight=0.05, relwidth=0.398)
        self.BOCombobox1.configure(values=BOCustomerGet())
        self.BOCombobox1.configure(state='readonly')
        self.BOCombobox1.configure(takefocus="", font=font, foreground="black")
        self.BOCombobox1.bind("<<ComboboxSelected>>", getBO)

        self.BOLabel1 = tk.Label(self.PNotebook1_t5)
        self.BOLabel1.place(relx=0.589, rely=0.021, height=22, width=90)
        self.BOLabel1.configure(activebackground="#f9f9f9")
        self.BOLabel1.configure(activeforeground="black")
        self.BOLabel1.configure(background=background)
        self.BOLabel1.configure(disabledforeground="#a3a3a3")
        self.BOLabel1.configure(foreground=foreground)
        self.BOLabel1.configure(highlightbackground=background)
        self.BOLabel1.configure(highlightcolor="black")
        self.BOLabel1.configure(text='''Customer:''', font=font)

        self.TNotebook2 = ttk.Notebook(self.PNotebook1_t5)
        self.TNotebook2.place(relx=0.0, rely=0.127,
                              relheight=0.879, relwidth=1.007)
        self.TNotebook2.configure(takefocus="")
        self.TNotebook2_t2 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t2, padding=3)
        self.TNotebook2.tab(0, text="List", compound="left", underline="-1",)
        self.TNotebook2_t2.configure(background=background)
        self.TNotebook2_t2.configure(highlightbackground=selected)
        self.TNotebook2_t2.configure(highlightcolor="black")
        self.TNotebook2_t1 = tk.Frame(self.TNotebook2)
        self.TNotebook2.add(self.TNotebook2_t1, padding=3)
        self.TNotebook2.tab(1, text="Edit", compound="left", underline="-1",)
        self.TNotebook2_t1.configure(background=background)
        self.TNotebook2_t1.configure(highlightbackground=background)
        self.TNotebook2_t1.configure(highlightcolor="black")

        self.BOScrolledlistbox = ScrolledListBox(self.TNotebook2_t2)
        self.BOScrolledlistbox.place(
            relx=0.0, rely=0.026, relheight=0.962, relwidth=1.002)
        self.BOScrolledlistbox.configure(background=background)
        self.BOScrolledlistbox.configure(cursor="hand2")
        self.BOScrolledlistbox.configure(disabledforeground="#a3a3a3")
        self.BOScrolledlistbox.configure(font=font)
        self.BOScrolledlistbox.configure(foreground=foreground)
        self.BOScrolledlistbox.configure(highlightbackground=background)
        self.BOScrolledlistbox.configure(highlightcolor="#d9d9d9")
        self.BOScrolledlistbox.configure(selectbackground="blue")
        self.BOScrolledlistbox.configure(selectforeground="white")
        self.BOScrolledlistbox.bind('<Double-1>', BOedSel)
        self.BOScrolledlistbox.bind("<3>", doclickS)
        self.BOScrolledlistbox.bind("<Triple-1>", BOdoPopUp)

        self.BOMessage = tk.Message(self.TNotebook2_t1)
        self.BOMessage.place(relx=0.018, rely=0.208,
                             relheight=0.159, relwidth=0.964)
        self.BOMessage.configure(background=background)
        self.BOMessage.configure(foreground=foreground)
        self.BOMessage.configure(highlightbackground=background)
        self.BOMessage.configure(highlightcolor="black")
        self.BOMessage.configure(width=850, font=font)

        self.BOQuantEntry = tk.Entry(self.TNotebook2_t1)
        self.BOQuantEntry.place(relx=0.714, rely=0.385,
                                height=20, relwidth=0.15)
        self.BOQuantEntry.configure(background=background)
        self.BOQuantEntry.configure(disabledforeground="#a3a3a3")
        self.BOQuantEntry.configure(font=font)
        self.BOQuantEntry.configure(foreground=foreground)
        self.BOQuantEntry.configure(highlightbackground=background)
        self.BOQuantEntry.configure(highlightcolor="black")
        self.BOQuantEntry.configure(insertbackground="black")
        self.BOQuantEntry.configure(selectbackground="blue")
        self.BOQuantEntry.configure(selectforeground="white")
        self.BOQuantEntry.bind("<Return>", BOupdateB)

        self.BOLabel4 = tk.Label(self.TNotebook2_t1)
        self.BOLabel4.place(relx=0.450, rely=0.385, height=23, width=210)
        self.BOLabel4.configure(activebackground="#f9f9f9")
        self.BOLabel4.configure(activeforeground="black")
        self.BOLabel4.configure(background=background)
        self.BOLabel4.configure(disabledforeground="#a3a3a3")
        self.BOLabel4.configure(foreground=foreground)
        self.BOLabel4.configure(highlightbackground=background)
        self.BOLabel4.configure(highlightcolor="black")
        self.BOLabel4.configure(text='''Enter Amount Recieved:''', font=font)

        self.BOButton = tk.Button(self.TNotebook2_t1)
        self.BOButton.place(relx=0.732, rely=0.462, height=44, width=90)
        self.BOButton.configure(activebackground="#ececec")
        self.BOButton.configure(activeforeground=foreground)
        self.BOButton.configure(background=background)
        self.BOButton.configure(disabledforeground="#a3a3a3")
        self.BOButton.configure(foreground=foreground)
        self.BOButton.configure(highlightbackground=background)
        self.BOButton.configure(highlightcolor="black")
        self.BOButton.configure(pady="0")
        self.BOButton.configure(text='''Update''', font=font)
        self.BOButton.configure(command=BOupdate)

        self.BOLabel3 = ttk.Label(self.PNotebook1_t5)
        self.BOLabel3.place(relx=-0.036, rely=0.127, height=29, width=585)
        self.BOLabel3.configure(background=background)
        self.BOLabel3.configure(foreground=foreground)
        self.BOLabel3.configure(relief="flat")
        self.BOLabel3.configure(anchor='w')
        self.BOLabel3.configure(justify='left')

        self.BOLabel2 = tk.Label(self.PNotebook1_t5)
        self.BOLabel2.place(relx=0.0, rely=0.085, height=23, width=200)
        self.BOLabel2.configure(activebackground="#f9f9f9")
        self.BOLabel2.configure(activeforeground="black")
        self.BOLabel2.configure(background=background)
        self.BOLabel2.configure(disabledforeground="#a3a3a3")
        self.BOLabel2.configure(foreground=foreground)
        self.BOLabel2.configure(highlightbackground=background)
        self.BOLabel2.configure(highlightcolor="black")
        self.BOLabel2.configure(text='''Search Part Number:''', font=font)

        var1 = tk.StringVar()
        var1.trace("w", lambda name, index, mode, var=var1: callback1(var1))
        self.BOEntry1 = tk.Entry(self.PNotebook1_t5)
        self.BOEntry1.place(relx=0.018, rely=0.148, height=20, relwidth=0.221)
        self.BOEntry1.configure(background=background)
        self.BOEntry1.configure(disabledforeground="#a3a3a3")
        self.BOEntry1.configure(font=font)
        self.BOEntry1.configure(foreground=foreground)
        self.BOEntry1.configure(highlightbackground=background)
        self.BOEntry1.configure(highlightcolor="black")
        self.BOEntry1.configure(insertbackground="black")
        self.BOEntry1.configure(selectbackground="blue")
        self.BOEntry1.configure(selectforeground="white")
        self.BOEntry1.configure(textvariable=var1)

        self.BOBackButton = tk.Button(self.TNotebook2_t1)
        self.BOBackButton.place(relx=0.018, rely=0.897, height=34, width=125)
        self.BOBackButton.configure(activebackground="#ececec")
        self.BOBackButton.configure(activeforeground=foreground)
        self.BOBackButton.configure(background=background)
        self.BOBackButton.configure(disabledforeground="#a3a3a3")
        self.BOBackButton.configure(foreground=foreground)
        self.BOBackButton.configure(highlightbackground=background)
        self.BOBackButton.configure(highlightcolor="black")
        self.BOBackButton.configure(pady="0")
        self.BOBackButton.configure(text='''Back''', font=font)
        self.BOBackButton.configure(command=BOBack)

        self.BOPDFButton = tk.Button(self.PNotebook1_t5)
        self.BOPDFButton.place(relx=0.75, rely=0.127, height=37, width=185)
        self.BOPDFButton.configure(activebackground="#ececec")
        self.BOPDFButton.configure(activeforeground=foreground)
        self.BOPDFButton.configure(background=background)
        self.BOPDFButton.configure(disabledforeground="#a3a3a3")
        self.BOPDFButton.configure(foreground=foreground)
        self.BOPDFButton.configure(highlightbackground=background)
        self.BOPDFButton.configure(highlightcolor="black")
        self.BOPDFButton.configure(pady="0")
        self.BOPDFButton.configure(text='''Save To PDF''', font=font)
        self.BOPDFButton.configure(command=BOPDF)

        self.SetScrolledlistbox = ScrolledListBox(self.PNotebook1_t4)
        self.SetScrolledlistbox.place(
            relx=0.018, rely=0.085, relheight=0.708, relwidth=0.359)
        self.SetScrolledlistbox.configure(background=background)
        self.SetScrolledlistbox.configure(cursor="xterm")
        self.SetScrolledlistbox.configure(disabledforeground="#a3a3a3")
        self.SetScrolledlistbox.configure(font=font)
        self.SetScrolledlistbox.configure(foreground=foreground)
        self.SetScrolledlistbox.configure(highlightbackground=background)
        self.SetScrolledlistbox.configure(highlightcolor="#d9d9d9")
        self.SetScrolledlistbox.configure(selectbackground="blue")
        self.SetScrolledlistbox.configure(selectforeground="white")
        self.SetScrolledlistbox.bind("<3>", doclick)
        self.SetScrolledlistbox.bind("<Triple-1>", setdoPopUp)

        self.SetLabel1 = tk.Label(self.PNotebook1_t4)
        self.SetLabel1.place(relx=0.018, rely=0.042, height=21, width=135)
        self.SetLabel1.configure(background=background)
        self.SetLabel1.configure(disabledforeground="#a3a3a3")
        self.SetLabel1.configure(foreground=foreground)
        self.SetLabel1.configure(text='''Customer List:''', font=font)

        self.SetCustEntry = tk.Entry(self.PNotebook1_t4)
        self.SetCustEntry.place(relx=0.018, rely=0.846,
                                height=20, relwidth=0.364)
        self.SetCustEntry.configure(background=background)
        self.SetCustEntry.configure(disabledforeground="#a3a3a3")
        self.SetCustEntry.configure(font=font)
        self.SetCustEntry.configure(foreground=foreground)
        self.SetCustEntry.configure(insertbackground="black")
        self.SetCustEntry.bind("<Return>", addCustomerToListB)

        self.SetUpButton = tk.Button(self.PNotebook1_t4)
        self.SetUpButton.place(relx=0.107, rely=0.909, height=40, width=107)
        self.SetUpButton.configure(activebackground="#ececec")
        self.SetUpButton.configure(activeforeground=foreground)
        self.SetUpButton.configure(background=background)
        self.SetUpButton.configure(disabledforeground="#a3a3a3")
        self.SetUpButton.configure(foreground=foreground)
        self.SetUpButton.configure(highlightbackground=background)
        self.SetUpButton.configure(highlightcolor="black")
        self.SetUpButton.configure(pady="0")
        self.SetUpButton.configure(text='''Update''', font=font)
        self.SetUpButton.configure(command=addCustomerToList)

        self.TSeparator4 = ttk.Separator(self.PNotebook1_t4)
        self.TSeparator4.place(relx=0.393, rely=0.0,  relheight=1.036)
        self.TSeparator4.configure(orient="vertical")

        self.SetLabel2 = ttk.Label(self.PNotebook1_t4)
        self.SetLabel2.place(relx=0.018, rely=0.803, height=23, width=200)
        self.SetLabel2.configure(background=background)
        self.SetLabel2.configure(foreground=foreground)
        self.SetLabel2.configure(font=font)
        self.SetLabel2.configure(relief="flat")
        self.SetLabel2.configure(anchor='w')
        self.SetLabel2.configure(justify='left')
        self.SetLabel2.configure(text='''Add New Customer:''')

        self.SetLabel3 = tk.Label(self.PNotebook1_t4)
        self.SetLabel3.place(relx=0.411, rely=0.742, height=21, width=110)
        self.SetLabel3.configure(background=background)
        self.SetLabel3.configure(disabledforeground="#a3a3a3")
        self.SetLabel3.configure(font=font)
        self.SetLabel3.configure(foreground=foreground)
        self.SetLabel3.configure(text='''Your Name:''')

        self.SetNameEntry = tk.Entry(self.PNotebook1_t4)
        self.SetNameEntry.place(relx=0.411, rely=0.784,
                                height=25, relwidth=0.221)
        self.SetNameEntry.configure(background=background)
        self.SetNameEntry.configure(disabledforeground="#a3a3a3")
        self.SetNameEntry.configure(font=font)
        self.SetNameEntry.configure(foreground=foreground)
        self.SetNameEntry.configure(insertbackground="black")
        self.SetNameEntry.insert(END, setting())

        self.SetSaveButton = tk.Button(self.PNotebook1_t4)
        self.SetSaveButton.place(relx=0.786, rely=0.825, height=74, width=107)
        self.SetSaveButton.configure(activebackground="#ececec")
        self.SetSaveButton.configure(activeforeground=foreground)
        self.SetSaveButton.configure(background=background)
        self.SetSaveButton.configure(disabledforeground="#a3a3a3")
        self.SetSaveButton.configure(foreground=foreground)
        self.SetSaveButton.configure(highlightbackground=background)
        self.SetSaveButton.configure(highlightcolor="black")
        self.SetSaveButton.configure(pady="0")
        self.SetSaveButton.configure(text='''Save''', font=font)
        self.SetSaveButton.configure(command=setSave)

        self.ELabel2 = tk.Label(self.PNotebook1_t3)
        self.ELabel2.place(relx=0.018, rely=0.042, height=23, width=60)
        self.ELabel2.configure(background=background)
        self.ELabel2.configure(disabledforeground="#a3a3a3")
        self.ELabel2.configure(foreground=foreground)
        self.ELabel2.configure(text='''Email:''', font=font)

        self.EEntry1 = tk.Entry(self.PNotebook1_t3)
        self.EEntry1.place(relx=0.018, rely=0.085, height=25, relwidth=0.311)
        self.EEntry1.configure(background=background)
        self.EEntry1.configure(disabledforeground="#a3a3a3")
        self.EEntry1.configure(font=font)
        self.EEntry1.configure(foreground=foreground)
        self.EEntry1.configure(insertbackground="black")

        self.ELabel3 = tk.Label(self.PNotebook1_t3)
        self.ELabel3.place(relx=0.018, rely=0.148, height=23, width=90)
        self.ELabel3.configure(background=background)
        self.ELabel3.configure(cursor="fleur")
        self.ELabel3.configure(disabledforeground="#a3a3a3")
        self.ELabel3.configure(foreground=foreground)
        self.ELabel3.configure(text='''Password:''', font=font)

        self.EEntry2 = tk.Entry(self.PNotebook1_t3)
        self.EEntry2.place(relx=0.018, rely=0.191, height=23, relwidth=0.311)
        self.EEntry2.configure(background=background)
        self.EEntry2.configure(disabledforeground="#a3a3a3")
        self.EEntry2.configure(font=font)
        self.EEntry2.configure(foreground=foreground)
        self.EEntry2.configure(highlightbackground=background)
        self.EEntry2.configure(highlightcolor="black")
        self.EEntry2.configure(insertbackground="black")
        self.EEntry2.configure(selectbackground="blue")
        self.EEntry2.configure(selectforeground="white")

        self.ESeparator1 = ttk.Separator(self.PNotebook1_t3)
        self.ESeparator1.place(relx=0.0, rely=0.233,  relwidth=0.5)

        self.ESeparator2 = ttk.Separator(self.PNotebook1_t3)
        self.ESeparator2.place(relx=0.5, rely=0.0,  relheight=0.233)
        self.ESeparator2.configure(orient="vertical")

        self.ELabel1 = ttk.Label(self.PNotebook1_t3)
        self.ELabel1.place(relx=0.196, rely=0.0, height=29, width=145)
        self.ELabel1.configure(background=background)
        self.ELabel1.configure(foreground=foreground)
        self.ELabel1.configure(
            font="-family {Segoe UI Black} -size 12 -weight bold")
        self.ELabel1.configure(relief="flat")
        self.ELabel1.configure(anchor='w')
        self.ELabel1.configure(justify='left')
        self.ELabel1.configure(text='''Email Credentials''')

        self.EScrolledlistbox1 = ScrolledListBox(self.PNotebook1_t3)
        self.EScrolledlistbox1.place(
            relx=0.0, rely=0.445, relheight=0.39, relwidth=0.502)
        self.EScrolledlistbox1.configure(background=background)
        self.EScrolledlistbox1.configure(cursor="hand2")
        self.EScrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.EScrolledlistbox1.configure(font=font)
        self.EScrolledlistbox1.configure(foreground=foreground)
        self.EScrolledlistbox1.configure(highlightbackground=background)
        self.EScrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.EScrolledlistbox1.configure(selectbackground="blue")
        self.EScrolledlistbox1.configure(selectforeground="white")
        for i in os.listdir(str(Epath)):
            self.EScrolledlistbox1.insert(END, i)
        self.EScrolledlistbox1.bind("<Double-1>", selectpdf)
        self.EScrolledlistbox1.bind("<3>", doclickS)
        self.EScrolledlistbox1.bind("<Triple-1>", EMdoPopUp)

        self.EScrolledlistbox2 = ScrolledListBox(self.PNotebook1_t3)
        self.EScrolledlistbox2.place(
            relx=0.5, rely=0.445, relheight=0.39, relwidth=0.502)
        self.EScrolledlistbox2.configure(background=background)
        self.EScrolledlistbox2.configure(cursor="hand2")
        self.EScrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.EScrolledlistbox2.configure(font=font)
        self.EScrolledlistbox2.configure(foreground=foreground)
        self.EScrolledlistbox2.configure(highlightbackground=background)
        self.EScrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.EScrolledlistbox2.configure(selectbackground="blue")
        self.EScrolledlistbox2.configure(selectforeground="white")
        self.EScrolledlistbox2.bind("<Double-1>", unselectpdf)
        self.EScrolledlistbox2.bind("<3>", doclickS)
        self.EScrolledlistbox2.bind("<Triple-1>", EM2doPopUp)

        self.ELabel4 = tk.Label(self.PNotebook1_t3)
        self.ELabel4.place(relx=0.518, rely=0.042, height=23, width=90)
        self.ELabel4.configure(background=background)
        self.ELabel4.configure(disabledforeground="#a3a3a3")
        self.ELabel4.configure(foreground=foreground)
        self.ELabel4.configure(text='''Send To:''', font=font)

        self.EEntry3 = tk.Entry(self.PNotebook1_t3)
        self.EEntry3.place(relx=0.518, rely=0.085, height=27, relwidth=0.471)
        self.EEntry3.configure(background=background)
        self.EEntry3.configure(disabledforeground="#a3a3a3")
        self.EEntry3.configure(font=font)
        self.EEntry3.configure(foreground=foreground)
        self.EEntry3.configure(insertbackground="black")
        self.EEntry3.insert(
            END, "strujillo@metrostaple.com,falves@metrostaple.com")

        # strujillo@metrostaple.com,falves@metrostaple.com

        self.ELabel5 = tk.Label(self.PNotebook1_t3)
        self.ELabel5.place(relx=0.518, rely=0.148, height=23, width=75)
        self.ELabel5.configure(background=background)
        self.ELabel5.configure(disabledforeground="#a3a3a3")
        self.ELabel5.configure(foreground=foreground)
        self.ELabel5.configure(text='''Subject:''', font=font)

        self.EEntry4 = tk.Entry(self.PNotebook1_t3)
        self.EEntry4.place(relx=0.518, rely=0.191, height=27, relwidth=0.471)
        self.EEntry4.configure(background=background)
        self.EEntry4.configure(disabledforeground="#a3a3a3")
        self.EEntry4.configure(font=font)
        self.EEntry4.configure(foreground=foreground)
        self.EEntry4.configure(insertbackground="black")
        self.EEntry4.insert(END, dateemailstr())

        self.EScrolledtext = ScrolledText(self.PNotebook1_t3)
        self.EScrolledtext.place(relx=0.0, rely=0.318,
                                 relheight=0.074, relwidth=1.009)
        self.EScrolledtext.configure(background=background)
        self.EScrolledtext.configure(font=font)
        self.EScrolledtext.configure(foreground=foreground)
        self.EScrolledtext.configure(highlightbackground=background)
        self.EScrolledtext.configure(highlightcolor="black")
        self.EScrolledtext.configure(insertbackground="black")
        self.EScrolledtext.configure(insertborderwidth="3")
        self.EScrolledtext.configure(selectbackground="blue")
        self.EScrolledtext.configure(selectforeground="white")
        self.EScrolledtext.configure(wrap="none")

        self.ELabel6 = tk.Label(self.PNotebook1_t3)
        self.ELabel6.place(relx=0.010, rely=0.254, height=23, width=50)
        self.ELabel6.configure(background=background)
        self.ELabel6.configure(disabledforeground="#a3a3a3")
        self.ELabel6.configure(foreground=foreground)
        self.ELabel6.configure(text='''Body:''', font=font)

        self.Label7E = tk.Label(self.PNotebook1_t3)
        self.Label7E.place(relx=0.0, rely=0.403, height=21, width=400)
        self.Label7E.configure(background=background)
        self.Label7E.configure(disabledforeground="#a3a3a3")
        self.Label7E.configure(foreground=foreground)
        self.Label7E.configure(text='''Current Orders''', font=font)

        self.ELabel8 = tk.Label(self.PNotebook1_t3)
        self.ELabel8.place(relx=0.518, rely=0.403, height=21, width=350)
        self.ELabel8.configure(background=background)
        self.ELabel8.configure(disabledforeground="#a3a3a3")
        self.ELabel8.configure(foreground=foreground)
        self.ELabel8.configure(text='''Selected Orders''', font=font)

        self.ESendButton = tk.Button(self.PNotebook1_t3)
        self.ESendButton.place(relx=0.661, rely=0.845, height=64, width=187)
        self.ESendButton.configure(activebackground="#ececec")
        self.ESendButton.configure(activeforeground=foreground)
        self.ESendButton.configure(background=background)
        self.ESendButton.configure(disabledforeground="#a3a3a3")
        self.ESendButton.configure(
            font="-family {Segoe UI Black} -size 15 -weight bold")
        self.ESendButton.configure(foreground=foreground)
        self.ESendButton.configure(highlightbackground=background)
        self.ESendButton.configure(highlightcolor="black")
        self.ESendButton.configure(pady="0")
        self.ESendButton.configure(text='''Send''')
        self.ESendButton.configure(command=collect_mail_info)

        self.EMessage = tk.Message(self.PNotebook1_t3)
        self.EMessage.place(relx=0.018, rely=0.869,
                            relheight=0.112, relwidth=0.625)
        self.EMessage.configure(background=background)
        self.EMessage.configure(
            font="-family {Segoe UI Black} -size 12 -weight bold")
        self.EMessage.configure(foreground="#00c600")
        self.EMessage.configure(highlightbackground=background)
        self.EMessage.configure(highlightcolor="black")
        self.EMessage.configure(width=350)

        self.EWarning = tk.Message(self.PNotebook1_t3)
        self.EWarning.place(relx=0.375, rely=0.106,
                            relheight=0.07, relwidth=0.125)
        self.EWarning.configure(background=background)
        self.EWarning.configure(font="-family {Segoe UI} -size 7 -weight bold")
        self.EWarning.configure(foreground="#ff0000")
        self.EWarning.configure(highlightbackground=background)
        self.EWarning.configure(highlightcolor="black")
        self.EWarning.configure(text='''Not Recomended!!''')
        self.EWarning.configure(width=70)

        self.ecb = BooleanVar()

        self.ECheckbutton = tk.Checkbutton(self.PNotebook1_t3)
        self.ECheckbutton.place(relx=0.357, rely=0.169,
                                relheight=0.053, relwidth=0.127)
        self.ECheckbutton.configure(activebackground="#ececec")
        self.ECheckbutton.configure(activeforeground=foreground)
        self.ECheckbutton.configure(background=background)
        self.ECheckbutton.configure(disabledforeground="#a3a3a3")
        self.ECheckbutton.configure(foreground="black")
        self.ECheckbutton.configure(highlightbackground=background)
        self.ECheckbutton.configure(highlightcolor="black")
        self.ECheckbutton.configure(justify='left')
        self.ECheckbutton.configure(offvalue=False, onvalue=True)
        self.ECheckbutton.configure(text='''Save Info''')
        self.ECheckbutton.configure(variable=self.ecb)
        self.ECheckbutton.configure(command=savecred)

        if credlist[0] == "1":
            self.ECheckbutton.select()
            self.EEntry1.insert(END, credlist[1])
            self.EEntry2.insert(END, credlist[2])

        self.FontCombobox1 = ttk.Combobox(self.PNotebook1_t4)
        self.FontCombobox1.place(
            relx=0.518, rely=0.869, relheight=0.05, relwidth=0.077)
        self.FontCombobox1.configure(state='readonly')
        self.FontCombobox1.configure(takefocus="", font=font)
        self.FontCombobox1.configure(values=[8, 9, 10, 11, 12, 13, 14, 15])

        self.SetLabel4 = tk.Label(self.PNotebook1_t4)
        self.SetLabel4.place(relx=0.411, rely=0.869, height=23, width=80)
        self.SetLabel4.configure(background=background)
        self.SetLabel4.configure(disabledforeground="#a3a3a3")
        self.SetLabel4.configure(foreground=foreground)
        self.SetLabel4.configure(text='''Font size:''', font=font)

        self.SetLabel5 = tk.Label(self.PNotebook1_t4)
        self.SetLabel5.place(relx=0.411, rely=0.932, height=23, width=65)
        self.SetLabel5.configure(background=background)
        self.SetLabel5.configure(disabledforeground="#a3a3a3")
        self.SetLabel5.configure(foreground=foreground)
        self.SetLabel5.configure(text='''Theme:''', font=font)

        self.ThemeCombobox2 = ttk.Combobox(self.PNotebook1_t4)
        self.ThemeCombobox2.place(
            relx=0.5, rely=0.932, relheight=0.05, relwidth=0.255)
        self.ThemeCombobox2.configure(takefocus="", font=font)
        self.ThemeCombobox2.configure(state='readonly')
        self.ThemeCombobox2.configure(values=themes)

        self.TSeparator5 = ttk.Separator(self.PNotebook1_t4)
        self.TSeparator5.place(relx=0.768, rely=0.847,  relheight=0.169)
        self.TSeparator5.configure(orient="vertical")

        self.TSeparator6 = ttk.Separator(self.PNotebook1_t4)
        self.TSeparator6.place(relx=0.393, rely=0.847,  relwidth=0.375)

        self.Button1 = tk.Button(self.PNotebook1_t4)
        self.Button1.place(relx=0.750, rely=0.021, height=44, width=200)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground=foreground)
        self.Button1.configure(background=background)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground=foreground)
        self.Button1.configure(highlightbackground=background)
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Open File Explorer''', font=font)
        self.Button1.configure(command=openExplorer)


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


class ScrolledText(AutoScroll, tk.Text):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @ _create_container
    def __init__(self, master, **kw):
        tk.Text.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)


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
