# Parking Lot Management System

This is a simple Python-based Parking Lot Management System. Users can park cars, retrieve cars, and check the status of the parking lot through a command-line interface. It ensures that cars with the same plate number are not parked more than once.

## Features

- **Display Parking Lot Status**: View the current status of all parking spots (occupied or empty).
- **Park a Car**: Add a car to the parking lot. Prevents adding the same car more than once.
- **Retrieve a Car**: Remove a car from the parking lot.
- **Full Parking Lot Warning**: Notifies the user if the parking lot is full.

## Menu Options

1. **Display Parking Lot Status:** View which parking spots are occupied and which are available.
2. **Park a Car:** Enter a car's plate number to park it in an available spot. If the car is already in the lot, it won’t be added again.
3. **Retrieve a Car:** Enter a car's plate number to retrieve it from the parking lot.
4. **Exit:** Exit the parking lot management system.

## Code Breakdown

### `ParkingLot` Class

This class manages the parking lot operations, including parking and retrieving cars.

- **`__init__(self, capacity)`**: Initializes the parking lot with a specified capacity.
- **`display_parking_lot(self)`**: Displays the current status of the parking spots.
- **`park_car(self, plate_number)`**: Parks a car in the parking lot if the car isn’t already parked and if there is space available.
  - It first checks if the plate number already exists in the lot. If so, it doesn't allow the car to be parked again.
- **`retrieve_car(self, plate_number)`**: Removes a car from the parking lot by its plate number.

### Main Functions

- **`parking_menu()`**: Displays the available menu options for managing the parking lot.
- **`main()`**: Main function that provides the user interface for interacting with the system. It continuously displays the menu until the user chooses to exit.
