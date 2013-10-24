#include <iostream>
#include <fstream>
#include <sstream>
#include <time.h>
#include <sys/time.h>
#include <jubatus/client/recommender_client.hpp>
#include <jubatus/client/recommender_types.hpp>
#include <pficommon/lang/util.h>

using namespace std;
using jubatus::client::common::datum;
using jubatus::recommender::client::recommender;

const string NAME = "recommender_ml";

int main(int argc, char* argv[]) {

  jubatus::recommender::client::recommender r("localhost", 9199, NAME, 5);

  ifstream ifs("../dat/ml-100k/u.data");
  if (!ifs) {
    throw string("cannot open data file");
  }

  string userid, movieid, rating, mtime;
  int n = 0;
  while ((ifs >> userid >> movieid >> rating >> mtime) != 0) {
    datum d;
    if (n % 1000 == 0)
       cout << n << endl;
    d.add_number(movieid, pfi::lang::lexical_cast<int>(rating));
    r.update_row(userid, d);
    n++;
  }
}


