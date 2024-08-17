#!/bin/bash
docker run -d \
  --name mongodb \
  -v $(pwd)/mongo-data:/data/db \
  -p 27017:27017 \
  mongo:latest