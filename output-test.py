import budou
parser = budou.get_parser('tinysegmenter')
result= parser.parse('今日も元気です')
sourceFile= open('test.txt', 'w', encoding="utf-8")
print(result['html_code'], file = sourceFile)
sourceFile.close()
