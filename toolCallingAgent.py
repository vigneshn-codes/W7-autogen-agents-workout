from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()

async def getWeather(city: str) -> str:
    return f"Weather in {city} is sunny with a high of 25°C and a low of 15°C."

async def main(question):
    # Load the OpenAI API key from environment variables
    api_key = os.getenv("OPENAI_API_KEY")

    # Initialize the model client with the specified model and API key
    model_client = OpenAIChatCompletionClient(
        model="gpt-4o-mini", 
        api_key=api_key
    )

    # Create an instance of the AssistantAgent with the model client
    assistant = AssistantAgent(name="Helpful_Assistant_Agent", 
                               model_client=model_client,
                               system_message="You are a helpful assistant that provides accurate and concise answers to user queries.",
                               tools=[getWeather])
    
        # Run the assistant with a specific task and print the result
    result = await assistant.run(task=question)

    print(result.messages[-1].content)

asyncio.run(main("What is the weather in Bangalore?"))

#output: Weather in Bangalore is sunny with a high of 25°C and a low of 15°C.