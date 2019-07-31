import os, sys
from conf import *
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader
#, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow
from framework.functions import GetLumi


year=2016
def GetUncYield(path, files, ch = 'ElMu', ilev = '1btag', histopref = 'H', year = 2016, filepref = '',var='', s = 'MuonEff', isdata = False):
  t = TopHistoReader(path, files)
  t.SetLevel(ilev)
  t.SetChan(ch)
  t.SetHistoNamePrefix(histopref)
  t.SetLumi(GetLumi(year)*1000)
  t.SetFileNamePrefix(filepref)
  t.SetIsData(isdata)
  y = t.GetUnc(s=s)
  return y

###print Unc efficiencies
sample=[ 'ElecEff','MuonEff', 'Btag', 'Mistag','PU']
for i in sample:
  print 'Uncertainty %s'%i, GetUncYield(path[year], processDic[year]['t#bar{t}'],s=i)*100 , '%'



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

sample=['TT_hdamp', 'TT_fsr','TT_isr']
for i in sample:
  print 'Uncertainty %s'%i, GetUncSamples(pr_var=i)*100 , '%'

print 'Uncertainty Color reconnection: ', GetUncSamples(pr_var=['TT_colourFlip','TT_QCDbasedCRTune_erdON','TT_GluonMoveCRTune'])*100 , '%'
print 'Uncertainty UE: ', GetUncSamples(pr_var=['TT_TuneCUETP8M2T4down','TT_TuneCUETP8M2T4up'])*100 , '%'


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


2017
Uncertainty ElecEff 2.29110097319 %
Uncertainty MuonEff 0.471787274038 %
Uncertainty Btag 0.894989031741 %
Uncertainty Mistag 0.0210757501063 %
Uncertainty PU 0.139548592907 %

2018

Uncertainty ElecEff 1.44184435486 %
Uncertainty MuonEff 0.212901950225 %
Uncertainty Btag 1.65182008635 %
Uncertainty Mistag 0.0116354098169 %
Uncertainty PU 0.246132333336 %


'''
