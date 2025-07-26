import asyncio
import shutil
from utils.innit import *
from func.cloner import *
from func.clone_stickers import *
from func.clone_emojis import *
from func.guild_info import *
from func.token_checker import *

async def menu():
    while True:
        clear()
        logo()

        # Option box with purple to blue gradient
        option_box = [
            "╔════════════════════════════════════════════════════════════════════╗",
            "║   [01] Server Copy     [02] Emoji Copy     [03] Sticker Copy       ║",
            "║   [04] Token Checker   [05] Server Info    [06] Exit               ║",
            "╚════════════════════════════════════════════════════════════════════╝"
        ]

        terminal_width = shutil.get_terminal_size().columns

        for line in option_box:
            print(Colorate.Horizontal(Colors.purple_to_blue, line.center(terminal_width)))

        # Prompt aligned to left with gradient color
        prompt_text = "[>] Select option (1-6): "
        prompt = Colorate.Horizontal(Colors.blue_to_cyan, prompt_text)
        cs = input(f"{prompt}")  # No centering — stays left

        # Handle selection
        if cs.strip() in ["1", "01"]:
            await cloner()
        elif cs.strip() in ["2", "02"]:
            await emoji_cloner()
        elif cs.strip() in ["3", "03"]:
            await sticker_cloner()
        elif cs.strip() in ["5", "05"]:
            await token_checker()
        elif cs.strip() in ["4", "04"]:
            await guild_info()
        elif cs.strip() in ["6", "06", "exit", "quit"]:
            print(f"\n{Colors.blue}[!]{Colors.white} Exiting Cloner...")
            break
        else:
            print(f"\n{Colors.red}[!]{Colors.white} Invalid option. Please try again.")
            await asyncio.sleep(1.5)

if __name__ == "__main__":
    try:
        asyncio.run(menu())
    except KeyboardInterrupt:
        print(f"\n{Colors.red}[!]{Colors.white} Cloner terminated by user.")
