#!/bin/bash

# Run the Docker container
s docker run -d -p 5000:5000 --env-file .env --name aseprob-backend-container aseprob-backend

echo "Docker container 'aseprob-backend-container' is now running."
echo "Access the application at http://localhost:5000"
