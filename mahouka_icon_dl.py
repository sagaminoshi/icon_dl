import sys
import os
import requests
import shutil

url = "https://mahouka.jp/assets/img/special/twitter_icon/"

#ディレクトリ"mahouka_icon"を作成
if not os.path.exists("mahouka_icon"):
	os.makedirs("mahouka_icon")
	print("ディレクトリ " + os.path.dirname(os.path.abspath(__file__)) + "/mahouka_iconを作成しました。")

#画像のダウンロード
for i in range(1,27):
    episode = str(i).zfill(2)
    for j in range(1,7):
        num = str(j).zfill(2)
        if os.path.exists(".\\mahouka_icon/" + episode+"_"+num+".jpg") == 0:
            r = requests.get(url + episode+"/"+num+".jpg", stream=True)
            if r.status_code == 200:
                with open(".\\mahouka_icon/" + episode+"_"+num+".jpg", 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
                    print (episode+"_"+num+".jpg をダウンロードしました。")