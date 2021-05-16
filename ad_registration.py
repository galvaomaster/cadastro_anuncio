import json
import os
from datetime import datetime
from os.path import isfile


json_file = {"ad_name": " ",
             "customer": "",
             "start_date": "",
             "end_date": "",
             "value": ""}


def read_json():
    json_file = {}
    if os.path.exists('ad.json'):
        with open('ad.json', 'r', encoding='utf-8') as f:
          json_file = json.load(f)
        
    return json_file

def create_json(json_file):
  with open('ad.json', 'w') as f:
    json.dump(json_file, f)


comand = 1
while comand != 0:
    print("                     ")
    comand = int(input("Deseja Cadastrar um Anúncio?  [1]-Sim  [0]-Não "))

    if comand == 1:
        ad_name = input("Digite o nome do Anúncio: ").strip()
        customer = input("Digite o nome do Cliente: ").strip()

        start_str_date = input(
            "Digite a data de início do anuncio no formato YYYY/MM/DD: ")
        start_date = datetime.strptime(start_str_date, '%Y/%m/%d').date()

        end_str_date = input(
            "Digite a data fim do anuncio no formato YYYY/MM/DD: ")
        end_date = datetime.strptime(end_str_date, '%Y/%m/%d').date()

        value = float(input("Digite o valor do Anúncio: ").strip())

        # start_str_date = start_date.strftime('%Y/%m/%d')
        # end_str_date = end_date.strftime('%Y/%m/%d')

        json_file = {
            "ad_name": ad_name,
            "customer": customer,
            "start_date": start_date,
            "end_date": end_date,
            "value": value
        }
create_json(json_file)
