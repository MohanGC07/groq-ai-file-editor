import os
import json
from groq import Groq
from dotenv import load_dotenv
from file_utils import read_file, write_file, append_file

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

tools = [
    {
        "type": "function",
        "function": {
            "name": "edit_selected_file",
            "description": "Modify the selected file based on instruction.",
            "parameters": {
                "type": "object",
                "properties": {
                    "operation": {
                        "type": "string",
                        "enum": ["read", "write", "append"]
                    },
                    "content": {
                        "type": "string",
                        "description": "Content to write or append"
                    }
                },
                "required": ["operation"]
            }
        }
    }
]

def run_agent(user_input, selected_file):

    system_prompt = f"""
    You are a file editing assistant.
    The user has selected this file: {selected_file}.
    You must only operate on this file.
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        tools=tools,
        tool_choice="auto"
    )

    message = response.choices[0].message

    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)

        operation = args["operation"]
        content = args.get("content", "")

        if operation == "read":
            return read_file(selected_file)

        elif operation == "write":
            return write_file(selected_file, content)

        elif operation == "append":
            return append_file(selected_file, content)

    return message.content