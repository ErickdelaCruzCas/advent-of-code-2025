


import requests

YEAR = 2025
DAY = 10

session_cookie = "53616c7465645f5fd44d6f480366191d72d942d87accf22b4d3a87d57a92458a1c6af851868975d767e22530d34e2a15e540cb3ea6b0739522377ce4175b2ec6"
headers = {"User-Agent": "erick-aoc-script"}
url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"
cookies = {"session": session_cookie}


def getDataFile():
    coords = []
    with open("first_input.txt", "r", encoding="utf-8") as f:
        for line in f:
            line = line.split()
            coords.append(line)
            # for i in range(len(line)):
            #     if line[i] == '{}':

                           
    return coords
    
def getDataHttp():
    resp = requests.get(url, cookies=cookies, headers=headers)
    if resp.status_code == 200:
        print(resp.text)

    else:
        print("Error:", resp.status_code)




if __name__ == "__main__":
    print(f"Empezamos")
    res = 0

    data = getDataFile()
    realData = getDataHttp()

    print(f"Solución y valor de Factory: {res}") 


