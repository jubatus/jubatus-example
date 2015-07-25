#include <iostream>
#include <string>
#include <utility>
#include <vector>

#include <jubatus/client.hpp>

using std::make_pair;
using std::pair;
using std::string;
using std::vector;
using jubatus::client::common::datum;
using jubatus::classifier::estimate_result;
using jubatus::classifier::labeled_datum;

datum make_datum(const string& name) {
	datum d;
	d.add_string("name", name);
	return d;
}

void train(jubatus::classifier::client::classifier client){
	vector<labeled_datum> train_data;
	
	train_data.push_back(labeled_datum("徳川",   make_datum("家康")));
	train_data.push_back(labeled_datum("徳川",   make_datum("秀忠")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家光")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家綱")));
	train_data.push_back(labeled_datum("徳川",   make_datum("綱吉")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家宣")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家継")));
	train_data.push_back(labeled_datum("徳川",   make_datum("吉宗")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家重")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家治")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家斉")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家慶")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家定")));
	train_data.push_back(labeled_datum("徳川",   make_datum("家茂")));
	// train_data.push_back(labeled_datum("徳川",   make_datum("慶喜")));
	
	train_data.push_back(labeled_datum("足利",   make_datum("尊氏")));
	train_data.push_back(labeled_datum("足利",   make_datum("義詮")));
	train_data.push_back(labeled_datum("足利",   make_datum("義満")));
	train_data.push_back(labeled_datum("足利",   make_datum("義持")));
	train_data.push_back(labeled_datum("足利",   make_datum("義量")));
	train_data.push_back(labeled_datum("足利",   make_datum("義教")));
	train_data.push_back(labeled_datum("足利",   make_datum("義勝")));
	train_data.push_back(labeled_datum("足利",   make_datum("義政")));
	train_data.push_back(labeled_datum("足利",   make_datum("義尚")));
	train_data.push_back(labeled_datum("足利",   make_datum("義稙")));
	train_data.push_back(labeled_datum("足利",   make_datum("義澄")));
	train_data.push_back(labeled_datum("足利",   make_datum("義稙")));
	train_data.push_back(labeled_datum("足利",   make_datum("義晴")));
	train_data.push_back(labeled_datum("足利",   make_datum("義輝")));
	train_data.push_back(labeled_datum("足利",   make_datum("義栄")));
	// train_data.push_back(labeled_datum("足利",   make_datum("義昭")));
	
	train_data.push_back(labeled_datum("北条",   make_datum("時政")));
	train_data.push_back(labeled_datum("北条",   make_datum("義時")));
	train_data.push_back(labeled_datum("北条",   make_datum("泰時")));
	train_data.push_back(labeled_datum("北条",   make_datum("経時")));
	train_data.push_back(labeled_datum("北条",   make_datum("時頼")));
	train_data.push_back(labeled_datum("北条",   make_datum("長時")));
	train_data.push_back(labeled_datum("北条",   make_datum("政村")));
	train_data.push_back(labeled_datum("北条",   make_datum("時宗")));
	train_data.push_back(labeled_datum("北条",   make_datum("貞時")));
	train_data.push_back(labeled_datum("北条",   make_datum("師時")));
	train_data.push_back(labeled_datum("北条",   make_datum("宗宣")));
	train_data.push_back(labeled_datum("北条",   make_datum("煕時")));
	train_data.push_back(labeled_datum("北条",   make_datum("基時")));
	train_data.push_back(labeled_datum("北条",   make_datum("高時")));
	train_data.push_back(labeled_datum("北条",   make_datum("貞顕")));
	// train_data.push_back(labeled_datum("北条",   make_datum("守時")));
	
	client.train(train_data);
	
}

void predict(jubatus::classifier::client::classifier client){
	vector<string> test_name;
	test_name.push_back("慶喜");
	test_name.push_back("義昭");
	test_name.push_back("守時");
	
	vector<datum> test_data;
	for(size_t i = 0; i < test_name.size(); ++i){
		test_data.push_back(make_datum(test_name[i]));
	}
	vector<vector<estimate_result> > results = client.classify(test_data);
	
	for (size_t i = 0; i < results.size(); ++i) {
		estimate_result& r = results[i][0];
		for (size_t j = 0; j < results[i].size(); ++j) {
			const estimate_result& temp = results[i][j];
			if(r.score < temp.score){
				r = temp;
			}
		}
		std::string name = test_name[i];
		std::cout << r.label << " " << name <<  std::endl;
	}
}

int main() {
	string host = "127.0.0.1";
	int port = 9199;
	string name = "test";
	
	jubatus::classifier::client::classifier client(host, port, name, 1.0);
	
	train(client);
	predict(client);
	
	return 0;
}