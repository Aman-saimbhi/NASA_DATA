
import pandas as  pd
%matplotlib inline
import seaborn as sns
sns.set_style('white')
import matplotlib.pyplot as plt
import sqlite3
conn=sqlite3.connect('NASA_CLEAN.sqlite')
cur=conn.cursor()
df=pd.read_sql_query('''SELECT eva,vehicle,country,crew,date,purpose,duration
                        FROM  EVA JOIN  CREW  JOIN  VEHICLE  JOIN COUNTRY
                        ON EVA.crew_id=crew.id AND  EVA.country_id=COUNTRY.id
                        and EVA.vehicle_id=VEHICLE.id''',conn)
#VISUALISATION1- SCATTER PLOT BETWEEN NUMBER OF EVAS AND YEARS.
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
df.plot(x='year',y='eva',kind='scatter');

#VISUALISATION 2 - NUMBER OF EVAS WITH SOME DIFFERENT YEARS.
df.groupby('year').count()['eva'][35:]
counts=[22,12,10,4,3]
labels=['2009','2010','2011','2012','2013']
x=[1,2,3,4,5]
plt.bar(x,counts,alpha=0.6,color='g')
plt.xticks(x,labels)
plt.xlabel('YEARS')
plt.ylabel('NO OF EVA')
plt.legend('eva');
