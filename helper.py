from rich import prompt
from rich.theme import Theme

console_theme = Theme({
    "info": "dim cyan",
    "warning": "yellow",
    "danger": "bold red",
})

def create_logo(console):
    ascii_logo = """
    
/$$      /$$           /$$        /$$$$$$                           /$$$$$$                                          /$$      
| $$  /$ | $$          | $$       /$$__  $$                         /$$__  $$                                        | $$      
| $$ /$$$| $$  /$$$$$$ | $$$$$$$ | $$  \__/  /$$$$$$  /$$$$$$/$$$$ | $$  \__/  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$$| $$$$$$$ 
| $$/$$ $$ $$ /$$__  $$| $$__  $$| $$       |____  $$| $$_  $$_  $$|  $$$$$$  /$$__  $$ |____  $$ /$$__  $$ /$$_____/| $$__  $$
| $$$$_  $$$$| $$$$$$$$| $$  \ $$| $$        /$$$$$$$| $$ \ $$ \ $$ \____  $$| $$$$$$$$  /$$$$$$$| $$  \__/| $$      | $$  \ $$
| $$$/ \  $$$| $$_____/| $$  | $$| $$    $$ /$$__  $$| $$ | $$ | $$ /$$  \ $$| $$_____/ /$$__  $$| $$      | $$      | $$  | $$
| $$/   \  $$|  $$$$$$$| $$$$$$$/|  $$$$$$/|  $$$$$$$| $$ | $$ | $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$| $$  | $$
|__/     \__/ \_______/|_______/  \______/  \_______/|__/ |__/ |__/ \______/  \_______/ \_______/|__/       \_______/|__/  |__/

    """
    console.print(ascii_logo, style="bold green")

options_list = ["1", "2"]
def main_input(prompt_text, console, default=None, choices=None):
    console.print("[red][[/red][cyan]1[/cyan][red]][/red]. Search for available WebCams XP5")
    console.print("[red][[/red]2[red]][/red]. Exit")
    result = prompt.Prompt.ask(prompt_text, default=default, choices=options_list)
    return result