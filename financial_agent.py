from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.file import FileTools  # Importing FileTools for file operations
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FileTools with the desired base directory
file_tools = FileTools(
    base_dir='./Reports',  # Directory for file operations
    save_files=True,       # Enable saving files
    read_files=True,       # Enable reading files
    list_files=True        # Enable listing files
)

# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources."],
    show_tool_calls=True,
    markdown=True,
)

# Finance Agent
finance_agent = Agent(
    name="Finance AI Agent",
    role="Provide financial analysis and insights.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display data clearly."],
    show_tool_calls=True,
    markdown=True,
)

# File System Agent utilizing FileTools
file_system_agent = Agent(
    name="File System Agent",
    role="Handle file system tasks like saving reports.",
    model=Groq(id="llama3-groq-70b-8192-tool-use-preview"),
    tools=[file_tools],
    instructions=[
        "Generate a suitable headline and save the markdown content in the 'Reports' folder."
    ],
    show_tool_calls=True,
    markdown=True,
)

# Multi-Agent System
multi_ai_agent = Agent(
    team=[web_search_agent, finance_agent, file_system_agent],
    instructions=[
        "Always include sources.",
        "Use tables to display data clearly.",
        "Save reports in markdown format in the 'Reports' folder."
    ],
    show_tool_calls=True,
    markdown=True,
    model=Groq(id="llama-3.3-70b-versatile"),
)

# Execute a Task
multi_ai_agent.print_response(
    "Summarize analyst recommendations and share the latest news for TSM. Save the report as a markdown file.",
    stream=True,
)
