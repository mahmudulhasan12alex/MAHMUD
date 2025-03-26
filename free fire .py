import requests
import os
import time
import sys
from rich import print
from rich.console import Console
from rich.panel import Panel
import json
console = Console()
#-----------------------#colour code.....#
X = "{XD}"
V = "[][]"
Y = "\033[31;1m"
Z = "\033[35;1m"
K = "\033[38;5;46m"
M = "\033[35;1m"
R = "\x1b[38;5;196m"
#_-------------Tarmux Enter face ---------#
sys.stdout.write('\x1b]2;<💚MAHMUDUL💚>\x07')
def clear():os.system('clear');print(logo)
def linex():print(f'{R}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━')
# Logo MENU-------#
logo = """
{Y}Y88b    / 888~-_  {K}
{R} Y88b  /  888   \  {M}
{K}  Y88b/   888    | {Y}
{K}  /Y88b   888    | {Z}
{M} /  Y88b  888   /  {R}
{K}/    Y88b 888_-~{Y}
"""

# Print the logo
print(logo)
print (" {K}DAVLOPER {X}{V}MAHMUDUL {X}")

print (" {M}TELIGERM {X}{V}https://t.me/mahmudul_master69")

print ("{R}TOOLS {X}{V} FREE Fire INFO {X} ")


# Function to fetch user information
def get_user_info(uid):
    url = f'http://api.not-perfect.xyz/ff-info.php?uid={uid}'
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()  # Assuming the API returns a JSON response
        return data
    else:
        return f"Error: {response.status_code}"

os.system('espeak -a 100 " Enter,  YOUR TARGETS FREE FIRE UID"')
uid = input("Please enter your UID: ")

# Fetch user info
user_info = get_user_info(uid)

# Display the information in a single line
if isinstance(user_info, dict):
    print("Account Avatar ID:", user_info.get("AccountAvatarId"))
    print("Account BP Badges:", user_info.get("AccountBPBadges"))
    print("Account BP ID:", user_info.get("AccountBPID"))
    print("Account Create Time:", user_info.get("AccountCreateTime"))
    print("Account EXP:", user_info.get("AccountEXP"))
    print("Account Language:", user_info.get("AccountLanguage"))
    print("Account Last Login:", user_info.get("AccountLastLogin"))
    print("Account Level:", user_info.get("AccountLevel"))
    print("Account Likes:", user_info.get("AccountLikes"))
    print("Account Name:", user_info.get("AccountName"))
    print("Account Pin ID:", user_info.get("AccountPinId"))
    print("Account Prefer Mode:", user_info.get("AccountPreferMode"))
    print("Account Region:", user_info.get("AccountRegion"))
    print("Account Season ID:", user_info.get("AccountSeasonId"))
    print("Account Signature:", user_info.get("AccountSignature"))
    print("Account Type:", user_info.get("AccountType"))
    print("Account UID:", user_info.get("AccountUID"))
    print("BR Max Rank:", user_info.get("BrMaxRank"))
    print("BR Rank:", user_info.get("BrRank"))
    print("CS Max Rank:", user_info.get("CsMaxRank"))
    print("CS Rank:", user_info.get("CsRank"))
    
    # Display equipped items and other nested details
    print("Equipped Outfit Items:")
    for item in user_info.get("Equipped Items", {}).get("Equipped Outfit", []):
        print(f"Item ID: {item.get('Items ID')}, Item Icon: {item.get('Items Icon')}")
    
    print("Equipped Weapon:")
    for weapon in user_info.get("Equipped Items", {}).get("Equipped Weapon", []):
        print(f"Weapon ID: {weapon.get('Items ID')}, Weapon Icon: {weapon.get('Items Icon')}")
    
    print("Equipped Skills:", user_info.get("Equipped Items", {}).get("EquippedSkills"))
    print("Equipped Title:", user_info.get("EquippedTittle"))
    print("Equipped Weapon IDs:", user_info.get("EquippedWeapon"))
    
    # Guild Information
    guild_info = user_info.get("Guild Information", {})
    print("Guild Capacity:", guild_info.get("GuildCapacity"))
    print("Guild ID:", guild_info.get("GuildID"))
    print("Guild Level:", guild_info.get("GuildLevel"))
    print("Guild Member Count:", guild_info.get("GuildMember"))
    print("Guild Name:", guild_info.get("GuildName"))
    print("Guild Owner ID:", guild_info.get("GuildOwner"))
    print("Guild Leader Info:", guild_info.get("LeaderInfo"))
    
    # Pet Information
    pet_info = user_info.get("Pet Information", {})
    print("Pet Equipped:", pet_info.get("Equipped?"))
    print("Pet EXP:", pet_info.get("PetEXP"))
    print("Pet ID:", pet_info.get("PetID"))
    print("Pet Level:", pet_info.get("PetLevel"))
    print("Pet Name:", pet_info.get("PetName"))
    
    # Miscellaneous details
    print("Release Version:", user_info.get("ReleaseVersion"))
    print("Show BR Rank:", user_info.get("ShowBrRank"))
    print("Show CS Rank:", user_info.get("ShowCsRank"))

else:
    print(user_info)