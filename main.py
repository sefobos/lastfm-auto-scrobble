







import pylast
import time
import random
import threading
from colorama import Fore

api_key = ""
api_secret = ""
username = ""
password = ""

niste_sclavi = [
    "Kendrick Lamar", "Lil Tjay", "Drake", "Juice WRLD", "Oscar", "Sleepy Hallow",
    "Tzanca Uraganu", "Deftones", "Suicideboys", "Costel Biju", "Chief Keef", "21 Savage", 
    "A Boogie wit da Hoodie, Ant13x3$V3R$AC3"
]

try:
    network = pylast.LastFMNetwork(
        api_key=api_key,
        api_secret=api_secret,
        username=username,
        password_hash=pylast.md5(password)
    )
except pylast.NetworkError as e:
    print(Fore.RED + f'Network error: {e}')
    exit()
except pylast.WSError as e:
    print(Fore.RED + f'API error: {e}')
    exit()

mata = threading.Lock()
scrobbles = 0
limit = 100000000
mtmtmt = 4
d1 = 10
d2 = 15
iarmt = None

def ttt():
    global scrobbles
    while scrobbles < limit:
        uwu = time.time()
        cvcvcv = random.sample(niste_sclavi, mtmtmt)
        for fraier in cvcvcv:
            nume = f"sug pula"
            album = f" sunt un cacat gen "
            
            try:
                with mata:
                    network.scrobble(artist=fraier, title=nume, timestamp=int(time.time()), album=album)
                scrobbles += 1
                print(Fore.BLUE + f'scrobbling {title} by {artist} - total: {scrobbles}/{limit}', end='\r', flush=True)
            except pylast.NetworkError as e:
                print(Fore.RED + f' {e}')
                time.sleep(2)
            except pylast.WSError as e:
                print(Fore.RED + f'{e}')
                time.sleep(2)
           
            if scrobbles % 1100 == 0:
                print(Fore.YELLOW + "pauza K nu vreau ratelimiT")
                time.sleep(10)  
                restart_script()  

        uwuw = time.time() - uwu
        if uwuw < 1:
            time.sleep(1 - uwuw)
        time.sleep(random.uniform(d1, d2 + 7))  

def restart():
    global scrobbles, iarmt
    print(Fore.YELLOW + "restarting....")
    time.sleep(60)
    scrobbles = 0
    iarmt = threading.Thread(target=ttt, daemon=True)
    iarmt.start()

def iariarmt():
    global iarmt
    if scrobbles >= limit:
        print(Fore.RED + f" gg sa FACUT destule dastea")
        return
    if iarmt and iarmt.is_alive():
        print(Fore.RED + f" ai dat deja start")
        return
    iarmt = threading.Thread(target=ttt, daemon=True)
    iarmt.start()
    print("lupta sclavule sati trag muie")

def scrobale():
    return {"scrobbles": scrobbles}

if __name__ == "__main__":
    print(Fore.BLUE + f"SAWUT ! BINE AI VEWIT LA CEL MAI BUN SCRIPT PENTRU LASTFM!    ESTE super BUN pentru A FACE scrobbles automat repede intro perioada scurta de timp si fara a lua ratelimit !")
    while True:
        pulamea = input(Fore.BLUE + f"foloseste (start, status, restart, exit pentru a folosi scriptullll): ").strip().lower()
        if pulamea == "start":
            iariarmt()
        elif pulamea == "status":
            scrobalestatus = scrobale()
            print(Fore.BLUE + f" {scrobalestatus['scrobbles']}")
        elif pulamea == "restart":
            restart()
        elif pulamea == "exit":
            print(Fore.RED + f"exiting...")
            break
        else:
            print(Fore.RED + f"nu exista nmc cu ce ai zis tu acolo sclavule foloseste 'start', 'status', 'restart' sau 'exit'")
