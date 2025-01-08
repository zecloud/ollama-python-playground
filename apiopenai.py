from openai import AsyncOpenAI
import chainlit as cl
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain.schema import StrOutputParser
from langchain.schema.runnable import Runnable
from langchain.schema.runnable.config import RunnableConfig
from typing import cast
#client = AsyncOpenAI(base_url="http://localhost:1234/v1", api_key="lm-studio")



MODEL_NAME = "phi3:mini"

client = AsyncOpenAI(
    base_url="http://localhost:11434/v1",
    api_key="nokeyneeded",
)
# Instrument the OpenAI client
cl.instrument_openai()
settings = {

    "model":MODEL_NAME,
    "temperature": 0.7,
    "n":1,
    # ... more settings
}
MODEL_NAME





@cl.on_message
async def on_message(message: cl.Message):
    response = await client.chat.completions.create(
        messages=[
            {
                "content": "You are a helpful bot, you always reply in French",
                "role": "system"
            },
            {
                "content": message.content,
                "role": "user"
            }
        ],
        **settings
    )
    await cl.Message(content=response.choices[0].message.content).send()
