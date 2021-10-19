# TODO:
# None!

# Imports
from fire import Fire # CLI
from json import load, dumps # JSON
from os import system # Open apps
from os import mkdir # Create directories
from pathlib import Path # Path-finding tools
from rich import print, console # COOL CONSOLE

# Constants
FAVSFILE = f'{Path.home()}/MacFavourites/favorites.json'

# Variables
global favs
favs = {}

# Manual command
def man():
    print("""
[b]Commands:[/b]
\t[b]man[/b] - Prints this manual
\t[b]run[/b] [i](favorite)[/i] - Runs a favorite
\t[b]add[/b] [i](name) (path)[/i] - Add a favorite
\t[b]remove[/b] [i](favorite/\'*\')[/i] - Removes a favorite, if \'*\' removes all favorites
\t[b]list[/b] - Lists all favorites

[b]Info:[/b][i]
\tFavorites\' names are [b]NOT[/b] case-sensitive.

\tRunning this cli-tool without a command will result in man command,
\trunning without commands but with favorite name will result in run command.[/i]
""")

# Commands
def run(favorite : str): # Run favorites
    # Check if favorite exists
    try: 
        system(f'open {favs[favorite.lower()]}') # Open app
        print("[b Green]Success!")
    # Error if not
    except KeyError: print(f"[b Red]Favorite {favorite} not found, add it first.")
def add(name : str, path : str): # Add favorites
    # Check if name is appropriate
    if name not in globals().keys():
        favs[name.lower()] = path # Add to favs
        print("[b Green]Success!")
    else:
        print("[b Red]Inappropriate name.") # Error if not
def remove(favorite : str): # Remove favorites
    global favs

    # Remove all
    if favorite=='*':
        if console.Console().input('[b Red]ARE YOU SURE? THIS WILL DELETE EVERY FAVORITE(Y/N): ').lower()=='y': # WARNING
            favs = {} # Set favs to empty dict
            print('[b Green]Success!')
        else: print('[b Red]Aborted.')
    # Remove one
    else:
        # Check if favorite exists
        try: 
            del favs[favorite.lower()] # Remove from favs
            print("[b Green]Success!")
        # Error if not
        except KeyError: print(f"[b Red]Favorite {favorite} not found, add it first.")
def list(): print('[b]' + '\n'.join(favs.keys()).title()) # Prints a list of favorites

# Command parser
def main(*args):
    # Check if no command and no args 
    if len(args):
        try: globals()[args[0]](*args[1:]) # Check if no command
        except KeyError: run(*args) # Runs favorite if not
    # Prints manual if not
    else:
        man()
# CLI stuff
if __name__ == '__main__':
    try: favs = load(open(FAVSFILE)) # Try to open JSON file
    except FileNotFoundError: # Create one if it doesn't exist
        print('[b]JSON file not found, creating new one...')
        try: mkdir(f'{Path.home()}/MacFavourites/') # Try to create new folder
        except FileExistsError: pass # Do nothing if already exists
        open(FAVSFILE, 'w+') # Create file
        favs = {} # Set favs to empty dict
    Fire(main) # CLI
    with open(FAVSFILE, 'w') as f: f.write(dumps(favs)) # Save favs to JSON file

