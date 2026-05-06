from services.ollama_vision_service import OllamaVisionService
from services.screenshot_service import ScreenshotService
from services.save_html_service import SaveHTMLService

ollamaVisionService = OllamaVisionService()

def takeScreenshotOfGivenWebpage(webpageUrl: str, fileName : str):
    print(f"Calling takeScreenshotOfGivenWebpage tool with {webpageUrl} and {fileName}")
    return ScreenshotService.createScreenshot(pageUrl=webpageUrl, fileName=fileName)

def getInstructionsFromWebpageImage(fileName : str):
    print(f"Calling getInstructionsFromWebpageImage from {fileName}")
    return ollamaVisionService.getVisionContent(fileName)

def saveHTMLInFileName(htmlStr : str, fileName : str):
    print(f"Calling saveHTMLInFileName tool in {fileName}")
    return SaveHTMLService.saveHTML(htmlStr, fileName)