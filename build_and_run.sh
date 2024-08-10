#!/bin/bash

# Build the Docker image
./build.sh

# Check if the build was successful
if [ $? -eq 0 ]; then
    echo "Build successful. Running the container..."
    
    # Check if a container with the same name is already running
    if [ "$(docker ps -q -f name=aseprob-backend-container)" ]; then
        echo "Container 'aseprob-backend-container' is already running. Stopping it..."
        docker stop aseprob-backend-container
        docker rm aseprob-backend-container
    fi
    
    # Run the Docker container
    ./run.sh
else
    echo "Build failed. Please check the errors above."
fi