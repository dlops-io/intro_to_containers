#!/bin/bash

# exit immediately if a command exits with a non-zero status
set -e

# Define some environement variables
#  Automatic export to the environment of subsequently executed commands
# source: the command 'help export' run in Terminal
export IMAGE_NAME="api-server"
export BASE_DIR=$(pwd)
export PERSISTENT_DIR=$(pwd)/../persistent-folder/

# build the image based on the Dockerfile
docker build -t $IMAGE_NAME -f Dockerfile .

# create the container
# --mount: Attach a filesystem mount to the container
# -p: Publish a container's port(s) to the host (host_port: container_port) (source: https://dockerlabs.collabnix.com/intermediate/networking/ExposingContainerPort.html)
# -e: set environment variables
docker run --rm --name $IMAGE_NAME -ti \
--mount type=bind,source="$BASE_DIR",target=/app \
--mount type=bind,source="$PERSISTENT_DIR",target=/persistent \
-p 9500:9000 \
-e DEV=1 $IMAGE_NAME