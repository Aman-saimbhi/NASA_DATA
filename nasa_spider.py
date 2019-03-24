#https://data.nasa.gov/resource/eva.json
#https://api.nasa.gov/planetary/apod?api_key=yoygy0NRI07n1wVPFxfLNlU1A3LyfEu8IvaYgWaL
#"https://data.nasa.gov/resource/eva.json?api_key=yoygy0NRI07n1wVPFxfLNlU1A3LyfEu8IvaYgWaL"
import urllib
import json
import urllib.request,urllib.parse,urllib.error
import ssl
import sqlite3
from datetime import datetime,timedelta
from datetime import date

url= "https://data.nasa.gov/resource/eva.json"             #no key required for this , as it is open data.
#to ignore certificate errors , to access https sites.
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
#to create a database named NASA_RAW
conn=sqlite3.connect("NASA_RAW.sqlite")
cur=conn.cursor()

cur.execute("DROP TABLE IF EXISTS RAWDATA")
cur.execute('''CREATE TABLE IF NOT EXISTS RAWDATA(
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, eva TEXT, country TEXT,
                 crew TEXT, date TEXT, vehicle TEXT, purpose TEXT,duration TEXT)''')

document=urllib.request.urlopen(url , context=ctx)
data=document.read().decode()                   #200 is a good error
if document.getcode()!=200 :
    print("ERROR NAME :",document.getcode())
else:
    #print(data)
    #print("___________________________________________________________________________________________")
    #print(document.getheaders())
    try:
        js=json.loads(data)
    except:
        js=None
#to iterate through each entry in the json file.
count=0
for entry in js:
#TO CONTINUE EVEN IF THERE IS DATE MISSING IN THE ENTRY
    try:
        tdate=entry["date"]
#TO CLEAN THE DATE FORMAT ,WHICH IS SEPERATED BY A T ,AND WE DONT WANT THE TIME.
        x=tdate.split("T")
        fdate=x[0]
        print(fdate)
    except:
        print("DATE NOT FOUND IN THIS ENTRY")
        fdate=None
        print(fdate)

    try:
        duration=entry["duration"]
        print(duration)
    except:
        print("DURATION IS MISSING FOR THIS ENTRY")
        duration=None
    try:
        eva=entry["eva"]
        print(eva)
    except:
        print("eva missing for this entry")


    try:
        country=entry["country"]
        print(country)
    except:
        print("COUNTRY IS MISSING FOR THIS ENTRY")
        country=None

    try:
        purpose=entry["purpose"]
        print(purpose)
    except:
        print("PURPOSE IS MISSING FOR THIS ENTRY")
        purpose=None

    try:
        crew=entry["crew"]
        print(crew)
    except:
        print("CREW IS MISSING FOR THIS ENTRY")
        crew=None

    try:
        vehicle=entry["vehicle"]
        print(vehicle,'\n\n')
    except:
        print("VEHICLE IS MISSING IN THIS ENTRY")
        vehicle=None
    cur.execute('''INSERT OR IGNORE INTO RAWDATA(eva,country,crew,date,vehicle,purpose,duration)
                   VALUES(?,?,?,?,?,?,?)''',(eva,country,crew,fdate,vehicle,purpose,duration))
    count=count+1
    #commits after every 10 entries in the database
    if count%10==0:
        conn.commit()
print(" \nALL THE RAW DATA ADDED TO THE DATABASE !")
document.close()
