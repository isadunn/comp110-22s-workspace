"""Demonstrations of dictionary capabiliites."""


# Declarning the type of a dictionary 
schools: dict[str, int]

#  Initialize to an empty dictionary 
schools = dict()

# Set a key-value pairing in the dictonary 
schools["UNC"] = 19400
schools["Duke"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation 
# print(schools)

# #  Acess a value by its key -- "lookup"
# print(f"UNC has {schools['UNC']} studnets")

# Remove a key vale pair from adictonary 
# by its key 
schools.pop("Duke")

# Test for the existenfce of a key
is_duke_present: bool = "Duke" in schools 
# print(f"Duke is presnet: {is_duke_present}")

# update / reasign a key-value pair
schools["UNC"] = 20000
schools["NCSU"] += 200

# print(schools)

# demonstration of dictionary literals 

# empty dictonary listeral
schools = {} 
# same as dict()

# alternatively, initarlize key-value pairs 
schools = {"UNC": 194000, "Duke": 6717, "NCSU": 2617}
# print(schools)

# print(schools["UNCC"])

for school in schools:
    print(f"Key: {key} -> Value: {schools[key]}")
