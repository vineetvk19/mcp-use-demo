# MCP-Use LLM Agent Demo

A demonstration of implementing an LLM Agent with tool access using MCP-Use and Groq.

## Features

- Integration with Groq's LLMs
- Tool access via MCP (Model Context Protocol)
- Web search capabilities using Brave Search API
- Conversation memory for context-aware responses
- Interactive chat interface

## Prerequisites

- Python 3.8+
- Node.js (for running certain MCP servers)
- Groq API key
- Brave Search API key

## Installation

1. Clone this repository
   ```bash
   git clone https://github.com/vineetvk19/mcp-use-demo.git
   cd mcp-use-demo

Set up a virtual environment
bashuv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install dependencies
bashuv add mcp-use langchain-groq python-dotenv

Create environment files:

Create a .env file with your Groq API key
Create a mcp.json file with your Brave Search API configuration



Usage
Run the application:
bashuv run app.py
Project Structure
mcp-use-demo/
├── app.py              # Main application file
├── mcp.json            # MCP server configuration
├── .env                # Environment variables (not in repo)
├── .gitignore          # Git ignore file
└── README.md           # This file
License
MIT License
Acknowledgments

Based on the tutorial by Arham Islam (May 2025)
Uses the MCP-Use library
Powered by Groq's LLMs and Brave Search
