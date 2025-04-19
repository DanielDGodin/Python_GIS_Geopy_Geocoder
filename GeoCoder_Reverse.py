from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Dans_Test_Reverse_Geocoder")
location = geolocator.reverse("43.5953475, -79.6075479")
print(location.address)

print((location.latitude, location.longitude))

print(location.raw)
