#include <iostream>
#include <jubatus/client/recommender_client.hpp>
#include <jubatus/client/recommender_types.hpp>
#include <jubatus/util/lang/util.h>

using namespace std;
using namespace jubatus;
using namespace jubatus::recommender;
using namespace jubatus::util::lang;

const string NAME = "recommender_ml";

int main(int argc, char* argv[]) {
  jubatus::recommender::client::recommender r("localhost", 9199, NAME, 5);

  for (int i = 1; i <= 943; i++) {
    std::vector<id_with_score> sr
        = r.similar_row_from_id(jubatus::util::lang::lexical_cast<string>(i), 10);
    cout <<  "user " << i << " is similar to :";
    for (size_t i = 1; i < sr.size(); ++i) {
      cout <<  sr[i].id << ", ";
    }
    cout << endl;
  }
}


