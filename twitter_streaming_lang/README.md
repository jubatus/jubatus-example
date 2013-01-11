Twitter Streaming Classification
================================

各言語版の Wikipedia データを Jubatus (Classifier) に学習させ、Twitter ストリームの言語を推定します。

![Screenshot](https://github.com/jubatus/jubatus-example/raw/master/twitter_streaming_lang/screenshot.png)

準備
----

* Jubatus 0.4.0 + Python クライアント、[tweepy](https://github.com/tweepy/tweepy) をインストールしてください。

* 各言語版の Wikipedia 要約データをダウンロードしてください (2 言語以上)。

  - 英語版: http://dumps.wikimedia.org/jawiki/latest/jawiki-latest-abstract.xml
  - 日本語版: http://dumps.wikimedia.org/enwiki/latest/enwiki-latest-abstract.xml
  - ドイツ語版: http://dumps.wikimedia.org/dewiki/latest/dewiki-latest-abstract.xml
  - ...

* Twitter API を使用するため、[Twitter Developers サイト](https://dev.twitter.com/apps/new) でアプリケーションを登録し、Consumer Key/Secret, Access Key/Secret を入手してください。

  - 入手したキーは `classify-twitter-stream.py` に記入してください。

サーバの起動
------------

jubaclassifier を起動します。

```
$ jubaclassifier --thread 12 --configpath twitter_streaming_lang.json &
```

学習
----

学習クライアントで、ダウンロードした要約データを学習させます。

引数にはラベル (言語) と Wikipedia 要約データの XML ファイルを指定します。

```
$ python train-wiki-abstract.py ja jawiki-latest-abstract.xml &
$ python train-wiki-abstract.py en enwiki-latest-abstract.xml &
$ python train-wiki-abstract.py de dewiki-latest-abstract.xml &
```

複数言語の学習を並行して走らせることができます。

分類
----

分類クライアントで、Twitter のパブリックタイムラインに流れるツイートの言語を推定 (分類) します。

学習クライアントの実行途中でも分類クライアントは実行できます。

引数にラベルを指定すると、該当するツイートが赤字で表示されます。

```
$ python classify-twitter-stream.py ja
```
