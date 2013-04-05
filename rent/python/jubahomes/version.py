VERSION = (0, 0, 1, '')

def get_version():
  version_string = '%s.%s.%s' % VERSION[0:3]
  if len(VERSION[3]):
    version_string += '-' + VERSION[3]
  return version_string
