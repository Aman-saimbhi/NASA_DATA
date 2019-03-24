import sqlite3

conn=sqlite3.connect("NASA_CLEAN.sqlite")
cur=conn.cursor()
#TO OPEN THE DATABASE FOR READING PURPOSES ONLY,SO THAT WE CAN USE TWO DATABASES TOGETHER.
conn_1=sqlite3.connect('file:NASA_RAW.sqlite?mode=ro', uri=True)
cur_1=conn_1.cursor()
#WE WILL CLEAN THE DATABASE DATA SO THAT THERE ARE NO STRING REPETITIONS.
cur.execute("DROP TABLE IF EXISTS EVA")
cur.execute("DROP TABLE IF EXISTS COUNTRY")
cur.execute("DROP TABLE IF EXISTS CREW ")
cur.execute("DROP TABLE IF EXISTS VEHICLE")

cur.executescript('''
                  CREATE TABLE IF NOT EXISTS EVA
                  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,eva INTEGER,
                  country_id INTEGER ,crew_id INTEGER ,date TEXT,vehicle_id INTEGER ,
                  purpose TEXT,duration TEXT);

                  CREATE TABLE IF NOT EXISTS COUNTRY
                  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,country TEXT UNIQUE);

                  CREATE TABLE IF NOT EXISTS CREW
                  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,crew TEXT UNIQUE);

                  CREATE TABLE IF NOT  EXISTS vehicle
                  (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,vehicle TEXT UNIQUE);

                 ''')
countries=list()
crews=list()
vehicles=list()
cur_1.execute("SELECT eva,country,crew,date,vehicle,purpose,duration FROM RAWDATA")
#this loop will itertate through each record of the RAWDATA table.
for row in cur_1:
    eva=row[0]
    country=row[1]
    crew=row[2]
    date=row[3]
    vehicle=row[4]
    purpose=row[5]
    duration=row[6]
    if country not in countries:
        countries.append(country)
        cur.execute("INSERT OR IGNORE INTO COUNTRY(country) VALUES(?)",(country,))
        cur.execute("SELECT id FROM COUNTRY WHERE country=?",(country,))
        try:
            country_id=cur.fetchone()[0]
        except:
            country_id=None
    if crew not in crews:
        crews.append(crew)
        cur.execute("INSERT OR IGNORE INTO CREW(crew) VALUES(?)",(crew,))
        cur.execute("SELECT ID FROM CREW WHERE crew=?",(crew,))
        try:
            crew_id=cur.fetchone()[0]
        except:
            crew_id=None
    if vehicle not in vehicles:
        vehicles.append(vehicle)
        cur.execute("INSERT OR IGNORE INTO vehicle(vehicle) VALUES(?)",(vehicle,))
        cur.execute("SELECT ID FROM vehicle WHERE vehicle=?",(vehicle,))
        #in case when vehicle is None
        try:
            vehicle_id=cur.fetchone()[0]
        except:
            vehicle_id=None
#DATA IN CLEAN MANNER IS STORED IN THE NEW DATABASE ,WHICH CAN BE ACCESSED FAST.
    cur.execute('''INSERT OR IGNORE INTO EVA(eva,country_id,crew_id,date,vehicle_id,purpose,duration)
                VALUES(?,?,?,?,?,?,?)''',(eva,country_id,crew_id,date,vehicle_id,purpose,duration,))
print("DATA ADDED TO THE DATABASE IN A CLEAN MANNER !!")
conn.commit()
