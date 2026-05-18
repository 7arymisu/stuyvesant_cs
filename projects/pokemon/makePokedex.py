#! /usr/bin/python3
print("Content-Type: text/html\n\n")

# used when debugging on the web
import os # import for chmod
'''import cgitb # import to catch HTTP errors (when running on the web)
cgitb.enable() # enable your error output for HTTP'''

# indent - constant
INDENT = "  "

# page template - global variable
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

# makes a table given its data
def table(data):
    headers = []

    # 1. ID column
    headers.append(f'\n{INDENT*5}<th>#</th>')

    # 2. Image columns
    headers.append(f'\n{INDENT*5}<th>Front</th>')
    headers.append(f'\n{INDENT*5}<th>Back</th>')

    # 3. All other stats columns
    for stat in stats:
        if stat != "#":
            headers.append(f'\n{INDENT*5}<th>{stat}</th>')

    header_row = f'''
    {INDENT*3}<thead>
    {INDENT*4}<tr>
    {"".join(headers)}
    {INDENT*4}</tr>
    {INDENT*3}</thead>
    '''
    
    body = []
    for entry in data:
        row = []

        # 1. ID number
        row.append(f'\n{INDENT*6}<td>{data[entry]["#"]}</td>')

        # 2. Front image
        row.append(
            f'\n{INDENT*6}<td><img src="/~thuang80/public_html/pokemon/img/front/{entry}.png"></td>'
        )

        # 3. Back image
        row.append(
            f'\n{INDENT*6}<td><img src="/~thuang80/public_html/pokemon/img/back/{entry}.png"></td>'
        )

        # 4. Stats
        for stat in stats:
            if stat != "#":
                row.append(f'\n{INDENT*6}<td>{data[entry][stat]}</td>')

        body.append(f'\n{INDENT*5}<tr>{"".join(row)}\n{INDENT*5}</tr>')

    body_rows = f'''
    {INDENT*4}<tbody>
    {"".join(body)}
    {INDENT*4}</tbody>
    '''

    return f'''
    {INDENT*2}<table>
    {header_row}
    {body_rows}
    {INDENT*2}</table>
    '''
# generates the table for all pokemon
def all_pokemon():
    return table(pokedict)

#generates the tables for each typing
def types():
    type_dict = {}

    for entry in pokedict:
        type1 = pokedict[entry]["Type 1"]
        if type1 not in type_dict:
            type_dict[type1] = {}
        type_dict[type1][entry] = pokedict[entry]

    type_list = list(type_dict.keys())

    for poke_type in type_dict:
        body = table(type_dict[poke_type])

        type_page = page
        type_page = type_page.replace("_TITLE_", poke_type)
        type_page = type_page.replace("_STYLE_", "/~thuang80/public_html/pokemon/CSS/PokeStyle.css")
        type_page = type_page.replace("_BODY_", body)
        type_page = type_page.replace("_NAVBAR_", navbar(type_list))

        filename = poke_type

        with open(f"HTML/{filename}.html", "w") as f:
            f.write(type_page)

# builds a list of types for  dropdown menu
def build_type_list():
    types = []

    for key in pokedict:
        t = pokedict[key]["Type 1"]
        if t not in types:
            types.append(t)

    return types

# generates the homepage
def home():
    body = ''
    body += f'\n{INDENT*2}<h1>Welcome to the Pokedex!</h1>'
    body += f'\n{INDENT*2}<p>Come on... Its Pikachu... Who doesnt love Pikachu?</p>'
    
    favorite_pokemon = {}

    for entry in pokedict:
        if pokedict[entry]["Name"] == "Pikachu":
            favorite_pokemon[entry] = pokedict[entry]
    
    body += table(favorite_pokemon)
    return body

