import factory.serie as SerieFactory
from service.htmlmock import MockService
from service.html import HtmlService
from repository.serie import SerieRepository
from logger.logger import CustomLogger
from connect import db_connection

class SerieService:
    logger: CustomLogger
    mockService : MockService
    htmlService : HtmlService
    serieRespository: SerieRepository
    series: list = []
    URL_PAGE = "https://lectortmo.com/populars-boys"
    FIND_PATTERN = 'element col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2 mt-2'

    def __init__(self) -> None:
        self.mockService = MockService("serie.mock")
        self.htmlService = HtmlService()
        self.logger = CustomLogger()
        self.serieRespository = SerieRepository(db_connection.cursor(), db_connection)

    def getSeriesDelDia(self):
        try:
            content = self.htmlService.getPage(self.URL_PAGE)
            self.mockService.write(content)
            
            self.logger.logger.info("Buscando series actualizadas ...")
            parse = self.htmlService.getParsed(content)
            html_obj = self.htmlService.getAll(parse, 'div', 'class', self.FIND_PATTERN)

            self.logger.logger.info(f'Se han encontrado {len(html_obj)} series')
            self.series = [SerieFactory.htmlToSerie(serie) for serie in html_obj]

        except:
            self.logger.logger.error(f'Problema no controlado')

        return self.series
    
    def getSeriesDelDiaMock(self):
        try:
            content = self.mockService.read()

            self.logger.logger.info("Buscando series actualizadas ...")
            parse = self.htmlService.getParsed(content)
            html_obj = self.htmlService.getAll(parse, 'div', 'class', self.FIND_PATTERN)

            self.logger.logger.info(f'Se han encontrado {len(html_obj)} series')
            self.series = [self.saveSerie(SerieFactory.htmlToSerie(serie)) for serie in html_obj]

        except:
            self.logger.logger.error(f'Problema no controlado')
            
        return self.series
    
    def saveSerie(self, serie) -> None:
        self.logger.logger.info(f'Guardando serie {serie}')
        if(self.serieRespository.findOneById(serie.id) != None):
            self.logger.logger.warn(f'Serie ya existe')
            return serie
        self.serieRespository.create(serie)
        return serie


    def show(self) -> None:
        for serie in self.series:
            self.logger.logger.info(f'Serie: [{serie}]')