summary_prompt = """Summarize the key ideas, topics, or goals discussed in this conversation.
Avoid explaining the assistant's capabilities or system behavior — just focus on the content of the chat.

CHAT:
{chat}
"""
instruction_prompt = """You are a task extraction assistant.

From the following chat conversation, extract clear and specific **action items** or **instructions** given to the user.
These should be phrased as direct, executable steps.

- Avoid describing the goal of this task.
- Do not reflect on your own role or summarization process.
- Just return the instructions mentioned in the chat, in bullet points.

CHAT:
{chat}
"""

tone_prompt = "Analyze the tone and style of this conversation (e.g., formal, casual, angry):\n\n{chat}"
