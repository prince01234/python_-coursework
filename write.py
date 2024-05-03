from read import read_land_data


def write_my_land(lands):
    with open('my_land.txt', 'w') as file:
        for land in lands:
            line = f"{land['kitta_number']}, {land['city']}, {land['direction']}, {land['area']}, {land['price']}, {land['availability']}\n"
            file.write(line)

def update_land_availability(kitta_number):
    lands = read_land_data() 
    for land in lands:
        if land['kitta_number'] == kitta_number:
            if land['availability'] == "Available":
                land['availability'] = "Not Available"
            else:
                land['availability'] = "Available"
            break
    write_my_land(lands)
