SET IMAGE_NAME="download-images"
SET BASE_DIR= %cd%
cd ..
cd persistent-folder
SET PERSISTENT_DIR= %cd%
cd ..
cd download-images

docker build -t %IMAGE_NAME% -f Dockerfile .
cd ..
docker run  --rm --name %IMAGE_NAME% -ti ^
            --mount type=bind,source="%cd%\download-images",target=/app ^
            --mount type=bind,source="%cd%\persistent-folder",target=/persistent %IMAGE_NAME%
