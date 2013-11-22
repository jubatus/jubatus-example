Twitter Streaming Classification: Location Estimation
=====================================================

Twitter ストリームに流れるジオタグ(位置情報)を学習し、ユーザの入力した文章がどの場所で発信されたものであるかを推定します。

Python と Java の 2 言語で実装されています。いずれも動作は同等です。

準備
----

* Jubatus 0.4.0 以降
  - Jubatus のインストール手順は [Quick Start](http://jubat.us/ja/quickstart.html) を参照してください。

* Twitter API を使用するため、[Twitter Developers サイト](https://dev.twitter.com/apps/new) でアプリケーションを登録し、Consumer Key/Secret, Access Key/Secret を入手してください。

* Python 版
  - Python 2.7 以降
  -  Python モジュール: [Jubatus Python クライアント](http://jubat.us/ja/quickstart.html), [tweepy](https://github.com/tweepy/tweepy)
      - `pip install jubatus tweepy` でインストールすることができます。
  - Twitter API Key
      - train.py を編集し、上記の Consumer Key/Secret, Access Key/Secret 入力してください。

* Java 版
  - Java SE (JDK) 1.5 以降
  - Maven 2
  - Twitter API Key
      - twitter4j.properties を編集し、上記の Consumer Key/Secret, Access Key/Secret 入力してください。

サーバの起動
------------

分類器 (jubaclassifier) を起動します。

```
$ jubaclassifier -f twitter_streaming_location.json -t 0 &
```

Twitter ストリームの学習
------------------------

学習クライアントを実行すると、Twitter ストリームからツイート情報を取得して学習します (学習したデータが表示されます)。
Ctrl-C で停止するまで学習を継続します。

* Python 版
  - `train.py` を実行します。
* Java 版
  - `train.sh` を実行します。

実行例を以下に示します。

```
$ ./train.py
```

取得対象は、東京/北海道/九州の範囲内にあるジオタグが付いたデータです。
ツイートの本文からハッシュタグを取り除いたデータに対して、Tokyo, Hokkaido, Kyusyu のいずれかのラベルを付けて分類器に学習させます。

ユーザの入力した文章の分類
--------------------------

分類クライアントに文章を与えると、その文章がツイートされた場所を推定します。

* Python 版
  - `classify.py` に引数として分類したい文章を引数で与えて実行します。
* Java 版
  - `classify.sh` を引数なしで実行し、表示されたプロンプトに分類したい文章を入力します。

実行例を以下に示します。

```
$ ./classify.py "ビッグサイトに遊びにきた！"
Estimated Location for ビッグサイトに遊びにきた！:
  Tokyo (43503.8398438)
  Hokkaido (16626.625)
  Kyusyu (-41064.7617188)

$ ./classify.py "雪降ってきた"
Estimated Location for 雪降ってきた:
  Hokkaido (31692.171875)
  Tokyo (1090.50634766)
  Kyusyu (-1015.706604)
```

学習が十分に行われていない場合は結果が表示できません。
