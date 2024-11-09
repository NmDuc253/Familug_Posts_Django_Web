import requests
from bs4 import BeautifulSoup as bs


result = []
r = requests.get("https://ketqua04.net")
tree = bs(markup=r.text, features='html.parser')
nodes = tree.find_all(name='td', attrs={'class': 'chu17 need_blank'})

for node in nodes:
	result.append(node.text)


def check(number):
	if str(number) in result:
		return "Xin chúc mừng, bạn đã trúng loto"
	else:
		return "Chúc bạn may mắn lần sau"


def main():
	print(result)
	print(check(23))


if __name__ == '__main__':
	main()
