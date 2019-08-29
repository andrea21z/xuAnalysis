import os, sys
from conf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader
#, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow
from framework.functions import GetLumi

def GetYield(path, files, ch = 'ElMu', level = 'dilepton', histopref = 'H', year = 2016, filepref = '', var = '', isdata = False):
  t = TopHistoReader(path, files)
  t.SetLevel(level)
  t.SetChan(ch)
  t.SetHistoNamePrefix(histopref)
  t.SetLumi(GetLumi(2016)*1000)
  #t.SetLumi(GetLumi(year)*1000)
  #t.SetLumi(1)
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
#'#2jets' #'1btag'#'dilepton'
year=2018

print 'yields year: %i'%year
'''
print 'ElMu (bb): ', GetYield(path[year], processDic[year]['bb'], ch='ElMu', level=lev, year=year)
print 'Muon (bb): ', GetYield(path[year], processDic[year]['bb'], ch='Muon', level=lev, year=year)
print 'Elec (bb): ', GetYield(path[year], processDic[year]['bb'], ch='Elec', level=lev, year=year)
'''
print 'ElMu (DY): ', GetYield(path[year], processDic[year]['DY'], ch='ElMu', level=lev, year=year)
print 'Muon (DY): ', GetYield(path[year], processDic[year]['DY'], ch='Muon', level=lev, year=year)
print 'Elec (DY): ', GetYield(path[year], processDic[year]['DY'], ch='Elec', level=lev, year=year)

print 'ElMu (Nonprompt): ', GetYield(path[year], processDic[year]['Nonprompt'], ch='ElMu', level=lev, year=year)
print 'Muon (Nonprompt): ', GetYield(path[year], processDic[year]['Nonprompt'], ch='Muon', level=lev, year=year)
print 'Elec (Nonprompt): ', GetYield(path[year], processDic[year]['Nonprompt'], ch='Elec', level=lev, year=year)

print 'ElMu (tW): ', GetYield(path[year], processDic[year]['tW'], ch='ElMu', level=lev, year=year)
print 'Muon (tW): ', GetYield(path[year], processDic[year]['tW'], ch='Muon', level=lev, year=year)
print 'Elec (tW): ', GetYield(path[year], processDic[year]['tW'], ch='Elec', level=lev, year=year)

print 'ElMu (VV): ', GetYield(path[year], processDic[year]['VV'], ch='ElMu', level=lev, year=year)
print 'Muon (VV): ', GetYield(path[year], processDic[year]['VV'], ch='Muon', level=lev, year=year)
print 'Elec (VV): ', GetYield(path[year], processDic[year]['VV'], ch='Elec', level=lev, year=year)

print 'ElMu (ttV): ', GetYield(path[year], processDic[year]['ttV'], ch='ElMu', level=lev, year=year)
print 'Muon (ttV): ', GetYield(path[year], processDic[year]['ttV'], ch='Muon', level=lev, year=year)
print 'Elec (ttV): ', GetYield(path[year], processDic[year]['ttV'], ch='Elec', level=lev, year=year)

print 'ElMu (background): ', GetYield(path[year], processDic[year]['DY'], ch='ElMu', level=lev, year=year)+GetYield(path[year], processDic[year]['ttV'], ch='ElMu', level=lev, year=year)+GetYield(path[year], processDic[year]['VV'], ch='ElMu', level=lev, year=year)+GetYield(path[year], processDic[year]['tW'], ch='ElMu', level=lev, year=year)+GetYield(path[year], processDic[year]['Nonprompt'], ch='ElMu', level=lev, year=year)
print 'Muon (background): ', GetYield(path[year], processDic[year]['DY'], ch='Muon', level=lev, year=year)+GetYield(path[year], processDic[year]['ttV'], ch='Muon', level=lev, year=year)+GetYield(path[year], processDic[year]['VV'], ch='Muon', level=lev, year=year)+GetYield(path[year], processDic[year]['tW'], ch='Muon', level=lev, year=year)+GetYield(path[year], processDic[year]['Nonprompt'], ch='Muon', level=lev, year=year)
print 'Elec (background): ', GetYield(path[year], processDic[year]['DY'], ch='Elec', level=lev, year=year)+GetYield(path[year], processDic[year]['ttV'], ch='Elec', level=lev, year=year)+GetYield(path[year], processDic[year]['VV'], ch='Elec', level=lev, year=year)+GetYield(path[year], processDic[year]['tW'], ch='Elec', level=lev, year=year)+GetYield(path[year], processDic[year]['Nonprompt'], ch='Elec', level=lev, year=year)

