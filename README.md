# SkyChart
This is a simple Python app that allows you to see the positions of the stars in the sky at any given moment and from any location. 
It makes use of the **Astropy** library for calculating the horizontal coordinates of the stars given the coordinates and the time. 
The equatorial coordinates are taken from the Hipparchus Catalogue and are stored in the hyp_data.dat file. 
The Nominatim API from **Geopy** is used to get the coordinates of a place from a string given by the user. 
The **pyQt5** framework is used for the UI and **Matplotlib** generates the graph.
