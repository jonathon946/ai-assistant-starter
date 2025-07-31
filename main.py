import asyncio
import os
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient

async def main():
    client = OpenAIChatCompletionClient(model="gpt-4o")
    assistant = AssistantAgent("assistant", model_client=client)
    while True:
        user_input = input("Jonathon: ")
        if user_input.strip().lower() in ("exit", "quit"):
            print("Assistant: Goodbye!")
            break
        response = await assistant.run(task=user_input)
        print("Assistant:", response)

if __name__ == "__main__":
    asyncio.run(main())
