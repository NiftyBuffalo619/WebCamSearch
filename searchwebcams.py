from googlesearch import search
from rich.console import Console
from rich.table import Table

def search_for_webcams_xp(console, num=5, stop=20, pause=2):
    table = Table(title="Web Cams XP")
    table.add_column("Service", justify="center", style="cyan", no_wrap=True)
    table.add_column("Country", justify="center", style="cyan", no_wrap=True)
    table.add_column("Address", justify="center", style="cyan", no_wrap=True)

    query = 'intitle:"webcamXP" inurl:8080'
    for result in search(query, num=5, stop=10, pause=2):
        table.add_row(result)
    console.print(table)