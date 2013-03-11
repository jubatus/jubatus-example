#include <iostream>
#include <fstream>
#include <sstream>
#include <time.h>
#include <sys/time.h>
#include <jubatus/client/recommender_client.hpp>
#include <jubatus/client/recommender_types.hpp>
#include <pficommon/lang/util.h>

using namespace std;
using namespace jubatus;
using namespace jubatus::recommender;
using namespace pfi::lang;

const string NAME = "recommender_ml";

int main(int argc, char* argv[]){
  
  jubatus::recommender::client::recommender r("localhost", 9199, 1.0);

  ifstream ifs("./dat/ml-100k/u.data");
  if (!ifs){
    throw string ("cannot open data file");
  }

  string userid, movieid, rating, mtime;
  datum d;
  int n = 0;
  while((ifs >> userid >> movieid >> rating >> mtime)!=0){
    d.num_values.clear();
    if (n % 1000 == 0)
       cout << n << endl;
    d.num_values.push_back(make_pair(movieid, pfi::lang::lexical_cast<int>(rating)));
    r.update_row(NAME, userid, d);
    n++;
  }
}


