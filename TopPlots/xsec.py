import os, sys
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis/',1)[0]+'/xuAnalysis/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow

### Input and output
path = 'histofiles/'
#path = 'temp/'
outpath = '~/www/temp/wz/'

### Definition of the processes
process = {
'WZ'  : 'WZTo3LNU',
'VV'  : 'WWTo2L2Nu,ZZTo2L2Nu',
'DY'  : 'DYJetsToLL_M_10to50,DYJetsToLL_MLL50',
'top' : 'TT,tW_noFullHad,tbarW_noFullHad',
'bkg' : 'WWTo2L2Nu,ZZTo2L2Nu,DYJetsToLL_M_10to50,DYJetsToLL_MLL50,TT,tW_noFullHad,tbarW_noFullHad',
'data': 'DoubleMuon,SingleMuon,HighEGJet'}
#prk = ['VV','WZ']
prk = ['VV', 'DY', 'top', 'WZ']

### Definition of colors for the processes
colors ={
'WZ'  : kYellow-4,
'VV'  : kGray+2,
'DY'  : kAzure-8,
'top' : kRed+1,
'data': 1}

lumi = 296.1

t = TopHistoReader(path)
t.SetLumi(lumi)
t.SetLevel(2)

def GetYield(pr):
 filename = pr if not pr in process.keys() else process[pr]
 if pr == 'data': t.SetIsData(True)
 else           : t.SetIsData(False)
 y = 0
 for ch in ['eee', 'emm', 'mee', 'mmm']:
   y += t.GetYield(filename,ch)
 return y

xsecth = 1.2*(47.13/4.42965)

wz   = GetYield('WZ')
dy   = GetYield('DY')
top  = GetYield('top')
bkg  = GetYield('bkg')
data = GetYield('data')

print 'top       : %1.2f'%top
print 'dy        : %1.2f'%dy
print 'Total bkg : %1.2f'%bkg
print 'wz        : %1.2f'%wz
print 'data      : %1.2f'%data

xsec   = (data-bkg)/wz*xsecth
xsecup = (data+sqrt(data)-bkg)/wz*xsecth
xsecdo = (data-sqrt(data)-bkg)/wz*xsecth
errxsec  = (abs(xsec-xsecup)+abs(xsec-xsecdo))/2
rerrxsec = (errxsec)/xsec*100

print '\nPredicted cross section: %1.2f\n'%xsecth
print 'Inclusive cross section: %1.2f +/- %1.2f (%1.2f %s)\n'%(xsec, errxsec, rerrxsec, '%')
