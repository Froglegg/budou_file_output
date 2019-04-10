import budou
import pyperclip
parser = budou.get_parser('tinysegmenter')
result= parser.parse('募尽ヱオラ北読レフ記世ヱナヘク鉄日未つどだれ自地ト用4目ぜみ合伊るす育制かルし入径ハネテ審活ムハモア産格情据灯もぎけ。将携で王32掲メ調止ぱで朝国フユウエ特門ウロヌ続表た億頃い点応ばだ良喜チ愛所ひぱねイ間間成ずらばト者公ぽたるろ関潤資冊もみゆの。')
sourceFile= open('output.txt', 'w', encoding="utf-8")
print(result['html_code'], file = sourceFile)
pyperclip.copy(result['html_code'])
sourceFile.close()
