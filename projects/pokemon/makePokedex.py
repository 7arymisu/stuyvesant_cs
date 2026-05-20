#! /usr/bin/python3
print("Content-Type: text/html\n\n")

# used when debugging on the web
import os # import for chmod
import cgitb # import to catch HTTP errors (when running on the web)
cgitb.enable() # enable your error output for HTTP

# CONSTANTS ----
INDENT = "  "

## HTML template for all pages
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
## generates the table given a dictionary of pokemon data
def table(data):
    table_template = '''
    <table>
        <thead>
            _HEADER_
        </thead>
        _BODY_
    </table>'''

    header = ''
    for i in stats:
        header += f'\n{INDENT*4}<th>{i}</th>'
    table_template = table_template.replace("_HEADER_", header)

    cell = ""
    cell_data = ""
    cell_template = '''
    <tr>
        _CELL_
    </tr>'''

    for entry in data:
        for stat in stats:
            value = data[entry][stat]
            if stat == stats[-1]:
                cell_data += f'\n{INDENT*4}<td>{value}</td>'
                cell += cell_template.replace("_CELL_", cell_data)
                cell_data = ""
            else:
                cell_data += f'\n{INDENT*4}<td>{value}</td>'
    
    table_template = table_template.replace("_BODY_", cell)
    return table_template

## generates the navbar for all pages
def navbar(type_list): ## takes in a list of types to generate the dropdown menu for types
    navbar_template = '''
    <header>
            <nav class="navbar">
                <ul>
                    <span class="dropdown">
                        _webbuttons_
                    </span>
                    <span class="dropdown">
                        <button class="button">Types</button>
                        <span class="dropdown-content">
                            _types_
                        </span>
                    </span>
                </ul>
            </nav>
        </header>
    '''

    page_list = ["homepage", "allpokemon", "top10"]
    page = []
    for page in page_list:
        if page == page_list[0]:
            page.append(f'<button class="button"><a href="/~thuang80/pokemon/HTML/{page}.html">{page}</a></button>')
        else:
            page.append(f'{INDENT*6}<button class="button"><a href="/~thuang80/pokemon/HTML/{page}.html">{page}</a></button>')
    page = "\n".join(page)

    types = []
    for type in type_list:
        if type == type_list[0]:
            types.append(f'<a href="/~thuang80/pokemon/HTML/{type}.html">{type}</a>') 
        else:
            types.append(f'{INDENT*7}<a href="/~thuang80/pokemon/HTML/{type}.html">{type}</a>') 
    types = "\n".join(types)

    navbar_template = navbar_template.replace("_webbuttons_", page)
    navbar_template = navbar_template.replace("_types_", types)
    page = page.replace("_NAVBAR_", navbar_template)

## generates the homepage
def home():
    body = '''
    <p>Come on... Its Pikachu... Who doesnt love Pikachu?</p>
    '''

    favorite_pokemon = {}
    for entry in pokedict:
        if pokedict[entry]["Name"] == "Pikachu":
            favorite_pokemon[entry] = pokedict[entry]
    body += table(favorite_pokemon)
    
    home_page = page
    home_page = home_page.replace("_TITLE_", "Taryn's Pokedex")
    home_page = home_page.replace("_Style_", "/~thuang80/pokemon/CSS/PokeStyle.css") 
    home_page = home_page.replace("_BODY_", body)

    with open("HTML/homepage.html", "w") as f:
        try:
            os.chmod("HTML/homepage.html", 0o777)
        except PermissionError:
            pass
        f.write(home_page)

    return print(home_page)

## generates the page with all pokemon present
def all_pokemon():
    body = ""
    body += table(pokedict)

    all_pokemon_page = page
    all_pokemon_page = all_pokemon_page.replace("_TITLE_", "Taryn's Pokedex")
    all_pokemon_page = all_pokemon_page.replace("_Style_", "/~thuang80/pokemon/CSS/PokeStyle.css") 
    all_pokemon_page = all_pokemon_page.replace("_BODY_", body)

    with open("HTML/allpokemon.html", "w") as f:
        try:
            os.chmod("HTML/allpokemon.html", 0o777)
        except PermissionError:
            pass
        f.write(all_pokemon_page)

## generates the pages for each type of pokemon
def typing():
    body = ""
    types = {} 

    for entry in pokedict:
        type_list = []
        pokemon = pokedict[entry]
        type1 = pokemon["Type 1"]
        type2 = pokemon["Type 2"]
        type_list.append(type1)

        if type2 != "":
            type_list.append(type2) 
            type_list.append(f"{type1} & {type2}")

        for type in type_list:
            if type not in types:
                types[type] = {}
            types[type][key] = {}
            types[type][key]["#"] = pokemon["#"]
            types[type][key][f'{type} Type Pokemon Names'] = pokemon["Name"]
            types[type][key]["Front"] = pokemon["Front"]
            types[type][key]["Back"] = pokemon["Back"]
            types[type][key]["Type 1"] = pokemon["Type 1"]
            types[type][key]["Type 2"] = pokemon["Type 2"]
            
    typings = []
    for type in types:
        typings.append(type)

    navbar(typings)

    for type in types: #create type websites
        body = ""
        body += table(types[type])

        type_page = page
        type_page = type_page.replace("_TITLE_", str(type))
        type_page = type_page.replace("_Style_", "/~thuang80/pokemon/CSS/PokeStyle.css") 
        type_page = type_page.replace("_BODY_", body)

        with open(f"HTML/{type}.html", "w") as f:
            try:
                os.chmod(f"HTML/{type}.html", 0o777)
            except PermissionError:
                pass
            f.write(type_page)
    return 

## generates the page with the top 10 pokemon based on overall stats
def ranking():
    body = ""
    body += f'{INDENT*2}<h1>Top 10</h1>'
    body += f'\n{INDENT*2}<p>These are objectively the best Pokemon based on their overall stats. \n No bias *wink* *wink*</p>'

    ranking_dict = {}
    best_pokemon = ["Arcanine", "Gyarados", "Lapras", "Snorlax", "Articuno", "Zapdos", "Moltres", "Dragonite", "Mewtwo", "Mew"]
    for entry in pokedict:
        if pokedict[entry]["Name"] in best_pokemon:
            ranking_dict[entry] = pokedict[entry]
    body += table(ranking_dict)

    ranking_page = page
    ranking_page = ranking_page.replace("_TITLE_", "Top 10 Pokemon O.A.T.")
    ranking_page = ranking_page.replace("_Style_", "/~thuang80/pokemon/CSS/PokeStyle.css")
    ranking_page = ranking_page.replace("_BODY_", body)
    
    with open("HTML/top10.html", "w") as f:
        try:
            os.chmod("HTML/top10.html", 0o777)
        except PermissionError:
            pass
        f.write(ranking_page)

# MAIN ----
with open("/home/students/even/2028/thuang80/public_html/pokemon/pokemon.csv", "r") as f:
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

typing()
all_pokemon()
home()
ranking()