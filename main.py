# Change this to control the amount of parking spots
MAX_PARKING = 10

# Creating parking class with its attributes
class ParkingLot:
    def __init__(self, capacity):
        self.capacity = capacity
        self.parking_spots = [None] * capacity

    # Function to display parking spots
    def display_parking_lot(self):
        print("\nParking Lot Status: ")
        for index, spot in enumerate(self.parking_spots):
            if spot is None:
                print(f"Spot {index + 1}: [Empty]")
            else: 
                print(f"Spot {index + 1}: [Occupied by car {spot}]")

    # Function to park a vehicle
    def park_car(self, plate_number):
        # Checks to see if plate number already exists within the parking lot
        if plate_number in self.parking_spots:
            print(f"\nCar with license plate number: {plate_number} is already parked!")
            return

        for index in range(self.capacity):
            if self.parking_spots[index] is None:
                self.parking_spots[index] = plate_number
                print(f"\nCar with plate number: {plate_number} parked in spot {index + 1}")
                return
        
        print("\nSorry, the parking lot is full!")

    # Function to retrieve a car
    def retrieve_car(self, plate_number):
        for index in range(self.capacity):
            if self.parking_spots[index] == plate_number:
                self.parking_spots[index] = None
                print(f"\nCar with plate number: {plate_number} retrieved from spot {index + 1}")
                return
        print(f"\nCar with plate number: {plate_number} is not in the parking lot.")

# Function to display parking menu
def parking_menu():
    print("\nParking Lot Management")
    print("1. Display parking lot status")
    print("2. Park a car")
    print("3. Retrieve a car")
    print("4. Exit module")

# Main function for UI
def main():
    parking_lot = ParkingLot(5) # Set the capacity of parking lot to appointed amount
    while True:
        parking_menu()
        choice = input("\nEnter your choice (1-4): ")
        if choice == "1":
            parking_lot.display_parking_lot()
        elif choice == "2":
            plate_number = input("Enter car number to park: ")
            parking_lot.park_car(plate_number)
        elif choice == "3":
            plate_number = input("Enter car plate number to retrieve: ")
            parking_lot.retrieve_car(plate_number)
        elif choice == "4":
            print("Exiting the module.")
            break
        else:
            print("Invalid choice! Please select from 1-4")

if __name__ == "__main__":
    main()