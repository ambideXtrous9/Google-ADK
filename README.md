# 🤖 Google ADK Multi-Agent System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.12+-blue.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)
![Google ADK](https://img.shields.io/badge/Google-ADK-4285F4?logo=google&logoColor=white)

**A powerful multi-agent system built with Google Agent Development Kit (ADK) for intelligent research, mythology queries, and Airbnb hotel search**

🚧 **Agentic Workflow Building in Progress** 🚧

[Features](#-features) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [Contributing](#-contributing)

</div>

---

## 📋 Table of Contents

- [✨ Features](#-features)
- [🏗️ Architecture](#️-architecture)
- [🚀 Installation](#-installation)
- [⚙️ Configuration](#️-configuration)
- [💻 Usage](#-usage)
- [🔧 Project Structure](#-project-structure)
- [📦 Dependencies](#-dependencies)
- [🎯 Functionalities](#-functionalities)
- [🛠️ Customization](#️-customization)
- [🤝 Contributing](#-contributing)

---

## ✨ Features

- 🎯 **Multi-Agent Architecture**: Intelligent agent orchestration with parallel and sequential patterns
- 🔍 **Web Search Integration**: DuckDuckGo search capabilities for real-time information
- 🏨 **Airbnb Integration**: MCP-powered hotel search with comprehensive listings and comparisons
- 🧠 **Advanced LLM Support**: Powered by LiteLLM with Groq's Qwen3-32B and Gemini 2.0 Flash
- 🎭 **Specialized Agents**: Dedicated agents for research, mythology, and travel planning
- ⚡ **Parallel Execution**: Multiple agents run simultaneously for faster results
- 🔄 **Sequential Workflow**: Smart orchestration with parallel fetch and sequential synthesis
- 🛠️ **MCP Tool Integration**: Model Context Protocol for seamless tool connectivity
- 📊 **Comprehensive Reports**: Automated summarization and comparison of results
- 🎨 **Structured Output**: Beautifully formatted results with tables and comparisons

---

## 🏗️ Architecture

This project implements a **sequential-parallel hybrid pattern** with the following components:

```
┌─────────────────────────────────────────────┐
│      Report Agent (Root - Sequential)       │
│  Orchestrates parallel fetch → synthesis   │
└──────────────┬──────────────────────────────┘
               │
       ┌───────┴────────┐
       │                │
┌──────▼──────┐  ┌──────▼──────────┐
│  Parallel   │  │  Summarizer     │
│   Agent     │  │    Agent        │
│             │  │                 │
│ Runs 3      │  │ Combines all    │
│ agents      │  │ outputs into    │
│ in parallel │  │ final report    │
└──────┬──────┘  └─────────────────┘
       │
  ┌────┴────┬──────────┐
  │         │          │
┌─▼───┐ ┌──▼───┐ ┌───▼────┐
│Airbnb│ │Mytho│ │Research│
│Agent │ │logy │ │ Agent  │
│      │ │Agent│ │        │
│🏨 MCP│ │🎭 DDG│ │🔬 DDG  │
│Gemini│ │Qwen │ │Qwen    │
└──────┘ └─────┘ └────────┘
```

### 🤖 Agent Descriptions

| Agent | Type | Purpose | Tools | Model | Output Key |
|-------|------|---------|-------|-------|------------|
| **Research Agent** 🔬 | LlmAgent | Performs comprehensive web research | `duckduckgo_search` | Qwen3-32B | `research` |
| **Mythology Agent** 🎭 | LlmAgent | Answers mythology questions | `duckduckgo_search` | Qwen3-32B | `mythology` |
| **Airbnb Agent** 🏨 | LlmAgent | Searches and formats hotel listings | `MCPToolset` (Airbnb) | Gemini 2.0 Flash | `airbnb` |
| **Parallel Agent** ⚡ | ParallelAgent | Runs multiple agents simultaneously | Sub-agents | N/A | N/A |
| **Summarizer Agent** 📊 | LlmAgent | Combines and formats all results | None | Qwen3-32B | N/A |
| **Report Agent** 📋 | SequentialAgent | Orchestrates workflow | Sub-agents | N/A | N/A |

### 🔄 Workflow Pattern

1. **Parallel Execution** ⚡: Three agents (Airbnb, Mythology, Research) run simultaneously
2. **Data Aggregation** 📊: All results are collected
3. **Synthesis** 🎯: Summarizer agent combines outputs into a comprehensive report
4. **Final Output** 📄: Structured report with mythology, research, and hotel listings

---

## 🚀 Installation

### Prerequisites

- Python 3.12 or higher
- pip package manager
- Node.js and npm (for MCP server)
- Virtual environment (recommended)

### Step-by-Step Setup

1. **Clone the repository** (if applicable)
   ```bash
   git clone <repository-url>
   cd Google-ADK
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies** (for MCP server)
   ```bash
   # MCP server will be installed automatically via npx on first use
   # Ensure Node.js and npm are installed on your system
   ```

5. **Set up environment variables**
   ```bash
   # Create .env file
   touch .env
   # Edit .env with your API keys
   ```

---

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Groq API Configuration
GROQ_API_KEY=your_groq_api_key_here

# Google API Configuration (for Gemini)
GOOGLE_API_KEY=your_google_api_key_here

# Other configuration variables
# Add as needed
```

### Model Configuration

The system uses multiple models:

- **Qwen3-32B** (via Groq): Used for research, mythology, and summarization
- **Gemini 2.0 Flash**: Used for Airbnb agent

You can modify models in `my_agent/agent.py`:

```python
# For Qwen model
model = LiteLlm(
    model="groq/qwen/qwen3-32b",  # Change to your preferred model
)

# For Gemini model (in Airbnb agent)
airbnb_agent = LlmAgent(
    model='gemini-2.0-flash',  # Change to your preferred Gemini model
    # ... other parameters
)
```

---

## 💻 Usage

### Basic Usage

```python
from my_agent.agent import root_agent

# Use the report agent (root_agent) for comprehensive queries
query = "Find hotels in Paris and tell me about Greek mythology related to the city"
response = root_agent.run(query)
print(response)
```

### Using Individual Agents

```python
from my_agent.agent import research_agent, mythology_agent, airbnb_agent

# Research query
research_result = research_agent.run("Latest developments in AI")
print(research_result)

# Mythology query
mythology_result = mythology_agent.run("Tell me about Norse gods")
print(mythology_result)

# Airbnb search
airbnb_result = airbnb_agent.run("Search hotels in Tokyo with max price 200")
print(airbnb_result)
```

### Using Parallel Agent

```python
from my_agent.agent import parallel_agent

# Run multiple agents in parallel
query = "Search hotels in Rome and research about Roman history"
results = parallel_agent.run(query)
# Returns results from all three agents
```

### Complete Workflow Example

```python
from my_agent.agent import root_agent

# The report agent orchestrates the complete workflow:
# 1. Runs parallel_agent (airbnb + mythology + research) simultaneously
# 2. Summarizes all results into a comprehensive report

query = """
Find hotels in Athens, Greece with max price 150 per night.
Also tell me about Greek mythology related to Athens and 
research interesting facts about the city.
"""

result = root_agent.run(query)

# Output includes:
# - Mythology summary about Athens
# - Research facts about Athens
# - Airbnb hotel listings with ratings, prices, amenities
# - Comparison table of hotels
# - Final recommendations (Best Value, Luxury, Budget, etc.)
print(result)
```

---

## 🔧 Project Structure

```
Google-ADK/
│
├── 📁 my_agent/                    # Main agent module
│   ├── __init__.py                 # Package initialization
│   ├── agent.py                    # 🎯 Main agent definitions
│   ├── mythology_instructions.txt  # Mythology agent instructions
│   └── research_instructions.txt   # Research agent instructions
│
├── 📁 gadk/                        # Virtual environment (if present)
│
├── 📄 prompt.py                    # 📝 Prompt templates
├── 📄 requirements.txt             # 📦 Project dependencies
├── 📄 README.md                    # 📖 This file
└── 📄 .env                         # 🔐 Environment variables (create this)
```

---

## 📦 Dependencies

| Package | Purpose | Version |
|---------|---------|---------|
| `google-adk` | Google Agent Development Kit | Latest |
| `python-dotenv` | Environment variable management | Latest |
| `litellm` | LLM abstraction layer | Latest |
| `duckduckgo_search` | DuckDuckGo search integration | Latest |
| `ddgs` | DuckDuckGo search client | Latest |
| `mcp` | Model Context Protocol | Latest |

### Install All Dependencies

```bash
pip install -r requirements.txt
```

---

## 🎯 Functionalities

### 🔍 Web Search Capability

The system includes a custom DuckDuckGo search tool that:
- Performs web searches with up to 5 results
- Returns structured search results
- Integrates seamlessly with agent workflows

```python
def duckduckgo_search(query: str) -> List:
    """
    Perform a web search using DuckDuckGo.
    Returns a list of search results.
    """
    results = DDGS().text(query, max_results=5)
    return results
```

### 🏨 Airbnb Hotel Search

The Airbnb agent uses **MCP (Model Context Protocol)** to:
- Search hotels by location and price
- Retrieve detailed hotel information
- Format results in structured tables
- Provide comparisons and recommendations

**Features:**
- ⭐ Rating and review information
- 💰 Price per night with tax details
- 📍 Full address and location details
- 🏠 Room categories and availability
- 📏 Distance from city center and airport
- 🔗 Direct booking links
- 📞 Contact information
- 🏆 Final picks (Best Value, Luxury, Budget, etc.)

### 🤖 Agent Capabilities

#### Research Agent 🔬
- Conducts comprehensive web research
- Gathers information from multiple sources
- Synthesizes research findings
- Output key: `research`

#### Mythology Agent 🎭
- Answers mythology-related questions
- Provides detailed explanations about myths and legends
- Covers various mythological traditions
- Output key: `mythology`

#### Airbnb Agent 🏨
- Searches hotels using MCP tools
- Formats results in beautiful tables
- Provides comprehensive hotel comparisons
- Outputs structured recommendations
- Output key: `airbnb`

#### Parallel Agent ⚡
- Executes multiple agents simultaneously
- Improves performance through parallelization
- Collects outputs from all sub-agents
- Sub-agents: `airbnb_agent`, `mythology_agent`, `research_agent`

#### Summarizer Agent 📊
- Combines results from all three agents
- Formats output in structured markdown
- Creates comprehensive reports
- Includes mythology, research, and hotel listings

#### Report Agent 📋
- Orchestrates the complete workflow
- Runs parallel agent first (data collection)
- Then runs summarizer agent (synthesis)
- Returns final comprehensive report

### 📊 Output Format

The system generates beautifully formatted reports with:

- **🎯 Search Summary**: Location, dates, guests, room details
- **🏨 Hotel Listings**: Detailed information per hotel
- **📈 Comparison Tables**: Side-by-side hotel comparisons
- **🏆 Final Picks**: Recommendations (Best Value, Luxury, Budget, Location, Amenities)
- **📝 Mythology Summary**: Contextual mythology information
- **🔬 Research Summary**: Interesting facts and information

---

## 🛠️ Customization

### Adding a New Agent

1. **Create the agent**:
   ```python
   from google.adk.agents import LlmAgent
   
   custom_agent = LlmAgent(
       name="custom_agent",
       model=model,
       description="Your agent description",
       instruction="Your agent instructions",
       tools=[your_tools],
       output_key="custom",
   )
   ```

2. **Add to parallel agent**:
   ```python
   parallel_agent = ParallelAgent(
       name="parallel_agent",
       sub_agents=[airbnb_agent, mythology_agent, research_agent, custom_agent],
   )
   ```

3. **Update summarizer**:
   ```python
   summarizer_agent = LlmAgent(
       # ... other parameters
       instruction="""
       Combine results from {airbnb}, {mythology}, {research}, and {custom}.
       # ... formatting instructions
       """,
   )
   ```

### Creating Custom Tools

#### Function Tool
```python
from google.adk.tools import FunctionTool

def my_custom_tool(input: str) -> str:
    """Tool description"""
    # Tool implementation
    return result

custom_tool = FunctionTool(func=my_custom_tool)
```

#### MCP Tool
```python
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StdioConnectionParams
from mcp import StdioServerParameters

mcp_tool = MCPToolset(
    connection_params=StdioConnectionParams(
        server_params=StdioServerParameters(
            command="npx",
            args=["-y", "@your/mcp-server"],
        ),
        timeout=180,
    ),
)
```

### Using Different Agent Types

```python
from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent

# LlmAgent: Single LLM-powered agent
agent = LlmAgent(...)

# ParallelAgent: Run multiple agents simultaneously
parallel = ParallelAgent(sub_agents=[agent1, agent2, agent3])

# SequentialAgent: Run agents in sequence
sequential = SequentialAgent(sub_agents=[agent1, agent2])
```

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. 🍴 Fork the repository
2. 🌿 Create a feature branch (`git checkout -b feature/amazing-feature`)
3. 💾 Commit your changes (`git commit -m 'Add amazing feature'`)
4. 📤 Push to the branch (`git push origin feature/amazing-feature`)
5. 🔀 Open a Pull Request

### Contribution Guidelines

- ✨ Follow the existing code style
- 📝 Add comments for complex logic
- 🧪 Include tests for new features
- 📖 Update documentation as needed
- 🎨 Maintain consistent formatting

---

## 🙏 Acknowledgments

- **Google ADK** for the Agent Development Kit
- **LiteLLM** for LLM abstraction
- **Groq** for providing fast inference with Qwen models
- **Google Gemini** for powerful language models
- **DuckDuckGo** for search capabilities
- **MCP** for Model Context Protocol integration
- **OpenAirbnb** for MCP server implementation

---

## 📞 Support

If you encounter any issues or have questions:

- 🐛 Open an issue on GitHub
- 💬 Start a discussion
- 📧 Contact the maintainers

---

<div align="center">

**Made with ❤️ using Google ADK**

⭐ Star this repo if you find it helpful!

---

🚧 **Agentic Workflow Building in Progress** 🚧

</div>
