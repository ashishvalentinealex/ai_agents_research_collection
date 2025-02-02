import os 
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
#tool 
from langchain_core.tools import Tool  
from langchain.agents import (
    create_react_agent,   #XMl,self ask and 
    AgentExecutor,
)
from langchain import hub

load_dotenv()
openapi_key = os.getenv("OPENAI_API_KEY")


def lookup(name:str)-> str :      # This function will take name as string and give a string
    llm = ChatOpenAI(temperature=0,
                     model="gpt-4o-mini-2024-07-18")
    
# PROMPT TEMPLATE 
    template = """given the full name {name_of_person} I want you to get me a link to their Linkedin profile page. 
                Your answer should contain only a URL"""
    
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
    tools_for_agents = [
        Tool(name="crawl Google 4 Linkedin profile page",
             func="?",
             description="useful for when you need get the Linkedin page URL",)
    ]

    react_prompt = hub.pull("hwchase17/react")
    agent = create_react_agent(llm=llm, tools=tools_for_agents, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agents,verbose=True)

    result  = agent_executor.invoke()


    return "https://www.linkedin.com/in/ashish-valentine-732ab2147/"