import os, sys
from conf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader
#, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow
from framework.functions import GetLumi


year=2018
def GetUncYield(path, files, ch = 'ElMu', ilev = '1btag', histopref = 'H', year = 2018, filepref = '',var='', s = 'MuonEff', isdata = False):
  t = TopHistoReader(path, files)
  t.SetLevel(ilev)
  t.SetChan(ch)
  t.SetHistoNamePrefix(histopref)
  t.SetLumi(GetLumi(year)*1000)
  t.SetFileNamePrefix(filepref)
  t.SetIsData(isdata)
  y = t.GetUnc(s=s)
  return y

def GetStatUncYield(path, files, ch = 'ElMu', ilev = '1btag', histopref = 'H', year = 2018, filepref = '',var='', s = 'MuonEff', isdata = False):
  t = TopHistoReader(path, files)
  t.SetLevel(ilev)
  t.SetChan(ch)
  t.SetHistoNamePrefix(histopref)
  t.SetLumi(GetLumi(year)*1000)
  t.SetFileNamePrefix(filepref)
  t.SetIsData(isdata)
  e = t.GetYieldStatUnc()
  y= t. GetYield()
  return e/y


###print Unc efficiencies
sample=[ 'ElecEff','MuonEff', 'Trig','Btag', 'Mistag','PU']
for i in sample:
  print 'Uncertainty %s'%i, GetUncYield(path[year], processDic[year]['t#bar{t}'],s=i)*100 , '%'
print 'Uncertainty MC statistics:', GetStatUncYield(path[year], processDic[year]['t#bar{t}'])*100 , '%'


def GetYields(path, files, ch = 'ElMu', level = '1btag', histopref = 'H', year = 2016, filepref = '', var = '', isdata = False):
  t = TopHistoReader(path, files)
  t.SetLevel(level)
  t.SetChan(ch)
  t.SetHistoNamePrefix(histopref)
  t.SetLumi(GetLumi(year)*1000)
  t.SetFileNamePrefix(filepref)
  t.SetIsData(isdata)  
  y = t.GetYield()
  return y


def GetUncSamples(pr = 't#bar{t}', pr_var='TT_hdamp'):
   ''' Return a systematic uncertainty (relative) ''' 
   nom = GetYields(path[year],processDic[year][pr])
   #print(nom)
   if isinstance(pr_var, list):
     l=len(pr_var)
     v=[]
     for i in range(l): v.append(abs(nom-GetYields(path[year], pr_var[i]))/nom)
     return(max(v))
   else:
     varUp = GetYields(path[year], pr_var+'Up')
     varDo = GetYields(path[year], pr_var+'Down')
     #print varUp, varDo
     return max(abs(nom-varUp)/nom if nom!=0 else 0, abs(nom-varDo)/nom if nom != 0 else 0)
if year==2016:
	sample=['TT_hdamp', 'TT_fsr','TT_isr']
	for i in sample:
		print 'Uncertainty %s'%i, GetUncSamples(pr_var=i)*100 , '%'

	print 'Uncertainty Color reconnection: ', GetUncSamples(pr_var=['TT_colourFlip','TT_QCDbasedCRTune_erdON','TT_GluonMoveCRTune'])*100 , '%'
	print 'Uncertainty UE: ', GetUncSamples(pr_var=['TT_TuneCUETP8M2T4down','TT_TuneCUETP8M2T4up'])*100 , '%'
else:
	print 'Uncertainty hdamp: ', GetUncSamples(pr_var=['TTTo2L2Nu_hdampDown','TTTo2L2Nu_hdampUp'])*100 , '%'
	print 'Uncertainty UE: ', GetUncSamples(pr_var=['TTTo2L2Nu_TuneCP5Down','TTTo2L2Nu_TuneCP5Up'])*100 , '%'


