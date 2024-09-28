# lots_in_gram = 13.3
# pounds_in_talent = 20
# lots_per_pound = 32
#
# talents = float(input("Enter talents: "))
# pounds = float(input("Enter pounds: "))
# lots = float(input("Enter lots: "))
# total_lots = (talents * pounds_in_talent * lots_per_pound ) + (pounds * lots_per_pound ) + lots
# total_grams = total_lots * lots_in_gram
#
#
# kilograms = int(total_grams // 1000)
# grams = total_grams % 1000
# print(f"The weight in modern units: {kilograms} kilograms and {grams:.2f} grams.")
#size_zander = int(input("Enter the size of zender in cm : "))
# if size_zander >= 42 :
#     print("fish released successfully")
# else:
#     print("fish released unsuccessfully")
#     print(f"The fish is {size_zander:.2f} centimeters below the size limit")

# def greet():
#     print("Hello!")
#     return
#
# print("A new day starts with a greeting.")
# greet()
# print("Now we can move to other business.")
# movies = []
# movies.append((input("Enter a movie name 1 : ")))
# movies.append((input("Enter a movie name 2 : ")))
# movies.append((input("Enter a movie name 3 : ")))
# print(movie

# import random
#
# random_num = random.randint(1, 10 )
# while True:
#     guess= int(input("Guess a number between 1 and 10 "))
#     if guess > random_num:
#         print("too high")
#     elif guess < random_num:
#         print("too low ")
#     else:
#         print("you guessed it right")
#         break
# print("welcome to leap year testing code ")
#
# while True:
#     year = int(input("enter the year to test leap year: "))
#     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#
#         print("leap year ")
#     else:
#         print("not leap year")
#
#
#
#
#
#Let's write a program that asks the user how many times to greet. After that the program will print out the greetings:
# count = int(input("enter how many times do you want to greet: "))
# finish_roumds = 0
#
# while count > finish_roumds:
#     print("Good morning")
#     finish_roumds = finish_roumds + 1
# print(finish_roumds
# first = 1
# while first <=5 :
#     second = 2
#     while second <=5:
#         print(f"{first} muliple by {second} is {first*second}")
#         second += 1
#     first +=  1
#
# names = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary"]
#
# print(names[-5])
# print(names[-1])
# print(names[-2])
# print(names[0:5])
# print(names[2:])
# print(names)
import mysql.connector

def get_city_id_by_country(country):
    cursor = connection.cursor()
    sql = f"SELECT id, name FROM city WHERE country = '{country}'"
    cursor.execute(sql)
    result = cursor.fetchone()  # Fetches the first city for simplicity; adjust as needed.
    cursor.close()
    return result

def get_airports_in_city(city_id):
    cursor = connection.cursor()
    sql = f"SELECT id, name FROM airport WHERE city_id = {city_id}"
    cursor.execute(sql)
    airports = cursor.fetchall()
    cursor.close()
    return airports

def get_available_flights(origin_airport_id, destination_airport_id):
    cursor = connection.cursor()
    sql = f"SELECT flight_number, departure_time, arrival_time FROM flight WHERE origin_airport_id = {origin_airport_id} AND destination_airport_id = {destination_airport_id}"
    cursor.execute(sql)
    flights = cursor.fetchall()
    cursor.close()
    return flights

def get_distance(city1_id, city2_id):
    cursor = connection.cursor()
    sql = f"SELECT distance_km FROM distance WHERE city1_id = {city1_id} AND city2_id = {city2_id}"
    cursor.execute(sql)
    result = cursor.fetchone()
    cursor.close()
    return result[0] if result else None

def get_weather_report(city_id):
    cursor = connection.cursor()
    sql = f"SELECT temperature, condition, date FROM weather WHERE city_id = {city_id} ORDER BY date DESC LIMIT 1"
    cursor.execute(sql)
    weather = cursor.fetchone()
    cursor.close()
    return weather

def select_option(prompt, options):
    print(prompt)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = int(input("Select an option by number: "))
    return options[choice - 1]

# Main program
conn = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='root',
    password='2004',
    charset='utf8mb4',
    collation='utf8mb4_general_ci',
    autocommit=True
)

# Ask for the current location
countries = ['United Kingdom', 'France', 'Germany', 'Italy', 'Spain', 'Portugal', 'Netherlands', 'Russia', 'Greece', 'Switzerland',
             'Japan', 'China', 'South Korea', 'Thailand', 'Singapore', 'India', 'United Arab Emirates', 'Saudi Arabia', 'Bangladesh', 'Pakistan']
current_country = select_option("Where are you now? Choose your country:", countries)
current_city = get_city_id_by_country(current_country)

