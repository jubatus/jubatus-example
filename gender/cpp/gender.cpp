#include <iostream>
#include <string>
#include <utility>
#include <vector>

#include <jubatus/client.hpp>

using std::make_pair;
using std::pair;
using std::string;
using std::vector;
using jubatus::common::datum;
using jubatus::classifier::estimate_result;

datum make_datum(const string& hair, const string& top, const string& bottom, double height) {
  datum d;
  d.add_string("hair", hair);
  d.add_string("top", top);
  d.add_string("bottom", bottom);

  d.add_number("height", height);
  return d;
}

int main() {
  string host = "127.0.0.1";
  int port = 9199;
  string name = "test";

  jubatus::classifier::client::classifier client(host, port, 1.0, name);
  
  vector<pair<string, datum> > train_data;
  train_data.push_back(labeled_datum("male",   make_datum("short", "sweater", "jeans", 1.70)));
  train_data.push_back(labeled_datum("female", make_datum("long", "shirt", "skirt", 1.56)));
  train_data.push_back(labeled_datum("male",   make_datum("short", "jacket", "chino", 1.65)));
  train_data.push_back(labeled_datum("female", make_datum("short", "T shirt", "jeans", 1.72)));
  train_data.push_back(labeled_datum("male",   make_datum("long", "T shirt", "jeans", 1.82)));
  train_data.push_back(labeled_datum("female", make_datum("long", "jacket", "skirt", 1.43)));
  //train_data.push_back(labeled_datum("male",   make_datum("short", "jacket", "jeans", 1.76)));
  //train_data.push_back(labeled_datum("female", make_datum("long", "sweater", "skirt", 1.52)));

  client.train(train_data);

  vector<datum> test_data;
  test_data.push_back(make_datum("short", "T shirt", "jeans", 1.81));
  test_data.push_back(make_datum("long", "shirt", "skirt", 1.50));

  vector<vector<estimate_result> > results = client.classify(test_data);

  for (size_t i = 0; i < results.size(); ++i) {
    for (size_t j = 0; j < results[i].size(); ++j) {
      const estimate_result& r = results[i][j];
      std::cout << r.label << " " << r.score << std::endl;
    }
    std::cout << std::endl;
  }
}
