# Introduction to Development using Containers

## Prerequisites
* Have Docker installed
* Cloned this repository to your local machine with a terminal up and running
* Check that your Docker is running with the following command

`docker run hello-world`

### Install Docker 
Install `Docker Desktop`

#### Ensure Docker Memory
- To make sure we can run multiple container go to Docker>Preferences>Resources and in "Memory" make sure you have selected > 4GB

### Install VSCode  
Follow the [instructions](https://code.visualstudio.com/download) for your operating system.  
If you already have a preferred text editor, skip this step.  

### Clone the github repository
- Clone or downloadhttps://github.com/dlops-io/intro_to_containers)

## Download Images Container
### Starting the Container
Type the command 
-  `cd download-images`
- Run `sh docker-shell.sh` or `docker-shell.bat` for windows

in the `download-images` directory to startup (build and run) the docker container. The container contains a Linux kernel and will install all dependencies for the image downloader. Running this command for the first time will take around 190 seconds (depending on the system you're using). This command automatically builds and runs the Docker container, where you should automatically be entered into the Linux kernel in the **app** Python virtual environment.

If you `exit` the Docker container, and run the command `docker images | grep download-images`, you'll see some nice information about the image name, tag, image ID, creation date, and size

### Running Downloader
Now that you are inside the Docker container, run the example command

`python -m cli --nums 10 --search "oyster mushrooms" "crimini mushrooms" "amanita mushrooms" --opp "search"`

`python -m cli --opp "verify"`

where 
- `nums` is the number of images to download
- `search` contains the search terms
- `opp` is the operation whether to `search` or `verify` the images

Images will be downloaded in a sub-directory named *<persistent-folder>/dataset*

## API Service Container
### Starting the Container
Type the command 
-  `cd api-service`
- Run `sh docker-shell.sh` or `docker-shell.bat` for windows

To install a new python package use `pipenv install requests` from the docker shell

To run development api service run `uvicorn_server` from the docker shell

Test the API service by going to `http://localhost:9500/`

* We want to run database-server before api-service because we want to have the API set up to connect to the database, and the API is then connected to the NGINX server, which talks with the user to get input regarding the data in the database *

## Frontend App Container
### Starting the Container
Type the command 
-  `cd frontend-app`
- Run `sh docker-shell.sh` or `docker-shell.bat` for windows

To install a new node package use `npm install <package name>` from the docker shell

To run development web server run `http-server -s` from the docker shell

Test the API service by going to `http://localhost:8080/`