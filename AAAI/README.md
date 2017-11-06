# AAAIの類似した論文探索

jubatusの近傍探索機能を使ってAAAIのaccepted paperから類似した論文を探します。

## データセットの用意

[UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/AAAI+2014+Accepted+Papers) からデータセットをダウンロードし、`data/papers.csv`に保存します。

```
$ mkdir data
$ wget -O data/papers.csv https://archive.ics.uci.edu/ml/machine-learning-databases/00307/%5bUCI%5d%20AAAI-14%20Accepted%20Papers%20-%20Papers.csv
```

## jubatus サーバの起動

今回は文字列をスペース区切り、bm25で重み付けをするコンフィグを使います。

```json
{
  "converter" : {
    "string_filter_types": {},
    "string_filter_rules":[],
    "num_filter_types": {},
    "num_filter_rules": [],
    "string_types": {
    },
    "string_rules":[
      { "key" : "*", "type" : "space", "sample_weight" : "tf", "global_weight" : "bm25" }
    ],
    "num_types": {},
    "num_rules": [
      {"key" : "*", "type" : "num"}
    ]
  },
  "parameter" : {
    "hash_num" : 512
  },
  "method": "lsh"
}
```

サーバは以下のコマンドで起動します。

```
$ jubanearest_neighbor -f "aaai.json" &
```

## クライントの実行
各言語のディレクトリに移動し、`README.md` を参照してください。
