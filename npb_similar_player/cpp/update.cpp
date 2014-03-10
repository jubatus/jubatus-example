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
    throw string ("cannot open data file");
  }

  string pname, team, bave, games, pa, atbat, hit, homerun,
      runsbat, stolen, bob, hbp, strikeout, sacrifice,
      dp, slg, obp, ops, rc27, xr27;

  string temp_string;
  while ((ifs >> temp_string) !=0) {
    jubatus::client::common::datum d;
    replace(temp_string.begin(), temp_string.end(), ',', ' ');
    istringstream iss(temp_string);
    iss >> pname >> team >> bave >> games >> pa >> atbat
        >> hit >> homerun >> runsbat >> stolen >> bob
        >> hbp >> strikeout >> sacrifice >> dp >> slg
        >> obp >> ops >> rc27 >> xr27;

    d.add_string("チーム", team);
    d.add_number("打率", pfi::lang::lexical_cast<float>(bave));
    d.add_number("試合数", pfi::lang::lexical_cast<float>(games));
    d.add_number("打席", pfi::lang::lexical_cast<float>(pa));
    d.add_number("打数", pfi::lang::lexical_cast<float>(atbat));
    d.add_number("安打", pfi::lang::lexical_cast<float>(hit));
    d.add_number("本塁打", pfi::lang::lexical_cast<float>(homerun));
    d.add_number("打点", pfi::lang::lexical_cast<float>(runsbat));
    d.add_number("盗塁", pfi::lang::lexical_cast<float>(stolen));
    d.add_number("四球", pfi::lang::lexical_cast<float>(bob));
    d.add_number("死球", pfi::lang::lexical_cast<float>(hbp));
    d.add_number("三振", pfi::lang::lexical_cast<float>(strikeout));
    d.add_number("犠打", pfi::lang::lexical_cast<float>(sacrifice));
    d.add_number("併殺打", pfi::lang::lexical_cast<float>(dp));
    d.add_number("長打率", pfi::lang::lexical_cast<float>(slg));
    d.add_number("出塁率", pfi::lang::lexical_cast<float>(obp));
    d.add_number("OPS", pfi::lang::lexical_cast<float>(ops));
    d.add_number("RC27", pfi::lang::lexical_cast<float>(rc27));
    d.add_number("XR27", pfi::lang::lexical_cast<float>(xr27));

    r.update_row(pname, d);
  }

  return 0;
}

