# Population Data Service

This project aims to develop a service that runs via Docker Compose, storing country population data in PostgreSQL and displaying aggregated region-wise data on the screen

## Stack

   - Python 3.10
   - SQLAlchemy
   - BS4
   - aiohttp
   - Docker/Docker-compose

## Getting Started

### Prerequisites

Before you begin, make sure you have the following tools and technologies installed:

- Docker

[How to install Docker](https://docs.docker.com/engine/install/)

## Installing / Getting started

> A quick introduction of the setup you need to get run a project.

### Using Git

1. Clone the repo:

```shell
git clone https://github.com/petrykivd/region_population_analysis
```

2. Change directory:

```shell
   cd region_population_analysis
```

3. You can open project in IDE and configure .env file using [.env.sample](.env.sample) file as an example.

<details>
<summary>Parameters for .env file:</summary>

- **DATA_SOURCE_URL**: `Source link for parser`
- **POSTGRES_DB**: `Your Postgres DB`
- **POSTGRES_USER**: `Your Postgres User`
- **POSTGRES_PASSWORD**: `Your password in DB`
- **POSTGRES_HOST** `Host of your DB`
- **POSTGRES_PORT** `Port of your DB`

</details>

4. Run docker-compose command to build and run containers:

### For parsing data from source
```shell
docker-compose up get_data
```
### For printing data from DB
```shell
docker-compose up print_data
```

## How it Works
1. get_data: Downloads, parses, and saves data into the database.
2. print_data: Reads data from the database and displays it on the screen, following the format:
   - Region Name
   - Total Population of the Region
   - Name of the Largest Country in the Region (by population)
   - Population of the Largest Country in the Region
   - Name of the Smallest Country in the Region
   - Population of the Smallest Country in the Region

## Author

Petrykiv Dmytro / petrykiv.dmytro11@gmail.com

Feel free to explore the code, test it out, and provide feedback. Contributions and improvements are welcome!


<p align="center">
<img style="width: 100%;" src="https://i.postimg.cc/nzykWKNd/result.gif">
</p>