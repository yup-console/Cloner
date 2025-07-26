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
        
        # Color definitions
        border_color = "\033[38;5;69m"
        option_color = "\033[38;5;81m"
        text_color = "\033[97m"
        
        # Menu items in two columns
        left_options = [
            "[01] Server Copy",
            "[02] Server Sticker Copy",
            "[03] Server Emoji Copy"
        ]
        right_options = [
            "[04] Server Status",
            "[05] Token Checker",
            "[06] Exit"
        ]
        
        # Calculate widths
        max_left = max(len(opt) for opt in left_options)
        max_right = max(len(opt) for opt in right_options)
        box_width = max_left + max_right + 7  # 3 spaces between columns + 4 for borders
        
        # Center the box
        terminal_width = shutil.get_terminal_size().columns
        padding = max(0, (terminal_width - box_width) // 2)
        center_pad = " " * padding
        
        # Build the menu box
        horizontal = "═" * (box_width - 2)
        top = f"{border_color}╔{horizontal}╗"
        title = f"{border_color}║{text_color}{'Discord Server Cloner - v1.0'.center(box_width - 2)}{border_color}║"
        divider = f"{border_color}╠{'═'*(max_left + 2)}╦{'═'*(max_right + 2)}╣"
        bottom = f"{border_color}╚{'═'*(max_left + 2)}╩{'═'*(max_right + 2)}╝"
        
        # Print the menu
        print(f"\n{center_pad}{top}")
        print(f"{center_pad}{title}")
        print(f"{center_pad}{divider}")
        
        # Print options in two columns
        for left, right in zip(left_options, right_options):
            line = f"{border_color}║{text_color} {left.ljust(max_left)} {border_color}║{text_color} {right.ljust(max_right)} {border_color}║"
            print(f"{center_pad}{line}")
        
        print(f"{center_pad}{bottom}\n")
        
        # Centered input prompt
        prompt = f"{option_color}[>]{text_color} Select option (1-6): "
        prompt_pad = " " * (padding + (box_width - len(prompt)) // 2)
        cs = input(f"{prompt_pad}{prompt}")
        
        # Process input
        if cs.strip() in ["1", "01"]:
            await cloner()
        elif cs.strip() in ["2", "02"]:
            await sticker_cloner()
        elif cs.strip() in ["3", "03"]:
            await emoji_cloner()
        elif cs.strip() in ["4", "04"]:
            await guild_info()
        elif cs.strip() in ["5", "05"]:
            await token_checker()
        elif cs.strip() in ["6", "06", "exit", "quit"]:
            print(f"\n{option_color}[*]{text_color} Exiting Cloner...")
            break
        else:
            print(f"\n{option_color}[!]{text_color} Invalid option. Please try again.")
            await asyncio.sleep(1.5)

if __name__ == "__main__":
    try:
        asyncio.run(menu())
    except KeyboardInterrupt:
        print(f"\n{option_color}[!]{text_color} Cloner terminated by user.")