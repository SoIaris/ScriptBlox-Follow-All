#ashly.luv.you on discord

from colorama import Fore
import requests

SBAuth = "" # Authorization

PageNum = 1

while True:
    PagesAPI = requests.get(f"https://scriptblox.com/api/script/fetch?page={PageNum}")
    if PagesAPI.status_code == 200:
        res = PagesAPI.json()
    else:
        print(f"error {Fore.MAGENTA}{PagesAPI.status_code}{Fore.RESET} | {Fore.RED}{PagesAPI.text}{Fore.RESET}")

    for page in res["result"]["scripts"]:
        if page["owner"]:
            UserId = page["owner"]["_id"]
            Username = page["owner"]["username"]
            
            FollowAPI = requests.post("https://scriptblox.com/api/user/follow", headers={"Authorization": SBAuth}, json={"userId": UserId})
            if FollowAPI.status_code == 400:
                print(f"[{Fore.LIGHTRED_EX}-{Fore.RESET}] already following {Fore.GREEN}{Username}{Fore.RESET}, skipped | Page {res['result']['nextPage'] - 1}")
      
            if FollowAPI.status_code == 200:
                print(f"[{Fore.LIGHTMAGENTA_EX}+{Fore.RESET}] successfully followed {Fore.GREEN}{Username}{Fore.RESET} | Page {res['result']['nextPage'] - 1}")

    if PageNum < res["result"]["totalPages"]:
        PageNum = res["result"]["nextPage"]
    else:
        break 
