# deploy_ml_model
Prototype for deploying a machine learning model inside docker container using Fask

## Informations utiles

This project allows you to deploy a machine learning model in a docker container using the Flask library

### example_model.py

```
The example_model.py file contains the trained model as well as an instruction which allows to save the model in pickle format.
So it is mandatory to run this intruction to ensure that the pickle file will be in the container.
```
### fask_deployement.py
```
This file contains the endpoints needed to make predections.

We have :
* @app.route("/test/prediction") : which allows to test with default values

* @app.route("/predict", methods = ["POST", "GET"]) : which allows you to make predictions based on inputs. Exemple : http://127.0.0.1:5000/predict?x=[3,4,4,4]
```

### The container

### Build the image
```
docker build -t ml_deploy:latest .
```

### Checking the image construction
```
docker images
```

### Run the container
```
docker run -it --rm -p 5000:5000 ml_deploy
```


## Example
* If you launched it locally :
  http://127.0.0.1:5000/predict?x=[3,4,4,4], http://127.0.0.1:5000/test/prediction, http://127.0.0.1:5000/
* Otherwise use the machine's ip address with the port to which you have 'bound' the port of flask (5000) 


