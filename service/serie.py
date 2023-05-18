import factory.serie as SerieFactory
from service.htmlmock import MockService
from service.html import HtmlService
from logger.logger import CustomLogger

class SerieService:
    logger: CustomLogger
    mockService : MockService
    htmlService : HtmlService
    series: list = []
    URL_PAGE = "https://lectortmo.com/populars-boys"
    FIND_PATTERN = 'element col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2 mt-2'

    def __init__(self) -> None:
        self.mockService = MockService("serie.mock")
        self.htmlService = HtmlService()
        self.logger = CustomLogger()

    def getSeriesDelDia(self):
        try:
            content = self.htmlService.getPage(self.URL_PAGE)
            self.mockService.write(content)
            
            self.logger.info("Buscando series actualizadas ...")
            parse = self.htmlService.getParsed(content)
            html_obj = self.htmlService.getAll(parse, 'div', 'class', self.FIND_PATTERN)

            self.logger.info(f'Se han encontrado {len(html_obj)} series')
            self.series = [SerieFactory.htmlToSerie(serie) for serie in html_obj]

        except:
            self.logger.error(f'Problema no controlado')

        return self.series
    
    def getSeriesDelDiaMock(self):
        try:
            content = self.mockService.read()

            self.logger.info("Buscando series actualizadas ...")
            parse = self.htmlService.getParsed(content)
            html_obj = self.htmlService.getAll(parse, 'div', 'class', self.FIND_PATTERN)

            self.logger.info(f'Se han encontrado {len(html_obj)} series')
            self.series = [SerieFactory.htmlToSerie(serie) for serie in html_obj]

        except:
            self.logger.error(f'Problema no controlado')
            
        return self.series

    def show(self) -> None:
        for serie in self.series:
            self.logger.info(f'Serie: [{serie}]')