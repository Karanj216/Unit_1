dict1={"Name":"Karanj",
       "Division":"SOC7",
       "Roll no":28}

dict1["City"]="Pune"
print(dict1)

removed=dict1.pop("Roll no",28)
print(dict1)

new={"Hometown":"Rajkot"}

dict1.update(new)
print(dict1)