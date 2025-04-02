 
# dictionary stores values in key value pair. {key:pair,...}

data={"name":"santhiya","age":18,"profession":"Doctor"}
print(data)
print(data.keys())
print(data.values())
print(data.get("age"))
data["age"]=21
print(data)
data.pop("age") # it will remove key with it's value
print(data)