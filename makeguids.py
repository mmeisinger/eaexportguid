#!/usr/bin/env python

"""
@file makeguids.py
@author Michael Meisinger
@brief Create guid named copies of EA export PNG files for permanent links
"""
import os, os.path, re, shutil, sys

BASE_DIR = "."
GUIDMAP_DIR = "js/data/guidmaps"
OUTPUT_DIR = "guidpng"

def add_guidmap(file):
    try:
        f = open(BASE_DIR+"/"+GUIDMAP_DIR+"/"+file, 'r')
        return f.read().split()
    finally:
        f.close()

def add_file(guidentry):
    guid, ppath, diagnum = re.search(r'^([^\/]+)/(.*?)EA(\d+)\.htm', guidentry).groups()
    diagnum = int(diagnum) + 1
    pngname = BASE_DIR+"/EARoot/"+ppath+"EA"+str(diagnum)+".png"
    #print guid, ppath, diagnum
    #print "", pngname

    if os.path.exists(pngname):
        #print "copy", pngname, BASE_DIR+"/"+OUTPUT_DIR+"/"+guid+".png"
        shutil.copy(pngname,BASE_DIR+"/"+OUTPUT_DIR+"/"+guid+".png")

def makeguids():
    global BASE_DIR
    guids = []
    print "makeguids.py - Create GUID diagram images from EA Export, M. Meisinger, Aug 2011"

    if len(sys.argv) > 1:
        BASE_DIR = sys.argv[1]

    if os.path.exists(BASE_DIR+"/"+GUIDMAP_DIR):
        print "Using dir:", BASE_DIR
    else:
        print "Dir", BASE_DIR, "does not contain EA export files"
        sys.exit(1)


    [guids.extend(add_guidmap(item)) for item in os.listdir(BASE_DIR+"/"+GUIDMAP_DIR) if item.endswith(".xml")]
    #[it for sublist in [add_guidmap(item) for item in os.listdir(BASE_DIR+"/"+GUIDMAP_DIR) if item.endswith(".xml")] for it in sublist]
    #print guids

    target = BASE_DIR+"/"+OUTPUT_DIR
    if not os.path.exists(target):
        os.mkdir(target)

    [add_file(entry) for entry in guids]

if __name__ == "__main__":
    makeguids()
