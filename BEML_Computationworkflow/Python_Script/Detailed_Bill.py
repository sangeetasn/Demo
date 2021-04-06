import os
count = 0
try:
    os.remove("C:\\Users\\dell\\Documents\\UiPath\\BEML_Workflow1set\\Python_Script\\CSV Files\\beml.csv")
except:
    pass
with open("C:\\Users\\dell\\Documents\\UiPath\\BEML_Workflow1set\\Python_Script\\Input text_files\\Capture.txt", "r") as fp:
    Lines = fp.readlines()
    title = "MED_ITEM_ID,PARTICULARS,QTY,PRICE,NET_AMT"
    with open("C:\\Users\\dell\\Documents\\UiPath\\BEML_Workflow1set\\Python_Script\\CSV Files\\beml.csv", "a+") as ff:
        title = title.replace(" ","")
        ff.write(title + "\n")
    nextLineNewRecord = False
    startRecording = False
    headerIsMedicineOrMaterial = False
    rows = []
    row = ""
    csv = ""
    temp = ""
    for line in Lines:
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
                with open("C:\\Users\\dell\\Documents\\UiPath\\BEML_Workflow1set\\Python_Script\\CSV Files\\beml.csv","a+") as ff:
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
                particulars=particulars.replace("'","''")

                if particulars.__contains__("]"):
                    csv = ',"[' + particulars.replace('"','""') + '",' + quantity + ',' + price + ',' + amount
                else:
                    csv = ',"' + particulars.replace('"','""') + '",' + quantity + ',' + price + ',' + amount
                with open("C:\\Users\\dell\\Documents\\UiPath\\BEML_Workflow1set\\Python_Script\\CSV Files\\beml.csv","a+") as ff:
                    ff.write(csv + "\n")
