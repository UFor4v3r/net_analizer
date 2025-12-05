#!/usr/bin/env python3
from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich import box
from sniffer.capture import start_sniffer

console = Console()
BANNER = r"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
                               [ UNKNOWN OPERATIONS ]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

      ▄████▄   ██╗   ██╗███╗   ██╗██╗  ██╗ ██████╗ ███╗   ██╗███╗   ██╗
     ▒██▀ ▀█╗  ██║   ██║████╗  ██║██║ ██╔╝██╔═══██╗████╗  ██║████╗  ██║
     ▒▓█    ▄  ██║   ██║██╔██╗ ██║█████╔╝ ██║   ██║██╔██╗ ██║██╔██╗ ██║
     ▒▓▓▄ ▄██▒ ██║   ██║██║╚██╗██║██╔═██╗ ██║   ██║██║╚██╗██║██║╚██╗██║
     ▒ ▓███▀ ░ ╚██████╔╝██║ ╚████║██║  ██╗╚██████╔╝██║ ╚████║██║ ╚████║
       ░▒ ▒  ░  ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═══╝

                        Adaptive Network Packet Framework
                               DEVELOPER: V01D
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

def draw_banner():
    console.print(Panel.fit(Text(BANNER, justify="center", style="bold green"), 
                            border_style="green", box=box.DOUBLE))

def menu():
    console.print(Panel.fit(
        "[bold green]1.[/bold green] Start Sniffer\n"
        "[bold green]2.[/bold green] Exit",
        title="[cyan]Main Menu[/cyan]",
        border_style="cyan",
        box=box.ROUNDED
    ))

def main():
    while True:
        console.clear()
        draw_banner()
        menu()


        choice = input(">")

        if choice == "1":
            start_sniffer(save=True)
        elif choice == "2":
            print("Good bye fuuuuuck u with love <3")
            break
        else:
            print("invalid choice")
if __name__ == "__main__":
    main()

