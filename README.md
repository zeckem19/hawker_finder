# Hawker finder
This web application finds the nearest hawker center within 20km of the input location (lat, long)  within Singapore .
  
## Requirements
1. docker engine or docker desktop on windows/ mac [Get docker](https://docs.docker.com/get-docker/)
2. docker-compose (should come together with docker desktop) [Get compose](https://docs.docker.com/compose/install/)

  ## Starting up
The **web application** starts by running (from within the project folder)
```bash
docker-compose up -d
```
on your shell with docker installed.
Run the following from outside the project folder:
```bash
docker-compose up -f <path to folder>/docker-compose.yml -d
```
The first run might take some time as images are downloaded and built.

Check out the app by going to [localhost:8501](http://localhost:8501/)  in a browser.
  
>  **Note:** You might need to disable firewall/ set firewall rules to allow port 8501.

## Components
The application comprises 3 containers
1. `ui` container developed with [Streamlit](https://streamlit.io/)
2. `db` container - MongoDB instance for geolocation queries
3. `ingest` container that downloads dataset from [data.gov.sg](https://data.gov.sg/dataset/hawker-centres?resource_id=8a6c2f75-5511-4e03-b8f2-23ce67d30b28)

## Checking out the project
Use the standard docker-compose CLI to explore the project

1. Display running containers: `docker-compose ps`
2. Display logs: `docker-compose logs`
3. Run project attached: `docker-compose up`
4. Run tests 
	- UI container 	`docker-compose exec ui pytest`
	- Ingest container	`docker-compose exec ingest pytest`


## Considerations
### Containers for development
This app uses docker containers starting from [development](https://code.visualstudio.com/docs/remote/remote-overview). This ensures a consistent, standardised environment for development, testing and running the application. 

1. A bridge docker network is used for communication between containers
2. A docker volume is mounted on mongodb container for persistent storage of db data.
3. The `<project folder>/compose` directory contains the Dockerfiles and other files required for building the images.

### Ingestion
Data is brought into the application by the `ingest` container. The following steps are taken:
1. Data is downloaded in a stream and unzipped.
2. Data is processed line by line - it is loaded as a JSON and a regex pattern is used to extract the PHOTOURL and NAME fields.
3. If the pattern matches and JSON is valid, a type [validator](https://pydantic-docs.helpmanual.io/) is used to validate the data.
4. The data is inserted into MongoDB
5. Geolocation indexes are created on the GeoJSON field
6. Data in DB is persisted in a docker volume

The above steps are written as `download_data` and `extract_data` functions and tested independently. The ingest container also exposes these steps as a REST api for the user to reload data.

### Querying
The web UI captures users' [lat, long] input  values and queries the DB on the [geolocation index](https://docs.mongodb.com/manual/geospatial-queries/). The query returns the 5 nearest locations within a (configurable) 20km radius. The UI renders the returned documents and also plots them on a map.