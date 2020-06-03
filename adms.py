import mysql.connector
from tabulate import tabulate


mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Toori7021998"
)

def addNewRecord(cnic, pName, num, email, add):
    mySql_use_query = "USE airline_management_system "
    mySql_insert_query = "INSERT INTO passenger_record VALUES(%s, %s, %s, %s, %s)"

    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_insert_query, (cnic, pName, num, email, add))
        print("Passenger created successfully")
    
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def updatePassDetail(cnic, flag, new):
    mySql_use_query = "USE airline_management_system "
    if flag == "1":
        mySql_update_query = "UPDATE passenger_record SET Name = %s WHERE CNIC = %s"
    elif flag == "2":
        mySql_update_query = "UPDATE passenger_record SET CNIC = %s WHERE CNIC = %s"
    elif flag == "3":
        mySql_update_query = "UPDATE passenger_record SET Contact_Number = %s WHERE CNIC = %s"
    elif flag == "4":
        mySql_update_query = "UPDATE passenger_record SET Email_Address = %s WHERE CNIC = %s"
    elif flag == "5":
        mySql_update_query = "UPDATE passenger_record SET Address = %s WHERE CNIC = %s"

    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_update_query, (new, cnic))
        print("Record inserted successfully into table")
    
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def getFlights(depart, arr, depart_t, arr_t):
    mySql_use_query = "USE airline_management_system "
    mySql_get_query = "SELECT * FROM flight_record where departure = %s and arrival = %s  and depart_time >= %s and arrival_time<= %s "
    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_get_query, (depart, arr, depart_t, arr_t))
        result = cursor.fetchall()
        if (len(result) == 0):
            print("\n")
            print("No flight found")
            print("\n")
        else:
            for row in result:
                print("\n")
                print("Flight ID: ", row[0])
                print("Departure: ", row[1])
                print("Arrival: ", row[2])
                print("Airplane ID: ", row[3])
                print("Fare: ", row[4])
                print("Departure Time: ", row[5])
                print("Arrival Time:", row[6])
                print("\n")

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def getMinFare(dep, arr):
    mySql_use_query = "USE airline_management_system "
    mySql_getFare_query = "SELECT * FROM flight_record where fare in (SELECT MIN(fare) FROM flight_record WHERE departure = %s and arrival = %s);"
    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_getFare_query, (dep, arr))
        result = cursor.fetchall()
        if (len(result) == 0):
            print("\n")
            print("No flight found")
            print("\n")
        else:
            print(tabulate(result, headers=['Flight ID', 'Departure', 'Arrival', 'Airplane ID', 'Fare', 'Departure time', 'Arrival Time' ], tablefmt='psql'))

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def addFlight(id, depart, arr, planeID, fare, depart_time, arr_time):
    mySql_use_query = "USE airline_management_system "
    mySql_insert_query = "INSERT INTO flight_record VALUES(%s, %s, %s, %s, %s, %s, %s)"

    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_insert_query, (id, depart, arr, planeID, fare, depart_time, arr_time))
        print("Flight created successfully")
    
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def updateFlight(id, flag, new):
    mySql_use_query = "USE airline_management_system "
    
    if flag == "1":
        mySql_update_query = "UPDATE flight_record SET departure = %s WHERE flight_ID = %s"
    elif flag == "2":
        mySql_update_query = "UPDATE flight_record SET arrival = %s WHERE flight_ID = %s"
    elif flag == "3":
        mySql_update_query = "UPDATE flight_record SET airplane_ID = %s WHERE flight_ID = %s"
    elif flag == "4":
        mySql_update_query = "UPDATE flight_record SET fare = %s WHERE flight_ID = %s"
    elif flag == "5":
        mySql_update_query = "UPDATE flight_record SET depart_time = %s WHERE flight_ID = %s"
    elif flag == "6":
        mySql_update_query = "UPDATE flight_record SET arrival_time = %s WHERE flight_ID = %s"

    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_update_query, (new, id))
        print("Record successfully updated")
    
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def deleteFlight(id):
    mySql_use_query = "USE airline_management_system"
    mySql_delete_query_flight = "DELETE FROM flight_record WHERE flight_ID = %s"
    mySql_delete_query_ticket = "DELETE FROM ticket WHERE flight_ID = %s"
    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_delete_query_ticket, (id,))
        cursor.execute(mySql_delete_query_flight, (id,))  
        print("Flight deleted successfully")
    
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def generateTicket(cnic, flightID):
    mySql_use_query = "USE airline_management_system "
    mySql_generate_query = "INSERT INTO ticket(CNIC, flight_ID) VALUES(%s, %s)"

    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_generate_query, (cnic, flightID))
        print("Flight created successfully")

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def getHistory(cnic):
    mySql_use_query = "USE airline_management_system "
    mySql_history_query = "SELECT flight_record.flight_ID, flight_record.departure, flight_record.arrival, flight_record.airplane_ID, flight_record.fare, flight_record.depart_time, flight_record.arrival_time FROM flight_record INNER JOIN ticket WHERE ticket.flight_ID = flight_record.flight_ID AND CNIC = %s"
    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_history_query, (cnic,))
        result = cursor.fetchall()
        print(tabulate(result, headers=['Flight ID', 'Departure', 'Arrival', 'Airplane ID', 'Fare', 'Departure time', 'Arrival Time' ], tablefmt='psql'))

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def deleteTicket(ticketNum):
    mySql_use_query = "USE airline_management_system"
    mySql_delete_query = "DELETE FROM ticket WHERE ticket_ID = %s"
    cursor = mydb.cursor()
    cursor.execute(mySql_use_query)
    try:
        cursor.execute(mySql_delete_query, (ticketNum,))  
        print("Ticket deleted successfully")
    
    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return 
    mydb.commit()
    cursor.close()

