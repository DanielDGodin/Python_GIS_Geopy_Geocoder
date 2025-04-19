from geopy.geocoders import Nominatim
geolocator = Nominatim(user_agent="Dans-Test_geocoder")  ### Dan is the name of user applicatoin
location = geolocator.geocode("420 Lana Terrace, Mississauga, Ontario") ##("175 5th Avenue NYC")
print(location.address)
print((location.latitude, location.longitude))
print(location.raw)