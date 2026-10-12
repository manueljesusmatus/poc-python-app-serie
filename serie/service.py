import serie.factory as SerieFactory
from serie.model import Serie
from mock.service import MockService
from page.service import PageService
from serie.repository import SerieRepository
from logger.logger import CustomLogger
from connect import db_connection

class SerieService:
    logger: CustomLogger
    mockService : MockService
    pageService : PageService
    serieRespository: SerieRepository
    series: list = []
    URL_PAGE = "https://lectortmo.com/populars-boys"
    FIND_PATTERN = 'element col-6 col-sm-6 col-md-4 col-lg-3 col-xl-2 mt-2'

    def __init__(self) -> None:
        self.mockService = MockService("serie.mock")
        self.pageService = PageService()
        self.logger = CustomLogger(__name__)
        self.serieRespository = SerieRepository(db_connection.cursor(), db_connection)

    def getSeriesDelDia(self):
        try:
            content = self.pageService.getPage(self.URL_PAGE)
            if(content is not None):
                self.mockService.write(content)
                return self.getSeries(content)
        except:
            self.logger.logger.error(f'Problema no controlado')

        return self.series
    
    def getSeriesDelDiaMock(self):
        try:
            content = self.mockService.read()
            return self.getSeries(content)
        except:
            self.logger.logger.error(f'Problema no controlado')

    def getSeries(self, content) -> list:
        try:
            self.logger.logger.info("Buscando series actualizadas ...")
            parse = self.pageService.getParsed(content)
            html_obj = self.pageService.getAll(parse, 'div', 'class', self.FIND_PATTERN)
            self.logger.logger.info(f'Se han encontrado {len(html_obj)} series')
            self.series = [self.saveSerie(SerieFactory.htmlToSerie(serie)) for serie in html_obj]
        except:
            self.logger.logger.error(f'Problema no controlado')
        return self.series
    
    def saveSerie(self, serie: Serie) -> None:
        self.logger.logger.info(f'Guardando serie {serie}')
        if(self.serieRespository.findOneById(serie.id) != None):
            self.logger.logger.warn(f'Serie {serie.id} ya existe')
            return serie
        self.serieRespository.create(serie)
        self.logger.logger.info(f'Serie {serie.id} creada')
        return serie


    def show(self) -> None:
        for serie in self.series:
            self.logger.logger.info(f'Serie: [{serie}]')