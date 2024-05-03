from read import read_land_data
from write import update_land_availability
from datetime import datetime



def rent_available_land():
    """Allows the user to rent available land by filling some requirements."""
    land_data = read_land_data()
    kitta_number = input("Enter kitta number of the land you want to rent: ")

    try:
        kitta_number = int(kitta_number)
    except ValueError:
        print("Kitta number must be a number.")
        return None
    
    land_found = False
    
    for land in land_data:
        if land['kitta_number'] == kitta_number:
            land_found = True
            if land['availability'] == "Available":
                customer_name = input("Enter your name: ")
                while True:
                    phone_number = input("Enter your phone number: ")
                    if phone_number_checker(phone_number):
                        break
                    print("Please enter a valid phone number.")
                
                try:
                    duration_months = int(input("Enter duration you want to rent (in months): "))
                    if duration_months <= 1:
                        raise ValueError
                except ValueError:
                    print("Rent duration should be more than 1 month.")
                    return None
                
                rent_amount = land['price'] * duration_months
                fine = 0
                discount = 0

                # Update land availability and generate invoice
                update_land_availability(kitta_number)  
                print("\nLand rented successfully!")
                rent_details = {
                    'kitta_number': kitta_number,
                    'city': land['city'],
                    'direction': land['direction'],
                    'duration_months': duration_months,
                    'rent_amount': rent_amount,
                    'customer_name': customer_name,
                    'phone_number': phone_number,
                    'fine': fine, 
                    'discount': discount, 
                    'duration': duration_months
                }
                generate_invoice(rent_details)
                return rent_details
            else:
                print(f"\n Land {kitta_number} is not available for rent.")
                return None
                
    if not land_found:
        print("\n No land found of this kitta number. \n Enter a valid Kitta number")
        return None





def return_rented_land():
    """Allows the user to return a rented land by filling some required information"""

    land_data = read_land_data()
    kitta_number = input("Enter kitta number of the land you want to return: ")

    try:
        kitta_number = int(kitta_number)
    except ValueError:
        print("Kitta number must be a number.")
        return None
    
    land_found = False
    
    for land in land_data:
        if land['kitta_number'] == kitta_number:
            land_found = True
            if land['availability'] == "Not Available":
                duration_returned = input("Enter duration you are returning (in months): ")
                duration_rented = input("Enter the original rented duration (in months): ")
                try:
                    duration_returned = int(duration_returned)
                    duration_rented = int(duration_rented)
                    if duration_returned < 1 and duration_rented < 1:
                        raise ValueError
                except ValueError:
                    print("Duration should be more than 1 month.")
                    return None
                
                customer_name = input("Enter your name: ")
                phone_number = input("Enter your phone number: ")
                if phone_number_checker(phone_number):
                    print("Enter your phone number:", phone_number)

                # Calculate the original rent amount based on the duration rented and price
                rent_price = land['price']
                original_rent = duration_rented * rent_price
                new_rent = duration_returned * rent_price

                # Calculate fine or discount based on duration returned
                if duration_returned > duration_rented:
                    fine = 10000 * (duration_returned - duration_rented)
                    discount = 0
                elif duration_returned < duration_rented:
                    discount = original_rent - (duration_returned * rent_price)
                    fine = 0
                else:
                    fine = 0
                    discount = 0
                
                # Update land availability and generate invoice
                update_land_availability(kitta_number)  
                print("\nLand returned successfully!")
                
                return_details = {
                    'kitta_number': kitta_number,
                    'duration_rented': duration_rented,  
                    'duration_returned': duration_returned,
                    'customer_name': customer_name,
                    'phone_number': phone_number,
                    'fine': fine,
                    'discount': discount,
                    'original_rent': original_rent,
                    'new_rent' : new_rent
                }

                generate_invoice(return_details)  
                return return_details
            else:
                print("This land is not currently rented.")
                return None
    
    if not land_found:
        print("\nInvalid kitta number. No land found.")
    
    return None


def phone_number_checker(phone_number):
    """Checks the phone number format and returns true if correct else return false"""
    if len(phone_number) == 10 and phone_number.isdigit():
        return True
    else:
        return False


def generate_invoice(invoice_details):
    current_date = datetime.now().strftime("%Y-%m-%d")
    invoice_file = f"{invoice_details['customer_name']}_Invoice.txt"

    try:
        with open(invoice_file, 'r') as f:
            mode = 'a'
    except FileNotFoundError:
        mode = 'w'

    with open(invoice_file, mode) as invoice:
        invoice.write("\n\n**************************************************\n")
        invoice.write("               Rental System Invoice\n")
        invoice.write("==================================================\n")
        invoice.write(f"Customer Name: {invoice_details['customer_name']}\t\t\tDate: {current_date}\n")
        invoice.write(f"Phone Number: {invoice_details['phone_number']}\n")
        invoice.write(f"Land (Kitta Number): {invoice_details['kitta_number']}\n")

        # For renting land
        if 'duration' in invoice_details:  
            invoice.write(f"Duration: {invoice_details['duration']} months\n")
            rent_amount = invoice_details['rent_amount']
            invoice.write(f"Total Amount: Rs{rent_amount}\n") 
            invoice.write("==================================================\n")
            invoice.write("         Thanks for renting with us!\n")
            invoice.write("**************************************************\n")
            return

        # For returning land
        duration_rented = invoice_details['duration_rented']
        duration_returned = invoice_details['duration_returned']
        fine = invoice_details['fine']
        discount = invoice_details['discount']
        original_rent = invoice_details['original_rent']
        new_rent = invoice_details['new_rent']
        total_amount =  (new_rent + fine ) - discount

        invoice.write(f"Original Rented Duration: {duration_rented} months\n")
        invoice.write(f"Duration Returned: {duration_returned} months\n")
        invoice.write(f"Original Rent Amount: Rs{original_rent}\n")
        # invoice.write(f"New Rent Amount: Rs{new_rent}\n")

        if fine > 0:
            invoice.write(f"Fine: {fine}\n")
        elif discount > 0:
            invoice.write(f"Discount: {discount}\n")
        else:
            invoice.write(f"Total Amount: ${total_amount}\n")
        invoice.write("==================================================\n")
        new_total_amount = original_rent + fine - discount
        invoice.write(f"New Total Amount: ${new_total_amount}\n")
        invoice.write("==================================================\n")
        invoice.write("         Thanks for renting with us!\n")
        invoice.write("**************************************************\n")

    print(f"Invoice generated successfully: {invoice_file}")

