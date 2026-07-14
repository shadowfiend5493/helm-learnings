# int stores whole numbers without decimal points.
int = 1
# str stores text values inside quotes.
str = "Hello"
# float stores numbers with decimal points.
float = 1.0
# bool stores either True or False values.
bool = True
# list stores an ordered, changeable collection of values.
list = [1, 2, 3, 4, 5]
# dict stores key-value pairs for looking up related data.
dict = {"name": "John", "age": 20}
# tuple stores an ordered collection of values that cannot be changed.
tuple = (1, 2, 3, 4, 5)
# set stores an unordered collection of unique values.
set = {1, 2, 3, 4, 5}
# range creates a sequence of numbers.
range = range(1, 10)


myfamily = ["Satish", "Savitha", "Sarthak", "Saro", "Gagan", 0]

for name in myfamily:

    print(name)




myfamily_dict = {
    "father": "Satish",
    "mother": "Savitha",
    "me": "Sarthak",
    "wife": "Saro",
    "brother": "Gagan",
}

for relation, name in myfamily_dict.items():
    print(relation, name)


myfamily_details = [
    {"name": "Satish", "relation": "father", "age": 50},
    {"name": "Savitha", "relation": "mother", "age": 48},
    {"name": "Sarthak", "relation": "me", "age": 20},
    {"name": "Saro", "relation": "wife", "age": 20},
    {"name": "Gagan", "relation": "brother", "age": 18},
]

for family_member in myfamily_details:
    print(family_member["name"], family_member["relation"], family_member["age"])


appname = {
    "name": "dcsm",
    "scheduled": "0 20 0 0 0",
    "enabled": True,
    "gitrepo": "https:sasa",
}

for key, value in appname.items():
    print(key, value)


appname_nested = {
    "dcsm": {
        "configfile": "dcsm_config.yaml",
        "gitrepo": "https://example.com/dcsm.git",
    },
    "camera": {
        "configfile": "camera_config.yaml",
        "gitrepo": "https://example.com/camera.git",
    },
}

# app:
#     dcsm:
#         configfile: dcsm_config.yaml
#         gitrepo: https://example.com/dcsm.git
#     camera:
#         configfile: camera_config.yaml
#         gitrepo: https://example.com/camera.git
 
for app_name, app_details in appname_nested.items():
    print(app_name) 
    for key, value in app_details.items():
        print(key, value)
