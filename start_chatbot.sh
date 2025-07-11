#!/bin/bash

# Stack Overflow QA Visual Chatbot Startup Script

echo "🤖 Starting Stack Overflow QA Visual Chatbot..."
echo "================================================"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv venv
fi

# Activate virtual environment
echo "Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Check for .env file
if [ ! -f "Chatbot/.env" ]; then
    echo "⚠️  Warning: No .env file found!"
    echo "📝 Please copy Chatbot/.env.example to Chatbot/.env and add your OpenAI API key"
    echo ""
fi

# Start the Flask application
echo "🚀 Starting the visual chatbot server..."
echo "📍 Open http://localhost:5000 in your browser"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

cd Chatbot && python3 app.py