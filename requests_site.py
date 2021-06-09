import requests
import time
from colorama import Fore, init

init()

username = input(Fore.GREEN + '[✓] Entrer le pseudonyme : ')

instagram = f'https://www.instagram.com/{username}'

twitch = f'https://www.twitch.tv/{username}'

facebook = f'https://www.facebook.com/{username}'

twitter = f'https://www.twitter.com/{username}'

youtube = f'https://www.youtube.com/{username}'

google_plus = f'https://plus.google.com/s/{username}/top'

reddit = f'https://www.reddit.com/user/{username}'

wordpress = f'https://{username}.wordpress.com'

pinterest = f'https://www.pinterest.com/{username}'

github = f'https://www.github.com/{username}'

steam = f'https://steamcommunity.com/id/{username}'

imgur = f'https://imgur.com/user/{username}'

spotify = f'https://open.spotify.com/user/{username}'

badoo = f'https://www.badoo.com/en/{username}'

dailymotion = f'https://www.dailymotion.com/{username}'

keybase = f'https://keybase.io/{username}'

pastebin = f'https://pastebin.com/u/{username}'

roblox = f'https://www.roblox.com/user.aspx?username={username}'

tripadvisor = f'https://tripadvisor.com/members/{username}'

wikipedia = f'https://www.wikipedia.org/wiki/User:{username}'

hackernews = f'https://news.ycombinator.com/user?id={username}'

ebay = f'https://www.ebay.com/usr/{username}'

WEBSITES = [
instagram, twitch, facebook, twitter, youtube, google_plus, reddit,
wordpress, pinterest, github, steam, imgur, spotify,
badoo, dailymotion, keybase, pastebin, roblox, 
tripadvisor, wikipedia, hackernews, ebay,
]

print(Fore.GREEN + f'[✓] Votre analyse à bien été envoyée sur le nom: {username}')
print(Fore.GREEN + '[✓] Analyse en cours veuillez patienter...')
time.sleep(2)

count = 0
match = True 
for url in WEBSITES:
    r = requests.get(url)

    if r.status_code == 200:
        if match == True:
            print(Fore.GREEN + '[✓] Information trouvée !')
            match = False
        if username in r.text:
            print(Fore.MAGENTA + f'\n{url} - {r.status_code} - [✓]')
            print(Fore.GREEN + f'TROUVÉ: Nom: {username} - Utilisateur Trouvé')
        else:
            print(Fore.MAGENTA + f'\n{url} - {r.status_code} - [X]')
            print(Fore.RED + f'INTROUVABLE: Nom: {username} - Utilisateur Introuvable')

print(Fore.WHITE + 'Fin de la recherche de Dox.')