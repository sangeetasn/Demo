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


            if vcount==1:
                print(Total)


            vcount += 1

            #str = Total
            #arr = str.split('\n')
            #print(arr[1])