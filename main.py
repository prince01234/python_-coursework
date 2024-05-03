import operation
import read 

def show_menu():
    print("\nWelcome to the Land Rental System")
    print("1. Display Available Lands")
    print("2. Rent Land")
    print("3. Return Land")
    print("4. Exit")

def main():
    while True:
        show_menu()
        choose = input("Enter your choice: ")
        
        if choose == '1':
            read.display_available_lands()      
        elif choose == '2':
            operation.rent_available_land()  
        elif choose == '3':
            operation.return_rented_land() 
        elif choose == '4':
            print("Thank you for using the Land Rental System. Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

            
# Check if the script is executed directly
if __name__ == "__main__":
    main()
