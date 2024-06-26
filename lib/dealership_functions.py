from dealership import Dealer
from tabulate import tabulate
from car import Car


Dealer.update_inventory() 
def view_all_dealerships():
    print("View All Dealerships:")
    dealerships = Dealer.get_all_dealers()
    if dealerships:
        headers = ["", "Title", "Location", "Phone Number", "Employees", "Inventory"]
        rows = []
        for dealership in dealerships:
            row = [dealership.id, dealership.title, dealership.location, dealership.phone_number, dealership.employees, dealership.inventory]
            rows.append(row)

        print(tabulate(rows, headers=headers, tablefmt="grid"))

        dealership_index = input("Enter the number of the dealership you want to view inventory for: ")

        try:
            dealership_index = int(dealership_index)
            if 1 <= dealership_index <= len(dealerships):
                selected_dealership = dealerships[dealership_index - 1]
                Dealer.update_inventory()
                car_data = selected_dealership.display_inventory(selected_dealership.id)
                display_inventory(car_data)
            else:
                print("Invalid dealership number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    else:
        print("No dealerships found.")


def display_inventory(car_data):
    if car_data:
        headers = ["Make", "Model", "Year", "Price", "Mileage", "Color", "Car Type", "Available"]
        rows = []
        for car_row in car_data:
            car = Car.car_from_db(car_row)
            availability_text = "Available" if car.available else "Sold"
            row = [car.make, car.model, car.year, car.price, car.mileage, car.color, car.car_type, availability_text]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No cars found in inventory for the selected dealership.")
        
        
def update_dealership():
    print("Update Dealership:")
    title = input("Enter name of the dealership: ")
    dealership = Dealer.find_by_title(title)

    if dealership:
        print("Enter each of the inputs in order to update")

        new_title = input(f"Enter new title [{dealership.title}]: ")
        new_location = input(f"Enter new location [{dealership.location}]: ")
        new_phone_number = input(f"Enter new phone number [{dealership.phone_number}]: ") 
        new_employees = input(f"Enter new employee count [{dealership.employees}]: ")  
        
        update_dealership = dealership.update(new_title, new_location, new_phone_number, new_employees)
        if update_dealership:
            print("Dealership updated successfully!")
        else: 
            print("Failed to update dealership")
    else:
        print("No dealership found.")


def sort_dealership_inventory_asc():
    print("View dealerships by inventory ascending:")
    sort_inventory_asc = Dealer.sort_dealership_inventory_asc()
    if sort_inventory_asc:
        headers = ["Title", "Location", "Inventory", "Phone Number", "Employees"]
        rows = []
        for dealership in sort_inventory_asc:
            row = [dealership.title, dealership.location, dealership.inventory, dealership.phone_number, dealership.employees]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No dealerships found.")

def sort_dealership_inventory_desc():
    print("View dealerships by inventory descending:")
    sort_inventory_desc = Dealer.sort_dealership_inventory_desc()
    if sort_inventory_desc:
        headers = ["Title", "Location", "Inventory", "Phone Number", "Employees"]
        rows = []
        for dealership in sort_inventory_desc:
            row = [dealership.title, dealership.location, dealership.inventory, dealership.phone_number, dealership.employees]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No dealerships found.")

def sort_dealership_employees_asc():
    print("View dealerships by employee count ascending:")
    sort_employees_asc = Dealer.sort_dealership_employees_asc()
    if sort_employees_asc:
        headers = ["Title", "Location", "Inventory", "Phone Number", "Employees"]
        rows = []
        for dealership in sort_employees_asc:
            row = [dealership.title, dealership.location, dealership.inventory, dealership.phone_number, dealership.employees]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No dealerships found.")

def sort_dealership_employees_desc():
    print("View dealerships by employee count descending:")
    sort_employees_desc = Dealer.sort_dealership_employees_desc()
    if sort_employees_desc:
        headers = ["Title", "Location", "Inventory", "Phone Number", "Employees"]
        rows = []
        for dealership in sort_employees_desc:
            row = [dealership.title, dealership.location, dealership.inventory, dealership.phone_number, dealership.employees]
            rows.append(row)
        print(tabulate(rows, headers=headers, tablefmt="grid"))
    else:
        print("No dealerships found.")
