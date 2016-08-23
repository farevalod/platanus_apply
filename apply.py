import requests

url = "http://platan.us/jobs/apply"
content_type = "application/json"
payload = {
    "name":"Francisco Arevalo",
    "email":"farevalod@gmail.com",
    "github":"http://github.com/farevalod",
    "city":"Santiago",
    "other": {
        "resume":"http://desastre.cl/cv.txt",
        "notes":"Hice un mini script usando la lib requests de python, y nc -l para levantar un server e ir revisando los POST que genera",
        "script_src":"https://github.com/farevalod/platanus_apply",
        "interests":"Skiing, Mountaineering, Rock Climbing, Cooking, Graphic Design, Typography",
        "BTC Wallet":"12sPLuqb52q4B9JEgfENpuG1mLAjp9REYj"
    }
}

r = requests.post(url, json=payload)
print(r.text)
