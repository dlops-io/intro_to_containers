#!/bin/bash

# `set -e` will exit immediately if a command exits with a non-zero status
set -e

# Define some environement variables
#  Automatic export to the environment of subsequently executed commands
# source: the command 'help export' run in Terminal
export IMAGE_NAME="download-images"
export BASE_DIR=$(pwd)
export PERSISTENT_DIR=$(pwd)/../persistent-folder/

# `docker build` is saying to build a Docker image
docker build -t $IMAGE_NAME -f Dockerfile .

# `docker run` is specifying to run a Docker container
docker run --rm --name $IMAGE_NAME -ti \
--mount type=bind,source="$BASE_DIR",target=/app \
--mount type=bind,source="$PERSISTENT_DIR",target=/persistent $IMAGE_NAME