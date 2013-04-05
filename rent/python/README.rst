==========
 家賃推測
==========

駅からの距離、専有面積、築年数 等の条件から家賃を推測します。


準備
====

- Jubauts 0.4.0 + Python クライアントをインストールします。

  - Python クライアントは `pip install jubatus` でインストールできます。


サーバーの起動
==============

jubaregression を起動します。

::

 $ jubaregression --configpath rent.json &


インストール
============

このサンプルでは、コマンドラインアプリケーションをインストールして利用します。

::

  $ python setup.py install


使い方
======

dat/rent-data.csv は賃貸情報サイトから取得した「S町の1Rマンション」の賃貸情報です。

rent-data.csv を学習し、 dat/myhome.yaml に記載した条件の物件の家賃を推測しましょう。

::

  $ jubahomes -t dat/rent-data.csv -a dat/myhome.yml

dat/myhome.yaml を変更し、いろんな条件で物件の家賃を推測しましょう。

::

  $ edit dat/myhome.yml
  $ jubahomes -a dat/myhome.yml
  $ edit dat/myhome.yml
  $ jubahomes -a dat/myhome.yml
     :

非常に簡単なサンプルです。プログラムを修正し、ペット可、ロフト付き、風呂トイレ別 などの条件を追加してみてはいかがでしょうか。
