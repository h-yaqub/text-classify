# Text Classification (Satalia)

## Tech Stack:
    - Python 3.12
    - Docker 26.1
    - Docker Compose 2.27.1

## Docker Setup

This project uses [Docker](https://www.docker.com/) and [Compose](https://docs.docker.com/compose/) to set up application environment. Docker has the advantage of creating isolated development environments. To run Docker setup, do:

    ./docker/scripts/setup.sh

The above command will build the image, create .env file if it doesn't exist, and run the necessary one-time commands to configure the environment.

Start the application container

    ./docker/scripts/run.sh

It will build the `docker` images for `app`.

Alternativley, you can bash into `app` container by running

    docker compose run --service-ports --name app --rm app bash

Bash directly into an already running `app` container by doing

    docker exec -it app bash

or you can do

    ./docker/scripts/ssh.sh

This will allow you to run any Linux command in the container.

#### All the `Docker` scripts reside in `/docker/scripts` and have the full description and usage written in them.


## Setup pre-commit

This project uses [pre-commit](https://pre-commit.com/) to ensure that code standard checks pass locally before pushing to the remote project repo. [Follow](https://pre-commit.com/#installation) the installation instructions, then set up hooks with `pre-commit install`.

Make sure everything is working correctly by running

    pre-commit run --all

### Setup pre-commit as pre-push hook

To use `pre-push` hooks with pre-commit, run:

    pre-commit install --hook-type pre-push
