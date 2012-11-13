家賃推測
========

概要
----
駅からの距離、専有面積、築年数 等の条件から家賃を推測する。

扱うトピック
------------
- jubaregression の使い方
- python-client の使い方

扱うデータ
----------
dat/rent-data.csv
賃貸情報サイトから取得した「S町の1Rマンション」の賃貸情報

使い方
------

::

  $ python setup.py install
  $ jubaregression &
  $ jubahomes -t dat/rent-data.csv -a dat/myhome.yml
  $ edit dat/myhome.yml
  $ jubahomes -a dat/myhome.yml
  $ edit dat/myhome.yml
  $ jubahomes -a dat/myhome.yml
     :

補足
----
- プログラムを修正すれば、ペット可、ロフト付き、風呂トイレ別 などの条件を追加することもできます。
