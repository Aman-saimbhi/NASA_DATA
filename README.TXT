IN THIS PROJECT I AM USING THE API OF NASA'S EVA (EXTRA VEHICULAR ACTIVITY) DATASET ,WHICH HAS DATA ABOUT THE EVA,
TO DO SOME ANALYSIS AND VISUALISATION.

nasa_spider.py :-

1) FIRSTLY, WE EXTRACT ALL THE DATA FROM THE DATSET WHICH IS PRESENT IN JSON,
2) THEN WE LOAD THE JSON FILE INTO OUR PYTHON PROGRAM AND CACHE IT IN THE MEMORY.
3) THEN, WE MAKE A DATABASE NASA_RAW.sqlite AND ADD ALL THE RAW DATA IN THE DATABASE.
4) WE ALSO DUMP THE JSON FILE TO PRINT THE DATA WHICH WE HAVE ADDED IN THE DATABASE.

(You have to download sqlite3 to be able to run this program.)

nasa_model.py :-

IN THIS PROGRAM,WE WILL MODEL OUR DATABASE,WHICH WILL HELP TO STORE DATA IN A CLEAN MANNER IN THE DATABASE.
WHY DO WE MODEL THE DATABASE ??
1 - It's faster. A JOIN on an integer is much quicker than a JOIN
    on a string field or combination of fields. It's more efficient to compare integers than strings.

2 - It's simpler. It's much easier to map relations based on a single numeric field than
    on a combination of other fields of varying data types.

3 - It's data-independent. If you match on the ID you don't need to worry about the relation changing.
   If you match on a name, what do you do if their name changes (i.e. marriage)? If you match on an address, what if someone moves?

4 - It's more efficient If you cluster on an (auto incrementing) int field,
    you reduce fragmentation and reduce overall size of the data set.
    This also simplifies indexes needed to cover your relations.

SO, RATHER THAN A SINGLE TABLE HAVING ALL THE RAW DATA,WE MAKE MULTIPLE TABLES NOW , AND MAP THE TABLES,
     SO THAT THE DATA CAN BE ACCESSED FASTER.
WHEN YOU RUN THIS PROGRAM YOU GET A DATABASE NAMELY NASA_CLEAN.sqlite , WHICH HAVE MULTIPLE TABLES,
AND CLEAN DATA.

nasa_duration.py :-

IN THIS PROGRAM WE WILL DO SOME ANALYSIS WITH THE DATA.
1) FIRSTLY, WE ARE EXTRACTING DATA FROM THE DATABASE NASA_CLEAN.sqlite,
   AND STORING IT AS CACHE MEMORY TEMPORARILY,SO THAT WE CAN PRINT THE DATA OUT.
2) USING THE SQL QUERY , WE ARE GETTING ROWS ,USING THE JOIN OPERATION ON DIFFERENT TABLES WHICH ARE
    MAPPED , WE HAVE ORDERED THE DATA ON THE BASIS OF DURATION IN DESCENDING ORDER.
3) THEN WE HAVE LIMITED THE ENTRIES UPTO 5.
REGULAR EXPRESSION IS USED TO REPLACE MULTIPLE SPACES WITH A SINGLE SPACE COMA , TO MAKE THE NAME OF CREW MORE NEAT.

SO THIS HOW THIS PROGRAM IS GIVING US THE DESCRIPTION OF THE TOP 5 LONGEST
EXTRA VEHICULAR ACTIVITY DURATION.

visual.py :-

IN THIS PROGRAM , IS SOME SMALL VISUALISATION OF THE NUMBER OF EVA'S OF A RESPECTIVE COUNTRY,
YOU CAN SEE THE VISUALISATION USING JUPYTER NOTEBOOK OR HYDROGEN IN ATOM ETC
WE HAVE USED PANDAS AND matplotlib TO PERFROM THE VISUALISATION.
SEABORN IS ALSO USED TO GIVE SOME ADDITIONAL LOOK TO THE GRAPH.
PANDAS read_sql_query FUNCTION IS USED TO STORE THE DATA IN THE DATAFRAME FROM THE DATABASE.

visual2.py :-

IN THIS PROGRAM WE HAVE DONE SOME MORE VISUALISATION , WE HAVE SHOWN THE RELATION
BETWEEN NUMBER OF EVAS WITH THE YEARS , USING SCATTER PLOTS AND BAR GRAPHS.
WE HAVE USED PANDAS TO CLEAN SOME OF THE DATA , AND USING SPLIT WE HAVE EXTRACTED THE
YEAR FROM THE DATE , AND MADE YEAR A NEW COLUMN IN THE DATAFRAME.

visual3.py :-

THIS PROGRAM GIVES US THE MOST USEFUL VISUALISATION SO FAR,THIS GIVES THE NUMBER OF EVAS
WITH THE YEARS WITH RESPECT TO EACH COUNTRY.
