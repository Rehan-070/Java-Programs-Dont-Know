from geopy.geocoders import Nominatim

def get_location(phone_number):
    geolocator = Nominatim(user_agent="geo_locator")

    # Replace 'phone_number' with the actual phone number
    location = geolocator.geocode(phone_number)

    if location:
        return location.address
    else:
        return "Location not found."

# Example usage
phone_number = input("Enter the mobile number: ")
result = get_location(phone_number)
print(result)