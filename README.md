# AI-Alpha

AI-Alpha is a FastAPI-based AI Agent application that provides a RESTful API for AI-powered services.

## Features

- **FastAPI Framework**: Modern, fast web framework for building APIs
- **Docker Support**: Containerized deployment for easy installation
- **Health Monitoring**: Built-in health check endpoints
- **CORS Support**: Cross-origin resource sharing enabled
- **RESTful API**: Clean API endpoints for AI agent interactions

## Quick Start

### Prerequisites

- Docker (recommended)
- Python 3.11+ (for local development)
- Git

### Installation Options

#### Option 1: Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Skivi2015/AI-Alpha.git
   cd AI-Alpha
   ```

2. **Build the Docker image:**
   ```bash
   docker build -f Dockerfile_Version2.txt -t ai-alpha .
   ```

3. **Run the container:**
   ```bash
   docker run -p 8000:8000 ai-alpha
   ```

4. **Access the API:**
   - Main API: http://localhost:8000
   - Health Check: http://localhost:8000/health
   - Agent Info: http://localhost:8000/api/v1/agent
   - API Documentation: http://localhost:8000/docs

#### Option 2: Local Python Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Skivi2015/AI-Alpha.git
   cd AI-Alpha
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application:**
   ```bash
   python api/app.py
   ```

## API Endpoints

### Core Endpoints

- **GET /** - Root endpoint with API information
- **GET /health** - Health check endpoint
- **GET /api/v1/agent** - AI agent information and capabilities

### Example API Responses

**Root Endpoint (`GET /`):**
```json
{
    "message": "Welcome to AI-Alpha API",
    "version": "1.0.0",
    "status": "running"
}
```

**Health Check (`GET /health`):**
```json
{
    "status": "healthy"
}
```

**Agent Info (`GET /api/v1/agent`):**
```json
{
    "agent_name": "AI-Alpha",
    "agent_type": "General Purpose AI Agent",
    "capabilities": [
        "Natural language processing",
        "Task automation",
        "Data analysis"
    ]
}
```

## GitHub Integration

### Setting up the repository on your GitHub account

1. **Fork this repository** to your GitHub account
2. **Clone your fork:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/AI-Alpha.git
   ```

3. **Set up GitHub Actions (Optional):**
   - The repository includes CI/CD configuration
   - Push changes will trigger automated builds and tests

### Development Workflow

1. **Create a new branch for features:**
   ```bash
   git checkout -b feature/new-feature
   ```

2. **Make your changes and commit:**
   ```bash
   git add .
   git commit -m "Add new feature"
   ```

3. **Push to your fork:**
   ```bash
   git push origin feature/new-feature
   ```

4. **Create a Pull Request** on GitHub

## Configuration

### Environment Variables

You can configure the application using environment variables:

- `HOST`: Server host (default: 0.0.0.0)
- `PORT`: Server port (default: 8000)
- `LOG_LEVEL`: Logging level (default: info)

### Docker Environment

When running with Docker, you can pass environment variables:
```bash
docker run -e PORT=9000 -p 9000:9000 ai-alpha
```

## Development

### Project Structure

```
AI-Alpha/
├── api/
│   └── app.py              # Main FastAPI application
├── requirements.txt        # Python dependencies
├── Dockerfile_Version2.txt # Docker build configuration
├── .gitignore             # Git ignore patterns
├── LICENSE                # Eclipse Public License v2.0
└── README.md              # This file
```

### Adding New Features

1. **Extend the FastAPI app** in `api/app.py`
2. **Add new dependencies** to `requirements.txt` if needed
3. **Test your changes** locally before committing
4. **Update documentation** as needed

### Testing

Test the API endpoints using curl or any HTTP client:

```bash
# Test all endpoints
curl http://localhost:8000/
curl http://localhost:8000/health
curl http://localhost:8000/api/v1/agent

# View interactive API docs
open http://localhost:8000/docs
```

## Deployment

### Production Deployment

For production deployment, consider:

1. **Use environment variables** for configuration
2. **Set up reverse proxy** (nginx/apache)
3. **Configure SSL/TLS** certificates
4. **Set up monitoring** and logging
5. **Use Docker Compose** for multi-service deployment

### Docker Compose Example

Create a `docker-compose.yml` file:
```yaml
version: '3.8'
services:
  ai-alpha:
    build:
      context: .
      dockerfile: Dockerfile_Version2.txt
    ports:
      - "8000:8000"
    environment:
      - LOG_LEVEL=info
    restart: unless-stopped
```

Run with: `docker-compose up -d`

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the Eclipse Public License v2.0 - see the [LICENSE](LICENSE) file for details.

## Support

For support, please open an issue on GitHub or contact the maintainers.

---

**Getting Started in 30 seconds:**
```bash
git clone https://github.com/Skivi2015/AI-Alpha.git
cd AI-Alpha
docker build -f Dockerfile_Version2.txt -t ai-alpha .
docker run -p 8000:8000 ai-alpha
# Visit http://localhost:8000
```