###para MC statistics usar GetYieldStatUnc	
####UNC ElMu 1btag
'''2016

Uncertainty ElecEff 1.36576967133 %
Uncertainty MuonEff 0.569074648953 %
Uncertainty Btag 1.01816836508 %
Uncertainty Mistag 0.156151655216 %
Uncertainty PU 0.309827423061 %
Uncertainty TT_hdamp 43.287409259 %
Uncertainty TT_fsr 4.89071233936 %
Uncertainty TT_isr 1.37371907216 %
Uncertainty Color reconnection:  6.4279063811 %
Uncertainty UE:  1.3617759986 %

#ver4:
Uncertainty ElecEff 1.38502341571 %
Uncertainty MuonEff 1.07479887931 %
Uncertainty Trig 1.37202242485 %
Uncertainty Btag 1.00208619471 %
Uncertainty Mistag 0.156592291713 %
Uncertainty PU 0.31097905819 %
Uncertainty MC statistics: 0.157759046287 %
Uncertainty TT_hdamp 3.57497669792 %
Uncertainty TT_fsr 6.76586491051 %
Uncertainty TT_isr 3.1958015335 %
Uncertainty Color reconnection:  8.34007748568 %
Uncertainty UE:  3.1976934999 %
ME scales (muR muF): 0.09 %



2017
Uncertainty ElecEff 2.29110097319 %
Uncertainty MuonEff 0.471787274038 %
Uncertainty Btag 0.894989031741 %
Uncertainty Mistag 0.0210757501063 %
Uncertainty PU 0.139548592907 %

#nuevos:
Uncertainty ElecEff 2.28821583123 %
Uncertainty MuonEff 0.968622833276 %
Uncertainty Trig 0.0151173730076 %
Uncertainty Btag 1.24327933614 %
Uncertainty Mistag 0.00860735042808 %
Uncertainty PU 0.150976456664 %
Uncertainty hdamp:  0.516617540441 %
Uncertainty UE:  0.336433844419 %
ME scales (muR muF): 0.09 %
PDF unc:  0.02 (1.00 %)
alpha_S:  0.01 (0.33 %)
Total PDF + alpha_S uncertainty: 0.02 (1.06 %)
=====================================================
[1] ISR=1.0, FSR=0.5  (ISR down): 209.0424 (-0.019 %)
[2] ISR=0.5, FSR=1.0  (FSR down): 205.8942 (-1.525 %)
[3] ISR=1.0, FSR=2.0  (ISR up  ): 209.1093 (0.013 %)
[4] ISR=2.0, FSR=1.0  (FSR up  ): 211.0989 (0.964 %)
=====================================================
Uncertainty MC statistics: 0.0492156428369 %

Uncertainty Trig 0.0151173730076 % (ElMu)
Uncertainty Trig 0.022633592206 % (Elec)
Uncertainty Trig 0.0118887749921 % (Muon)

ver4:
Uncertainty ElecEff 2.28245264162 %
Uncertainty MuonEff 0.957201923587 %
Uncertainty Trig 1.34586949068 %
Uncertainty Btag 1.2412204917 %
Uncertainty Mistag 0.00727845848174 %
Uncertainty PU 0.132334647018 %
Uncertainty MC statistics: 0.0492250230446 %
Uncertainty hdamp:  1.06750949582 %
Uncertainty UE:  0.33822135297 %
ME scales (muR muF): 0.09 %
PDF unc:  0.02 (1.00 %)
alpha_S:  0.01 (0.33 %)
Total PDF + alpha_S uncertainty: 0.02 (1.05 %)
=====================================================
[1] ISR=1.0, FSR=0.5  (ISR down): 205.1659 (-0.018 %)
[2] ISR=0.5, FSR=1.0  (FSR down): 202.0503 (-1.536 %)
[3] ISR=1.0, FSR=2.0  (ISR up  ): 205.2260 (0.012 %)
[4] ISR=2.0, FSR=1.0  (FSR up  ): 207.1850 (0.966 %)
=====================================================



2018

ver2:

Uncertainty ElecEff 1.45536384096 %
Uncertainty MuonEff 0.691738696678 %
Uncertainty Trig 0.0114955670024 %
Uncertainty Btag 1.68172523298 %
Uncertainty Mistag 0.0195560372348 %
Uncertainty PU 0.235163174927 %
Uncertainty hdamp:  1.04350815868 %
Uncertainty UE:  1.02756719235 %
ME scales (muR muF):  0.09 %
PDF unc:  0.00 (0.67 %)
alpha_S:  0.00 (0.22 %)
Total PDF + alpha_S uncertainty: 0.00 (0.71 %)
=====================================================
[1] ISR=1.0, FSR=0.5  (ISR down): 207.9158 (-0.001 %)
[2] ISR=0.5, FSR=1.0  (FSR down): 0.0000 (-100.000 %)
[3] ISR=1.0, FSR=2.0  (ISR up  ): 0.0000 (-100.000 %)
[4] ISR=2.0, FSR=1.0  (FSR up  ): 0.0000 (-100.000 %)
=====================================================
Uncertainty MC statistics: 0.0548823153702 %

Uncertainty Trig 0.0114955670024 % (ElMu)
Uncertainty Trig 0.0176360888214 % (Elec)
Uncertainty Trig 0.0308137823454 % (Muon)


ver4: (corregido lo trigSF)

Uncertainty ElecEff 1.47140555582 %
Uncertainty MuonEff 0.71091552333 %
Uncertainty Trig 1.14393153557 %
Uncertainty Btag 1.65074584517 %
Uncertainty Mistag 0.0139339442573 %
Uncertainty PU 0.245049947871 %
Uncertainty MC statistics: 0.0548836568938 %
Uncertainty hdamp:  1.03116006186 %
Uncertainty UE:  0.98866544572 %
ME scales (muR muF):  0.08 % %
PDF unc:  0.00 (0.67 %)
alpha_S:  0.00 (0.22 %)
Total PDF + alpha_S uncertainty: 0.00 (0.71 %)
=====================================================
[1] ISR=1.0, FSR=0.5  (ISR down): 206.1182 (-0.001 %)
[2] ISR=0.5, FSR=1.0  (FSR down): 0.0000 (-100.000 %)
[3] ISR=1.0, FSR=2.0  (ISR up  ): 0.0000 (-100.000 %)
[4] ISR=2.0, FSR=1.0  (FSR up  ): 0.0000 (-100.000 %)
=====================================================


'''
