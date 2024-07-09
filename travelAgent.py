import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits.load_tools import load_tools
from langchain.agents import initialize_agent

# Carregando o modelo GPT-3.5 Turbo da OpenAI
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Carregando as ferramentas "duckduckgo-search" e "wikipedia"
tools = load_tools(["ddg-search", "wikipedia"], llm=llm)

# Imprimindo o nome e a descrição da ferramenta "ddg-search"
# print(tools[0].name, tools[0].description)

# Imprimindo o nome e a descrição da ferramenta "wikipedia"
# print(tools[1].name, tools[1].description)

# Inicializando o agente "zero-shot-react-description"
agent = initialize_agent(
    tools,
    llm,
    agent= 'zero-shot-react-description',
    verbose = True
)

# Imprimindo o template de prompt da cadeia LLM do agente
#print(agent.agent.llm_chain.prompt.template)

# Definindo uma query
query = """
Vou viajar para Londres em agosto de 2024. Quero que faça um roteiro de viagem para mim com os eventos que irão ocorrer na data da viagem e com o preço da passagem de São Paulo para Londres.
"""

agent.run(query)