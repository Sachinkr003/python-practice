#dictionary = a collection of {key: value} pairs
#             ordered and changeable. No duplicicates

capitals = {"India": "New Delhi",
            "USA": "Washington DC",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(dir(capitals))
#print(help(capitals))
#print(capitals.get("India")) 

#if capitals.get("tokyo"):
#    print("That capital exists")
#else:
#    print("That capital doesn't exist")

#capitals.update({"Germany": "Berlin"})
#capitals.update({"USA": "Detroit"})
#capitals.pop("China")
#capitals.popitem()
#capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#    print(value)

#tems = capitals.items()
for key, value in capitals.items():
    print(f"{key}: {value}")