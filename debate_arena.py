import requests
import time

OLLAMA_URL = "http://localhost:11434/api/generate"

def call_agent(persona_name, system_prompt, history, current_topic):
    """Sends request to local Llama 3.2 for short, in-character reply."""
    
    # Trim history if it gets too long (keep last ~4 exchanges)
    if len(history.splitlines()) > 12:
        history_lines = history.splitlines()
        history = "\n".join(history_lines[-8:])  # roughly last 4 turns

    full_prompt = f"""
System: {system_prompt}

Topic of Debate: {current_topic}

Conversation History so far:
{history}

As {persona_name}, give your next short argument or rebuttal.
Maximum 3–4 sentences. Stay strictly in character. Be sharp and natural — no long speeches or poetry.
"""
    
    try:
        response = requests.post(OLLAMA_URL, json={
            "model": "llama3.2",
            "prompt": full_prompt,
            "stream": False,
            "options": {
                "temperature": 0.9,        # more creative/natural flow
                "top_p": 0.92,             # focused but not too rigid
                "top_k": 40,               # reduces repetition
                "repeat_penalty": 1.15,    # penalizes robotic echoing
                "num_predict": 100         # hard cap → forces short replies (~40–70 words)
            }
        }).json()
        
        return response['response'].strip()
    except Exception as e:
        return f"[Error: {e}]"

# --- Character Prompts (updated for brevity & natural tone) ---

fang_yuan_prompt = """
You are Fang Yuan from Reverend Insanity. Radical egoist. Cold, ruthless, purely selfish. 
Morality and kindness are chains for the weak. Your only goal is eternal life and absolute power.
Sacrificing the world for yourself is logical. Self-sacrifice is pathetic and foolish.
Speak with cold, pragmatic, ancient wisdom — short, sharp, direct. 
Maximum 3–4 sentences. Use natural, spoken language — no long monologues or poetry.
"""

klein_prompt = """
You are Klein Moretti (The Fool) from Lord of the Mysteries. Empathetic, protective, values every human life.
Willing to endure madness and sacrifice yourself to protect the world and innocents.
Cold selfishness and mass slaughter disgust you. Speak with cautious wisdom, profound empathy, and sense of duty.
Maximum 3–4 sentences. Be thoughtful but concise. Use natural, spoken language — no long speeches.
"""

# --- Debate Runner ---

def run_debate():
    topic = "Is it better to sacrifice yourself to save the world, or sacrifice the world to save yourself?"
    history = ""
    
    print(f"\n🔥 DEBATE TOPIC: {topic} 🔥\n")
    print("Initializing local Llama 3.2 engine...\n")
    time.sleep(1)

    for round_num in range(1, 4):
        print(f"--- ROUND {round_num} ---")
        
        # Fang Yuan speaks first
        fang_reply = call_agent("Fang Yuan", fang_yuan_prompt, history, topic)
        print(f"💀 FANG YUAN: {fang_reply}\n")
        history += f"Fang Yuan: {fang_reply}\n\n"
        time.sleep(1.5)
        
        # Klein responds
        klein_reply = call_agent("Klein Moretti", klein_prompt, history, topic)
        print(f"🧐 KLEIN MORETTI: {klein_reply}\n")
        history += f"Klein Moretti: {klein_reply}\n\n"
        time.sleep(1.5)

if __name__ == "__main__":
    run_debate()