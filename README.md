# KlayTracker

Our goal is to create a monitoring service for our client's cryptocurrency using JavaScript and Python.

## System Architecture

### Frontend
- UI
- Logic
- iOS and Browser compatibility
- HTML, CSS, JS
- Live tracking 

### Backend
- Python based Web Server
- Blockchain data retrieval and update


## How to install 
### Backend
```
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install Flask
python3 -m pip install web3py-ext
```
### Database
[Refer to mariadb install using docker]https://mariadb.com/kb/en/installing-and-using-mariadb-via-docker/
```
cd database
./docker_launch.sh
```



## How to run
```
$ flask --app flaskr run --debug
```
## External References: 
- [flask quickstart guide](https://flask.palletsprojects.com/en/3.0.x/quickstart/)

## ERD
![KlayTracker intial ER diagram](https://github.com/nohkwak/KlayTracker/blob/main/doc/ERD%20KlayTracker.png)
