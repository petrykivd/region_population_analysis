import asyncio
import os

import aiohttp
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from sqlalchemy import insert

from db.db import Session
from db.models import Country

load_dotenv()


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def main():
    session = Session()
    source = os.environ.get('SOURCE')
    source_mapper = {
        "wiki": "https://en.wikipedia.org/w/index.php?title=List_of_countries_by_population_(United_Nations)&oldid=1215058959/",
        "statisticstimes": "https://statisticstimes.com/demographics/countries-by-population.php"
    }
    if source not in source_mapper:
        raise Exception("Unknown source for parsing.")
    url = source_mapper[source]
    html = asyncio.run(fetch(url))
    soup = BeautifulSoup(html, 'html.parser')

    if source == "wiki":
        table = soup.find('table', class_='wikitable')
        rows = table.find_all('tr')[2:]
        population_col = 2
        region_col = 4
    else:
        table = soup.find("table", id="table_id")
        rows = table.find_all("tr")
        population_col = 1
        region_col = -1

    for row in rows:
        try:
            columns = row.find_all('td')
            if "world" in row.text.lower():
                break
            if len(columns) >= 3:
                country_name = columns[0].text.strip()
                population = int(columns[population_col].text.strip().replace(',', ''))
                region = columns[region_col].text.strip()
                stmt = insert(Country).values(name=country_name, population=population, region=region)
                session.execute(stmt)
        except ValueError:
            continue
    session.commit()
    session.close()
    print(f"{'***'* 20} Parsed successfully {'***'* 20}")


if __name__ == "__main__":
    main()
