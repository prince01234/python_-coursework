def read_land_data():
    """Reads land data from the specified file."""
    # Initialize an empty list to store land data
    land_data = []
    
    # Open the file 'my_land.txt' in read mode
    with open('my_land.txt', 'r') as file:
        # Iterate over each line in the file
        for line in file:
            # Strip any leading/trailing whitespace and split the line by comma and space
            land_info = line.strip().split(", ")
            
            # Create a dictionary for each land entry with appropriate keys and values
            land_entry = {
                'kitta_number': int(land_info[0]),
                'city': land_info[1],
                'direction': land_info[2],
                'area': int(land_info[3]),
                'price': int(land_info[4]),
                'availability': land_info[5]
            }
            
            # Append the land entry dictionary to the land_data list
            land_data.append(land_entry)
    
    # Return the list of land data
    return land_data


#this function displays all available land in tabular form
def display_available_lands():
    """Displays available land"""
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Kitta\t\tCity/District\t\tDirection\t\tArea(Anna)\t\tPrice\t\tStatus")
    print("--------------------------------------------------------------------------------------------------------------------")
    
    # Read land data from the file
    lands = read_land_data()
    
    # Iterate over each land entry
    for land in lands:
        # Checks the land if it is available
        if land['availability'] == "Available":
            # Print details of the available land in a formatted manner
            print(f"{land['kitta_number']:<16}{land['city']:<24}{land['direction']:<25}{land['area']:<23}{land['price']:<15}{land['availability']}")

    print("--------------------------------------------------------------------------------------------------------------------")

