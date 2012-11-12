#include <jubatus/plugin.hpp>
#include <pficommon/lang/cast.h>
#include <jubatus/fv_converter/exception.hpp>
#include <map>
#include <string>

class normalize_num_feature : public jubatus::fv_converter::num_feature {
  public:
    void add_feature(const std::string& key, double value,
                           std::vector<std::pair<std::string, float> >& ret_fv) const;
    normalize_num_feature(double max, double min);

  private:
    double min_val;
    double max_val;

};


