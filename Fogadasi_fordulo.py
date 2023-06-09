class Fogadasi_fordulo:
    def __init__(self, sor: str):
        splittedData = sor.strip().split(';')
        #Év;Hét;Forduló;T13p1;Ny13p1;Eredmények
        self.ev = splittedData[0]
        self.het = splittedData[1]
        self.fordulo = splittedData[2]
        self.t13p1 = int(splittedData[3])
        self.ny13p1 = splittedData[4]
        self.eredmenyek = splittedData[5]