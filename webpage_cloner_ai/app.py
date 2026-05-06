from agents.webpage_agent import createWebpageAsync
import asyncio 
import sys 

if __name__ == "__main__" and len(sys.argv) > 1:
    createWebpageAsync(sys.argv[1:])
    