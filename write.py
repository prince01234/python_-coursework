from read import read_land_data

def write_my_land(lands):
    # Open the file 'my_land.txt' in write mode
    with open('my_land.txt', 'w') as file:
        # Iterate over each land in the list 'lands'
        for land in lands:
            line = f"{land['kitta_number']}, {land['city']}, {land['direction']}, {land['area']}, {land['price']}, {land['availability']}\n"
            file.write(line)


def update_land_availability(kitta_number):
    # Read land data from the file
    lands = read_land_data() 
    
    # Iterate over each land in the list
    for land in lands:
        # Check if the kitta number matches the provided kitta number
        if land['kitta_number'] == kitta_number:
            # Toggle the availability status of the land
            if land['availability'] == "Available":
                land['availability'] = "Not Available"
            else:
                land['availability'] = "Available"
            # Exit the loop once the land is found and updated
            break
    
    # Write the updated land data back to the file
    write_my_land(lands)

