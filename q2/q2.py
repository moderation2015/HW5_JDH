import csv

def main():
    f= open('q2.csv', 'r', encoding='ANSI')
    maxi =-1000
    temp =0
    datemaxi = ""
    mini =1000
    datemini = ""
    data = csv.reader(f)
    next(data)
    for row in data:
        if(row[0]=='' or row[1]=='' or row[2]=='' or row[3]=='' or row[4]==''):
            continue
        row[2]= float(row[2])
        row[3]= float(row[3])
        row[4]= float(row[4])
        temp = row[4] - row[3]
        if(maxi < temp):
            maxi = temp
            datemaxi = row[0]
        if(mini > temp):
            mini = temp
            datemini = row[0]

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Day with the Largest Temperature Variation: {0:s}".format(datemaxi))
    print("Maximum Temperature Difference: {0:.1f} Celsius".format(maxi))
    print("Day with the Smallest Temperature Variation: {0:s}".format(datemini))
    print("Miniimum Temperature Difference: {0:.1f} Celsius".format(mini))
    f.close()

if __name__ == "__main__":
    main()
