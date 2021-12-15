class Converter:
    def __init__(self, usd: float, eur: float, jpy: float):
        self.rateUSD = usd
        self.rateEUR = eur
        self.rateJPY = jpy

    def convert(self, rubles: float, currency: int):
        if currency == 1:
            print("Ваши сбережения в долларах:", rubles/self.rateUSD)
        elif currency == 2:
            print("Ваши сбережения в евро:", rubles/self.rateEUR)
        elif currency == 3:
            print("Ваши сбережения в иенах:", rubles/self.rateJPY)
        else:
            print("Неизвестная валюта")