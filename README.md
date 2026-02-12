# LangChain Chatbot Project

A chatbot built with LangChain, LangGraph, LangSmith, and MCP tools.

## Setup

1. Create virtual environment using conda yaml file:
   ```bash
   conda env create -f environment.yaml
   cond activate <name of conda environment> # Here name: Chatbot
   ```

3. Configure environment file (.env):
   ```bash
   - create .env file
   - copy paste the all the variables from env_example file to .env file
   - edit .env and add your API keys
   ```

4. Run the application:
   ```bash
   python -m src.frontend.app
   ```

## Project Structure
