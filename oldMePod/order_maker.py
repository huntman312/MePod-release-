#!/usr/bin/env python
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

system = sys.platform
path = os.getcwd()


def customer_to_bill():
    return input("customer to bill: ").upper()


def ship_to():
    return input("where to ship: ").upper()


def date_of_order():
    d = datetime.datetime.today()
    return str(d.month) + "-" + str(d.day) + "-" + str(d.year)


def tool_brand():
    return input("tool brand: ").upper()


def tool_model():
    return input("tool model: ").upper()


def path_to_tool(toolBrand, toolModel):
    if system == "darwin":
        check = toolModel.replace('/', ':')
    elif system == "win32":
        check = toolModel.replace('/', '!')
    else:
        print("OS not supported yet")
        exit()

    filePath = path + "/" + "TOOL_DATABASE" + \
        "/" + toolBrand + "/" + check + ".txt"

    if os.path.isfile(filePath) == False:
        # if input("TOOL DOESNT EXIST, WOULD YOU LIKE TO ADD CUSTOM ENTRY? Y or N").upper() == "Y"

        return tool_parts_dict(False)

    else:
        return tool_parts_dict(filePath)

# call path to tool to get dctionary


def tool_parts_dict(filePath):
    if filePath == False:
        return False
    else:
        with open(filePath, "r") as toolTextFile:
            toolDict = toolTextFile.read()
            return literal_eval(toolDict)


customer = customer_to_bill()
shipTo = ship_to()
dateOfOrder = date_of_order()
pdfName = "parts order (" + customer + ") " + dateOfOrder + ".pdf"


def list_builder():
    finalPartsList = [["TOOL", "QUANTITY", "PART#", "DESCRIPTION"]]
    while 0 == 0:
        toolBrand = tool_brand()
        toolModel = tool_model()
        while 0 == 0:
            brand = toolBrand
            model = toolModel
            tempDict = path_to_tool(brand, model)
            if tempDict == False:
                ask = input(
                    "NO TOOL FOUND!! would you like to add a custom entry Y or N: ").upper()
                if ask == "Y":
                    fList = []

                    while 0 == 0:
                        print("type E to exit: or D to delete last entry: ")
                        cAmount = input("how many: ").upper()
                        if cAmount == "E":
                            print("                  !!EXITED!!")
                            break
                        if cAmount == "D":
                            print("                  !!DELETED!!")
                            print(
                                "-----------------------------------------------------------------------------------------------")
                            del finalPartsList[-1]
                        else:
                            customList = []
                            cPart = input("part#: ").upper()
                            cDescription = input("description: ").upper()
                            customList.append(brand + " " + model)
                            customList.append(cAmount)
                            customList.append(cPart)
                            customList.append(cDescription)
                            fList.append(customList)
                            print(
                                "-----------------------------------------------------------------------------------------------")
                            print("((LAST ENTRY))" + str(customList))
                    breakpoint
                    for x in fList:
                        finalPartsList.append(x)
                    break
                else:
                    break

            else:
                while 0 == 0:
                    print(
                        "-----------------------------------------------------------------------------------------------")
                    print("((LAST ENTRY))" + str(finalPartsList[-1]))
                    print("TYPE  E  WHEN DONE or  D  to delete last entry")
                    partQuantity = input("how many: ").upper()
                    if partQuantity == "E":
                        print("                  !!EXITED!!")
                        print(
                            "-----------------------------------------------------------------------------------------------")
                        loop2 = 2
                        break
                    if partQuantity == "D":
                        print("                  !!DELETED!!")
                        print(
                            "-----------------------------------------------------------------------------------------------")
                        del finalPartsList[-1]
                    else:
                        loop2 = 1
                        break
                breakpoint
                if loop2 == 2:
                    break
                else:
                    schemNumb = input("enter schematic number: ").upper()
                    if schemNumb in tempDict.keys():
                        list1 = []
                        list1.append(str(brand) + " " + str(model))
                        list1.append(str(partQuantity))
                        temp = list(tempDict[schemNumb])
                        for x in temp:
                            list1.append(x)
                        finalPartsList.append(list1)

                    else:
                        print("            **********(PART NOT FOUND)**********")
        breakpoint
        loop1 = 0
        while 0 == 0:
            print("-----------------------------------------------------------------------------------------------")
            print("((LAST ENTRY))" + str(finalPartsList[-1]))
            addNewTool = input(
                "add another tool Y or N:  D to delete last entry:  S to show current list: ").upper()
            if addNewTool == "N":
                loop1 = 1
                break
            if addNewTool == "S":
                print(" ")
                print("                   [[[CURRENT LIST OF PARTS]]]")
                for x in finalPartsList:
                    print(x)
            if addNewTool == "D":
                print("                     !!DELETED!!")
                print(
                    "-----------------------------------------------------------------------------------------------")
                del finalPartsList[-1]
            if addNewTool == "Y":
                loop1 = 2
                break
        breakpoint
        if loop1 == 1:
            break
        else:
            continue
    breakpoint
    return finalPartsList


info = [["BILL: ", customer], ["SHIP: ", shipTo], ["DATE: ", dateOfOrder]]

data = list_builder()


def pdfMaker():

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


pdfMaker()
