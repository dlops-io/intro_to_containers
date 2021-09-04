SET IMAGE_NAME="api-server"
SET BASE_DIR= %cd%
cd ..
cd persistent-folder
SET PERSISTENT_DIR= %cd%
cd ..
cd api-service

docker build -t %IMAGE_NAME% -f Dockerfile .
cd ..
docker run  --rm --name %IMAGE_NAME% -ti ^
            --mount type=bind,source="%cd%\api-service",target=/app ^
            --mount type=bind,source="%cd%\persistent-folder",target=/persistent ^
            -p 9500:9000 -e DEV=1 %IMAGE_NAME%
