from services.ollama_vision_service import OllamaVisionService
from services.screenshot_service import ScreenshotService
from services.save_html_service import SaveHTMLService

def takeScreenshotOfGivenWebpage(webpageUrl: str, fileName : str):
    print(f"Calling takeScreenshotOfGivenWebpage tool with {webpageUrl} and {fileName}")
    return ScreenshotService.createScreenshot(webpageUrl, fileName)

def getInstructionsFromWebpageImage(fileName : str):
    print(f"Calling getInstructionsFromWebpageImage from {fileName}")
    return ScreenshotService.createScreenshot(fileName=fileName)

def saveHTMLInFileName(htmlStr : str, fileName : str):
    print(f"Calling saveHTMLInFileName tool in {fileName}")
    return SaveHTMLService.saveHTML(htmlStr, fileName)