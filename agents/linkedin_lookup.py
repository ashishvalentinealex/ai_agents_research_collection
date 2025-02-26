import os 
import sys 
import re
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# print("sys.path:", sys.path)  # Debugging: Print all paths

# Get the absolute path of the project root
ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Add it to sys.path if not already present
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)  # Use insert(0, ...) to prioritize it


from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
#tool 
# from tools.tools import get_profile_url_tavily
from langchain_core.tools import Tool


#Agent
from langchain.agents import (
    create_react_agent,   #XMl,self ask and 
    AgentExecutor,
)
from langchain import hub

#Search
from tools.tools import get_profile_url_tavily

load_dotenv()
openapi_key = os.getenv("OPENAI_API_KEY")


def lookup(name:str)-> str :      # This function will take name as string and give a string
    llm = ChatOpenAI(temperature=0,
                     model="gpt-4o-mini-2024-07-18")
    
# PROMPT TEMPLATE 
    template = """Given the full name {name_of_person}, find their LinkedIn profile.
Only return the **single most relevant LinkedIn URL**. Do not include any explanation, reasoning, or extra text.  
Just return the URL itself, nothing else."""

    
    prompt_template = PromptTemplate(template=template, input_variables=["name_of_person"])
    tools_for_agents = [
        Tool(name="crawl Google 4 Linkedin profile page",
             func=get_profile_url_tavily,
             description="useful for when you need get the Linkedin page URL",)
    ]

    react_prompt = hub.pull("hwchase17/react")
    # react_prompt = prompt_template
    agent = create_react_agent(llm=llm, tools=tools_for_agents, prompt=react_prompt)
    agent_executor = AgentExecutor(agent=agent,tools=tools_for_agents,verbose=True, handle_parsing_errors=True)

    result  = agent_executor.invoke(
        input={"input":prompt_template.format_prompt(name_of_person=name)}
    )

    linkedin_profile = result["output"]

    match = re.search(r"https?://[^\s]+linkedin\.com/[^\s]+", linkedin_profile)
    linkedin_profile = match.group(0) if match else "No valid LinkedIn URL found."
    return linkedin_profile


    # return "https://www.linkedin.com/in/ashish-valentine-732ab2147/"

# if __name__ == "__main__":
#     linkedin_url = lookup(name="Ashish Valentine Alex, AI Engineer")
#     print(linkedin_url)