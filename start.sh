#!/bin/bash

# AI-Alpha Startup Script
# This script helps you quickly start the AI-Alpha application

set -e

echo "🤖 AI-Alpha Startup Script"
echo "=========================="

# Check if Docker is available
if command -v docker &> /dev/null; then
    echo "✅ Docker is available"
    DOCKER_AVAILABLE=true
else
    echo "❌ Docker is not available"
    DOCKER_AVAILABLE=false
fi

# Check if Python is available
if command -v python3 &> /dev/null; then
    echo "✅ Python 3 is available"
    PYTHON_AVAILABLE=true
else
    echo "❌ Python 3 is not available"
    PYTHON_AVAILABLE=false
fi

echo ""

# Function to run with Docker
run_with_docker() {
    echo "🐳 Running AI-Alpha with Docker..."
    
    # Check if image exists
    if ! docker image inspect ai-alpha:latest &> /dev/null; then
        echo "📦 Building Docker image..."
        docker build -f Dockerfile_Version2.txt -t ai-alpha:latest .
    else
        echo "📦 Using existing Docker image"
    fi
    
    echo "🚀 Starting AI-Alpha container..."
    docker run --rm -p 8000:8000 ai-alpha:latest
}

# Function to run with Python
run_with_python() {
    echo "🐍 Running AI-Alpha with Python..."
    
    # Check if requirements are installed
    if ! python3 -c "import fastapi" &> /dev/null; then
        echo "📦 Installing Python dependencies..."
        python3 -m pip install -r requirements.txt
    else
        echo "📦 Python dependencies already installed"
    fi
    
    echo "🚀 Starting AI-Alpha application..."
    python3 api/app.py
}

# Ask user for preference or auto-select
if [ "$1" = "docker" ] && [ "$DOCKER_AVAILABLE" = true ]; then
    run_with_docker
elif [ "$1" = "python" ] && [ "$PYTHON_AVAILABLE" = true ]; then
    run_with_python
elif [ "$DOCKER_AVAILABLE" = true ]; then
    echo "🎯 Auto-selecting Docker (recommended)"
    run_with_docker
elif [ "$PYTHON_AVAILABLE" = true ]; then
    echo "🎯 Auto-selecting Python"
    run_with_python
else
    echo "❌ Neither Docker nor Python 3 is available!"
    echo "Please install Docker or Python 3 to run AI-Alpha"
    exit 1
fi