import datetime

# Hardcoded data for each file's contents
vehicles_data = [
    ["BKV-943", "Ford Fiesta", "35", "Manual Transmission"],
    ["JMB-535", "Ford Fiesta", "48", "Air Conditioning", "Manual Transmission"],
    ["SKF-124", "Ford Focus", "52", "Air Conditioning", "Manual Transmission"],
    ["MSQ-731", "Ford Focus Wagon", "52", "Air Conditioning", "Manual Transmission"],
    ["AMG-111", "Toyota Yaris", "65", "Air Conditioning", "Hybrid", "Automatic Transmission"],
    ["MER-611", "Kia Rio", "52", "Air Conditioning", "Manual Transmission"],
    ["ZEQ-851", "Toyota Corolla Touring Sports", "63", "Air Conditioning", "Hybrid", "Automatic Transmission"],
    ["CHF-337", "Volkswagen Up", "58", "Air Conditioning", "Manual Transmission"],
    ["BMC-69", "Nissan Micra", "42", "Manual Transmission"],
    ["TTC-513", "Volkswagen Golf", "51", "Air Conditioning", "Manual Transmission"],
    ["VIG-326", "Nissan Micra", "43", "Manual Transmission"],
    ["DKG-477", "Toyota Corolla", "52", "Air Conditioning", "Manual Transmission"],
    ["HYA-544", "Toyota Yaris", "66", "Hybrid", "Automatic Transmission"],
    ["XJY-604", "Volkswagen Polo", "62", "Air Conditioning", "Automatic Transmission"],
    ["AJB-123", "SEAT Ibiza", "65", "Air Conditioning", "Automatic Transmission"],
    ["MDZ-471", "Skoda Kodiaq", "71", "Air Conditioning", "Automatic Transmission"],
    ["TUS-674", "Volkswagen T-Cross", "72", "Air Conditioning", "Manual Transmission"],
    ["WYN-482", "Mercedes A-Class", "90", "Air Conditioning", "Manual Transmission"],
    ["KOL-99", "Audi Q5", "110", "Air Conditioning", "Automatic Transmission"]
]

customers_data = [
    ["12/12/1985", "Alice", "Wonder", "Alice.Wonder@outlook.com"],
    ["23/03/1990", "Mark", "Smith", "Mark.Smith@hotmail.com"],
    ["05/05/1995", "Emma", "Stone", "Emma.Stone@live.com"],
    ["11/11/1988", "David", "Lee", "David.Lee@aol.com"],
    ["30/06/1992", "Sarah", "Connor", "Sarah.Connor@gmail.com"],
    ["22/02/1961", "James", "Bond", "James.Bond@mi6.co.uk"],
    ["07/07/1977", "John", "Lucky", "John.Lucky@email.com"],
    ["09/09/1999", "Tom", "Shark", "Tom.Shark@gmail.com"],
    ["28/01/2002", "Laura", "Driver", "Laura.Driver@garage.fi"],
    ["17/04/1997", "Jia", "Mei", "Jia.Mei@163.com"],
    ["17/08/1978", "Jack", "Mobile", "Jack.Mobile@yahoo.com"],
    ["16/10/2001", "Tom", "Johanson", "Tom.Johanson@gmail.com"],
    ["14/07/2000", "Matti", "Virtanen", "Matti.Virtanen@lut.fi"]
]

rented_vehicles_data = [
    ["AJB-123", "07/07/1977", "21/10/2024 10:31"],
    ["TTC-513", "28/01/2002", "23/10/2024 14:32"],
    ["MER-611", "14/07/2000", "24/10/2024 10:46"],
    ["ZEQ-851", "16/10/2001", "24/10/2024 15:45"],
    ["CHF-337", "22/02/1961", "25/10/2024 12:33"],
    ["MSQ-731", "05/05/1995", "28/10/2024 13:29"]
]

transactions_data = [
    ["XJY-604", "23/03/1990", "01/10/2024 11:15", "05/10/2024 20:10", "5", "310.00"],
    ["MER-611", "05/05/1995", "10/10/2024 08:00", "15/10/2024 16:30", "6", "312.00"],
    ["BMC-69", "17/04/1997", "15/10/2024 14:01", "19/10/2024 22:20", "5", "210.00"],
    ["VIG-326", "17/08/1978", "13/10/2024 12:23", "20/10/2024 14:03", "8", "344.00"],
    ["KOL-99", "11/11/1988", "15/10/2024 14:45", "22/10/2024 19:20", "8", "880.00"],
    ["AJB-123", "12/12/1985", "20/10/2024 09:30", "25/10/2024 18:45", "6", "390.00"],
    ["TTC-513", "30/06/1992", "25/10/2024 10:05", "28/10/2024 21:50", "4", "204.00"]
]

# Function to list available cars
def list_available_cars():
    rented_plates = []
    for r in rented_vehicles_data:
        rented_plates.append(r[0])
    
    print("\nAvailable Cars:")
    for vehicle in vehicles_data:
        if vehicle[0] not in rented_plates:
            print(f"Plate: {vehicle[0]}, Model: {vehicle[1]}, Rate: ${vehicle[2]}/day, Features: {vehicle[3:]}")

# Function to rent a car
def rent_a_car():
    customer_birthdate = input("Enter customer's birthdate (dd/mm/yyyy): ")
    customer = None
    for c in customers_data:
        if c[0] == customer_birthdate:
            customer = c
            break

    # If the customer is new, collect additional details
    if not customer:
        first_name = input("Enter customer's first name: ")
        last_name = input("Enter customer's last name: ")
        email = input("Enter customer's email: ")
        new_customer = [customer_birthdate, first_name, last_name, email]
        customers_data.append(new_customer)
        print("New customer added.")
    
    vehicle_plate = input("Enter the plate number of the car to rent: ")
    vehicle = None
    for v in vehicles_data:
        if v[0] == vehicle_plate:
            vehicle = v
            break
    
    if vehicle:
        start_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M")
        rented_vehicles_data.append([vehicle_plate, customer_birthdate, start_time])
        print(f"Car {vehicle_plate} rented successfully.")
    else:
        print("Vehicle not found.")

# Function to return a car
def return_a_car():
    vehicle_plate = input("Enter the plate number of the returning car: ")
    rental = None
    for r in rented_vehicles_data:
        if r[0] == vehicle_plate:
            rental = r
            break

    if rental:
        rented_vehicles_data.remove(rental)
        start_time = datetime.datetime.strptime(rental[2], "%d/%m/%Y %H:%M")
        end_time = datetime.datetime.now()
        duration = (end_time - start_time).days + 1
        vehicle = None
        for v in vehicles_data:
            if v[0] == vehicle_plate:
                vehicle = v
                break
        price = int(vehicle[2]) * duration
        transactions_data.append([vehicle_plate, rental[1], rental[2], end_time.strftime("%d/%m/%Y %H:%M"), str(duration), f"{price:.2f}"])
        print(f"Car {vehicle_plate} returned. Total cost: ${price:.2f}")
    else:
        print("Rental record not found.")

# Function to count total money from transactions
def count_the_money():
    total = 0
    for t in transactions_data:
        total += float(t[5])
    print(f"\nTotal earnings from all transactions: ${total:.2f}")

# Main menu function
def main_menu():
    while True:
        print("\n--- Car Rental Management System ---")
        print("1. List available cars")
        print("2. Rent a car")
        print("3. Return a car")
        print("4. Count the money")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            list_available_cars()
        elif choice == "2":
            rent_a_car()
        elif choice == "3":
            return_a_car()
        elif choice == "4":
            count_the_money()
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the program
if __name__ == "__main__":
    main_menu()
