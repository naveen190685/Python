import requests
import re

fireballAPI = 'https://ssd-api.jpl.nasa.gov/fireball.api'
dateMin = ''#'2017-01-01'
dateMax = ''#'2020-01-01'
myD = {}


class Place:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude


boston = Place("42.354558N", "71.054254W")
ncr = Place("28.574389N", "77.312638E")
sanFransisco = Place("37.793700N", "122.403906W")
directions = ["N", "E", "W", "S"]


def callFB_API():
    callAPI = fireballAPI + "?req-loc=true"
    if dateMin != "":
        callAPI = callAPI + "&date-min=" + dateMin
    if dateMax != "":
        callAPI = callAPI + '&date-max=' + dateMax
    # print('Requesting: ' + callAPI)
    try:
        result = requests.get(callAPI)
        if result.status_code != 200:
            print("Error: " + str(result.status_code) + " " + result.reason)
            exit(1)
    except requests.exceptions.ConnectionError:
        print("Are you connected to internet?")
        exit(1)
    return result.json()


def checkLatitudeIsDegreeDirectionFormat(lat, latDir):
    if (0 <= lat <= 90) is False:
        print("Latitude: " + str(lat) + " is expected to be between 0 to 90")
        exit(1)
    if directions.__contains__(latDir) is False:
        print("Latitude: " + latDir + " don't contain any of the valid directions appended e.g. N, E, W, S")
        exit(1)


def checkLongitudeIsDegreeDirectionFormat(lon, lonDir):
    if (0 <= lon <= 180) is False:
        print("Longitude: " + str(lon) + " is expected to be between 0 to 180")
        exit(1)
    if directions.__contains__(lonDir) is False:
        print("Longitude: " + lonDir + " don't contain any of the valid directions appended e.g. N, E, W, S")
        exit(1)


def checkLatitudeIsSignedFormat(lat):
    if (-90 <= lat <= 90) is False:
        print("Latitude: " + str(
            lat) + " is expected to be between -90 to 90 when not mentioning direction e.g. N, E, W or S")
        exit(1)


def checkLongitudeIsSignedFormat(lon):
    if (-180 <= lon <= 180) is False:
        print("Longitude: " + str(lon) + " is expected to be between -180 to 180")
        exit(1)


def fireball(latitude: str, longitude: str):
    try:
        # Check if latitude is in Degree plus compass direction
        if latitude[len(latitude) - 1].isalpha():
            lat = float(latitude[0:len(latitude) - 1])
            latDir = latitude[-1]
            checkLatitudeIsDegreeDirectionFormat(lat, latDir)
        elif latitude[0].isalpha():
            lat = float(latitude[1::])
            latDir = latitude[0]
            checkLatitudeIsDegreeDirectionFormat(lat, latDir)
        # Check if latitude is in signed degree
        else:
            lat = float(latitude)
            checkLatitudeIsSignedFormat(lat)
    except:
        print("Please provide latitude " + latitude + " in correct signed or degree direction format")
        exit(1)

    # Check if longitude is in Degree plus compass direction
    try:
        if longitude[len(longitude) - 1].isalpha():
            lon = float(longitude[0:len(longitude) - 1])
            lonDir = longitude[-1]
            checkLongitudeIsDegreeDirectionFormat(lon, lonDir)
        elif longitude[0].isalpha():
            lon = float(longitude[1::])
            lonDir = longitude[0]
            checkLongitudeIsDegreeDirectionFormat(lon, lonDir)
        # Check if longitude is in signed degree
        else:
            lon = float(longitude)
            checkLongitudeIsSignedFormat(lon)
    except:
        print("Please provide longitude " + longitude + " in correct signed or unsigned format")
        exit(1)
    global myD
    if not myD:
        myD = callFB_API()

    record = [0, 0]
    for e in myD["data"]:
        if e[3] is not None and abs(float(e[3]) - lat) <= 15:
            if e[5] is not None and abs(float(e[5]) - lon) <= 15:
                try:
                    if e[4] == latDir and e[6] == lonDir:
                        print(f'Brightness: {e[1]}     Latitude: {e[3]} {e[4]}  Longiture: {e[5]} {e[6]}')
                        if float(record[1]) < float(e[1]):
                            record = e
                except UnboundLocalError:
                    print(f'Brightness: {e[1]}     Latitude: {e[3]} {e[4]}  Longiture: {e[5]} {e[6]}')
                    if float(record[1]) < float(e[1]):
                        record = e
    if record == [0, 0]:
        record = "No place with fireball"
    return record


compare: float = 0
myRecord: list

# bostonFireball = fireball("42.354558N", "71.054254W")
# bostonFireball = fireball("N42.354558", "W71.054254")
# bostonFireball = fireball("42.354558 N", "W 271.054254")
# bostonFireball = fireball("42.354558N", "71.054W254")
# bostonFireball = fireball("42.35N4558", "71.054254W")
# bostonFireball = fireball("42.354558", "71.054254")
# bostonFireball = fireball("42.354558", "71.054254")
# print("BostonFireball: " + str(bostonFireball))

print("Boston " + boston.latitude + " " + boston.longitude)
bostonFireball = fireball(boston.latitude, boston.longitude)
print("Boston Brightest: " + str(bostonFireball))
print("\nNCR " + ncr.latitude + " " + ncr.longitude)
ncrFireball = fireball(ncr.latitude, ncr.longitude)
print("NCR Brightest: " + str(ncrFireball))
print("\nSan Fransisco " + sanFransisco.latitude + " " + sanFransisco.longitude)
sanFireball = fireball(sanFransisco.latitude, sanFransisco.longitude)
print("San Fransisco Brightest " + str(sanFireball))

collect = [bostonFireball, ncrFireball, sanFireball]
for ele in collect:
    if ele != "No place with fireball":
        if compare < float(ele[1]):
            compare = float(ele[1])
            myRecord = ele

print(f'\n\nHIGHEST: Energy {myRecord[1]} Latitude {myRecord[3]} Longitude {myRecord[5]}')