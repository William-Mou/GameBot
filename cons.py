import requests
import re
constellation = {"牡羊":"AAxffoP","金牛":"AAxfhqs","雙子":"AAxf5pe","巨蟹":"AAxffoX", "獅子":"AAxf3l1", "處女":"AAxfcJw", "天秤":"AAxf0LJ", "天蠍":"AAxf7ZD", "射手":"AAxeW1G", "摩羯":"AAxfcJH", "水瓶":"AAxffpc", "雙魚":"AAxfjLM"}
def remove_punctuation(line):
    rule = re.compile(u"[^0-9\u4e00-\u9fa5：，。；、]")
    line = rule.sub('',line)
    return line
def find_cons(cons):
    r = requests.get("https://www.msn.com/zh-tw/lifestyle/horoscope/" + cons + "座/ar-" + constellation[cons])
    r = str(r.text)
    ans = str(r[r.find("今日整體",1048): r.find("</div>",r.find("今日整體",1048))])
    ans = ans.replace("</p><p>","空格空格")
    ans = remove_punctuation(ans)
    ans = ans.replace("空格空格", "\n")
    return ans
def all_cons():
    ans = ""
    for i in constellation:
        ans += i +"座：\n"
        ans += find_cons(i)
        ans += "~~~~~~~~~~~~~~~\n\n"
        print(ans)
    return ans