import csv

def main():
    f= open('q3.csv', 'r', encoding='ANSI')
    data = csv.reader(f)
    next(data)

    arr = [0]*9
    for row in data:
        row[4] = int(row[4])
        row[5] = int(row[5])
        hap = row[4]+ row[5]
        if(row[1]== "1호선"):
            arr[0]+=hap
        elif(row[1] == "2호선"):
            arr[1] +=hap
        elif(row[1] == "3호선"):
            arr[2] +=hap
        elif(row[1] == "4호선"):
            arr[3] +=hap
        elif(row[1] == "5호선"):
             arr[4] +=hap
        elif(row[1] == "6호선"):
            arr[5] +=hap
        elif(row[1] == "7호선"):
            arr[6] +=hap
        elif(row[1] == "8호선"):
            arr[7] +=hap
        elif(row[1] == "9호선"):
            arr[8] +=hap

    ans = [0]*4
    temp =0
    pos = 0
    for i in range(0,9):
        if ( temp < arr[i]):
            pos = i
            temp = arr[i]
    max1 = pos
    arr[pos] =0
    ans[0] = temp

    temp =0
    pos = 0
    for i in range(0,9):
        if ( temp < arr[i]):
            pos = i
            temp = arr[i]
    max2 = pos
    arr[pos] =0
    ans[1] = temp

    temp = 1000000000000
    pos = 0
    for i in range(0,9):
        if( temp > arr[i] and arr[i] >=1 ):
            temp = arr[i]
            pos = i
    min1 = pos
    arr[pos] =0
    ans[2] = temp

    temp = 1000000000000
    pos = 0
    for i in range(0,9):
        if( temp > arr[i] and arr[i] >=1 ):
            temp = arr[i]
            pos = i
    min2 = pos
    arr[pos] =0
    ans[3] = temp
        
    print("***Subway Report for Seoul on March 2023 ***")
    print("1st Busiest Line: Line {0:d} ({1:d})".format(max1+1,ans[0]))
    print("2st Busiest Line: Line {0:d} ({1:d})".format(max2+1,ans[1]))
    print("1st Least used Line: Line {0:d} ({1:d})".format(min1+1,ans[2]))
    print("2st Least used Line: Line {0:d} ({1:d})".format(min2+1,ans[3]))
    f.close()

if __name__ == "__main__":
    main()
