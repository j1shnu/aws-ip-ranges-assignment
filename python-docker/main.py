from requests import get
from fastapi import FastAPI
from json import dump, load
from fastapi_utils.tasks import repeat_every

app = FastAPI()
IP_FILE="/app/ip_prefixes.json"


@app.on_event("startup")
@repeat_every(seconds=5, wait_first=False)
def get_ips():
    URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"
    response = get(URL)
    jsonData = response.json()
    ipList = [i["ip_prefix"] for i in jsonData.get("prefixes")]
    ipList = [(i) for i in ipList if i.endswith("/32")]
    ipDictionary = {"ip_prefixes": ipList}
    with open(IP_FILE, "w") as outfile:
        dump(ipDictionary, outfile)


@app.get("/")
async def ips():
    with open(IP_FILE, "r") as openfile:
        ipList = load(openfile)
    return ipList.get("ip_prefixes")
