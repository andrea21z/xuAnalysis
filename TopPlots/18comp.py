import os, sys
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis/',1)[0]+'/xuAnalysis/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow
from conf import *

def GetYield(path, files, ch = 'ElMu', level = 'dilepton', histopref = 'H', lumi = 41200, filepref = '', var = '', isdata = False):
  t = TopHistoReader(path, files)
  t.SetLevel(level)
  t.SetChan(ch)
  t.SetHistoNamePrefix(histopref)
  t.SetLumi(lumi)
  t.SetFileNamePrefix(filepref)
  t.SetIsData(isdata)
  if var != '':
    pref = histopref + '_' if histopref != '' else ''
    h = t.GetNamedHisto(pref + var + '_' + ch + '_' + level)
    y = h.Integral()
  else:  
    y = t.GetYield()
  return y

lev = 'dilepton'
year = 2017

def pyields(year = 2017, lev = 'dilepton'):
  print '### Year: ', year, ', level: ', lev
  print 'TT ElMu: ', GetYield(path[year], process[year]['t#bar{t}'], ch='ElMu', level=lev, lumi = GetLumi(year)*1000)
  print 'TT Muon: ', GetYield(path[year], process[year]['t#bar{t}'], ch='Muon', level=lev, lumi = GetLumi(year)*1000)
  print 'TT Elec: ', GetYield(path[year], process[year]['t#bar{t}'], ch='Elec', level=lev, lumi = GetLumi(year)*1000)
  print 'DY ElMu: ', GetYield(path[year], process[year]['DY'      ], ch='ElMu', level=lev, lumi = GetLumi(year)*1000)
  print 'DY Muon: ', GetYield(path[year], process[year]['DY'      ], ch='Muon', level=lev, lumi = GetLumi(year)*1000)
  print 'DY Elec: ', GetYield(path[year], process[year]['DY'      ], ch='Elec', level=lev, lumi = GetLumi(year)*1000)
  print '   ElMu: ', GetYield(path[year], process[year]['data'], isdata = True, ch='ElMu', level=lev, lumi = GetLumi(year)*1000)
  print '   Muon: ', GetYield(path[year], process[year]['data'], isdata = True, ch='Muon', level=lev, lumi = GetLumi(year)*1000)
  print '   Elec: ', GetYield(path[year], process[year]['data'], isdata = True, ch='Elec', level=lev, lumi = GetLumi(year)*1000)

pyields(2017, lev)
pyields(2018, lev)
