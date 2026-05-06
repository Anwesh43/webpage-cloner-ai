from services.ollama_vision_service import OllamaVisionService

ollamaVisionService = OllamaVisionService()

if __name__ == "__main__":
    print(ollamaVisionService.getVisionContent("leet.png"))
