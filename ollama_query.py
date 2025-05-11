import subprocess

def run_ollama(prompt: str, model: str = "mistral") -> str:
    command = ["ollama", "run", model]
    try:
        result = subprocess.run(
            command,
            input=prompt.encode("utf-8"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=60
        )
        return result.stdout.decode("utf-8").strip()
    except Exception as e:
        return f"Error running model: {e}"

def compress_chat(chat: str):
    from prompts import summary_prompt, instruction_prompt, tone_prompt

    summary = run_ollama(summary_prompt.format(chat=chat))
    instructions = run_ollama(instruction_prompt.format(chat=chat))
    tone = run_ollama(tone_prompt.format(chat=chat))

    return {
        "summary": summary,
        "instructions": instructions,
        "tone": tone
    }
