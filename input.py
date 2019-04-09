# copy/paste japanese text into the parser.parse('japanese-text-goes-here'). Make sure you have a "output.txt" file created in your file directory.
import budou
parser = budou.get_parser('tinysegmenter')
result= parser.parse('今日も元気です')
sourceFile= open('output.txt', 'w', encoding="utf-8")
print(result['html_code'], file = sourceFile)
sourceFile.close()
