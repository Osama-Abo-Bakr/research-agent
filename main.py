from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_community.tools.semanticscholar.tool import SemanticScholarQueryRun
from langchain_groq import ChatGroq
from langchain import hub
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Iinitialize Prompt Template
instructions = "You are an expert researcher."
base_prompt = hub.pull("langchain-ai/openai-functions-template")
prompt = base_prompt.partial(instructions=instructions)

# Initialize LLM
llm = ChatGroq(
    model='deepseek-r1-distill-llama-70b'
)

# Initialize Semantic Scholar Tool
tools = [SemanticScholarQueryRun()]

# Initialize Agent
agent = create_openai_functions_agent(llm, tools, prompt)

# Create Agent Executor
agent_executor = AgentExecutor(agent=agent, 
                               tools=tools, 
                               verbose=True)


# Run Agent
result = agent_executor.invoke(
    {
        "input": "Explain me what the multi head attention in transformer"
    }
)


print('### Output ###')
print(result['output'])