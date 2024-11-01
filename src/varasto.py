class Varasto:
    def __init__(self, tilavuus, alku_saldo = 0):
        if tilavuus > 0.0:
        # if tilavuus > 1000.0: # rikotaan testi, jotta nähdään mitä GitHub actions:issä tapahtuu
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= self.tilavuus:   # tää oli 'tilavuus' eikä 'self.tilavuus', minkä takia pysty mennä negatiiviseks aiemmin, joten korjasin
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = self.tilavuus      # tää oli 'tilavuus' eikä 'self.tilavuus', minkä takia pysty mennä negatiiviseks aiemmin, joten korjasin

    # huom: ominaisuus voidaan myös laskea. Ei tarvita erillistä kenttää viela_tilaa tms.
    def paljonko_mahtuu(self):
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:   # jos yrittää laittaa enemmän ku mahtuu, loput hukkaan
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"

# if __name__ == '__main__':
#     negatiivinen_varasto = Varasto(-10)
#     varasto = Varasto(10,-10)
#     # print(str(varasto))