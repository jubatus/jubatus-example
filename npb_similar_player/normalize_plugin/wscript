subdirs = 'src'

def options(opt):
  opt.load('compiler_cxx')
  opt.recurse(subdirs)

def configure(conf):
  conf.env.CXXFLAGS += ['-O2', '-Wall', '-g', '-pipe']
  conf.load('compiler_cxx')

  conf.check_cxx(lib = 'jubaconverter')

  # for clients
  conf.check_cxx(lib = 'msgpack')
  conf.check_cfg(package = 'pficommon', args = '--cflags --libs')
  conf.check_cxx(header_name = 'pficommon/network/mprpc.h')

  conf.recurse(subdirs)

def build(bld):
  bld.recurse(subdirs)
