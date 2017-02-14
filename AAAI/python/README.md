##python クライアントの実行方法

### 学習

はじめにデータを学習させます。
オプションを何も付けない場合、タイトルのテキストだけを使って学習を行います。
`-a` オプションをつけるとタイトルに加えアブストラクトのテキストも使い学習します。

```
(タイトルだけで学習する場合)
$ python set_row.py

(タイトル + アブストラクトで学習する場合)
$ python set_row.py -a
```

### 分析

分析はanalyze.pyを実行します。
第一引数に論文のID(0~397)を与えると、その論文の近傍の論文のタイトルとスコアが3つ表示されます。

```
$ python analyze.py 1
query is : "Source Free" Transfer Learning for Text Classification
similar paper is ID:3 "Lifetime Lexical Variation in Social Media"(score: 0.7109375)
similar paper is ID:0 "Kernelized Bayesian Transfer Learning"(score: 0.701171875)
similar paper is ID:2 "A Generalization of Probabilistic Serial to Randomized Social Choice"(score: 0.689453125)
```
