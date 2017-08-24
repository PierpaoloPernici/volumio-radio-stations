import ConfigParser
import os

print "["

def PrintEntry(thisfile):
  String1 = ""
  Config = ConfigParser.ConfigParser()
  Config.read(thisfile)
  url=ConfigSectionMap(Config,"playlist")['file1']
  name=ConfigSectionMap(Config,"playlist")['title1']
  ## {"service":"webradio","name":"SomaFM: Groove Salad","uri":"http://somafm.com/groovesalad256.pls"},
  String1 = '{"service":"webradio","name":"%s","uri":"%s"},' % (name,url)
  return String1

def ConfigSectionMap(Config,section):
  dict1 = {}
  options = Config.options(section)
  for option in options:
      try:
          dict1[option] = Config.get(section, option)
          #if dict1[option] == -1:
          #    DebugPrint("skip: %s" % option)
      except:
          print("exception on %s!" % option)
          dict1[option] = None
  return dict1

for filename in os.listdir('.'):
  if filename.endswith(".pls"):
    print  PrintEntry(filename)

print "]"


