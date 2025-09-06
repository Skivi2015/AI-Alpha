"""
AI-Alpha: AI Agent FastAPI Application
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI(
    title="AI-Alpha",
    description="AI Agent API",
    version="1.0.0"
)

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    """Root endpoint returning basic API information."""
    return {
        "message": "Welcome to AI-Alpha API",
        "version": "1.0.0",
        "status": "running"
    }

@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy"}

@app.get("/api/v1/agent")
async def get_agent_info():
    """Get AI agent information."""
    return {
        "agent_name": "AI-Alpha",
        "agent_type": "General Purpose AI Agent",
        "capabilities": [
            "Natural language processing",
            "Task automation",
            "Data analysis"
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)