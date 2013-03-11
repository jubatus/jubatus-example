def options(opt):
    opt.load('compiler_cxx')


def configure(conf):
  conf.env.CXXFLAGS += ['-O2', '-Wall', '-g', '-pipe']
  conf.load('compiler_cxx')
  conf.check_cfg(package = 'pficommon', args = '--cflags --libs')
  conf.check_cxx(lib = 'msgpack')
  conf.check_cxx(lib = 'jubatus_mpio')
  conf.check_cxx(lib = 'jubatus_msgpack-rpc')


def build(bld):
  bld.program(
    source = 'ml_update.cpp',
    target = 'ml_update',
    use = 'PFICOMMON MSGPACK JUBATUS_MPIO JUBATUS_MSGPACK-RPC',
    )

  bld.program(
    source = 'ml_analysis.cpp',
    target = 'ml_analysis',
    use = 'PFICOMMON MSGPACK JUBATUS_MPIO JUBATUS_MSGPACK-RPC',
    )

