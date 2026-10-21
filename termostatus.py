import json
import os
class temperatura:
    def __init__(self, temp):
        self.temp = temp
    def att_temp(self):
        return print(f"{self.temp}°C")
class arquivo:
    def salva_temp(self, neg):
        self.neg = neg
        leitura = [{"temp": self.neg}]
        if not os.path.exists("temp_neg.json"):
            with open("temp_neg.json", "w", encoding="utf-8") as arquivo:
                json.dump(leitura, arquivo, indent=4, ensure_ascii=False)
        else:
            with open("temp_neg.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
            if int(dados[0]["temp"]) > int(leitura[0]["temp"]):
                dados[0]["temp"] = self.neg
                with open("temp_neg.json", "w", encoding="utf-8") as arquivo:
                    json.dump(dados, arquivo, indent=4, ensure_ascii=False)