def viewFlights(airport, day):
    print("\n Ye nahi hua :( \n")
    # mySql_use_query = "USE airline_management_system"
    # mySql_departsTodate_query = "SELECT CONVERT(depart_time, date) FROM flight_record"
    # mySql_arrivesTodate_query = "SELECT CONVERT(arrival_time, date) FROM flight_record"
    # cursor = mydb.cursor()
    # mySql_getFlights_query = "SELECT * FROM flight_record WHERE departure = %s OR arrival = %s AND WHERE day in deparDates OR  "
    
    # try:
    #     cursor.execute(mySql_use_query)
    #     cursor.execute(mySql_getFlights_query, (airport, airport, day, day,))
    #     result = cursor.fetchall()
    #     if (len(result) == 0):
    #         print("\n")
    #         print("No flight found")
    #         print("\n")
    #     else:
    #         for row in result:
    #             print("\n")
    #             print("Flight ID: ", row[0])
    #             print("Departure: ", row[1])
    #             print("Arrival: ", row[2])
    #             print("Airplane ID: ", row[3])
    #             print("Fare: ", row[4])
    #             print("Departure Time: ", row[5])
    #             print("Arrival Time:", row[6])
    #             print("\n")
    # except mysql.connector.Error as error:
    #     print("Error: {}".format(error))
    #     return 
    # mydb.commit()
    # cursor.close()

def printAll():
    mySql_use_query = "USE airline_management_system"
    mySql_flight_query = "SELECT * FROM flight_record"
    mySql_passenger_query = "SELECT * FROM passenger_record"
    mySql_ticket_query = "SELECT * FROM ticket"
    cursor = mydb.cursor()
    try:
        cursor.execute(mySql_use_query)
        cursor.execute(mySql_flight_query)
        result = cursor.fetchall()
        print(tabulate(result, headers=['Flight ID', 'Departure', 'Arrival', 'Airplane ID', 'Fare', 'Departure time', 'Arrival Time' ], tablefmt='psql'))
        cursor.execute(mySql_passenger_query)
        result = cursor.fetchall()
        print(tabulate(result, headers=['CNIC', 'Name', 'Contact Number', 'Email address', 'Address'], tablefmt='psql'))
        cursor.execute(mySql_ticket_query)
        result = cursor.fetchall()
        print(tabulate(result, headers=['Ticket ID', 'CNIC', 'Flight ID'], tablefmt='psql'))

    except mysql.connector.Error as error:
        print("Error: {}".format(error))
        return
    mydb.commit()
    cursor.close()

