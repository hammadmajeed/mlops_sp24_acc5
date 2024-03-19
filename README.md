## MongoDB connection URI with authentication
    uri = f"mongodb://{username}:{password}@localhost:27017/?{auth_source}"


You are connecting to localhost:27017 within your app container - that’s not you host‘s localhost, but the one inside the container.

And as containers are about isolation, that way you can’t connect to other services.

Use the service name instead mongodb:27017, as Docker DNS makes the containers automatically available by their service name.

## Correct MongoDB connection URI with authentication
    uri = f"mongodb://{username}:{password}@mongodb:27017/?{auth_source}"

##  $ echo "mypassword" | docker secret create my_secret -

This command will create a new secret called my_secret, containing the password “mypassword.” Notice the use of the — at the end of the command, which tells Docker to read the secret’s value from standard input instead of a file

## Using environment variable for secret management 

Within docker-compose.yml, you can specify a file that contains the environment variables for the container:

 env_file:
- .env

Make sure to add .env to .gitignore, then set the credentials within the .env file like:

SOME_USERNAME=myUser

SOME_PWD_VAR=myPwd

Store the .env file locally or in a secure location where the rest of the team can grab it.