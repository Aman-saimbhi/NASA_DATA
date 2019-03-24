import pandas as  pd
import numpy as np
%matplotlib inline
import seaborn as sns
sns.set_style('darkgrid')
import matplotlib.pyplot as plt
import sqlite3
conn=sqlite3.connect('NASA_CLEAN.sqlite')
cur=conn.cursor()
df=pd.read_sql_query('''SELECT eva,vehicle,country,crew,date,purpose,duration
                        FROM  EVA JOIN  CREW  JOIN  VEHICLE  JOIN COUNTRY
                        ON EVA.crew_id=crew.id AND  EVA.country_id=COUNTRY.id
                        and EVA.vehicle_id=VEHICLE.id''',conn)

df.dropna(inplace=True)
years=list()
for x in df['date']:
    if x is None:
        continue
    year=x.split('-')[0]
    years.append(year)
df['year']=years
df.isnull().any().sum()
df=df.astype({'year':int})

#VISUALISATION3 : number of evas with respect to each country.
#df.groupby(['country','year']).count()['eva']['Russia'][24:]
df.groupby(['country','year']).count()['eva']['USA'][24:]
rus_count=[2,3,3,3,1]
usa_count=[12,19,9,7,3]
#to make evenly spaced values.
locations=np.arange(5)
width=0.35
p1=plt.bar(locations,rus_count,alpha=0.6,color='r',width=0.35)
p2=plt.bar(locations+width,usa_count,alpha=0.6,color='g',width=0.35)
plt.xlabel('YEARS')
plt.ylabel('NUMBER OF EVA')
labels=['2008','2009','2010','2011','2012']
#we have done locations + width/2 so as to locate the labels in center.
plt.xticks(locations+width/2,labels)
plt.title('NUMBER OF EVAS BY COUNTRIES WITH YEARS.')
plt.legend((p1[0],p2[0]),('russia','usa'));
