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
no_russia=df.groupby('country').count()['eva'][0]
no_usa=df.groupby('country').count()['eva'][1]
locations=[1,2]
heights=[no_russia,no_usa]
labels=['RUSSIA','USA']
plt.bar(locations,heights,alpha=0.6,color='y')
plt.xticks(locations,labels)
plt.xlabel('COUNTRY')
plt.ylabel('NO: OF EVA ')
plt.legend('eva');
