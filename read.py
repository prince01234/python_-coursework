def read_land_data():
    """Reads land data from the specified file."""
    land_data = []
    with open('my_land.txt', 'r') as file:
        for line in file:
            land_info = line.strip().split(", ")
            land_data.append({
                'kitta_number': int(land_info[0]),
                'city': land_info[1],
                'direction': land_info[2],
                'area': int(land_info[3]),
                'price': int(land_info[4]),
                'availability': land_info[5]
            })
    return land_data

def display_available_lands():
    """Displays available land"""
    print("--------------------------------------------------------------------------------------------------------------------")
    print("Kitta\t\tCity/District\t\tDirection\t\tArea(Anna)\t\tPrice\t\tStatus")
    print("--------------------------------------------------------------------------------------------------------------------")
    lands = read_land_data()
    for land in lands:
        if land['availability'] == "Available":
            print(f"{land['kitta_number']:<16}{land['city']:<24}{land['direction']:<25}{land['area']:<23}{land['price']:<15}{land['availability']}")
    print("--------------------------------------------------------------------------------------------------------------------")
