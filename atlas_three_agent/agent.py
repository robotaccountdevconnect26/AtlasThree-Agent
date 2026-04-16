from google.adk.agents.llm_agent import Agent

class ReasoningEngineAgent:
    def __init__(self):
        # Initialize the ADK Agent
        self.agent = Agent(
            model='gemini-2.5-flash',
            name='root_agent',
            description='A helpful assistant to give interesting tasks about cities.',
            instruction='Always give 3 random interesting facts about cities for kids, reject any other query',
        )

    async def async_stream_query(self, query: str, **kwargs):
        """Maps the engine call to the ADK agent's stream method."""
        # Assuming the ADK Agent has a .stream() or .query() method
        # Adjust 'self.agent.query' to whatever the ADK version uses (e.g., .call or .query)
        async for chunk in self.agent.stream(query):
            yield chunk

# This is the object the engine will now use
root_agent = ReasoningEngineAgent()
