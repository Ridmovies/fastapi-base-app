<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a id="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->


<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

<!-- PROJECT NAME AND DESCRIPTION -->
<h2 align="center">fastapi-base-app</h2>
<p align="center">
Simple fastapi app as carcass for future applications
</p>

<!-- ABOUT THE PROJECT -->
## About The Project
This is a basic application project on Fastapi
Origin course: https://github.com/mahenzon/FastAPI-base-app

<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Built With
* Poetry
* FastApi
* SQLAlchemy
* Postgresql+asyncpg (Docker compose)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- ROADMAP -->
## Roadmap

- [x] Poetry
- [x] Readme.md
- [x] .env Settings and Environment Variables 
- [] async database (Docker compose)
- [x] example app "posts"
- [] Unittest with Pytest
- [] Auth app
    - [] bearer access jwt token
    - [] hashed password + salt
    - [] refresh token
- [] Admin Panel
- [] Docker
    - [] Docker compose



## Installation
### Installation for Linux with Virtual Environment
*  #### Clone the repo
   ```bash
   git clone https://github.com/Ridmovies/fastapi-base-app.git
   ```  
   
* #### Enter the application root folder: 
```bash
cd <root folder>
```
   
* #### Create a virtual environment in the project's root folder:
```bash
python3 -m venv .venv 
```

* #### Activate the virtual environment:
```bash
source .venv/bin/activate 
```

* #### Install dependencies for the production environment: 
```bash
pip install -r requirements.txt 
```

* #### Change .env file
1. Create postgres database or launch postgres docker 
2. Rename '.env.template' to '.env'
3. Replace the settings with your own

* #### Start your application using Uvicorn in root folder :
 ``` 
uvicorn src.main:app --host 127.0.0.1 --port 8000 --reload 
```

<!-- USAGE EXAMPLES -->
## Usage

* ### OpenAPI (Swagger UI) Documentation
        http://127.0.0.1:8000/docs



## Develop 
### Poetry Dependency Management System
### Creating a New Project

```bash
poetry new my-project
```
This command will create a new project structure with a `pyproject.toml` file where dependencies are stored.

### Initializing an Existing Project
```bash
poetry init
```

This command initializes the project by asking for necessary parameters and creating a `pyproject.toml` file.

### Adding a Package
```bash
poetry add requests
```
Adds the `requests` package to your project's list of dependencies.
To add a package under the `[tool.poetry.dev-dependencies]` section in the `pyproject.toml` file, use the following command:
```bash
poetry add black --group dev
```
### Updating All Packages
```bash
poetry update
```
Updates all packages to their latest compatible versions.

### Synchronizing Poetry with Virtual Environment
```bash
poetry install --sync
```
### Showing the Package Tree
```bash
poetry show --tree
```
### Removing a Package
```bash
poetry remove <package_name>
```

## Docker
## Commands for working with Docker and Docker Compose
These commands will help you manage containers and images in your project, providing a convenient development and testing process.

### Creating an image from a Dockerfile
```bash
docker build -t image_name .
```

### Run a container from an image
```bash
docker run -p 8000:8000 image_name
```

### Remove all containers
```bash
docker rm $(docker ps -aq)
```

### Remove all images
```bash
docker rmi $(docker images -q)
```

### Stop and remove all services and images

```bash
docker-compose down --rmi all
```

### To start a console inside a running Docker container, use the docker exec command
```bash
docker exec -it container_name bash
```

### Run the container in interactive mode to gain shell access inside the container:
```bash
docker run -it --rm -p 9000:8000 container_name sh
```

### Build a new image and run containers

```bash
docker-compose up --build
```
This command builds a new image based on the instructions in `docker-compose.yml`.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
