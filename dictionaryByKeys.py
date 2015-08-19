# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 00:10:57 2015

@author: aduba_000
"""
import collections

mydict = {'carl':40,
          'alan':2,
          'bob':1,
          'danny':3}
d = collections.OrderedDict()

for key in sorted(mydict.iterkeys()):
    d[key] = mydict[key]
    #print "%s: %s" % (key, mydict[key])

def getSortedDict(mydict):
    d = collections.OrderedDict()
    for key in sorted(mydict.iterkeys()):
        d[key] = mydict[key]
    return d
    
print getSortedDict(mydict)
    
