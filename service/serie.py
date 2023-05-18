import factory.serie as SerieFactory
from service.htmlmock import MockService
from service.html import HtmlService

class SerieService:
    mockService : MockService
    htmlService : HtmlService
    series: list = []
    URL_PAGE = "https://lectortmo.com/populars-boys"
    FIND_PATTERN = 'element col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2 mt-2'

    def __init__(self) -> None:
        self.mockService = MockService("serie.mock")
        self.htmlService = HtmlService()

    def getSeriesDelDia(self):
        content = self.htmlService.getPage(self.URL_PAGE)
        self.mockService.write(content)
        parse = self.htmlService.getParsed(content)
        html_obj = self.htmlService.getAll(parse, 'div', 'class', self.FIND_PATTERN)
        self.series = [SerieFactory.htmlToSerie(serie) for serie in html_obj]
        return self.series
    
    def getSeriesDelDiaMock(self):
        content = self.mockService.read()
        parse = self.htmlService.getParsed(content)
        html_obj = self.htmlService.getAll(parse, 'div', 'class', self.FIND_PATTERN)
        self.series = [SerieFactory.htmlToSerie(serie) for serie in html_obj]
        self.series
        return self.series

    def show(self) -> None:
        for serie in self.series:
            print(serie)