果物の統計分析(Java版)
===============

オレンジ・りんご・メロンの直径・重さ・価格を学習し、フルーツ毎にパラメータの合計値や標準偏差など統計分析をします。


準備
====

- Jubauts 0.5.0 以降 + JDK 1.7以降 をインストールします。


サーバーの起動
==============

jubastat を起動します。
```
 $ jubastat --configpath stat.json &
```

実行
============

`../dat/fruit.csv` は人工的に作成したオレンジ・りんご・メロンの直径・重さ・価格の情報です。

`fruit.csv` のデータを学習し、 それぞれのフルーツに対して合計や標準偏差などを取得します。
ソースコードのビルド、学習及び分析結果の表示はシェルスクリプトから起動します。

```
  $ ./run.sh
 sum :orangediameter 1503.4
 sdv :orangediameter 10.868084075829087
 max :orangediameter 49.9
 min :orangediameter -2.1
 ent :orangediameter 2.1964245302595096
 mmt :orangediameter 28.911538461538463
 sum :orangeweight 10394.399999999996
 sdv :orangeweight 54.922588261272196
 max :orangeweight 299.4
 min :orangeweight 39.5
 ent :orangeweight 2.1964245302595096
 mmt :orangeweight 196.12075471698105
 sum :orangeprice 1636.0
 sdv :orangeprice 7.936154992801973
 (以下略)
```

プログラムを修正し、様々なデータで統計分析を実施してみてはいかがでしょうか。
