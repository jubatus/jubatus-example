#include <jubatus/core/plugin.hpp>
#include <jubatus/util/lang/cast.h>
#include <jubatus/core/fv_converter/exception.hpp>
#include <map>
#include <string>

class normalize_num_feature : public jubatus::core::fv_converter::num_feature {
  public:
    void add_feature(const std::string& key, double value,
                           std::vector<std::pair<std::string, float> >& ret_fv) const;
    normalize_num_feature(double max, double min);

  private:
    double min_val;
    double max_val;

};


