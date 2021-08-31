# Introduction to Development using Containers

## Prerequisites
---
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
---
### Starting the Container
Type the command 
-  `cd download-images`
- Run `sh docker-shell.sh` or `docker-shell.bat` for windows

in the project directory to startup (build and run) the docker container. The container contains a Linux kernel and will install all dependencies for the image downloader. Running this command for the first time will take around 190 seconds (depending on the system you're using). This command automatically builds and runs the Docker container, where you should automatically be entered into the Linux kernel in the **app** Python virtual environment.

If you `exit` the Docker container, and run the command `docker images | grep download-images`, you'll see some nice information about the image name, tag, image ID, creation date, and size

### Running Downloader
Now that you are inside the Docker container, run the example command

`python -m cli --nums 10 --search "oyster mushrooms" "crimini mushrooms" "amanita mushrooms" --opp "search"`

`python -m cli --opp "verify"`

where 
- `nums` is the number of images to download
- `search` contains the search terms
- `opp` is the operation whether to `search` or `verify` the images

Images will be downloaded in a sub-directory named *dataset* within the project directory