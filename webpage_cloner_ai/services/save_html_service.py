class SaveHTMLService:
    @staticmethod
    def saveHTML(htmlStr: str, fileName: str):
        with open(fileName, "w") as f:
            f.write(htmlStr)
        return {
            "status": "success",
            "fileName": fileName
        }