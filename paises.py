import json
import sys

import requests

URL_ALL = 'https://restcountries.eu/rest/v2/all'
URL_NAME ='https://restcountries.eu/rest/v2/name/'


def request_url(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
    except:
        print('Erro ao fazer requisicao em: ', url)
        
def parsing(response_text):
    try:
        return json.loads(response_text)
    except:
        print('erro ao fazer parsing')
        
def count_countries():
    response = request_url(URL_ALL)
    if response:
        all_countries = parsing(response)
        if all_countries:
            return len(all_countries)

def list_countries(all_countries):
    for country in all_countries:
        print(country)

    
def show_population(country_name):
    response = request_url(URL_NAME + country_name)
    if response:
        countries_list = parsing(response)
        for country in countries_list:
            print('{}: {} de habitantes'.format(country['name'], country['population']))
    else:
        print('pais nao encontrado!')

def show_currency(country_name):
    response = request_url(URL_NAME + country_name)
    if response:
        countries_list = parsing(response)
        for country in countries_list:
            print('Moedas do {}: '.format(country['name']))
            currencies = country['currencies']
            for currency in currencies:
                print('{} - {}'.format(currency['name'], currency['code']))
    else:
        print('pais nao encontrado!')

def show_capital(country_name):
    response = request_url(URL_NAME + country_name)
    if response:
        countries_list = parsing(response)
        for country in countries_list:
            print('capital do {}: {}' .format(country['name'], country['capital']))
    else:
        print('pais nao encontrado')

def read_country_name():
    try:
        country_name = sys.argv[2]
        return country_name
    except:
        print('argumento invalido, falta o nome do pais')
        
if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('-------------sistema de paises-------------')
        print('Uso: python paises.py <acao> <nome do pais>')
        print('acoes: contagem, moeda, populacao, capital')
    else:
        user_argument = sys.argv[1]
        
        if user_argument == 'contagem':
            result = count_countries()
            print('existem {} paises atualmente'.format(result))
            exit(0)
            
        elif user_argument == 'moeda':
            country_name = read_country_name()
            if country_name:
                show_currency(country_name)
                exit(0)
                
        elif user_argument == 'populacao':
            country_name = read_country_name()
            if country_name:
                show_population(country_name)
                exit(0)
                
        elif user_argument == 'capital':
            country_name = read_country_name()
            if country_name:
                show_capital(country_name)
                exit(0)
        else:
            print('Argumento invalido')
            
    #estudar argparse