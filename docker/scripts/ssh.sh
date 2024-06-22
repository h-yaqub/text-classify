#!/usr/bin/env bash
# Run this command to quickly run any command in container. For example:
# `````
# ./docker/scripts/ssh.sh npm run watch
# `````
# Or
# `````
# ./docker/scripts/ssh.sh python3 test.py
# `````

if [[ $# = 0 ]]; then
	args=bash
else
	args="${@:1}"
fi

container=app

docker inspect --format={{.State.Running}} $container &> /dev/null

if [[ $? = 1 ]]; then
	docker compose run --rm --service-ports --name "$container" app $args
else
	docker exec -it $container $args
fi
