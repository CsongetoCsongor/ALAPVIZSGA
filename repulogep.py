class RepuloGep:
    def __init__(self, sor: str):
        #típus;év;utas;személyzet;utazósebesség;felszállótömeg;fesztáv
        #Airbus A300;1972;220-336;3;911;142000;44,84
        splittedData = sor.strip().split(';')
        self.tipus = splittedData[0]
        self.ev = int(splittedData[1])
        self.utas = splittedData[2]
        self.szemelyzet = splittedData[3]
        self.sebesseg = int(splittedData[4])
        self.tomeg = int(splittedData[5])
        self.fesztav = float(splittedData[6].replace(',', '.'))

        self.maxUtas = int(self.utas.split('-')[-1])

    def kategoriaNev(self):
        if self.sebesseg < 500:
            return 'Alacsony sebességű'
        if self.sebesseg < 1000:
            return 'Szubszonikus'
        if self.sebesseg < 1200:
            return 'transzszonikus'
        return 'Szuperszonikus'