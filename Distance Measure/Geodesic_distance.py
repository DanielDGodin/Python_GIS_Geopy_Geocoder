# The geodesic distance is the shortest distance on the surface of an ellipsoidal model of the earth. 
# The default algorithm uses the method is given by Karney (2013) (geodesic); 
# this is accurate to round-off and always converges.

from geopy import distance
newport_ri = (41.49008, -71.312796)
cleveland_oh = (41.499498, -81.695391)
print(distance.distance(newport_ri, cleveland_oh).miles)
#538.39044536

wellington = (-41.32, 174.81)
salamanca = (40.96, -5.50)
print(distance.distance(wellington, salamanca).km)
#19959.6792674


# change the ellipsoid model used by the geodesic formulas like so:
ne, cl = newport_ri, cleveland_oh
print(distance.geodesic(ne, cl, ellipsoid='GRS-80').miles)

# or specify the ellipsoid parameters:
distance.geodesic(ne, cl, ellipsoid=(6377., 6356., 1 / 297.)).miles