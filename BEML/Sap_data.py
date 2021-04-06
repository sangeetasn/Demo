from datetime import date
import os
count = 0
try:
    os.remove("Sap_data.csv")
except:
    pass
    title = "Document_date, Posting_date, Batch_inv_no, Doc_header_test, vendor,  Bill_amount, business_area, Section_code, assignment, Text, Amount"
    with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Python\\SAP_Data.csv", "a+") as ff:
        ff.write(title + "\n")

def check(a):
   with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Output.txt", "r") as fp:
        global b
        for line in fp:
            #a = 'Patient Name'
            if a in line:
                found = True
                txt = (line[line.find(a) + len(a):])
                txt = txt.replace(':', ' ')
                #print(a, txt)
                b=txt
                break



        return found

check('Discharge Date')
Document_Date=b
Doc_date = Document_Date.rstrip("\n")
#print('Document Date:',Doc_date)

today = date.today()
post_date =today.strftime("%d/%m/%Y")
Posting_date = post_date.rstrip("\n")
#print("Posting Date:", Posting_date)

check('Batch Inv.  No.')
Batch_Inv_No=b
Batch_No = Batch_Inv_No.rstrip("\n")
#print('Batch Inv Number:',Batch_No)

check('Auth Code :')
Auth_Code=b
Doc_Text = Auth_Code.rstrip("\n")
#print('Doc. Header Test:',Doc_Text)

Vendor='629035'
BusinessArea='100'
SectionCode='1000'

check('Bill No.')
Assign=b
Assignment = Assign.rstrip("\n")
#print('Assignment:',Assignment)

with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Output.txt", "r") as fp:
    Lines = fp.readlines()
    nextLineNewRecord = False
    startRecording = False
    headerIsMedicineOrMaterial = False
    rows = []
    row = ""
    csv = ""
    temp = ""
    vcount = 0
    for line in Lines:
        x = 'Total '

        if x in line:

            y = (line[line.find(x) + len(x):])
            Total = ''.join(filter(lambda i: i.isdigit(), y))

            if vcount == 1:
                Bill_Amount = Total
                #print(Bill_Amount)

            vcount += 1
    data = Doc_date + ',' + Posting_date +','+Batch_No+','+ Doc_Text +','+Vendor + ','+Bill_Amount+','+BusinessArea+','+SectionCode +','+Assignment
    #data = Document_Date+ ',' + post_date + ',' + Batch_Inv_No +',' + Auth_Code +','+Vendor +','+ Bill_Amount +','+BusinessArea+','+SectionCode+','+Assign+','+"null"+','+"null"
    with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Python\\SAP_Data.csv", "a+") as ff:
        ff.write(data + "\n")
