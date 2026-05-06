from ollama import chat 

class OllamaVisionService:
    def __init__(self):
        self.fileExplanationMap = {}

    def getVisionContent(self, image : str):
        content = "What is in the image of webpage? Give instructions as a UI/UX designer so we can create html with css"
        message = {
            "role": "user",
            "content": content, 
            "images": [image] 
        }
        response = chat(model = "gemma3", messages = [message])
        self.fileExplanationMap = {
            image: response.message.content
        }
        return response.message.content