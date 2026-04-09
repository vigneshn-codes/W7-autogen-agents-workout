from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from dotenv import load_dotenv
import asyncio
import os
import requests
import json
load_dotenv()

async def main(question):
    openRouter_api_key = os.getenv("OPENROUTER_API_KEY")
    
    open_router_client = OpenAIChatCompletionClient(
        base_url="https://openrouter.ai/api/v1",
        model="mistralai/mistral-small-3.2-24b-instruct",
        api_key=openRouter_api_key,
        
        model_info={
            "family": "mistral",
            "vision": True,
            "function_calling": True,
            "json_output": True,
            "structured_output": True
        },
        # extra_headers={
        #     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
        #     "X-OpenRouter-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
        # },
    )
    assistant = AssistantAgent(name="Helpful_Assistant_Agent", 
                               model_client=open_router_client,
                               system_message="You are a helpful assistant that provides accurate and concise answers to user queries.")
    result = await assistant.run(task=question)
    print(result.messages[-1].content)

asyncio.run(main('Tell me about Autogen?'))