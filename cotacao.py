from bs4 import BeautifulSoup
import requests
import unidecode

def get_result_set_from_page():
	page = requests.get("https://economia.uol.com.br/cotacoes/cambio")
	soup = BeautifulSoup(page.content, 'html.parser')
	find_class = soup.find_all('li', class_ = 'select-option')

	return find_class

def get_name_and_url():
	result_set = get_result_set_from_page()
	currency_name = list()
	currency_url = list()

	for info in result_set:
		if unidecode.unidecode(info.label.string.lower()) not in currency_name:
			try:
				currency_url.append(info.attrs['data-url'])
			except:
				continue
			currency_name.append(unidecode.unidecode(info.label.string.lower()))
	return currency_name, currency_url

def get_currency_value(currency_info, currency_request):
	currency_request = currency_request.lower()
	link = 'https://economia.uol.com.br/cotacoes/cambio'
	found = False
	for i in range(len(currency_info[0])):
		if(currency_request == currency_info[0][i]):
			link += '/' + currency_info[1][i] + '/'
			found = True
			break

	if(not found):
		return False
	else:
		page = requests.get(link)
		soup = BeautifulSoup(page.content, 'html.parser')
		find_class = soup.find_all('input', class_ = 'field normal')
		value = 0
		for info in find_class:
			if info.attrs['name'] == 'currency2':
				value = float(info.attrs['value'].replace(',', '.'))
		return value

def get_link_from_search(currency_and_links, request_currency):
	currency_list = list()
	request_currency = unidecode.unidecode(request_currency)
	for currency in currency_and_links[0]:
		if request_currency in currency.split():
			currency_list.append(currency)
	return currency_list
