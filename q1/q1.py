import csv

def main():
    f= open('q1.csv', 'r', encoding='ANSI')
    avg =0.0
    mini = 0.0
    maxi = 0.0
    count =0
    data = csv.reader(f)
    next(data)
    for row in data:
        if(row[0]=='' or row[1]=='' or row[2]=='' or row[3]=='' or row[4]==''):
            continue
        avg += float(row[2])
        mini += float(row[3])
        maxi += float(row[4])
        count+=1
    avg /= count
    mini /= count
    maxi /= count
    avg = round(avg,2)
    mini = round(mini,2)
    maxi = round(maxi,2)

    print("*** Annual Temperature Report for Seoul in 2022 ***")
    print("Average Temperature: {0:.2f} Celsius".format(avg))
    print("Average Minimum Temperature: {0:.2f} Celsius".format(mini))
    print("Average Maximum Temperature: {0:.2f} Celsius".format(maxi))
    f.close()

if __name__ == "__main__":
    main()