# ranks the top 10 pokemon
def ranking():
    body = ''
    body += f'\n{INDENT*2}<h1>Top 10</h1>'
    body += f'\n{INDENT*2}<p>These are objectively the best Pokemon based on their overall stats. \n No bias *wink* *wink*</p>'
    
    best_pokemon = ["Arcanine", "Gyarados", "Lapras", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dragonite", "Mewtwo", "Mew"]
    ranking = {}

    for entry in pokedict:
        if pokedict[entry]["Name"] in best_pokemon:
            ranking[entry] = pokedict[entry]

    return body + table(ranking)

def navbar(type_list):

    pages = ["homepage", "allpokemon", "top10"]

    page_buttons = []
    for p in pages:
        page_buttons.append(
            f'\n{INDENT*6}<button class="button">'
            f'<a href="/~thuang80/public_html/pokemon/HTML/{p}.html">{p}</a>'
            f'</button>'
        )

    type_links = []
    for t in type_list:
        type_links.append(
            f'\n{INDENT*7}<a href="{t}.html">{t}</a>'
        )

    return f'''
    {INDENT*2}<header>
    {INDENT*3}<nav class="navbar">
    {INDENT*4}<ul>

    {INDENT*5}<span class="dropdown">
    {"".join(page_buttons)}
    {INDENT*5}</span>

    {INDENT*5}<span class="dropdown">
    {INDENT*6}<button class="button">Types</button>

    {INDENT*6}<span class="dropdown-content">
    {"".join(type_links)}
    {INDENT*6}</span>

    {INDENT*5}</span>

    {INDENT*4}</ul>
    {INDENT*3}</nav>
    {INDENT*2}</header>
    '''

# -----------------------
# MAIN
# -----------------------
with open('/~thuang80/public_html/pokemon/pokemon.csv', "r") as f:
    pokedata =f.read().strip().split("\n")
    
    stats = pokedata[0].split(",") # gets the stats from the first line of the csv file and stores them in a list
    pokedict = {}

    for entry in pokedata[1:]:
        pokeinfo = entry.split(",")
        key = pokeinfo[0]

        pokedict[key] = {}

        for i, data in enumerate(pokeinfo):
            pokedict[key][stats[i]] = data

types()

# homepage
home_page = page
home_page = home_page.replace("_TITLE_", "Welcome to the Pokedex!")
home_page = home_page.replace("_STYLE_", "/~thuang80/pokemon/CSS/PokeStyle.css") 
home_page = home_page.replace("_BODY_", home())
home_page = home_page.replace("_NAVBAR_",navbar(build_type_list()))

with open("HTML/homepage.html", "w") as f:
    try:
        os.chmod("HTML/homepage.html", 0o777)
    except PermissionError:
        pass
    f.write(home_page)

print(home_page)

# all pokemon page
all_pokemon_page = page
all_pokemon_page = all_pokemon_page.replace("_TITLE_", "All Pokemon")
all_pokemon_page = all_pokemon_page.replace("_STYLE_", "/~thuang80/pokemon/CSS/PokeStyle.css") 
all_pokemon_page = all_pokemon_page.replace("_BODY_", all_pokemon())
all_pokemon_page = all_pokemon_page.replace("_NAVBAR_",navbar(build_type_list()))

with open("HTML/allpokemon.html", "w") as f:
    try:
        os.chmod("HTML/allpokemon.html", 0o777)
    except PermissionError:
        pass
    f.write(all_pokemon_page)

ranking_page = page
ranking_page = ranking_page.replace("_TITLE_", "Top 10 Pokemon O.A.T.")
ranking_page = ranking_page.replace("_STYLE_", "/~thuang80/pokemon/CSS/PokeStyle.css") 
ranking_page = ranking_page.replace("_BODY_", ranking())
ranking_page = ranking_page.replace("_NAVBAR_",navbar(build_type_list()))

with open("HTML/top10.html", "w") as f:
    try:
        os.chmod("HTML/top10.html", 0o777)
    except PermissionError:
        pass
    f.write(ranking_page)