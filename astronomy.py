from astropy.coordinates import SkyCoord, EarthLocation, AltAz
from astropy.time import Time

from hipparcos import ralist, declist, maglist


def get_coords(location, time):
    object = SkyCoord(ralist, declist, unit='deg')

    observing_time = Time(time)
    pos = EarthLocation.of_address(location)
    aa = AltAz(location=pos, obstime=observing_time)

    rez = object.transform_to(aa)
    return (90 - rez.alt.degree, rez.az.degree, maglist)
