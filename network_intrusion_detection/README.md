# Network Intrusion Detection (KDD Cup 1999)

## 概要

Jubatusのjubaanomalyを使ったネットワーク侵入検出のサンプルです。
サンプルとして、KDD Cup (Knowledge Discovery and Data Mining Cup)の結果データを学習させ、外れ値を検出します。

## データ

以下の要領で学習データをダウンロードします。
```
$ wget http://kdd.ics.uci.edu/databases/kddcup99/kddcup.data_10_percent.gz
$ gunzip kddcup.data_10_percent.gz
$ mv kddcup.data_10_percent kddcup.data_10_percent.txt
```

## 実行

### サーバの起動
jubaanomalyを起動します。
```
$ jubaanomaly --configpath config.json
```
    
### 実行(python)
python クライアントを起動し、外れ値検知を行います。
```
$ cd python
$ python anomaly.py
```

### 実行(ruby)
ruby クライアントを起動し、外れ値検知を行います。
```
$ cd ruby
$ ruby anomaly.rb
```
