import re
from logger.logger import CustomLogger
from model.serie import Serie
from service.html import HtmlService

def htmlToSerie(html) -> Serie:
    htmlService = HtmlService()
    logger = CustomLogger()
    serie = {}
    try:
        serie['id'] = html['data-identifier']
        serie['tipo'] = htmlService.get(html, 'span', 'class', 'book-type').string.lower()
        serie['nombre'] = htmlService.get(html, 'div', 'class', 'thumbnail-title').h4['title']
        match = re.search("https:\/\/.*.jpg", html.div.style.string) 
        serie['imagen'] = match.group()
        serie['url'] = html.a['href'].strip()
        return Serie((serie['id'], serie['tipo'], serie['nombre'], serie['imagen'], serie['url']))
    except:
        logger.error(f'Error al crear objeto serie de {html["data-identifier"]}')
        return {}
