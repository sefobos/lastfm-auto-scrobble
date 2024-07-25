

import pylast
import time
import random
import threading
from colorama import Fore

api_key = ""
api_secret = ""
username = ""
password = ""

# put another tracks here if u want lol
piese = [
    {"artist": "Kendrick Lamar", "track": "HUMBLE.", "album": "DAMN."},
    {"artist": "Kendrick Lamar", "track": "DNA.", "album": "DAMN."},
    {"artist": "Kendrick Lamar", "track": "King Kunta", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "Alright", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "The Blacker the Berry", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "i", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "Swimming Pools (Drank)", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "Bitch, Don’t Kill My Vibe", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "Money Trees", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "M.A.A.D City", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "HiiiPoWeR", "album": "Section.80"},
    {"artist": "Kendrick Lamar", "track": "Rigamortus", "album": "Section.80"},
    {"artist": "Kendrick Lamar", "track": "The Heart Part 2", "album": "Section.80"},
    {"artist": "Kendrick Lamar", "track": "Sherane a.k.a Master Splinter’s Daughter", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "Backseat Freestyle", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "Sing About Me, I’m Dying of Thirst", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "The Art of Peer Pressure", "album": "good kid, m.A.A.d city"},
    {"artist": "Kendrick Lamar", "track": "Complexion (A Zulu Love)", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "Wesley’s Theory", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "Mortal Man", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "For Free? (Interlude)", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "How Much a Dollar Cost", "album": "To Pimp a Butterfly"},
    {"artist": "Kendrick Lamar", "track": "King Kunta", "album": "To Pimp a Butterfly"},
    {"artist": "Lil Tjay", "track": "F.N", "album": "F.N"},
    {"artist": "Lil Tjay", "track": "Calling My Phone", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Leaked", "album": "State of Emergency"},
    {"artist": "Lil Tjay", "track": "Hold On", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Brothers", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Ruthless", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Mood Swings", "album": "F.N"},
    {"artist": "Lil Tjay", "track": "None of Your Love", "album": "State of Emergency"},
    {"artist": "Lil Tjay", "track": "Pop Out", "album": "F.N"},
    {"artist": "Lil Tjay", "track": "Gang Gang", "album": "F.N"},
    {"artist": "Lil Tjay", "track": "One Take", "album": "State of Emergency"},
    {"artist": "Lil Tjay", "track": "Goat", "album": "F.N"},
    {"artist": "Lil Tjay", "track": "Bleed", "album": "State of Emergency"},
    {"artist": "Lil Tjay", "track": "Tutu", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "For You", "album": "State of Emergency"},
    {"artist": "Lil Tjay", "track": "The Ringer", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Stop Snitchin", "album": "State of Emergency"},
    {"artist": "Lil Tjay", "track": "War", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Swervin", "album": "F.N"},
    {"artist": "Lil Tjay", "track": "Shoot for the Stars", "album": "Destined 2 Win"},
    {"artist": "Lil Tjay", "track": "Best Friend", "album": "F.N"},
    {"artist": "Drake", "track": "God's Plan", "album": "Scorpion"},
    {"artist": "Drake", "track": "In My Feelings", "album": "Scorpion"},
    {"artist": "Drake", "track": "One Dance", "album": "Views"},
    {"artist": "Drake", "track": "Hotline Bling", "album": "Views"},
    {"artist": "Drake", "track": "Controlla", "album": "Views"},
    {"artist": "Drake", "track": "Too Good", "album": "Views"},
    {"artist": "Drake", "track": "Passionfruit", "album": "More Life"},
    {"artist": "Drake", "track": "Nice for What", "album": "Scorpion"},
    {"artist": "Drake", "track": "Nonstop", "album": "Scorpion"},
    {"artist": "Drake", "track": "Sicko Mode", "album": "Scorpion"},
    {"artist": "Drake", "track": "Laugh Now Cry Later", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Wants and Needs", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Life Goes On", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Fair Trade", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "In Too Deep", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Papi’s Home", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Way 2 Sexy", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "TSU", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Champagne Poetry", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "No Friends in the Industry", "album": "Certified Lover Boy"},
    {"artist": "Drake", "track": "Knife Talk", "album": "Certified Lover Boy"},
    {"artist": "Juice WRLD", "track": "Lucid Dreams", "album": "Goodbye & Good Riddance"},
    {"artist": "Juice WRLD", "track": "All Girls Are the Same", "album": "Goodbye & Good Riddance"},
    {"artist": "Juice WRLD", "track": "Legends", "album": "Goodbye & Good Riddance"},
    {"artist": "Juice WRLD", "track": "Robbery", "album": "Legends Never Die"},
    {"artist": "Juice WRLD", "track": "Wishing Well", "album": "Legends Never Die"},
    {"artist": "Juice WRLD", "track": "Come & Go", "album": "Legends Never Die"},
    {"artist": "Juice WRLD", "track": "Smile", "album": "Legends Never Die"},
    {"artist": "Juice WRLD", "track": "Stay High", "album": "Legends Never Die"},
    {"artist": "Juice WRLD", "track": "Conversations", "album": "Legends Never Die"},
    {"artist": "Juice WRLD", "track": "Up Up and Away", "album": "Goodbye & Good Riddance"},
    {"artist": "Oscar", "track": "Aici", "album": "Marea Dragoste"},
    {"artist": "Oscar", "track": "Un Suflet", "album": "Marea Dragoste"},
    {"artist": "Oscar", "track": "Zile Frumoase", "album": "Marea Dragoste"},
    {"artist": "Oscar", "track": "Marea Dragoste", "album": "Marea Dragoste"},
    {"artist": "Oscar", "track": "Frumosul", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Tu", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Poveste", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Vise", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Rădăcini", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Noapte", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Sărută-mă", "album": "Rădăcini"},
    {"artist": "Oscar", "track": "Băiatul cu Fata", "album": "Vise"},
    {"artist": "Oscar", "track": "Departe", "album": "Vise"},
    {"artist": "Oscar", "track": "Cine", "album": "Vise"},
    {"artist": "Oscar", "track": "În Oglindă", "album": "Vise"},
    {"artist": "Oscar", "track": "Te Voi Iubi", "album": "Vise"},
    {"artist": "Oscar", "track": "Despre Tine", "album": "Vise"},
    {"artist": "Oscar", "track": "Timpul", "album": "Vise"},
    {"artist": "Oscar", "track": "Efectul", "album": "Vise"},
    {"artist": "Oscar", "track": "Fără Tine", "album": "Vise"},
    {"artist": "Sleepy Hallow", "track": "Deep End Freestyle", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "2055", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Don’t Play", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Backseat", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "No Deal", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Let It Go", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Blow My Mind", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Out The Window", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Warrior", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "DND", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Free Young Thug", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Survival", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Skyline", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Just Hold On", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Sick Of Us", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Lean On", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Goodbye", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Late Nights", "album": "Still Sleep"},
    {"artist": "Sleepy Hallow", "track": "Runnin Up", "album": "Sleepy Hallow"},
    {"artist": "Sleepy Hallow", "track": "Never Again", "album": "Sleepy Hallow"}
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
mtmtmt = 10
iarmt = None

def ttt():
    global scrobbles
    while scrobbles < limit:
        uwu = time.time()
        for _ in range(mtmtmt):
            piesa = random.choice(piese)
            artist = piesa['artist']
            title = piesa['track']
            album = piesa['album']
            
            try:
                with mata:
                    network.scrobble(artist=artist, title=title, timestamp=int(time.time()), album=album)
                scrobbles += 1
                print(Fore.BLUE + f'scrobbling {title} by {artist} - total: {scrobbles}/{limit}', end='\r', flush=True)
            except pylast.NetworkError as e:
                print(Fore.RED + f' {e}')
                time.sleep(2)
            except pylast.WSError as e:
                print(Fore.RED + f'{e}')
                time.sleep(2)
            
            if scrobbles % 1000 == 0:
                print(Fore.BLUE + " pauza de 5 minute sa nu iei ratelimit U~U")
                time.sleep(300)  
        
        uwuw = time.time() - uwu
        if uwuw < 1:
            time.sleep(1 - uwuw)

def iariarmt():
    global iarmt
    if scrobbles >= limit:
        print(Fore.RED + f" gg sa FACUT destule dastea")
        return
    if iarmt and iarmt.is_alive():
        print(Fore.RED + f" ai dat deja start")
        return
    wuuwu = threading.Thread(target=ttt, daemon=True)
    wuuwu.start()
    print("lupta sclavule sati trag muie")

def scrobale():
    return {"scrobbles": scrobbles}

if __name__ == "__main__":
    print(Fore.BLUE + f"SAWUT ! BINE AI VEWIT LA CEL MAI BUN SCRIPT PENTRU LASTFM!    ESTE super BUN pentru A FACE scrobbles automat repede intro perioada scurta de timp si fara a lua ratelimit ! scwiptul este facut de 27mxnk Pe DisCord Si instagraM ")
    while True:
        pulamea = input(Fore.BLUE + f"foloseste (start, status, exit pentru a folosi scriptullll): ").strip().lower()
        if pulamea == "start":
            iariarmt()
        elif pulamea == "status":
            scrobalestatus = scrobale()
            print(Fore.BLUE + f" {scrobalestatus['scrobbles']}")
        elif pulamea == "exit":
            print(Fore.RED + f"exiting...")
            break
        else:
            print(Fore.RED + f"nu exista nmc cu ce ai zis tu acolo sclavule foloseste 'start', 'status', sau 'exit'")
