# Python_GIS_Geopy_Geocoder

Contains Python Code for Geo coding and reverse geocoding

1) Geo Coder:

This Python script demonstrates **geocoding** using the `geopy` library. Geocoding is the process of converting a human-readable address into geographic coordinates (latitude and longitude) and retrieving additional location details.

### Code Explanation:

1. **Importing the Library**:
   ```python
   from geopy.geocoders import Nominatim
   ```
   - The `Nominatim` geocoder from the `geopy` library is imported. Nominatim is a geocoding service provided by OpenStreetMap.

2. **Creating a Geolocator Instance**:
   ```python
   geolocator = Nominatim(user_agent="Dans-Test_geocoder")
   ```
   - A `Nominatim` geolocator object is created. The `user_agent` parameter is required and identifies the application making the request. Here, the user agent is set to `"Dans-Test_geocoder"`, which is a custom identifier for the user's application.

3. **Performing Geocoding**:
   ```python
   location = geolocator.geocode("420 Lana Terrace, Mississauga, Ontario")
   ```
   - The `geocode` method is called with the address `"420 Lana Terrace, Mississauga, Ontario"`. This sends a request to the Nominatim service to retrieve the geographic coordinates and other details for the given address.

4. **Checking if a Location is Found**:
   ```python
   if location:
   ```
   - This checks if the `location` object is not `None`. If the address is valid and found, the block inside the `if` statement is executed.

5. **Printing the Address**:
   ```python
   print(location.address)
   ```
   - The `address` attribute of the `location` object contains the full formatted address returned by the geocoding service. This is printed to the console.

6. **Printing Latitude and Longitude**:
   ```python
   print((location.latitude, location.longitude))
   ```
   - The `latitude` and `longitude` attributes of the `location` object contain the geographic coordinates of the address. These are printed as a tuple.

7. **Printing Raw Location Data**:
   ```python
   print(location.raw)
   ```
   - The `raw` attribute contains the raw JSON response from the Nominatim service, which includes all the details about the location.

8. **Handling the Case Where No Address is Found**:
   ```python
   else:
       print("Address not found.")
   ```
   - If the `location` object is `None` (i.e., no address is found for the given input), this block is executed, and a message is printed to indicate that the address could not be found.

### Example Output:
If the address is valid and found, the output might look like:
```
420 Lana Terrace, Mississauga, Ontario, Canada
(43.589045, -79.644120)
{'place_id': ..., 'licence': ..., 'osm_type': ..., 'lat': '43.589045', 'lon': '-79.644120', ...}
```

If the address is invalid or not found, the output will be:
```
Address not found.
```



2) Reverse Geo coder

This Python script demonstrates **reverse geocoding** using the `geopy` library. Reverse geocoding converts geographic coordinates (latitude and longitude) into a human-readable address.

### Code Explanation:

1. **Importing the Library**:
   ```python
   from geopy.geocoders import Nominatim
   ```
   - The `Nominatim` geocoder from the `geopy` library is imported. Nominatim is a geocoding service provided by OpenStreetMap.

2. **Creating a Geolocator Instance**:
   ```python
   geolocator = Nominatim(user_agent="Dans_Test_Reverse_Geocoder")
   ```
   - A `Nominatim` geolocator object is created. The `user_agent` parameter is required and identifies the application making the request. Here, the user agent is set to `"Dans_Test_Reverse_Geocoder"`.

3. **Performing Reverse Geocoding**:
   ```python
   location = geolocator.reverse("43.5953475, -79.6075479")
   ```
   - The `reverse` method is called with the geographic coordinates `"43.5953475, -79.6075479"`. This sends a request to the Nominatim service to retrieve the address and other details for the given coordinates.

4. **Checking if a Location is Found**:
   ```python
   if location:
   ```
   - This checks if the `location` object is not `None`. If the coordinates are valid and a location is found, the block inside the `if` statement is executed.

5. **Printing the Address**:
   ```python
   print(location.address)
   ```
   - The `address` attribute of the `location` object contains the full formatted address corresponding to the coordinates. This is printed to the console.

6. **Printing Latitude and Longitude**:
   ```python
   print((location.latitude, location.longitude))
   ```
   - The `latitude` and `longitude` attributes of the `location` object contain the geographic coordinates. These are printed as a tuple. These coordinates should match the input coordinates.

7. **Printing Raw Location Data**:
   ```python
   print(location.raw)
   ```
   - The `raw` attribute contains the raw JSON response from the Nominatim service, which includes all the details about the location.

8. **Handling the Case Where No Location is Found**:
   ```python
   else:
       print("Location not found.")
   ```
   - If the `location` object is `None` (i.e., no location is found for the given coordinates), this block is executed, and a message is printed to indicate that the location could not be found.

### Example Output:
If the coordinates are valid and found, the output might look like:
```
420 Lana Terrace, Mississauga, Ontario, Canada
(43.5953475, -79.6075479)
{'place_id': ..., 'licence': ..., 'osm_type': ..., 'lat': '43.5953475', 'lon': '-79.6075479', ...}
```

If the coordinates are invalid or not found, the output will be:
```
Location not found.
```