from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import TextMessage
from dotenv import load_dotenv
import asyncio
import os
import requests
import json
load_dotenv()

#using TextMessage 

async def main(question):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=openai_api_key)
    
    assistant = AssistantAgent(name="Helpful_Assistant_Agent",
                                 model_client=model_client,
                                 system_message="You are a helpful assistant that provides accurate and concise answers to user queries.")  
    
    text_message = TextMessage(content=question, source="user")
    result = await assistant.run(task=text_message)
    print(result.messages[-1].content)
    
asyncio.run(main('Tell me about Autogen?'))

#output: "Autogen" can refer to various concepts or tools depending on the context, but commonly, it is associated with automated generation processes in software development, data generation, or documentation.

# 1. **Software Development**: In programming, Autogen often refers to tools or libraries that automatically generate code or configuration files based on certain inputs or templates. This can simplify and speed up development tasks.

# 2. **Documentation Generation**: It may also refer to automated documentation tools that generate readable documents from source code comments or annotations, such as Doxygen or Sphinx.

# 3. **Data Generation**: In data science, Autogen might relate to tools that create synthetic data sets for testing purposes.

# If you have a specific context or a different reference for "Autogen" in mind, please let me know!