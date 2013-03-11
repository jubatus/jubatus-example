#include <iostream>
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

  for (int i = 0 ; i< 943 ; i++)
  {
        similar_result sr = r.similar_row_from_id(NAME, pfi::lang::lexical_cast<string>(i), 10);
        cout <<  "user " << i << " is similar to :";
      for (size_t i = 1; i < sr.size(); ++i){
        cout <<  sr[i].first << ", ";
      }
      cout << endl;
  }



}


