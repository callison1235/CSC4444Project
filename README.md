# CSC4444Project

## Introduction
This is an AI Agent designed to teach new employees at different restaurants. Designed using Ollama as the LLM allows for well thought and desriptive responses.

## Prerequisites
Python 3.13.3
Ensure you have microsoft tools c++ 14.0 or above installed or the dependencies will not install properly. 
When you run the pip install command later, there will be an error message telling you how if necessary

Download Ollama locally to your computer. https://ollama.com/
Once downloaded, run the .exe file to install.
After installation run these two commands in your command prompt:

- ollama pull llama3.2
- ollama pull mxbai-embed-large

## Getting Started
Run the command: python -m venv venv to initiate virtual environment

- Windows: ./venv/Scripts/activate initiates the virtual environment
- Linux/macOS: ./venv/bin/activate initiates the virtual environment

pip install -r .\requirements.txt allows installation of the required LLM features and dependencies

## Usage
- Windows: python .\main.py
- Linux/macOS: python3 .\main.py

You must prompt the agent using one of the following restaurant names:
- Sapphire Bistro
- Golden Dragon Palace
- Bella Napoli
- Moonlight Grill
- Spice Avenue
- Taco Fiesta
- Sakura Sushi
- Olive & Vine
- Paris Brasserie
- Smokehouse BBQ
- Mumbai Spice
- El Ranchero
- Bamboo Garden
- The Hungry Owl
- Pasta Paradise
- Copenhagen
- Texas Roadhouse
- Fusion Kitchen
- Mamma Mia
- Le Petit Château

The agent will prompt a user to ask questions regarding their new job at whichever restaurant is selected.

## Authors
    - Christian Allison
    - John Braham