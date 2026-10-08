from dotenv import load_dotenv
from typing import List
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from tavily import TavilyClient
from pydantic import BaseModel ,Field
tavily=TavilyClient()

load_dotenv()
@tool
def search (query : str) -> str :
    """
    tool that Searches over internet
    Args :
        query : the query to search for it 
    Returns :
        the search result  
    """
    print(f"Searching for {query}")
    return tavily.search(query=query)

class source (BaseModel) :
    """schema for a source used by the agent"""
    url:str = Field(description="The url of the Source")

class AgentResponse(BaseModel):
    """Schema for Agent response with Anwers and Sources"""
    answer:str=Field(description="The Agent Answer to the query")
    sourcs:List[source]= Field(default_factory=List ,description="List of sources used by the agent to generate the answer ") 

llm =ChatOpenAI()
tools=[search]
agent= create_agent(model=llm ,tools=tools,response_format=AgentResponse)

def main() :
    print("Hello from Langchain-course")
    result=agent.invoke({"messages":HumanMessage(content="search for 3 job postings for an ai engineer using langchain in the bay area on linkedin and list their details?")})
    print(result)

if __name__ == "__main__":
    main()