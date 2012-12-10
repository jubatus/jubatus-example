Train Route: Pseudo Shortest Path by Hops
=========================================

Graph の `shortest_path` API を使用して、鉄道路線の最短経路 (ホップ数) を推定します。

準備
----

* Jubatus 0.3.4 + Python クライアントをインストールしてください。

サーバの起動
------------

jubagraph を起動します。

```
$ jubagraph &
```

グラフの作成
------------

鉄道の接続を表すグラフを作成します。

```
$ ./create_graph.py
=== Station IDs ===
0       品川
1       大崎
4       田町
...
139     中野
144     四ツ谷
147     御茶ノ水
```

駅名に対応する駅 ID (グラフ上の node ID) が出力されます。

経路の探索
----------

2 つの駅 ID から最短経路を検索します。

```
$ ./search_route.py 0 144
Pseudo-Shortest Path (hops) from 0 to 144:
  0     品川
  4     田町
  7     浜松町
  10    新橋
  13    有楽町
  16    東京
  19    神田
  147   御茶ノ水
  144   四ツ谷
```

謝辞
----

このプログラムでは駅間接続情報のデータ取得に [駅データ.jp](http://www.ekidata.jp/) の API を利用しています。
