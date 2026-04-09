from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_agentchat.messages import MultiModalMessage, TextMessage
from autogen_core import Image as AutogenImage

from PIL import Image
from io import BytesIO
import requests
from dotenv import load_dotenv, main
import asyncio
import os

load_dotenv()

#using MultiModelMessageAgent 

async def multi_model_task(question):
    openai_api_key = os.getenv("OPENAI_API_KEY")
    
    model_client = OpenAIChatCompletionClient(model="gpt-4o-mini", api_key=openai_api_key)
    
    assistant = AssistantAgent(name="Helpful_Assistant_Agent",
                                 model_client=model_client,
                                 system_message="You are a helpful assistant that provides accurate and concise answers to user queries.")  
    
    image_url = "https://picsum.photos/200/300?grayscale"
    image_response = requests.get(image_url)
    image = Image.open(BytesIO(image_response.content))
    autogen_image = AutogenImage(image)
    
    text_message = MultiModalMessage(content=[question, autogen_image], source="user")
    result = await assistant.run(task=text_message)
    print(result.messages[-1].content)
    
asyncio.run(multi_model_task('what is this image about?'))

#output: The image depicts a black and white landscape featuring a forested area and a body of water. The trees are prominent, with their reflection visible in the calm water, creating a peaceful and serene vibe typical of nature scenes. The overall aesthetic conveys tranquility and the beauty of natural surroundings.