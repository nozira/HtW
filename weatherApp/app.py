# coding: utf-8
from flask import Flask, render_template
from flask import request
import funpy.app as funpy


app = Flask(__name__) #インスタンス生成

@app.route('/weather',methods=['GET', 'POST'])
def add_numbers():
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    num = funpy.api(lat,lng)
    return render_template('index.html',message = num)

@app.route("/") #アプリケーション/indexにアクセスが合った場合
def index():
    num = funpy.api(35.681167,139.767052)
    return render_template('index.html',message = num) #/indexにアクセスが来たらtemplates内のindex.htmlが開きます
#ここがサーバーサイドからクライアントサイドへなにかを渡すときのポイントになります。

if __name__ == "__main__":
    # webサーバー立ち上げ
    app.run()
