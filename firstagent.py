from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def main():
    # Load the OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the model client with the specified model and API key
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=api_key)

    # Create an instance of the AssistantAgent with the model client
    assistant = AssistantAgent(name='Assistant', model_client=model_client)

    # Run the assistant with a specific task and print the result
    result = await assistant.run(task="What is the capital of France?")

    print(result.messages[-1].content)

asyncio.run(main())
