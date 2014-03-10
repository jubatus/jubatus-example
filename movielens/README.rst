MovieLens Recommender Example
================================

Usage
----------

First download the dataset and start Jubatus recommender with configuration file (config.json).

::

  mkdir dat
  cd dat
  wget http://www.grouplens.org/system/files/ml-100k.zip
  unzip ml-100k.zip
  cd ..
  jubarecommender -f config.json

C++
::::::::::::

::

  cd cpp
  ./waf configure
  ./waf build
  ./build/ml_update
  ./build/ml_analysis

Python
::::::::::::

::

 cd python
 ./ml_update.py
 ./ml_analyze.py

Ruby
::::::::::::

::

 cd ruby
 ./ml_update.rb
 ./ml_analyze.rb

Java
::::::::::::

::

 cd java
 ./run-update.sh
 ./run-analyze.sh

References
------------------

See http://jubat.us/ and http://www.grouplens.org/node/73
