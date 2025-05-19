from dotenv import load_dotenv
from langchain_groq import ChatGroq
from mcp_use import MCPAgent, MCPClient
import os
import sys
import warnings

warnings.filterwarnings("ignore", category=ResourceWarning)

# Setting up the chatbot
async def run_chatbot():
    """ Running a chat using MCPAgent's built in conversation memory """
    load_dotenv()
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    configFile = "mcp.json"
    print("Starting chatbot...")

    # Creating MCP client and LLM instance
    client = MCPClient.from_config_file(configFile)
    llm = ChatGroq(model="llama-3.1-8b-instant")

    # Creating an agent with memory enabled
    agent = MCPAgent(
        llm=llm,
        client=client,
        max_steps=15,
        memory_enabled=True,
        verbose=False
    )

    # Implementing the chatbot
    print("\n-----Interactive MCP Chat----")
    print("Type 'exit' or 'quit' to end the conversation")
    print("Type 'clear' to clear conversation history")

    try:
        while True:
            user_input = input("\nYou: ")

            if user_input.lower() in ["exit", "quit"]:
                print("Ending conversation....")
                break
           
            if user_input.lower() == "clear":
                agent.clear_conversation_history()
                print("Conversation history cleared....")
                continue
           
            print("\nAssistant: ", end="", flush=True)

            try:
                response = await agent.run(user_input)
                print(response)
           
            except Exception as e:
                print(f"\nError: {e}")

    finally:
        if client and client.sessions:
            await client.close_all_sessions()

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(run_chatbot())
    except KeyboardInterrupt:
        print("Session interrupted. Goodbye!")
   
    finally:
        sys.stderr = open(os.devnull, "w")