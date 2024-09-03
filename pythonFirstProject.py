print("")
cName = input("Enter Country Name: ")
olympicData = []

# function 1: 
def addDetails():
    print(f"Enter the only {cName}an Country data:")
    record = int(input("Enter limit how many athletes' data you want to add: "))
    for i in range(record):
        aName = input(f"Enter the {i+1} athlete's name: ")
        aEventName = input(f"Enter {i+1} event name: ")
        aEventYear = int(input("Enter the event year: "))
        aBronzeMedal = int(input("Enter how many Bronze medals he/she won: "))
        aSilverMedal = int(input("Enter how many Silver medals he/she won: "))
        aGoldMedal = int(input("Enter how many Gold medals he/she won: "))
        olympicData.append(
            {
                "Name": aName,
                "EventName": aEventName,
                "EventYear": aEventYear,
                "BronzeMedal": aBronzeMedal,
                "SilverMedal": aSilverMedal,
                "GoldMedal": aGoldMedal
            }
        )

#Function 2:
def viewData():
    header = f"{'Name':<20}{'EventName':<20}{'EventYear':<20}{'BronzeMedal':<20}{'SilverMedal':<20}{'GoldMedal':<20}"
    print(header)
    for data in olympicData:
        row = f"{data['Name']:<20}{data['EventName']:<20}{data['EventYear']:<20}{data['BronzeMedal']:<20}{data['SilverMedal']:<20}{data['GoldMedal']:<20}"
        print(row)

#Function 3:
def viewTotalMedals():
    totalBronze = 0
    totalSilver = 0
    totalGold = 0
    for data in olympicData:
        # totalBronze = totalBronze + data['BronzeMedal']
        totalBronze += data['BronzeMedal']
        totalSilver += data['SilverMedal']
        totalGold += data['GoldMedal']

    grandTotal = sum([totalBronze,totalSilver,totalGold])

    
    print(f"\nTotal Medals for {cName}:")
    print(f"Bronze Medals: {totalBronze}")
    print(f"Silver Medals: {totalSilver}")
    print(f"Gold Medals: {totalGold}")
    print(f"Total Medals: {grandTotal}\n")
    
#Function 4:
def viewAthletePerformance():
    searchName = input("Enter the Athlete name: ")
    found = False  
    for data in olympicData:
        if data['Name'].lower() == searchName.lower():    #Ujvl> ujvl      UJVL> ujvl 
            print(f"\nPerformance Statistics for {searchName}:")
            print(f"Event: {data['EventName']}")
            print(f"Year: {data['EventYear']}")
            print(f"Bronze Medals: {data['BronzeMedal']}")
            print(f"Silver Medals: {data['SilverMedal']}")
            print(f"Gold Medals: {data['GoldMedal']}\n")
            sum = (data['BronzeMedal'] + data['SilverMedal'] + data['GoldMedal'])
            print(f"Total medal by {searchName} {sum}")
            # def total():
            #     for data in olympicData:
            #         totalMedalByUser = BronzeMedal + SilverMedal + GoldMedal
            #         print(f"Total medal by {searchName} {totalMedalByUser}")
            found = True
            break
    if not found:
        print(f"No data found for athlete {searchName}.\n")

#Function 5:
def viewEventDetails():
    eventName = input("Enter the Event name: ")
    eventYear = int(input("Enter the Event year: "))
    found = False
    print(f"\nDetails for Event: {eventName} ({eventYear})")
    header = f"{'Athlete Name':<20}{'BronzeMedals':<15}{'SilverMedals':<15}{'GoldMedals':<15}"
    print(header)
    for data in olympicData:
        if data['EventName'].lower() == eventName.lower() and data['EventYear'] == eventYear:
            row = f"{data['Name']:<20}{data['BronzeMedal']:<15}{data['SilverMedal']:<15}{data['GoldMedal']:<15}"
            print(row)
            found = True
    if not found:
        print(f"No data found for event {eventName} in {eventYear}.\n")
   

#Function 6:
def viewStatistics():
    totalAthletes = len(olympicData)
    if totalAthletes == 0:
        print("No data available for statistics.\n")
        return
    print("\nOlympic Statistics:")
    print(f"Total Athletes: {totalAthletes}")
    for data in olympicData:
        totalBronze = sum([data['BronzeMedal']])
        totalSilver = sum([data['SilverMedal']])
        totalGold = sum([data['GoldMedal']])
        totalMedals = totalBronze + totalSilver + totalGold

        avgBronze = totalBronze / totalAthletes
        avgSilver = totalSilver / totalAthletes
        avgGold = totalGold / totalAthletes
        avgTotalMedals = totalMedals / totalAthletes

        

        print(f"Average Bronze Medals per Athlete: {avgBronze:.2f}")
        print(f"Average Silver Medals per Athlete: {avgSilver:.2f}")
        print(f"Average Gold Medals per Athlete: {avgGold:.2f}")
        print(f"Average Total Medals per Athlete: {avgTotalMedals:.2f}\n")
    
    

while True:
    print("1. Add Data")
    print("2. View Data")
    print("3. View Medal Count by Country")
    print("4. View Athlete Performance")
    print("5. View Event Details")
    print("6. View Statistics")
    print("7. Exit")
    choice = input("Enter your choice: ")
    match choice:
        case '1':
            addDetails()
        case '2':
            viewData()
        case '3':
            viewTotalMedals()
        case '4':
            viewAthletePerformance()
        case '5':
            viewEventDetails()
        case '6':
            viewStatistics()
        case '7':
            exit()
            break
        case _:
            print("You Entered Something Wrong, Try Again!")
            break
