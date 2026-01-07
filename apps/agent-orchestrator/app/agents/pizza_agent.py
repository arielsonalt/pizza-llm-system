from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI

def build_agent(tools):
    llm = OpenAI(temperature=0)
    return initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=True
    )
