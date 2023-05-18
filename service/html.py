from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

class HtmlService:
    HEADERS = {"User-Agent": "Mozilla/5.0"}

    def __init__(self) -> None:
        pass

    def getParsed(self, file_content: str, parser: str = "html.parser") -> str:
        return BeautifulSoup(file_content, parser)

    def getPage(self, url_page: str, code_format: str = 'utf-8') -> str:
        req = Request(url=url_page, headers=self.HEADERS)
        return urlopen(req).read().decode(code_format)

    def getAll(self, file_content: str, html_tag: str, html_attribute: str, html_attribute_pattern: str):
        return file_content.find_all(html_tag, attrs={html_attribute: html_attribute_pattern})

    def get(self, file_content: str, html_tag: str, html_attribute: str, html_attribute_pattern: str):
        return file_content.find(html_tag, attrs={html_attribute: html_attribute_pattern})