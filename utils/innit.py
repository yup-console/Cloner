import requests
import threading
import asyncio
import base64
from pystyle import *
import random
from datetime import datetime
import os
import time

def logo():
    cloner_art = """
 ▄████▄   ██▓     ▒█████   ███▄    █ ▓█████  ██▀███  
▒██▀ ▀█  ▓██▒    ▒██▒  ██▒ ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒
▒▓█    ▄ ▒██░    ▒██░  ██▒▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒
▒▓▓▄ ▄██▒▒██░    ▒██   ██░▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  
▒ ▓███▀ ░░██████▒░ ████▓▒░▒██░   ▓██░░▒████▒░██▓ ▒██▒
░ ░▒ ▒  ░░ ▒░▓  ░░ ▒░▒░▒░ ░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
  ░  ▒   ░ ░ ▒  ░  ░ ▒ ▒░ ░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░
░          ░ ░   ░ ░ ░ ▒     ░   ░ ░    ░     ░░   ░ 
░ ░          ░  ░    ░ ░           ░    ░  ░   ░     
░
"""
    centered_art = "\n".join(" " * 15 + line for line in cloner_art.strip("\n").splitlines())
    tagline = " " * 20 + "MADE BY CONSOLE"
    print(Colorate.Horizontal(Colors.red_to_yellow, centered_art))
    print(Colorate.Horizontal(Colors.purple_to_red, tagline))

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def current_time():
    return datetime.now().strftime("%H:%M:%S")

b = Colors.dark_blue
r = Colors.red
g = Colors.green
y = Colors.yellow
w = Colors.white
