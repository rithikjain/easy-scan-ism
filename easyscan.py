import typer
from enum import Enum
import subdomains
import os
from notification.notifier import send_reports_to_tg

app = typer.Typer()

class Notifiers(Enum):
    telegram = "telegram"

@app.command()
def do_recon(
    domain: str = typer.Argument("", help="The domain name for the required host"),
    all: bool = typer.Option(True, help="Selects all available tools for recon"),
    notify: Notifiers = typer.Option("", help="Select notification service"),
):

    if all:
        total_subdomains = subdomains.get_subdomains(domain)
        print(total_subdomains)
        os.system("httpx -l temp_db/subdomains.txt -status-code -title -tech-detect -probe -o temp_db/probe.txt")
        os.system("arjun -u https://" + domain + " -oJ temp_db/arjun.json") # TODO: Run it for all the subdomains
    else:
        """
        TODO: selection logic
        """

    if notify == Notifiers.telegram:
        send_reports_to_tg(domain)
        print("Reports sent to Telegram!")


app()

"""
easyscan dscvit.com --all --notify telegram|discord
"""
