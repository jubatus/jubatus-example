==========
 自然言語分類
==========

欧米の言語を見分ける事は並の日本人には困難です。
しかし各言語はスペース区切りで単語を分割できる上、各単語は言語固有の物が数多くあるのでそこに注目することで分類が可能です。

準備
====

- Jubauts 0.4.0 + Ruby クライアントをインストールします

  - Ruby クライアントは `gem install jubatus` でインストールできます


サーバーの起動
==============

jubaclassifier を起動します

```
 $ jubaclassifier -f space_split.json &
```


実行
====

***_train.txtというファイルをWikipediaのそれぞれのページから言語サンプルとして用意してあります。それらを行単位で言語名とのペアでJubatusに学習させています。
Jubatusは受け取った文字列をスペースで区切り言語名と関連付けて学習します。

```
 $ ruby train.rb
 train Nederland : Religie ...
 train France : Articles détaillés : Royaumes francs, Mérovingiens, Caroling ...
 train Germany : Berlin ...
 ...
```

という形でだーっと出力が流れたら成功です。出力は例えば
train Germany : foo bar
と書かれていれば「foo bar」という文字列に「Germany」というラベルを付けてJubatusに学習させた事を意味しています。
学習したJubatusを試すにはtest.rbを実行します。

```
 $ ruby test.rb
 > this is a pen（←手で入力する
 [["America", 0.18081830441951752],
 ["Italia", 0.06510651856660843],
 ["Nederland", 0.042192161083221436],
 ["Germany", -0.02702118270099163],
 ["France", -0.15504489839076996]]
```

このように出力されたら、「this is a penという文字列は英語である可能性が濃厚」という事を意味します。他の単語も試してみましょう。

non_split.json というJSONファイルも用意してあります。
こちらは受け取ったデータをスペース区切りなどをせず一行単位で特徴量としてJubatusに解釈させる設定です。
行の完全一致でしか学習が行われなくなるのでtest.rbの結果がうまく行かなくなることが観測できます。

```
$ jubaclassifier -f non_split.json &
 $ ruby train.rb
 $ ruby test.rb
 > this is a pen（←手で入力する
 [] （←良い結果が得られない
```

各***_train.txtファイルはそれぞれWikipediaからの抜粋です。著作権はWikipediaに帰属します。