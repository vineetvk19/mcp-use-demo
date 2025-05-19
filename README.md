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

2. Set up a virtual environment
   ```bash
   bashuv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate

3. Install dependencies
   ```bash
   bashuv add mcp-use langchain-groq python-dotenv

## Create environment files:

- Create a .env file with your Groq API key
- Create a mcp.json file with your Brave Search API configuration
  ```bash
  {
  "mcpServers": {
    "brave-search": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-brave-search"
      ],
      "env": {
        "BRAVE_API_KEY": "<BRAVE-API-KEY>"
      }
    }
  }


## Usage
Run the application:
   ```bash
   bashuv run app.py


