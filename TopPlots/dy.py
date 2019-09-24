import os,sys
sys.path.append(os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/')
from plotter.TopHistoReader import TopHistoReader
from plotter.WeightReader import WeightReader
from ROOT.TMath import Sqrt as sqrt
from ttxsec.DrellYanDataDriven import DYDD
from conf import *

### Input and output
year = 2016
path = path[year]
DYsamples   = processDic[year]['DY']
datasamples = processDic[year]['data']

outpath = '/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver5/tablas_DY/'%year

def DrawDYDD(lev = '2jets', doSF = False):
  if not doSF and lev == 'MET': return 
  d = DYDD(path,outpath,'ElMu',lev, DYsamples=DYsamples, DataSamples=datasamples, lumi = GetLumi(year)*1000) 
  lab = 'SF' if doSF else 'OF'
  d.PrintDYestimate(doSF,  'DYDD_'+lev+'_'+lab)

def DrawDYDDnjets(lev='2jets'):
  d = DYDD(path,outpath,lev)
  d.PrintDYSFnjets()

for ilev in ['dilepton','1btag','2jets']:
  DrawDYDD(lev=ilev)


