from google.adk.agents.llm_agent import Agent

from dotenv import load_dotenv
from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import FunctionTool
from ddgs import DDGS
from typing import List

load_dotenv()

model = LiteLlm(
    model="groq/qwen/qwen3-32b",  # use "groq/<groq-model-name>"
)


def duckduckgo_search(query: str) -> List:
    """
    input: str
    output: List
    Perform a web search using DuckDuckGo.
    """
    results = DDGS().text(query, max_results=5)
    return results

ddg_search_tool = FunctionTool(func=duckduckgo_search)

research_agent = Agent(
    name="research_agent",
    model=model,
    description="This agent does research.",
    instruction="""
    You are a helpful assistant that does research by using the 'duckduckgo_search' tool.
    """,
    tools=[ddg_search_tool],
    output_key="research",
)


mythology_agent = Agent(
    name="mythology_agent",
    model=model,
    description="This agent answers mythology questions.",
    instruction="""
    You are a helpful assistant that answers mythology questions by using the 'duckduckgo_search' tool.
    """,
    tools=[ddg_search_tool],
    output_key="mythology",
)



supervisor_agent = Agent(
    name="supervisor_agent",
    model=model,
    description="This agent supervises the user.",
    instruction="""
    You are a helpful assistant that supervises the two agents and generate final response from their outputs.
    """,
    sub_agents=[mythology_agent, research_agent],
)


root_agent = supervisor_agent