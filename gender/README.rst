==========
 性別分類
==========

性別分類は最も簡単なJubatusのサンプルです。
人の特徴（髪型、服装、身長）から、性別を推定します。
一番簡単なjubaclassifierのサンプルです。


準備
====

- Jubauts 0.5.0 以降をインストールします。
- 各言語ごとのクライアントはそれぞれ用意します。


サーバーの起動
==============

jubaclassifierを起動します。
設定はjubatusのデフォルト設定を利用します。

::

 $ jubaclassifier --configpath /path/to/jubatus/share/jubatus/example/config/classifier/perceptron.json &


実行
====

各言語のサンプルを実行してください。
50行程度の非常に短いサンプルなので、中を読むとどのように動くかの理解が深まります。
