from flaskext.mysql import MySQL
from flask import Flask, render_template, request
import os

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'beml_1'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
con = mysql.connect()
cursor = con.cursor()

def pushData():
    cursor.execute("INSERT INTO txn_inpatient_item_det(MED_ITEM_ID,particulars,qty,price,NET_AMT, INPAITENT_ID) VALUES (%s,%s,%s,%s,%s,%s)",
                   (SrNo,particulars, quantity, price, amount,patient_id))
    con.commit()

def pushHeader():
    cursor.execute("INSERT INTO txn_inpatient_item_det(MED_ITEM_ID,INPAITENT_ID,particulars) VALUES (%s,%s,%s)",
                   (SrNo,patient_id," ".join(headerText)))
    con.commit()


count = 0
try:
    os.remove("beml.csv")
except:
    pass
with open("Capture.txt", "r") as fp:
    Lines = fp.readlines()
    title = "Sl No, Particulars, Quantity, Price, Amount"
    #with open("beml.csv", "a+") as ff:
    #    ff.write(title + "\n")
    nextLineNewRecord = False
    startRecording = False
    headerIsMedicineOrMaterial = False
    rows = []
    row = ""
    csv = ""
    temp = ""
    for line in Lines:
        x = 'InPatient No'
        if x in line:
            y = (line[line.find(x) + len(x):])
            patient_id = ''.join(filter(lambda i: i.isdigit(), y))
            #print(patient_id)
        if (startRecording):
            line_s = line.strip().replace("\\''","")
            # print(line_s)
            if line_s:
                if line_s.startswith("Sub Total"):
                    nextLineNewRecord = True
                    headerIsMedicineOrMaterial = False
                else:
                    nextLineNewRecord = False
                if nextLineNewRecord:
                    rows.append(row)
                    row = ""
                else:
                    if row:
                        if not headerIsMedicineOrMaterial:
                            row = row + " " + line_s
                        else:
                            data = line_s.split()
                            if not line_s.__contains__("Packed:"):
                                temp = temp + " " + line_s
                                try:
                                    a =  float(data[len(data) - 1])
                                    a = float(data[len(data) - 2])
                                    a = float(data[len(data) - 3])
                                    row = row + "[" + temp.replace("Charged :","")
                                    temp = ""
                                except Exception as e:
                                    pass
                    else:
                        row = line_s
                        if line_s.__contains__("Medicines") or line_s.__contains__("Materials"):
                            headerIsMedicineOrMaterial = True
        else:
            if line.strip().startswith("Ref"):
                startRecording = True
    if row:
        rows.append(row)

    for data in rows:
        dataSub = data.strip('"').split("[")
        header = dataSub[0].split()
        if header or len(dataSub) > 1:
            if header:
                SrNo = header[0]
                headerText = header[1:]
                #with open("beml.csv","a+") as ff:
                #   ff.write(SrNo + "," + " ".join(headerText) + "\n")
                pushHeader()
            for dd in dataSub[1:]:
                data_s = dd.strip('"').split()
                l = len(data_s)
                particulars = ""
                quantity = ""
                price = ""
                amount = ""

                for i, d in enumerate(data_s):
                    if (i < l - 3) or l < 3:
                        if particulars:
                            particulars = particulars + " " + d
                        else:
                            particulars = d
                    elif i == l - 3:
                        quantity = d
                    elif i == l - 2:
                        price = d
                    elif i == l - 1:
                        amount = d


                """
                if particulars.__contains__("]"):
                    csv = ',"[' + particulars.replace('"','""') + '",' + quantity + ',' + price + ',' + amount
    
                else:
                    csv = ',"' + particulars.replace('"','""') + '",' + quantity + ',' + price + ',' + amount
                """
                #with open("beml.csv","a+") as ff:
                    #ff.write(csv + "\n")
                #cursor.execute("DELETE FROM det_bill")
                pushData()
    print("Data inserted successfully")











"""
def authonticate():
  
    #reference_number = request.form['Reference Number']
    #date = request.form['Date']
    #staff_number = request.form['Staff Number']
    #staff_name = request.form['Staff Name']
    #patient_name = request.form['Patient Name']
    #patient_relationship = request.form['Patient Relationship']
    #hospital_name = request.form['Hospital Name']
    #hospital_address = request.form['Hospital Address']
    #reason_for_hospitality = request.form['Reason for Hospitality']
    #signature = request.form['signature']
    #patient_photo = request.form['Patient_Photo']

    cursor.execute("INSERT INTO costumer_data(Reference_Number,Date,Staff_Number,Staff_Name,Patient_Name,Patient_Relationship,Hospital_Name,Hospital_Adrdress,Reason_For_Hospitality,Signature,Patient_Photo) \
     #VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
      #             (reference_number, date, staff_number, staff_name, patient_name, patient_relationship, hospital_address, hospital_name,
       #             reason_for_hospitality, signature, patient_photo))
  
    cursor.execute("INSERT INTO detailed_bill(id,particulars,qty,price,amount) \
        VALUES (%s,%s,%s,%s,%s)",
                                (1,"particulars", 10, 200, 2000))
    con.commit()

    print("Data inserted successfully")

authonticate()
  """
