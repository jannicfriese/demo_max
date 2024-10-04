# Sample docker fastapi app

## Setup
1. Install docker
2. Build the image
From [this directory](.) run the following command
```bash
docker build -t fastapi-sample .
```
3. Run the container
```bash
docker run -p 8000:8000 fastapi-sample
```
4. Open your browser and go to `http://localhost:8000/redoc`
