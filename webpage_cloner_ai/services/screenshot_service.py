from playwright.sync_api import sync_playwright


class ScreenshotService:
    @staticmethod 
    def createScreenshot(pageUrl : str, fileName : str):
        with sync_playwright() as p:
            browser = p.chromium.launch(channel = 'chrome')
            page = browser.new_page()
            page.goto(pageUrl)
            page.wait_for_timeout(3000)
            page.screenshot(path = fileName)
            browser.close()
        
        return {
            "status": "success",
            "fileName": fileName
        }
    