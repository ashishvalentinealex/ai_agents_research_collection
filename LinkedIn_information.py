import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain 
from dotenv import load_dotenv

from third_parties.linkedin import scrape_linkedin_profile 
from agents.linkedin_lookup import lookup as linkedin_lookup_agent

def get_linkedin_info(name:str) -> str:
   linkedin_username = linkedin_lookup_agent(name=name)
   linkedin_data = scrape_linkedin_profile(linkedin_profile=linkedin_username)

   prompt_template = """
You are an expert profile summarizer. Given the LinkedIn information {information} about a person, generate the following:

1. A Compelling Short Summary (3-4 sentences)  
   - Capture their profession, key skills, and achievements.  
   - Highlight what makes them unique or outstanding.  
   - Maintain a professional yet engaging tone.  

2. Two Interesting Facts About Them 
   - These should be unique, engaging, and insightful.  
   - They can be about their career, achievements, personal branding, or impact.  

3. Potential Conversation Starters (2-3 Points)
   - Provide engaging questions or topics one could use to start a conversation with this person.  
   - These should be based on their interests, skills, or past work.  

4. Key Strengths & Skills (Bullet Points)
   - Summarize their core competencies and expertise.  
   - Keep this concise but impactful.  

Make the response structured, natural, and engaging, as if a career expert wrote it.  
"""
   summary_prompt_template = PromptTemplate(input_variables=["information"],
                                             template=prompt_template
                                             )
   llm = LLMChain(llm=OpenAI(), prompt=summary_prompt_template)
   chain = summary_prompt_template | llm 
   # linkedin_data = scrape_linkedin_profile(linkedin_profile="hello world",
   #    mock=True
   # )

   res = chain.invoke(input={"information": linkedin_data})

   print("\n")
   print(res["text"])





if __name__ == "__main__":
   load_dotenv()
   openai_api = os.getenv("OPENAI_API_KEY")
   get_linkedin_info(name="Anushree Kose, Pipra Solutions")


    
    

    
    
    
    
