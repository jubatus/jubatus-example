#include <jubatus/core/plugin.hpp>
#include <pficommon/lang/cast.h>
#include <jubatus/core/fv_converter/exception.hpp>
#include <map>
#include <string>

class normalize_num_filter : public jubatus::core::fv_converter::num_filter {
  public:
    normalize_num_filter(double max, double min);
    double filter(double value) const;

  private:
    double min_val;
    double max_val;
    normalize_num_filter();

};


