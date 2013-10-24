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
  jubatus::recommender::client::recommender r("localhost", 9199, NAME, 1.0);

  ifstream ifs("./dat/baseball.csv");
  if (!ifs) {
    throw string("cannot open data file");
  }

  string pname, team, bave, games, pa, atbat, hit, homerun,
      runsbat, stolen, bob, hbp, strikeout, sacrifice,
      dp, slg, obp, ops, rc27, xr27;
  string temp_string;

  while ((ifs >> temp_string) != 0) {
    jubatus::client::common::datum d;
    replace(temp_string.begin(), temp_string.end(), ',', ' ');
    istringstream iss(temp_string);
    iss >> pname >> team >> bave >> games >> pa >> atbat
        >> hit >> homerun >> runsbat >> stolen >> bob
        >> hbp >> strikeout >> sacrifice >> dp >> slg
        >> obp >> ops >> rc27 >> xr27;
    
    std::vector<id_with_score> sr = r.similar_row_from_id(pfi::lang::lexical_cast<string>(pname), 4);
    cout << "player " << pname << " is similar to :";
    for (size_t i = 1; i < sr.size(); ++i) {
      cout << " " << sr[i].id;
    }
    cout << endl;
  }
  return 0;
}

