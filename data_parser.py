import asyncio

import aiohttp
from bs4 import BeautifulSoup
from sqlalchemy import insert

import config
from db import Session
from models import Country

SOURCE_URL = config.SOURCE_URL


async def fetch(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()


def main():
    session = Session()
    url = SOURCE_URL
    html = asyncio.run(fetch(url))
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table', class_='wikitable')
    rows = table.find_all('tr')[2:]

    for row in rows:
        try:
            columns = row.find_all('td')
            country_name = columns[0].text.strip()
            population_2023 = int(columns[2].text.strip().replace(',', ''))
            region = columns[4].text.strip()
            stmt = insert(Country).values(name=country_name, population=population_2023, region=region)
            session.execute(stmt)
        except ValueError:
            continue
    session.commit()
    session.close()
    print(f"{'***'* 20} Parsed successfully {'***C'* 20}")


if __name__ == "__main__":
    main()
