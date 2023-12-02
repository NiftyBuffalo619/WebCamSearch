from googlesearch import search
from rich import print
from rich.console import Console
from helper import create_logo, main_input
from rich import prompt
from searchwebcams import search_for_webcams_xp

if __name__ == "__main__":
    console = Console()
    create_logo(console)

    runsoftware = True
    while runsoftware:
        option = main_input("[red][[/red][cyan]-[/cyan][red]][/red]Option", console)
        if option == "1":
            search_for_webcams_xp(console)
        elif option == "2":
            runsoftware = False
            console.__exit__