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
