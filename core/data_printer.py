from sqlalchemy import text
from db.db import engine


with engine.connect() as con:
    rs = con.execute(text('''
        SELECT region AS "Region Name",
            SUM(population) AS "Total Population of the Region",
            (
                SELECT name 
                FROM country 
                WHERE region = c.region 
                ORDER BY population DESC 
                LIMIT 1
            ) AS "Name of the Largest Country in the Region",
            (
                SELECT population 
                FROM country 
                WHERE region = c.region 
                ORDER BY population DESC 
                LIMIT 1
            ) AS "Population of the Largest Country in the Region",
            (
                SELECT name 
                FROM country 
                WHERE region = c.region 
                ORDER BY population ASC 
                LIMIT 1
            ) AS "Name of the Smallest Country in the Region",
            (
                SELECT population 
                FROM country 
                WHERE region = c.region 
                ORDER BY population ASC 
                LIMIT 1
            ) AS "Population of the Smallest Country in the Region"
        FROM
            country AS c
        GROUP BY
            region;
    '''))

    for row in rs:
        print("Region Name:", row[0])
        print("Total Population of the Region:", row[1])
        print("Largest Country in the Region:", row[2])
        print("Population of the Largest Country in the Region:", row[3])
        print("Smallest Country in the Region:", row[4])
        print("Population of the Smallest Country in the Region:", row[5])
        print(f"{'***' * 45}")
