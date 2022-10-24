from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.coordinates.name_resolve import NameResolveError
from astropy.time import Time

from hipparcos import ralist, declist, maglist


def get_coords(location, time):
    celestial_object = SkyCoord(ralist, declist, unit='deg')

    observing_time = Time(time)
    try:
        pos = EarthLocation.of_address(location)
    except NameResolveError:
        pos = EarthLocation.of_address("Bucuresti")
    aa = AltAz(location=pos, obstime=observing_time)

    rez = celestial_object.transform_to(aa)
    return 90 - rez.alt.degree, rez.az.degree, maglist
