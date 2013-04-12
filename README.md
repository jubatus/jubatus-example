Jubatus Examples
================

1. shogun
   - classifier
   - Python/Ruby/Java
   - 分類器を利用した最も簡単なサンプルです。徳川家、足利家、北条家の各将軍の特徴を学習します。未知の将軍の名前を与えて、どの将軍とおもわれるか推定します。
2. gender
   - classifier
   - C++/Python/Ruby/Java
   - 分類器を利用した最も簡単なサンプルです。服装や髪形などの特徴を学習して、性別を推定します。
3. twitter\_streaming\_lang
   - classifier
   - Python
   - 分類器を利用した応用です。Wikipediaのデータを学習し、Twitterのストリームから受け取った、各つぶやきデータの言語を推定します。
4. twitter\_streaming\_location
   - classifier
   - Python/Java
   - 分類器を利用した応用です。Twitterのストリームから位置情報付きのツイートを学習し、文章がどの地域から発信されたものかを推定します。
5. malware\_classification
   - classifier
   - C++
   - 分類器を利用した応用です。バイナリの実行を受け取って、マルウェアかどうかを推定します。
6. movielens
   - recommender
   - C++/Python
   - レコメンダーを利用した最も簡単なサンプルです。MovieLens という映画の評価情報公開データを利用して、あるユーザーに対して似ているユーザーを表示します。
7. npb\_similar\_player
   - recommender
   - Python
   - レコメンダーを利用した最も簡単なサンプルです。野球選手のプロフィール情報を学習して、未知のそれぞれの選手と最も類似した特徴の選手を探します。
8. rent
   - regression
   - Python
   - 回帰を利用した最も簡単なサンプルです。物件情報から、その物件の家賃を予測します。
9. train\_route
   - graph
   - Python
   - グラフ解析の特に最短路探索を利用した最も簡単なサンプルです。都内の路線の経路情報を学習して、駅間の最短経路を探索します。

|                                     | classifer | recommender | regression | stat | graph | anomaly | Language     |
|-------------------------------------|-----------|-------------|------------|------|-------|---------|--------------|
| 1. shogun                           | :+1:      |             |            |      |       |         | Py/Ru/Ja     |
| 2. gender                           | :+1:      |             |            |      |       |         | C++/Py/Ru/Ja |
| 3. twitter\_streaming\_lang         | :+1:      |             |            |      |       |         | Py           |
| 4. twitter\_streaming\_location     | :+1:      |             |            |      |       |         | Py/Ja        |
| 5. malware\_classification          | :+1:      |             |            |      |       |         | C++          |
| 6. movielens                        |           | :+1:        |            |      |       |         | C++/Py       |
| 7. npb\_similar\_player             |           | :+1:        |            |      |       |         | Py           |
| 8. rent                             |           |             | :+1:       |      |       |         | Py           |
| 9. train\_route                     |           |             |            |      | :+1:  |         | Py           |
