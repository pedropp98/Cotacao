from lxml import html
import requests

def getDolar():
	page = requests.get("https://economia.uol.com.br/")
	tree = html.fromstring(page.content)

	real = tree.xpath("/html/body/section[1]/div[2]/div/div[1]/div[1]/h3/a[3]/text()")
	valor = real[0]

	return valor

def DolarToFloat():
	valor = getDolar()
	valor = valor.replace("R$ ", "")
	valor = valor.replace(",", ".")

	v_float = float(valor)
	v_float = round(v_float, 2)

	return v_float