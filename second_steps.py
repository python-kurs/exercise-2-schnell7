# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500,
                "GOES"     :2000,
                "worldview" : 0.31
               }
#%%
# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]



# 2) print out all satellite names contained in the dictionary [2P]

print("I have the following satellites in my database:")
print(list(sat_database.keys()))

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]


# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 

#%%
check = input()
if check in list(sat_database):
    print(" '%s' ist in Datenbank mit Aufloesung %f Meter" %(check ,sat_database[check]))
else:
    print("nicht in Datenbank, überprüfe gross kleinschreibung")
    print(list(sat_database.keys()))
    