from pg import pygen
import features

if __name__ == '__main__':

  off = ['maps', 'functions', 'classes', 'files', 'containers']

  for name in features.values:
      features.values[name] = name not in off

  line = pygen.generate(features.values)
  print(line)
