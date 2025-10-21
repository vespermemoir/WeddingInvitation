import uuid, os
import json

# List of Guests

listOfGuests = [
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Teguh Pramono",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Yohan Yuwono",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Fifi Wijaya",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Hendra Ohalim",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Welly Ohalim",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Linggayani Ohalim",
    "GuestMaxAttendance": 5,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "San Ku",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Yenny",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Amika",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Vinsencius Tanaya",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Novelia Liestia",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Emmanuela Maria Jessica S.",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Evilia Rahardjo",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Shania Angelina",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Angelia Handoko",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Vijjadewi Sugiarto",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Arcelina Saputri",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Kevin Tirta",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Lukas Fernando",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Orang tua Ce Vera",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Winston Chamora",
    "GuestMaxAttendance": 1,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Nadia Felicia",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Fadli Anugrah",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
},
{
    "GuestID": "",
    "Updated": 0,
    "GuestName": "Nouchka",
    "GuestMaxAttendance": 2,
    "GuestActualAttendance": 0
}]

# Delete all item in the "guests" folder
folderPath = "guests"
for filename in os.listdir(folderPath):
    file_path = os.path.join(folderPath, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)

# Create new ID for every Guest
for Guest in listOfGuests:
    NewUuid = str(uuid.uuid4())
    Guest.update({"GuestID": NewUuid})
    with open(f"guests/{NewUuid}.json", 'w') as file:
        json.dump(Guest, file, indent=4)