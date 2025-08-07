#!/bin/bash

# Build script for Render.com deployment
# This script builds a Docker image for linux/amd64 platform (required by Render.com)
# Compatible with Mac M1/M2 (ARM64) development machines

set -e

echo "================================================"
echo "Building Docker image for Render.com deployment"
echo "Platform: linux/amd64"
echo "================================================"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker Desktop."
    exit 1
fi

# Check if buildx is available
if ! docker buildx version > /dev/null 2>&1; then
    echo "Error: Docker buildx is not available. Please update Docker Desktop."
    exit 1
fi

# Image name
IMAGE_NAME=${1:-voice-chat-ai-render}
TAG=${2:-latest}

echo ""
echo "Image: $IMAGE_NAME:$TAG"
echo ""

# Create and use buildx builder if it doesn't exist
if ! docker buildx ls | grep -q "multiplatform"; then
    echo "Creating buildx builder for multi-platform builds..."
    docker buildx create --name multiplatform --use
else
    echo "Using existing buildx builder..."
    docker buildx use multiplatform
fi

# Build the image for linux/amd64
echo ""
echo "Building Docker image for linux/amd64..."
echo "This may take several minutes on ARM64 machines due to emulation..."
echo ""

docker buildx build \
    --platform linux/amd64 \
    --tag $IMAGE_NAME:$TAG \
    --file docker/Dockerfile.render \
    --load \
    .

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful!"
    echo ""
    echo "Image built: $IMAGE_NAME:$TAG"
    echo ""
    echo "To test locally (will run under emulation on ARM64):"
    echo "  docker run -d -p 8000:8000 --env-file .env --name voice-chat-test --platform linux/amd64 $IMAGE_NAME:$TAG"
    echo ""
    echo "To push to Docker Hub for Render deployment:"
    echo "  docker tag $IMAGE_NAME:$TAG your-dockerhub-username/$IMAGE_NAME:$TAG"
    echo "  docker push your-dockerhub-username/$IMAGE_NAME:$TAG"
    echo ""
    echo "For Render.com deployment:"
    echo "  1. Push image to Docker Hub or other registry"
    echo "  2. Use the image URL in Render's Docker deployment"
    echo "  3. Set environment variables in Render dashboard"
else
    echo ""
    echo "❌ Build failed!"
    echo "Please check the error messages above."
    exit 1
fi