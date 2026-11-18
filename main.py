DELIMITER = ";"

class TIMESTAMP:
    weekday = ""
    hour = int()
    kWh = int()
    price = float()

def readTimestamps(Pfilename:str, Plist:list[TIMESTAMP]):
    print (f"Reading file \"{Pfilename}\"")
    file = open(Pfilename, 'r', encoding="UTF-8")
    data = file.readlines()
    for i in range(1,len(data)):
        if (len(data[i].strip()) == 0):
            continue
        else:
            tempList = data[i].rstrip().split(DELIMITER)
            timestamp = TIMESTAMP()
            timestamp.weekday = tempList[0]
            timestamp.hour = int(tempList[1])
            timestamp.kWh = int(tempList[2])
            timestamp.price = float(tempList[3])
            Plist.append(timestamp)
            tempList.clear()
    file.close()
    return None

def displayTimestamps(Pdata:list[TIMESTAMP]):
    print ("Electricity usage:")
    for i in range(len(Pdata)):
        print (f" - {Pdata[i].weekday} {Pdata[i].hour}:00, price {Pdata[i].price} €, consumption {Pdata[i].kWh} kWh, total {(Pdata[i].kWh * Pdata[i].price):.2f} €")
    return None

def main():
    print ("Program starting")
    csvData:list[TIMESTAMP] = []
    filename = input("Insert filename: ")
    readTimestamps(filename, csvData)
    displayTimestamps(csvData)
    print ("Program ending.")
    return None

if __name__ == "__main__":
    main() 