if current_city:
    print(f"The closest city is {current_city[1]}.")
    current_airports = get_airports_in_city(current_city[0])

    if current_airports:
        print("Available airports in your current city:")
        for i, airport in enumerate(current_airports, 1):
            print(f"{i}. {airport[1]}")
        origin_airport_id = current_airports[int(input("Select an airport by number: ")) - 1][0]

        # Ask for the destination
        destination_country = select_option("Where do you want to go? Choose your destination country:", countries)
        destination_city = get_city_id_by_country(destination_country)

        if destination_city:
            print(f"The closest city is {destination_city[1]}.")
            destination_airports = get_airports_in_city(destination_city[0])

            print("\nAvailable airports in the destination city:")
            for i, airport in enumerate(destination_airports, 1):
                print(f"{i}. {airport[1]}")
            destination_airport_id = destination_airports[int(input("Select an airport by number: ")) - 1][0]

            # Show available flights
            flights = get_available_flights(origin_airport_id, destination_airport_id)
            if flights:
                print("\nAvailable flights:")
                for flight in flights:
                    print(f"Flight {flight[0]} departs at {flight[1]} and arrives at {flight[2]}")
            else:
                print("No flights available between the selected airports.")

            # Calculate travel time
            distance = get_distance(current_city[0], destination_city[0])
            if distance:
                print(f"\nThe distance between {current_city[1]} and {destination_city[1]} is {distance} km.")
                travel_time = distance / 800  # Assuming an average speed of 800 km/h
                print(f"Estimated travel time: {travel_time:.2f} hours.")
            else:
                print("Distance data is not available for the selected cities.")

            # Display weather report at the destination after "arrival"
            weather = get_weather_report(destination_city[0])
            if weather:
                print(f"Weather at {destination_city[1]} upon arrival: {weather[1]} with temperature {weather[0]}°C.")
            else:
                print("No weather data available for the destination.")
        else:
            print("Destination city not found.")
    else:
        print("No airports found in your city.")
else:
    print("Current city not found.")

connection.close()




INSERT INTO flight (flight_number, origin_airport_id, destination_airport_id, departure_time, arrival_time) VALUES

-- Add more rows following this format



-- Flights from Dhaka (19) to all other airports

-- Continue this for all airports with each to each other airport pair
INSERT
INTO
flight(flight_number, origin_airport_id, destination_airport_id, departure_time, arrival_time)
VALUES
('FL301', 19, 1, '07:00:00', '10:00:00'), -- Dhaka
to
Heathrow(London)
('FL302', 19, 2, '08:00:00', '11:00:00'), -- Dhaka
to
Charles
de
Gaulle(Paris)
('FL303', 19, 3, '09:00:00', '12:00:00'), -- Dhaka
to
Berlin
Brandenburg
('FL304', 19, 4, '10:00:00', '13:00:00'), -- Dhaka
to
Leonardo
da
Vinci(Rome)
('FL305', 19, 5, '11:00:00', '14:00:00'), -- Dhaka
to
Madrid
('FL306', 19, 6, '12:00:00', '15:00:00'), -- Dhaka
to
Lisbon
('FL307', 19, 7, '13:00:00', '16:00:00'), -- Dhaka
to
Amsterdam
Schiphol
('FL308', 19, 8, '14:00:00', '18:00:00'), -- Dhaka
to
Sheremetyevo(Moscow)
('FL309', 19, 9, '15:00:00', '19:00:00'), -- Dhaka
to
Athens
('FL310', 19, 10, '16:00:00', '20:00:00'), -- Dhaka
to
Zurich
('FL311', 19, 11, '17:00:00', '23:00:00'), -- Dhaka
to
Narita(Tokyo)
('FL312', 19, 12, '18:00:00', '02:00:00'), -- Dhaka
to
Beijing
Capital
('FL313', 19, 13, '19:00:00', '04:00:00'), -- Dhaka
to
Incheon(Seoul)
('FL314', 19, 14, '20:00:00', '05:00:00'), -- Dhaka
to
Suvarnabhumi(Bangkok)
('FL315', 19, 15, '21:00:00', '06:00:00'), -- Dhaka
to
Changi(Singapore)
('FL316', 19, 16, '22:00:00', '07:00:00'), -- Dhaka
to
Indira
Gandhi(New
Delhi)
('FL317', 19, 17, '23:00:00', '09:00:00'), -- Dhaka
to
Dubai
('FL318', 19, 18, '05:00:00', '10:00:00'), -- Dhaka
to
King
Khalid(Riyadh)
('FL319', 19, 20, '06:00:00', '11:00:00'), -- Dhaka
to
Jinnah
International(Karachi)

-- Flights
from London Heathrow