print 'TT ElMu : ', GetYield(path[year], processDic[year]['t#bar{t}'], ch='ElMu', level=lev, year=year)
print 'TT Muon : ', GetYield(path[year], processDic[year]['t#bar{t}'], ch='Muon', level=lev, year=year)
print 'TT Elec : ', GetYield(path[year], processDic[year]['t#bar{t}'], ch='Elec', level=lev, year=year)

print 'ElMu (data): ', GetYield(path[year], processDic[year]['data'], ch='ElMu', level=lev, year=year,isdata = True)
print 'Muon (data): ', GetYield(path[year], processDic[year]['data'], ch='Muon', level=lev, year=year, isdata=True)
print 'Elec (data): ', GetYield(path[year], processDic[year]['data'], ch='Elec', level=lev, year=year, isdata=True)

##### DIFERENCIA DE YIELDS ENTRE DOS ANIOS
year = 2016
year2 = 2018
print 'yields difference between %i and %i'%(year, year2)

print 'ElMu (DY) difference: ', (GetYield(path[year], processDic[year]['DY'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['DY'], ch='ElMu', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['DY'], ch='ElMu', level=lev, year=year)
print 'Muon (DY) difference: ', (GetYield(path[year], processDic[year]['DY'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['DY'], ch='Muon', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['DY'], ch='Muon', level=lev, year=year)
print 'Elec (DY) difference: ', (GetYield(path[year], processDic[year]['DY'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['DY'], ch='Elec', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['DY'], ch='Elec', level=lev, year=year)

print 'ElMu (Nonprompt) difference: ', (GetYield(path[year], processDic[year]['Nonprompt'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['Nonprompt'], ch='ElMu', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['Nonprompt'], ch='ElMu', level=lev, year=year)
print 'Muon (Nonprompt) difference: ', (GetYield(path[year], processDic[year]['Nonprompt'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['Nonprompt'], ch='Muon', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['Nonprompt'], ch='Muon', level=lev, year=year)
print 'Elec (Nonprompt) difference: ', (GetYield(path[year], processDic[year]['Nonprompt'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['Nonprompt'], ch='Elec', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['Nonprompt'], ch='Elec', level=lev, year=year)

print 'ElMu (tW) difference: ', (GetYield(path[year], processDic[year]['tW'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['tW'], ch='ElMu', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['tW'], ch='ElMu', level=lev, year=year)
print 'Muon (tW) difference: ', (GetYield(path[year], processDic[year]['tW'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['tW'], ch='Muon', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['tW'], ch='Muon', level=lev, year=year)
print 'Elec (tW) difference: ', (GetYield(path[year], processDic[year]['tW'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['tW'], ch='Elec', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['tW'], ch='Elec', level=lev, year=year)

print 'ElMu (VV) difference: ', (GetYield(path[year], processDic[year]['VV'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['VV'], ch='ElMu', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['VV'], ch='ElMu', level=lev, year=year)
print 'Muon (VV) difference: ', (GetYield(path[year], processDic[year]['VV'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['VV'], ch='Muon', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['VV'], ch='Muon', level=lev, year=year)
print 'Elec (VV) difference: ', (GetYield(path[year], processDic[year]['VV'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['VV'], ch='Elec', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['VV'], ch='Elec', level=lev, year=year)

print 'ElMu (ttV) difference: ', (GetYield(path[year], processDic[year]['ttV'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['ttV'], ch='ElMu', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['ttV'], ch='ElMu', level=lev, year=year)
print 'Muon (ttV) difference: ', (GetYield(path[year], processDic[year]['ttV'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['ttV'], ch='Muon', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['ttV'], ch='Muon', level=lev, year=year)
print 'Elec (ttV) difference: ', (GetYield(path[year], processDic[year]['ttV'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['ttV'], ch='Elec', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['ttV'], ch='Elec', level=lev, year=year)

print 'TT ElMu difference: ', (GetYield(path[year], processDic[year]['t#bar{t}'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['t#bar{t}'], ch='ElMu', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['t#bar{t}'], ch='ElMu', level=lev, year=year)
print 'TT Muon difference: ', (GetYield(path[year], processDic[year]['t#bar{t}'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['t#bar{t}'], ch='Muon', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['t#bar{t}'], ch='Muon', level=lev, year=year)
print 'TT Elec difference: ', (GetYield(path[year], processDic[year]['t#bar{t}'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['t#bar{t}'], ch='Elec', level=lev, year=year2))*100/GetYield(path[year], processDic[year]['t#bar{t}'], ch='Elec', level=lev, year=year)

print 'ElMu (data) difference: ', (GetYield(path[year], processDic[year]['data'], ch='ElMu', level=lev, year=year,isdata = True)-GetYield(path[year2], processDic[year2]['data'], ch='ElMu', level=lev, year=year2,isdata = True))*100/GetYield(path[year], processDic[year]['data'], ch='ElMu', level=lev, year=year,isdata = True)
print 'Muon (data) difference: ', (GetYield(path[year], processDic[year]['data'], ch='Muon', level=lev, year=year, isdata=True)-GetYield(path[year2], processDic[year2]['data'], ch='Muon', level=lev, year=year2,isdata = True))*100/GetYield(path[year], processDic[year]['data'], ch='Muon', level=lev, year=year,isdata = True)
print 'Elec (data) difference: ', (GetYield(path[year], processDic[year]['data'], ch='Elec', level=lev, year=year, isdata=True)-GetYield(path[year2], processDic[year2]['data'], ch='Elec', level=lev, year=year2,isdata = True))*100/GetYield(path[year], processDic[year]['data'], ch='Elec', level=lev, year=year,isdata = True)

##comparacion 2016 con TOP-17-001
year=2016
year2=2015

print 'ElMu (DY) difference: ', (GetYield(path[year], processDic[year]['DY'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['DY'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['DY'], ch='ElMu', level=lev, year=year)
print 'Muon (DY) difference: ', (GetYield(path[year], processDic[year]['DY'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['DY'], ch='Muon', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['DY'], ch='Muon', level=lev, year=year)
print 'Elec (DY) difference: ', (GetYield(path[year], processDic[year]['DY'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['DY'], ch='Elec', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['DY'], ch='Elec', level=lev, year=year)

print 'ElMu (Nonprompt) difference: ', (GetYield(path[year], processDic[year]['Nonprompt'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['Nonprompt'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['Nonprompt'], ch='ElMu', level=lev, year=year)
print 'Muon (Nonprompt) difference: ', (GetYield(path[year], processDic[year]['Nonprompt'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['Nonprompt'], ch='Muon', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['Nonprompt'], ch='Muon', level=lev, year=year)
print 'Elec (Nonprompt) difference: ', (GetYield(path[year], processDic[year]['Nonprompt'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['Nonprompt'], ch='Elec', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['Nonprompt'], ch='Elec', level=lev, year=year)

print 'ElMu (tW) difference: ', (GetYield(path[year], processDic[year]['tW'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['tW'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['tW'], ch='ElMu', level=lev, year=year)
print 'Muon (tW) difference: ', (GetYield(path[year], processDic[year]['tW'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['tW'], ch='Muon', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['tW'], ch='Muon', level=lev, year=year)
print 'Elec (tW) difference: ', (GetYield(path[year], processDic[year]['tW'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['tW'], ch='Elec', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['tW'], ch='Elec', level=lev, year=year)

print 'ElMu (VV) difference: ', (GetYield(path[year], processDic[year]['VV'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['VV'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['VV'], ch='ElMu', level=lev, year=year)
print 'Muon (VV) difference: ', (GetYield(path[year], processDic[year]['VV'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['VV'], ch='Muon', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['VV'], ch='Muon', level=lev, year=year)
print 'Elec (VV) difference: ', (GetYield(path[year], processDic[year]['VV'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['VV'], ch='Elec', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['VV'], ch='Elec', level=lev, year=year)

print 'ElMu (ttV) difference: ', (GetYield(path[year], processDic[year]['ttV'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['ttV'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['ttV'], ch='ElMu', level=lev, year=year)
print 'Muon (ttV) difference: ', (GetYield(path[year], processDic[year]['ttV'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['ttV'], ch='Muon', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['ttV'], ch='Muon', level=lev, year=year)
print 'Elec (ttV) difference: ', (GetYield(path[year], processDic[year]['ttV'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['ttV'], ch='Elec', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['ttV'], ch='Elec', level=lev, year=year)

print 'TT ElMu difference: ', (GetYield(path[year], processDic[year]['t#bar{t}'], ch='ElMu', level=lev, year=year)-GetYield(path[year2], processDic[year2]['t#bar{t}'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['t#bar{t}'], ch='ElMu', level=lev, year=year)
print 'TT Muon difference: ', (GetYield(path[year], processDic[year]['t#bar{t}'], ch='Muon', level=lev, year=year)-GetYield(path[year2], processDic[year2]['t#bar{t}'], ch='Muon', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['t#bar{t}'], ch='Muon', level=lev, year=year)
print 'TT Elec difference: ', (GetYield(path[year], processDic[year]['t#bar{t}'], ch='Elec', level=lev, year=year)-GetYield(path[year2], processDic[year2]['t#bar{t}'], ch='Elec', level=lev, year=year2,filepref = 'Tree_'))*100/GetYield(path[year], processDic[year]['t#bar{t}'], ch='Elec', level=lev, year=year)

print 'ElMu (data) difference: ', (GetYield(path[year], processDic[year]['data'], ch='ElMu', level=lev, year=year,isdata = True)-GetYield(path[year2], processDic[year2]['data'], ch='ElMu', level=lev, year=year2,filepref = 'Tree_',isdata = True))*100/GetYield(path[year], processDic[year]['data'], ch='ElMu', level=lev, year=year,isdata = True)
print 'Muon (data) difference: ', (GetYield(path[year], processDic[year]['data'], ch='Muon', level=lev, year=year, isdata=True)-GetYield(path[year2], processDic[year2]['data'], ch='Muon', level=lev, year=year2,filepref = 'Tree_',isdata = True))*100/GetYield(path[year], processDic[year]['data'], ch='Muon', level=lev, year=year,isdata = True)
print 'Elec (data) difference: ', (GetYield(path[year], processDic[year]['data'], ch='Elec', level=lev, year=year, isdata=True)-GetYield(path[year2], processDic[year2]['data'], ch='Elec', level=lev, year=year2,filepref = 'Tree_',isdata = True))*100/GetYield(path[year], processDic[year]['data'], ch='Elec', level=lev, year=year,isdata = True)





path = '/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/temp2017/'
#print 'TT ElMu: ', GetYield('/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/tempyear/', 'TT', ch='ElMu', var='',level=lev, year=year)
#print 'TT Muon: ', GetYield('/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/tempyear/', 'TT', ch='Muon', level=lev, year=year)
#print 'TT Elec: ', GetYield('/mnt_pool/ciencias_users/user/andreatf/PAFnanoAOD/tempyear/', 'TT', ch='Elec', level=lev, year=year)


'''print 'DY ElMu: ', GetYield(path[year], process[year]['DY'      ], ch='ElMu', level=lev, year=year)
print 'DY Muon: ', GetYield(path[year], process[year]['DY'      ], ch='Muon', level=lev, year=year)
print 'DY Elec: ', GetYield(path[year], process[year]['DY'      ], ch='Elec', level=lev, year=year)
print '   ElMu: ', GetYield(path[year], process[year]['data'], isdata = True, ch='ElMu', level=lev, year=year)
print '   Muon: ', GetYield(path[year], process[year]['data'], isdata = True, ch='Muon', level=lev, year=year)
print '   Elec: ', GetYield(path[year], process[year]['data'], isdata = True, ch='Elec', level=lev, year=year)


pathold = '/nfs/fanae/user/juanr/nanoAOD/Top_temp/feb22/'
dataold = ['SingleMuon', 'SingleElectron', 'DoubleMuon', 'DoubleEG', 'MuonEG']
print '########### OLD'
print 'TT ElMu: ', GetYield(pathold, 'TTTo2L2Nu', filepref = 'Tree_', year=year)
print 'TT Muon: ', GetYield(pathold, 'TTTo2L2Nu', filepref = 'Tree_', ch = 'Muon', year=year)
print 'TT Elec: ', GetYield(pathold, 'TTTo2L2Nu', filepref = 'Tree_', ch = 'Elec', year=year)
print 'DY ElMu: ', GetYield(pathold, 'DYJetsToLL_M_50', filepref = 'Tree_', ch='ElMu', level=lev, year=year)
print 'DY Muon: ', GetYield(pathold, 'DYJetsToLL_M_50', filepref = 'Tree_', ch='Muon', level=lev, year=year)
print 'DY Elec: ', GetYield(pathold, 'DYJetsToLL_M_50', filepref = 'Tree_', ch='Elec', level=lev, year=year)
print '   ElMu: ', GetYield(pathold, dataold    , filepref = 'Tree_', isdata = True, ch='ElMu', level=lev, year=year)
print '   Muon: ', GetYield(pathold, dataold    , filepref = 'Tree_', isdata = True, ch='Muon', level=lev, year=year)
print '   Elec: ', GetYield(pathold, dataold    , filepref = 'Tree_', isdata = True, ch='Elec', level=lev, year=year)'''
