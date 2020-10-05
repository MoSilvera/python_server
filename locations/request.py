LOCATIONS = [
    {
        "id": 1,
        "name": "Nashville North",
        "address": "500 Circle Way"
    },
    {
        "id": 2,
        "name": "Nashville South",
        "address": "10101 Binary Court"
    }
]



def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location