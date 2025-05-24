D = input()

direction = {
    "N": "S",
    "S": "N",
    "W": "E",
    "E": "W",
    "NE": "SW",
    "SW": "NE",
    "NW": "SE",
    "SE": "NW"
}

print(direction[D])