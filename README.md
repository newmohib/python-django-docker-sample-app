### Credential 
- username: admin
- password: admin
- email: admin@gmail.com

#### Make the Script Executable: Run the following command to make the script executable:

    chmod +x script.sh && ./script.sh

### run with docker
- docker build -t django-sample-app .
- docker run -p 4000:8000 django-sample-app

#### Remove all container and image
- Remove all image
- docker image rm -f $(docker image ls -q)
- Remove all container
- docker container rm -f $( docker container ls -aq )
