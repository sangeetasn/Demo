import os
count = 0
try:
    os.remove("C:\\Users\\wali\\Documents\\UiPath\\BEML2.0\\Python\\beml.csv")
except:
    pass
with open("C:\\Users\\wali\\Documents\\UiPath\\BEML2.0\\Python\\Capture.txt", "r") as fp:
    Lines = fp.readlines()
    title = "MED_ITEM_ID, PARTICULARS, QTY, PRICE, NET_AMT, INPAITENT_ID"
    with open("C:\\Users\\wali\\Documents\\UiPath\\BEML2.0\\Python\\beml.csv", "a+") as ff:
        ff.write(title + "\n")
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
            print(patient_id)
        if (startRecording):
            line_s = line.strip().replace("\\''","")
            print(line_s)
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
                with open("C:\\Users\\wali\\Documents\\UiPath\\BEML2.0\\Python\\beml.csv","a+") as ff:
                    ff.write(SrNo + "," + " ".join(headerText) + "\n")
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

                if particulars.__contains__("]"):
                    csv = ',"[' + particulars.replace('"','""') + '",' + quantity + ',' + price + ',' + amount + ',' + patient_id
                else:
                    csv = ',"' + particulars.replace('"','""') + '",' + quantity + ',' + price + ',' + amount + ',' + patient_id
                with open("C:\\Users\\wali\\Documents\\UiPath\\BEML2.0\\Python\\beml.csv","a+") as ff:
                    ff.write(csv + "\n")