(1)
to
all
other
airports
('FL401', 1, 2, '06:00:00', '08:00:00'), -- Heathrow
to
Charles
de
Gaulle(Paris)
('FL402', 1, 3, '07:00:00', '09:30:00'), -- Heathrow
to
Berlin
Brandenburg
('FL403', 1, 4, '08:00:00', '11:00:00'), -- Heathrow
to
Leonardo
da
Vinci(Rome)
('FL404', 1, 5, '09:00:00', '12:00:00'), -- Heathrow
to
Madrid
('FL405', 1, 6, '10:00:00', '13:00:00'), -- Heathrow
to
Lisbon
('FL406', 1, 7, '11:00:00', '13:30:00'), -- Heathrow
to
Amsterdam
Schiphol
('FL407', 1, 8, '12:00:00', '16:00:00'), -- Heathrow
to
Sheremetyevo(Moscow)
('FL408', 1, 9, '13:00:00', '17:00:00'), -- Heathrow
to
Athens
('FL409', 1, 10, '14:00:00', '17:00:00'), -- Heathrow
to
Zurich
('FL410', 1, 11, '15:00:00', '06:00:00'), -- Heathrow
to
Narita(Tokyo)
('FL411', 1, 12, '16:00:00', '07:00:00'), -- Heathrow
to
Beijing
Capital
('FL412', 1, 13, '17:00:00', '08:30:00'), -- Heathrow
to
Incheon(Seoul)
('FL413', 1, 14, '18:00:00', '10:00:00'), -- Heathrow
to
Suvarnabhumi(Bangkok)
('FL414', 1, 15, '19:00:00', '11:00:00'), -- Heathrow
to
Changi(Singapore)
('FL415', 1, 16, '20:00:00', '12:00:00'), -- Heathrow
to
Indira
Gandhi(New
Delhi)
('FL416', 1, 17, '21:00:00', '13:00:00'), -- Heathrow
to
Dubai
('FL417', 1, 18, '22:00:00', '14:00:00'), -- Heathrow
to
King
Khalid(Riyadh)
('FL418', 1, 19, '23:00:00', '05:00:00'), -- Heathrow
to
Dhaka
('FL419', 1, 20, '23:30:00', '06:30:00');
-- Heathrow
to
Jinnah
International(Karachi)

-- Flights
from Paris Charles

de
Gaulle(2)
to
all
other
airports
('FL501', 2, 1, '2024-09-22 06:00:00', '2024-09-22 08:00:00'), -- Charlesde
Gaulle
to
Heathrow(London)
('FL502', 2, 3, '2024-09-22 07:00:00', '2024-09-22 09:00:00'), -- Charles
de
Gaulle
to
Berlin
Brandenburg
('FL503', 2, 4, '08:00:00', '10:30:00'), -- Charles
de
Gaulle
to
Leonardo
da
Vinci(Rome)
('FL504', 2, 5, '09:00:00', '11:30:00'), -- Charles
de
Gaulle
to
Madrid
('FL505', 2, 6, '10:00:00', '12:30:00'), -- Charles
de
Gaulle
to
Lisbon
('FL506', 2, 7, '11:00:00', '12:30:00'), -- Charles
de
Gaulle
to
Amsterdam
Schiphol
('FL507', 2, 8, '12:00:00', '16:00:00'), -- Charles
de
Gaulle
to
Sheremetyevo(Moscow)
('FL508', 2, 9, '13:00:00', '16:30:00'), -- Charles
de
Gaulle
to
Athens
('FL509', 2, 10, '14:00:00', '16:00:00'), -- Charles
de
Gaulle
to
Zurich
('FL510', 2, 11, '15:00:00', '06:30:00'), -- Charles
de
Gaulle
to
Narita(Tokyo)
('FL511', 2, 12, '16:00:00', '07:00:00'), -- Charles
de
Gaulle
to
Beijing
Capital
('FL512', 2, 13, '17:00:00', '08:00:00'), -- Charles
de
Gaulle
to
Incheon(Seoul)
('FL513', 2, 14, '18:00:00', '09:30:00'), -- Charles
de
Gaulle
to
Suvarnabhumi(Bangkok)
('FL514', 2, 15, '19:00:00', '10:00:00'), -- Charles
de
Gaulle
to
Changi(Singapore)
('FL515', 2, 16, '20:00:00', '11:00:00'), -- Charles
de
Gaulle
to
Indira
Gandhi(New
Delhi)
('FL516', 2, 17, '21:00:00', '13:00:00'), -- Charles
de
Gaulle
to
Dubai
('FL517', 2, 18, '22:00:00', '13:30:00'), -- Charles
de
Gaulle
to
King
Khalid(Riyadh)
('FL518', 2, 19, '23:00:00', '05:00:00'), -- Charles
de
Gaulle
to
Dhaka
('FL519', 2, 20, '23:30:00', '06:00:00');
-- Charles
de
Gaulle
to
Jinnah
International(Karachi)
