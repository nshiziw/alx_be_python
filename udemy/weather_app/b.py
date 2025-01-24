import requests
def getLoc(ip):
    r = requests.get('https://ipinfo.io/{ip}/json'.format(ip=ip)).json()
    return {
        "city": r["city"],
        "loc": r["loc"]
    }
print(getLoc('63.116.61.253'))