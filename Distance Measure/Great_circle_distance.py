# Great-circle distance (great_circle) uses a spherical model of the earth, using the mean earth radius as defined by the International 
# Union of Geodesy and Geophysics, (2a + b)/3 = 6371.0087714150598 kilometers approx 6371.009 km (for WGS-84), 
# resulting in an error of up to about 0.5%. The radius value is stored in distance.EARTH_RADIUS, so it can be customized (it should always be in kilometers, however).

from geopy import distance
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)


print(distance.great_circle(newport_ri, cleveland_oh).miles)
#536.997990696