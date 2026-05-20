#! /usr/bin/python3
print("Content-Type: text/html\n\n")

# used when debugging on the web
'''import os # import for chmod
import cgitb # import to catch HTTP errors (when running on the web)
cgitb.enable() # enable your error output for HTTP'''

# CONSTANTS ----
page = '''
<!DOCTYPE html>
<html lang="en">
    <head>
        <!-- Metadata -->
        <meta charset="UTF-8" />
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <!-- Stylesheet -->
        <link rel="stylesheet" href="_STYLE_" />
        <!-- Title -->
        <title>_TITLE_</title>
    </head>
    <body>
        _NAVBAR_
        _BODY_
    </body>
</html>
'''

# DEFINITIONS ----
def table(data):
    table_template = '''
    <table>
        <thead>
            _HEADER_
        </thead>
        _BODY_
    </table>'''


# MAIN ----
with open("projects/pokemon/pokemon.csv", "r") as f:
    pokedata = f.read().strip().split("\n")
    stats = pokedata[0].split(",") # gets the stats from the first line of the csv file and stores them in a list
    pokedict = {}

    for entry in pokedata[1:]:
        pokeinfo = entry.split(",") # splits the line into a list of values
        key = pokeinfo[0] # the key is the first value (the pokemon's name)
        pokedict[key] = {} # creates a new dictionary for the pokemon

        for i, data in enumerate(pokeinfo):
            pokedict[key][stats[i]] = data

            if i == 1:
                pokedict[key]["Front"] = f'''<img src="/~thuang80/pokemon/img/front/{key}.png">''' #add Front stat and img
                pokedict[key]["Back"] = f'''<img src="/~thuang80/pokemon/img/back/{key}.png">''' #add Back stat and img

print(stats)