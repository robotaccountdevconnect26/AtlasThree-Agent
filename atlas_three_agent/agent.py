from google.adk.agents.llm_agent import Agent

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_agent',
    description='A helpful assistant to give interesting tasks about cities.',
    instruction='Always give 3 random interesting facts about cities for kids, reject any other query',
)
