#!/usr/bin/python
# coding:utf-8

import sys
import string
import ConfigParser
import os


def cnfread(_baseini):
    ConfDict = {}
    for line in open(_baseini):
        if line.startswith('#'):
            continue
        if "=" in line:
            key, value = line.split('=', 1)
            ConfDict[key] = value.strip()
    return ConfDict


def rdini():
    cf = ConfigParser.ConfigParser()
    cf.read('path.cnf')
    opts = cf.options("path")
    baseini = cf.get("path", "baseini")
    newini = cf.get("path", "newini")
    return baseini, newini


def cmpini(_onedict, _twodict):
    nolist = []
    inlist = []
    basekeys = _onedict.keys()
    newkeys = _twodict.keys()
    for key in basekeys:
        if key not in newkeys:
            nolist.append(key)
            continue
        if cmp(_onedict[key], _twodict[key]) != 0:
            inlist.append(key)
            continue
    return nolist, inlist


def diffprint(_bnolist, _inlist, _nnolist, _basedict, _newdict):
    # print "--femas.ini比对结果：--".decode("utf-8").encode("gbk")
    print "--femas.ini比对结果：--"
    if _bnolist:
        # print "##删减的参数##".decode("utf-8").encode("gbk")
        print "##删减的参数##"
        for key in _bnolist:
            print key + "=" + _basedict[key]
    if _nnolist:
        # print "##新增的参数##".decode("utf-8").encode("gbk")
        print "##新增的参数##"
        for key in _nnolist:
            print key + "=" + _newdict[key]
    if _inlist:
        # print "##配置不一致的参数##".decode("utf-8").encode("gbk")
        print "##配置不一致的参数##"
        for key in _inlist:
            print key + "=" + _basedict[key]
            print key + "=" + _newdict[key]
    print "---------------------"


def main():
    baseini, newini = rdini()
    basedict = cnfread(baseini)
    newdict = cnfread(newini)
    bnolist, inlist = cmpini(basedict, newdict)
    nnolist, _ = cmpini(newdict, basedict)
    diffprint(bnolist, inlist, nnolist, basedict, newdict)


if __name__ == "__main__":
    main()
