#!/usr/bin/env bash
# Setup, Build and Run Application.
# `````
# ./docker/scripts/run.sh
# `````

./docker/scripts/setup.sh

# Verify Dataset and Download if not any
echo "Verifying Dataset..."
docker compose run app python3 core/download_data.py

# Running App
echo "Running App..."
docker compose up
