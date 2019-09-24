import os,sys
sys.path.append(os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/')
from plotter.TopHistoReader import TopHistoReader
from plotter.WeightReader import WeightReader
from ROOT.TMath import Sqrt as sqrt
from ttxsec.NonpromptDataDriven import NonpromptDD
from conf import *

### Input and output
year = 2018
path = path[year]

outpath = '/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver5/tablas_nonprompt/'%year

def DrawNonprompt(lev = '2jets'):
  d = NonpromptDD(path,outpath,'ElMu',lev, process=processDic[year] , lumi = GetLumi(year)*1000) 
  d.PrintSSyields('SSyields_'+lev, lev)
  for chan in ['ElMu']:
    d.PrintNonpromptEstimate('NonpromptDD_'+lev+'_'+chan, chan, lev)


for ilev in ['dilepton','2jets']:
  DrawNonprompt(lev=ilev)

