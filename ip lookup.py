import json
import requests

print ("""__________                                   ___. \n    
\______   \__________  ___  ________________ \_ |__  
 |     ___/\_  __ \  \/  / / ___\_  __ \__  \ | __ \ 
 |    |     |  | \/>    < / /_/  >  | \// __ \| \_\ \\n
 |____|     |__|  /__/\_ \\___  /|__|  (____  /___  /
                        \/_____/            \/    \/  """)

def lookup(ip):
    with requests.get(f"http://ip-api.com/json/{ip}?fields-satus,message,contient,continentcode,country,countrycode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,orp,as,asname,reverse,mobile,proxy,hosting,query", verify=False) as result:
        info = result.json()
    return print(json.dumps(info, indent=4))

while True:
      ip = input('Entrer l adresse ip de votre citime:')
      lookup(ip)
      question = input("Voulez-vous continuer à chercher des ip? dire oui ou non : ")
      if question.lower() =="non":
          break