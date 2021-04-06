import os
count = 0
try:
    os.remove("Bill_Summary.csv")
except:
    pass
with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Output.txt", "r") as fp:
    Lines = fp.readlines()
    title = "sl No, PARTICULARS, Amount"
    with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Python\\Bill_Summary.csv", "a+") as ff:
        ff.write(title + "\n")
    for line in Lines:
        data = line.split()
        if len(data) > 0 and data[0].strip().isnumeric():
            try:
                a = float(data[len(data)-1].strip())
                if len(data)>=3:
                    csv = data[0] + ","+ " ".join(data[1:len(data)-1])+"," +data[len(data)-1]
                    with open("C:\\Users\\Vinayak\\PycharmProjects\\BEML\\Python\\beml.csv", "a+") as ff:
                        ff.write(csv + "\n")
            except Exception as e:
                print(str(e))
                pass