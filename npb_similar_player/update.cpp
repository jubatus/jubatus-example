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

    ifstream ifs("./dat/baseball.csv");
    if (!ifs) {
        throw string ("cannot open data file");
    }

    string pname, team, bave, games, pa, atbat, hit, homerun,
        runsbat, stolen, bob, hbp, strikeout, sacrifice,
        dp, slg, obp, ops, rc27, xr27;
    datum d;

    string temp_string;
    while ((ifs >> temp_string) !=0) {
        replace(temp_string.begin(), temp_string.end(), ',', ' ');
        istringstream iss(temp_string);
        iss >> pname >> team >> bave >> games >> pa >> atbat
            >> hit >> homerun >> runsbat >> stolen >> bob
            >> hbp >> strikeout >> sacrifice >> dp >> slg
            >> obp >> ops >> rc27 >> xr27;

        d.string_values.clear();
        d.num_values.clear();

        d.string_values.push_back(make_pair("チーム", team));
        d.num_values.push_back(make_pair("打率", pfi::lang::lexical_cast<float>(bave)));
        d.num_values.push_back(make_pair("試合数", pfi::lang::lexical_cast<float>(games)));
        d.num_values.push_back(make_pair("打席", pfi::lang::lexical_cast<float>(pa)));
        d.num_values.push_back(make_pair("打数", pfi::lang::lexical_cast<float>(atbat)));
        d.num_values.push_back(make_pair("安打", pfi::lang::lexical_cast<float>(hit)));
        d.num_values.push_back(make_pair("本塁打", pfi::lang::lexical_cast<float>(homerun)));
        d.num_values.push_back(make_pair("打点", pfi::lang::lexical_cast<float>(runsbat)));
        d.num_values.push_back(make_pair("盗塁", pfi::lang::lexical_cast<float>(stolen)));
        d.num_values.push_back(make_pair("四球", pfi::lang::lexical_cast<float>(bob)));
        d.num_values.push_back(make_pair("死球", pfi::lang::lexical_cast<float>(hbp)));
        d.num_values.push_back(make_pair("三振", pfi::lang::lexical_cast<float>(strikeout)));
        d.num_values.push_back(make_pair("犠打", pfi::lang::lexical_cast<float>(sacrifice)));
        d.num_values.push_back(make_pair("併殺打", pfi::lang::lexical_cast<float>(dp)));
        d.num_values.push_back(make_pair("長打率", pfi::lang::lexical_cast<float>(slg)));
        d.num_values.push_back(make_pair("出塁率", pfi::lang::lexical_cast<float>(obp)));
        d.num_values.push_back(make_pair("OPS", pfi::lang::lexical_cast<float>(ops)));
        d.num_values.push_back(make_pair("RC27", pfi::lang::lexical_cast<float>(rc27)));
        d.num_values.push_back(make_pair("XR27", pfi::lang::lexical_cast<float>(xr27)));

        r.update_row(NAME, pname, d);
    }

    return 0;
}

