dictionary = {
    "key1" :"value1",
    "key2" :"value2"
}

# print(dictionary["gabar"])
print(dictionary.get("wiil" ,"wiil not found"))


# print(dictionary["key3"])
print(type(dictionary))
print(dir(dictionary))

my_contacts = {
    "Kasim":"08176665",
    "abdullahi":"071415681",
    "nuur":"072415681"
}

# print(my_contacts["halima"])
print(my_contacts.get("Halima" , "Key not found"))
my_contacts.pop("nuur")
my_contacts.update({"Aisha":"0714168910"})
my_contacts.update({"Kasim" :"0125637373"})
my_contacts.popitem()
print(my_contacts.keys())
print(my_contacts.values())
print(my_contacts.items())

universities = {
    "Garissa University" :{
        "location":"Garissa" ,
        "total_students":6000,
        "total_buildings":30,
        "vice_chancellor":{
            "name":"Prof Ahmed",
            "email":"ahmed65@gau.ac.ke"
        }
    },
    
    "MKU":{
        "location":"Thinka" ,
        "total_students":8000,
        "total_buildings":70,
        "vice_chancellor":{
            "name":"Prof Kamau",
            "email":"kamau65@gau.ac.ke"
        }
    },

}

for key, value in universities.items():
    print(key)
    vice_chancelor_name =value["vice_chancellor"]["name"]
    print(value)
    print(vice_chancelor_name)


print(universities)
print(universities.get("Garissa University").get("location"))
print(universities["Garissa University"]["location"])
print(universities["MKU"]["vice_chancellor"]["name"])