def recepMenu():
    print("\n1: Create a new passenger record.")
    print("2: Update details on an existing passenger record.")
    print("3: View all available flights in a time window.")
    print("4: Generate ticket record for a passenger.")
    print("5: View the cheapest flight.")
    print("6: View flight history of passenger.")
    print("7: Cancel a ticket record.")
    print("0: Logout.\n")

def adminMenu():
    print("\n1: Add a new flight record.")
    print("2: Update details of a flight record.")
    print("3: Cancel a flight record.")
    print("4: View incoming and outgoing flights of an airport for a date.")
    print("5: View all data in tabular form.")
    print("0: Logout.\n")

def main():
    print("\nWelcome to the Airline database\n")
    adminUname = "TaimoorArif"
    adminPasswrd = "7021998"
    recepUname = "Recep"
    recepPasswrd = "12345"
    login = False
    inUse = ""
    while (login is False):
        username = input("Username: ")
        password = input("Password: ")
        print("\n")
        if (username == recepUname and password == recepPasswrd):
            print("Welcome", username)
            inUse = "Receptionist"
            login = True
        elif (username == adminUname and password == adminPasswrd):
            print("Welcome", username)
            inUse = "Admin"
            login = True
        else:
            print("Username or password not recognized. Please try again.")
    if (inUse == "Receptionist"):
        print('\n')
        val = ""
        while (val != "0"):
            recepMenu()
            print('\n')
            val = input("")
            
            if (val == "1"):
                while (True):
                    name = input("Enter Full Name: ")
                    cnic = input("Enter CNIC number: ")
                    if (len(cnic) != 15):
                        print("Invalid CNIC number")
                        continue
                    contactNum = input("Enter contact number: ")
                    if (len(contactNum) != 11):
                        print("Invalid contact number")
                        continue
                    email = input("Enter email address: ")
                    address = input("Enter address: ")
                    break
                
                addNewRecord(cnic, name, contactNum, email,address)                        
            
            elif(val == "2"):
                while True:
                    cnic = input("Enter CNIC of passenger whose detail you want to update: ")
                    if (len(cnic) != 15):
                        print("Invalid CNIC number")
                        continue
                    else:
                        choice = input("Update: \n 1: Name \n 2: CNIC \n 3: Contact Number \n 4: Email address \n 5: Address \n")
                        newVal = input("Input new data value: ")
                        if (choice == "1"):
                            updatePassDetail(cnic, "1", newVal)
                        elif (choice == "2"):
                            if (len(newVal) != 15):
                                print("Invalid CNIC number")
                                continue
                            else:
                                updatePassDetail(cnic, "2", newVal)
                        elif (choice == "3"):
                            if (len(newVal) != 11):
                                print("Invalid Contact number")
                                continue
                            else:
                                updatePassDetail(cnic, "3", newVal)
                        elif (choice == "4"):
                            updatePassDetail(cnic, "4", newVal)
                        elif (choice == "5"):
                            updatePassDetail(cnic, "5", newVal)
                    break
            elif (val == "3"):
                IATAs = ["LHE", "UET", "LYP", "MUX," "RYK," "MUD", "BHV", "PEW", "KHI", "WNS"]
                
                while (True):
                    departIATA = input("Enter the departure airport IATA: ")
                    if (departIATA not in IATAs):
                        print("Airport not covered")
                        continue
                    arrIATA = input("Enter the arrival airport IATA: ")
                    if (arrIATA not in IATAs):
                        print("Airport not covered")
                        continue
                    break
                
                departTime = input("Enter departure time in format (YYYY-MM-DD HH:MM:SS): ")
                arrTime = input("Enter arrival time in format (YYYY-MM-DD HH:MM:SS): ")
                getFlights(departIATA, arrIATA, departTime, arrTime)                     
            elif (val == "4"):
                while True:
                    cnic = input("Enter CNIC number: ")
                    if (len(cnic) != 15):
                        print("Invalid CNIC number")
                        continue
                    flightid = input("Enter flight ID: ")
                    generateTicket(cnic, flightid)
                    break
            
            elif (val == "5"):
                IATAs = ["LHE", "UET", "LYP", "MUX," "RYK," "MUD", "BHV", "PEW", "KHI", "WNS"]
                
                while (True):
                    departIATA = input("Enter the departure airport IATA: ")
                    if (departIATA not in IATAs):
                        print("Airport not covered")
                        continue
                    arrIATA = input("Enter the arrival airport IATA: ")
                    if (arrIATA not in IATAs):
                        print("Airport not covered")
                        continue
                    break
                getMinFare(departIATA, arrIATA)     
            
            elif(val == "6"):
                while True:
                    cnic = input("Enter CNIC number: ")
                    if (len(cnic) != 15):
                        print("Invalid CNIC number")
                        continue
                    break
                getHistory(cnic)

            elif (val == "7"):
                ticketNum = int(input("Enter ticket number: "))
                deleteTicket(ticketNum)
            
            elif (val == "0"):
                print("Logged out.")
                break
    
    if (inUse == "Admin"):
        
        val = ""
        while(val != "0"):
            print('\n')
            adminMenu()
            print('\n')
            val = input()
            IATAs = ["LHE", "UET", "LYP", "MUX," "RYK," "MUD", "BHV", "PEW", "KHI", "WNS"]
            if (val == "1"):
                while True:
                    flightID = int(input("Enter flight ID: "))
                    departure = input("Enter departure airport IATA: ")
                    if (departure not in IATAs):
                        print("Airport not covered")
                        continue
                    arrival = input("Enter arrival airport IATA: ")
                    if (arrival not in IATAs):
                        print("Airport not covered")
                        continue
                    airplaneID = input("Enter airplane ID: ")
                    fare = input("Enter flight fare: ")
                    departTime = input("Enter departure time in format (YYYY-MM-DD HH:MM:SS): ")
                    arrTime = input("Enter arrival time in format (YYYY-MM-DD HH:MM:SS): ")
                    addFlight(flightID, departure, arrival, airplaneID, fare, departTime, arrTime)
                    break
            elif (val == "2"): 
                id = int(input("Enter the flight ID for the flight you want to alter: "))
                choice = input("Update: \n 1: Departure ariport \n 2: Arrival airport \n 3: Airplane ID \n 4: Flight fare \n 5: Departure time \n 6: Arrival time \n")
                if (choice == "1"):
                    while True:
                        departure = input("Enter Departure airport IATA: ")
                        if (departure not in IATAs):
                            print("Airport not covered")
                            continue
                        else:
                            updateFlight(id, choice, departure)
                            break 
                
                elif (choice == "2"):
                    while True:
                        arrival = input("Enter arrival airport IATA: ")
                        if (arrival not in IATAs):
                            print("Airport not covered")
                            continue
                        else:
                            updateFlight(id, choice, arrival)
                            break
                
                elif (choice == "3"):
                    newID = input("Please input new plane ID: ")
                    updateFlight(id, choice, newID)
                    break
                
                elif (choice == "4"):
                    newFare = input("Please inpute new flight fare: ")
                    updateFlight(id, choice, newFare)
                    break
                
                elif(choice == "5"):
                    departTime = input("Enter new departure time in format (YYYY-MM-DD HH:MM:SS): ")
                    updateFlight(id, choice, departTime)
                    break

                elif(choice == "6"):
                    arrivalTime = input("Enter new arrival time in format (YYYY-MM-DD HH:MM:SS): ")
                    updateFlight(id, choice, arrivalTime)
                    break

            elif (val == "3"):
                id = int(input("Enter ID for the flight record you'd like to remove: "))
                deleteFlight(id)
            
            elif (val == "4"):
                IATAs = ["LHE", "UET", "LYP", "MUX," "RYK," "MUD", "BHV", "PEW", "KHI", "WNS"]
                while True:
                    airport = input("Enter airport IATA: ")
                    if airport not in IATAs:
                        print("Airport not covered")
                        continue
                    break
                date = input("Enter the date (YYYY-MM-DD): ")
                viewFlights(airport, date)
            elif (val == "5"):
                printAll()
            
            elif (val == "0"):
                print("Logged out successfully")
                break
        
    return 0

main()