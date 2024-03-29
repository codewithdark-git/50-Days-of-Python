from geopy.geocoders import Nominatim

def get_geo_data(ip_address):
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode(ip_address)
    return location

ip = "192.168.1.1" #int(input("Enter Your IP Address : "))
geo_data = get_geo_data(ip)

if geo_data:
    print("Latitude:", geo_data.latitude)
    print("Longitude:", geo_data.longitude)
    print("Address:", geo_data.address)
else:
    print("Location not found for the provided IP.")
