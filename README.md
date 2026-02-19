[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


Offline multi-agent debate simulator using **Ollama** + local LLMs (Llama 3.2 example).

Watch **Fang Yuan** (Reverend Insanity) and **Klein Moretti** (Lord of the Mysteries) argue about sacrifice, power, morality, and egoism — fully local, no API costs, no internet needed after model download.

## Features
- 100% offline roleplay with local LLMs via Ollama
- Strict character personas with short, sharp replies
- Automatic history trimming to avoid context overflow
- Easy to swap characters / add new personas
- Debate any topic you want

## Quick Start

1. Install Ollama → https://ollama.com
2. Pull model:  
   ```bash
   ollama pull llama3.2
Run the script: Bash python debate.py

Example Output
text🔥 DEBATE TOPIC: Is it better to sacrifice yourself to save the world, or sacrifice the world to save yourself? 🔥

--- ROUND 1 ---
💀 FANG YUAN: Sacrificing yourself is pathetic. The strong survive by consuming the weak. I'd burn the world if it bought me immortality.

🧐 KLEIN MORETTI: That's the logic of a monster. Some things — love, duty, the innocent — are worth more than survival.
Requirements

Python 3.8+
Ollama running locally
requests library (pip install requests)
