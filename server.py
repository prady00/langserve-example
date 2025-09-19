from fastapi import FastAPI
from langserve import add_routes

from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

app = FastAPI()

model = ChatOpenAI(model="gpt-4o-mini")
prompt = ChatPromptTemplate.from_template("Say hello to {name}")
chain = prompt | model

add_routes(app, chain, path="/hello")
