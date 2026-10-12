import re
from logger.logger import CustomLogger
from serie.model import Serie
from page.service import PageService

def htmlToSerie(html) -> Serie:
    pageService = PageService()
    logger = CustomLogger(__name__)
    serie = {}
    try:
        serie['id'] = html['data-identifier']
        serie['tipo'] = pageService.get(html, 'span', 'class', 'book-type').string.lower()
        serie['nombre'] = pageService.get(html, 'div', 'class', 'thumbnail-title').h4['title']
        match = re.search("https:\/\/.*.jpg", html.div.style.string) 
        serie['imagen'] = match.group()
        serie['url'] = html.a['href'].strip()
        return Serie((serie['id'], serie['tipo'], serie['nombre'], serie['imagen'], serie['url']))
    except:
        logger.logger.error(f'Error al crear objeto serie de {html["data-identifier"]}')
        return {}
