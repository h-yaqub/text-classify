#!/usr/bin/env bash
# Setup application.
# `````
# ./docker/scripts/setup.sh
# `````

# Copy sample env if does not exist
echo "Setting Up..."
[ ! -f .env ] && cp env.sample .env

# Run App
echo "Building App..."
if [[ $(arch) = 'aarm64' ]]; then
	# We will force the docker to install Intel images. Then Apple M1 will use Rosetta to translate
	# Intel instructions to arm instructions.
	docker compose build --build-arg platform=linux/amd64
else
	docker compose build
fi
