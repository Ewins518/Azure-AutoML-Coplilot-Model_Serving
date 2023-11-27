# Azure-AutoML-Coplilot-Model_Serving

## Overview
In this project, we used Azure AutoML Copilot to train and deploy the best model as micro-service using Azure container.
Then we consumed this service with a web application.

![Screenshot](/screenshot/1.png)
![Screenshot](/screenshot/2.png)

You can see the link here (*REST Endpoint*), that we'll use to consume this service:
![Screenshot](/screenshot/3.png)


## How to run this project?

*You have to do the training and deployement with Azure AutoML copilot before run this*

1. Clone this repository to your local machine:

```bash
git clone git@github.com:Ewins518/Azure-AutoML-Coplilot-Model_Serving.git
```

2. Navigate to the project directory:

```bash
cd Azure-AutoML-Coplilot-Model_Serving
```

Replace the url in *weather_app.py* by yours.

3. Build the docker image

```bash
docker build -t inference .
```

4. Run a container of this image locally

When the image construction is finished,execute this command to run a container

```bash
docker run -d -p 5000:5000 --name weathercontainer inference
```

5. You can if your container is running by execute this command
```bash
docker ps
```
6. Fianlly, open your web browser and visit http://localhost:5000 to access the application.

You should this :

![Screenshot](/screenshot/4.png)
