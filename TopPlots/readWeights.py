import os,sys
sys.path.append(os.path.abspath(__file__).rsplit('/xuAnalysis_all/',1)[0]+'/xuAnalysis_all/')
from plotter.TopHistoReader import TopHistoReader
from plotter.WeightReader import WeightReader
from ROOT.TMath import Sqrt as sqrt
from framework.functions import GetLumi


### Input and output
'''
path = '/mnt_pool/ciencias_users/user/juanr/test/PAFnanoAOD/temp2017/'
sample = 'TTTo2L2Nu'

pathToTrees = '/pool/cienciasrw/userstorage/juanr/nanoAODv4/2017/'
motherfname = 'TTTo2L2Nu'
'''

year = 2018

path = '/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver5/'%year
sample = 'TTTo2L2Nu'# 'TTTo2L2Nu'

pathToTrees = '/pool/cienciasrw/userstorage/juanr/nanoAODv4/22jul2019/%s/'%year
motherfname = 'TTTo2L2Nu_TuneCP5'#'TT_TuneCUETP8M2T4'#

if year == 2016:
  #sample='TTTo2L2Nu'
  #motherfname = 'TTTo2L2Nu_TuneCP5_PSweights'
  sample = 'TT'
  motherfname = 'TT_TuneCUETP8M2T4'

outpath = '/nfs/fanae/user/andreatf/PAFnanoAOD/temp%s_new/ver5/Weights/'%year

## PDF and scale systematics
def DrawWeightSystematics(sample, chan = 'ElMu', lev = '1btag'):
  w = WeightReader(path, outpath, chan, lev, sampleName = sample, pathToTrees=pathToTrees, motherfname=motherfname, PDFname = 'PDFweights', ScaleName = 'ScaleWeights', lumi = GetLumi(year)) #59.7
  w.PrintMEscale('ScaleWeights_'+chan+'_'+lev)
  w.PrintPDFyields('PDFweights_'+chan+'_'+lev)
  w.PrintPSunc('PSunc_'+chan+'_'+lev)

DrawWeightSystematics(sample)
