from service.serie import SerieService

def OBTENER_INFO(usar_mock=False):
    serieService = SerieService()
    result = serieService.getSeriesDelDiaMock() if usar_mock else serieService.getSeriesDelDia()
    serieService.show()
    return result

if __name__=='__main__':
    response = OBTENER_INFO(False)