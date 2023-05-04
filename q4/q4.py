import csv

def main():
    f= open('q3.csv', 'r', encoding='ANSI')
    data = csv.reader(f)
    next(data)

    maxi = [0]*4
    mini = [10000000000]*4
    mostname = ['']*4
    leastname = ['']*4
    for row in data:
        row[4] = int(row[4])
        row[5] = int(row[5])
        hap = row[4]+ row[5]
        if(row[1]== "1호선"):
            if(maxi[0] <hap):
                maxi[0] = hap
                mostname[0] = row[3]
            if(mini[0] > hap):
                mini[0] = hap
                leastname[0] = row[3]
        elif(row[1] == "2호선"):
            if(maxi[1] <hap):
                maxi[1] = hap
                mostname[1] = row[3]
            if(mini[1] > hap):
                mini[1] = hap
                leastname[1] = row[3]
        elif(row[1] == "3호선"):
            if(maxi[2] <hap):
                maxi[2] = hap
                mostname[2] = row[3]
            if(mini[2] > hap):
                mini[2] = hap
                leastname[2] = row[3]
        elif(row[1] == "4호선"):
            if(maxi[3] <hap):
                maxi[3] = hap
                mostname[3] = row[3]
            if(mini[3] > hap):
                mini[3] = hap
                leastname[3] = row[3]

    print("***Subway Report for Seoul on March 2023***")
    for i in range(0,4):
        print("Line{0:d}:".format(i+1))    
        print("Busiest Station: {0:s} ({1:d})".format(mostname[i],maxi[i]))    
        print("Least used Station: {0:s} ({1:d})".format(leastname[i],mini[i]))
    f.close()

if __name__ == "__main__":
    main()
