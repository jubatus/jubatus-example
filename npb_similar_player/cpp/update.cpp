#include <iostream>
#include <fstream>
#include <sstream>
#include <time.h>
#include <sys/time.h>
#include <jubatus/util/lang/cast.h>
#include <jubatus/client/recommender_client.hpp>
#include <jubatus/client/recommender_types.hpp>

using namespace std;
using namespace jubatus;
using namespace jubatus::recommender;
using namespace jubatus::util::lang;

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
    d.add_number("打率", lexical_cast<double>(bave));
    d.add_number("試合数", lexical_cast<double>(games));
    d.add_number("打席", lexical_cast<double>(pa));
    d.add_number("打数", lexical_cast<double>(atbat));
    d.add_number("安打", lexical_cast<double>(hit));
    d.add_number("本塁打", lexical_cast<double>(homerun));
    d.add_number("打点", lexical_cast<double>(runsbat));
    d.add_number("盗塁", lexical_cast<double>(stolen));
    d.add_number("四球", lexical_cast<double>(bob));
    d.add_number("死球", lexical_cast<double>(hbp));
    d.add_number("三振", lexical_cast<double>(strikeout));
    d.add_number("犠打", lexical_cast<double>(sacrifice));
    d.add_number("併殺打", lexical_cast<double>(dp));
    d.add_number("長打率", lexical_cast<double>(slg));
    d.add_number("出塁率", lexical_cast<double>(obp));
    d.add_number("OPS", lexical_cast<double>(ops));
    d.add_number("RC27", lexical_cast<double>(rc27));
    d.add_number("XR27", lexical_cast<double>(xr27));

    r.update_row(pname, d);
  }

  return 0;
}

