# data-upload
Data upload microservice.

### API

"message": "The data value transmitted exceeds the capacity limit.", 413 REQUEST ENTITY TOO LARGE

### Docker

#### Build and run the app.

Build the image:
`docker build -t data-upload-microservice:latest ./app/`

Run the container as deamon on port 5000:
`docker run -d -p 5000:5000 data-upload-microservice`

### Push the image to DockerHub
- docker tag 3db6288b6b26 leon11sj/data-upload-microservice:version-1.0.0
- docker push leon11sj/data-upload-microservice


#### TODOji
- dodaj host pri app zagonu v konfig, localhost, izven dockerja, 0.0.0.0 v dockerju


#### Dodatno
- pip install pytest-flake8
- pytest --flake8