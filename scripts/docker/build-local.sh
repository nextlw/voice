#!/bin/bash

# Build script for Mac M1/M2 (ARM64) - Native build
# This script builds a Docker image natively for ARM64 without emulation

set -e

echo "================================================"
echo "Building Docker image for Mac ARM64 (Native)"
echo "Platform: linux/arm64"
echo "================================================"

# Check if Docker is running
if ! docker info > /dev/null 2>&1; then
    echo "Error: Docker is not running. Please start Docker Desktop."
    exit 1
fi

# Image name
IMAGE_NAME=${1:-voice-chat-ai-local}
TAG=${2:-latest}

echo ""
echo "Image: $IMAGE_NAME:$TAG"
echo ""

# Build the image natively for ARM64
echo "Building Docker image for ARM64 (native - fast build)..."
echo ""

docker build \
    --tag $IMAGE_NAME:$TAG \
    --file docker/Dockerfile.local \
    .

if [ $? -eq 0 ]; then
    echo ""
    echo "✅ Build successful!"
    echo ""
    echo "Image built: $IMAGE_NAME:$TAG"
    echo ""
    echo "To run locally on your Mac:"
    echo "  docker run -d -p 8000:8000 --env-file .env --name voice-chat-local $IMAGE_NAME:$TAG"
    echo ""
    echo "To access the application:"
    echo "  http://localhost:8000"
    echo ""
    echo "⚠️  Note: This image is for local Mac use only."
    echo "For Render.com deployment, use ./scripts/docker/build-render.sh instead."
else
    echo ""
    echo "❌ Build failed!"
    echo "Please check the error messages above."
    exit 1
fi