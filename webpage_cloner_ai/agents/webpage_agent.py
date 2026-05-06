from pydantic_ai import Agent 
from prompts.system_prompt import SYSTEM_PROMPT
from tools.webpage_tools import takeScreenshotOfGivenWebpage, getInstructionsFromWebpageImage, saveHTMLInFileName
from dotenv import load_dotenv 

load_dotenv()

webpage_agent = Agent(
    model = "openai:gpt-5.1",
    tools = [takeScreenshotOfGivenWebpage, getInstructionsFromWebpageImage, saveHTMLInFileName],
    system_prompt = SYSTEM_PROMPT
)

async def createWebpageAsync(prompt : str):
    async with webpage_agent.run_stream(prompt) as result:
        async for token in result.stream_text(delta=True):
            print(token, end="")
