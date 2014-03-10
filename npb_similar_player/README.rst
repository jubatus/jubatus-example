===================
 NPBの似た野手探し
===================

2012年日本プロ野球の野手成績を学習し、似たタイプの選手を出力します。


準備
====

- Jubauts 0.5.0 + Python クライアントをインストールします。

  - Python クライアントは `pip install jubatus` でインストールできます。

- このサンプルでは、 num_feature の plugin を利用することもできます。plugin は以下の手順でインストールします。

  - `/path/to/jubatus` にはJubatusのインストールパス（ `/usr/local` など）を指定して下さい。

::

 $ cd normalize_plugin
 $ ./waf configure --prefix=/path/to/jubatus
 $ ./waf build
 $ ./waf install


サーバーの起動
==============

jubarecommender を起動します。

::

 $ jubarecommender --configpath npb_similar_player.json &

plugin を利用する場合は、 npb_similar_player.plugin.json を指定します。


実行
====

dat/baseball.csv は、 プロ野球データfreak(http://baseball-data.com/) から取得した「規定打席の1/3以上の全野手のデータ」を打席数順にソートしたものです。

このデータを学習し、それぞれの似たタイプの選手を表示します。

::

 $ python update.py
 $ python analyze.py
