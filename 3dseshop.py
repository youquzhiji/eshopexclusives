from __future__ import annotations

import csv
import json
import requests

if __name__ == '__main__':
    with open('games.json', 'r', encoding='utf-8') as f:
        with open('3dseshop.csv', 'w',newline='', encoding='utf-8') as csvfile:
            games = json.load(f)
            writer = csv.writer(csvfile)
            writer.writerow(['Name', "Price", "VC", "Cover Art", "URL"])

            for game in games:
                wr=[]
                if len(game["howToShop"])==1 and game["howToShop"][0]!="At retail":
                    wr.append(game["title"])
                    wr.append(game["msrp"])
                    if "virtualConsole" in game:
                        wr.append(game["virtualConsole"])
                    else:
                        wr.append(" ")
                    if "boxart" in game:
                        wr.append(game["boxart"])
                    else:
                        wr.append(" ")
                    wr.append("www.nintendo.com"+game["url"])
                    writer.writerow(wr)