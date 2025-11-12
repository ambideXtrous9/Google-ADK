from google.adk.agents.llm_agent import Agent
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from dotenv import load_dotenv
from google.adk.tools import google_search
from google.adk.models.lite_llm import LiteLlm
from google.adk.tools import FunctionTool
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters
from ddgs import DDGS
from typing import List
from prompt import airbnb_prompt

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

research_agent = LlmAgent(
    name="research_agent",
    model=model,
    description="This agent does research.",
    instruction="""
    You are a helpful assistant that does research by using the 'duckduckgo_search' tool.
    """,
    tools=[ddg_search_tool],
    output_key="research",
)


mythology_agent = LlmAgent(
    name="mythology_agent",
    model=model,
    description="This agent answers mythology questions.",
    instruction="""
    You are a helpful assistant that answers mythology questions by using the 'duckduckgo_search' tool.
    """,
    tools=[ddg_search_tool],
    output_key="mythology",
)


airbnb_agent = LlmAgent(
    model='gemini-2.0-flash',
    name='airbnb_agent',
    instruction="""Use the airbnb search mcp tool to get the hotel details. 
    put place name in form of string and max price in form of int.
    output the hotel details in the following format:
    
    ## 🎯 Search Summary
    - **Location:** [location] | **Dates:** [checkin] → [checkout]
    - **Guests:** [adults]A, [children]C, [infants]I, [pets]P
    - **Room:** [room type] | **Stars:** [rating] | **Amenities:** [amenities]
    - **Results:** [number] hotels
    
    ## 🏨 Hotel Listings
    ### [Hotel Name]
    | Detail | Info |
    |--------|------|
    | ⭐ Rating | [rating]/5 ([reviews]) |
    | 📍 Address | [full address] |
    | 💰 Rate | $[price]/night (+$[tax]) |
    | 🏠 Rooms | [categories] |
    | 📏 Distance | [city center] • [airport] |
    | 🔗 Booking | [URL] |
    | 📞 Contact | [phone] • [website] |
    
    -- repeat per hotel --
    
    ## 📈 Comparison
    | Hotel | Rating | Price | Features | Link |
    |-------|--------|-------|----------|------|
    | [H1] | [rating]⭐ | $[price] | [2 highlights] | [URL] |
    | [H2] | [rating]⭐ | $[price] | [2 highlights] | [URL] |
    
    ## 🏆 Final Picks
    - **Best Value:** [hotel + reason]
    - **Luxury:** [hotel + features]
    - **Budget:** [hotel + savings]
    - **Location:** [hotel + benefit]
    - **Amenities:** [hotel + standout]
    """,
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                    server_params = StdioServerParameters(
                    command= "npx",
                    args= [
                        "-y",
                        "@openbnb/mcp-server-airbnb",
                        "--ignore-robots-txt"
                    ],
                ),
                timeout=180,
            ),
        )
    ],
    output_key="airbnb",
)



parallel_agent = ParallelAgent(
    name="parallel_agent",
    sub_agents=[airbnb_agent,mythology_agent,research_agent],
)

summarizer_agent = LlmAgent(
    name="summarizer_agent",
    model=model,
    description="This agent summarizes the results from airbnb, mythology and research agents.",
    instruction="""
    Combine results from {airbnb} and {mythology} and {research}.
    
    **Output Format:**
    
    ## 🎯 Mythology Summary
    - **Mythology:** [mythology details about the topic/place]
    
    ## 🎯 Research Summary
    - **Facts:** [Interesting facts about the topic/place]
    
    ## 🎯 AirBNB Search Summary
    - **Location:** [location] | **Dates:** [checkin] → [checkout]
    - **Guests:** [adults]A, [children]C, [infants]I, [pets]P
    - **Room:** [room type] | **Stars:** [rating] | **Amenities:** [amenities]
    - **Results:** [number] hotels
    
    ## 🏨 Hotel Listings
    ### [Hotel Name]
    | Detail | Info |
    |--------|------|
    | ⭐ Rating | [rating]/5 ([reviews]) |
    | 📍 Address | [full address] |
    | 💰 Rate | $[price]/night (+$[tax]) |
    | 🏠 Rooms | [categories] |
    | 📏 Distance | [city center] • [airport] |
    | 🔗 Booking | [URL] |
    | 📞 Contact | [phone] • [website] |
    
    -- repeat per hotel --
    
    ## 📈 Comparison
    | Hotel | Rating | Price | Features | Link |
    |-------|--------|-------|----------|------|
    | [H1] | [rating]⭐ | $[price] | [2 highlights] | [URL] |
    | [H2] | [rating]⭐ | $[price] | [2 highlights] | [URL] |
    
    ## 🏆 Final Picks
    - **Best Value:** [hotel + reason]
    - **Luxury:** [hotel + features]
    - **Budget:** [hotel + savings]
    - **Location:** [hotel + benefit]
    - **Amenities:** [hotel + standout]
    
    """,
)

report_agent = SequentialAgent(
    name="report_agent",
    sub_agents=[parallel_agent, summarizer_agent] # Run parallel fetch, then synthesize
)



root_agent = report_agent