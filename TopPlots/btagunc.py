import os, sys
basepath = os.path.abspath(__file__).rsplit('/xuAnalysis/',1)[0]+'/xuAnalysis/'
sys.path.append(basepath)
from plotter.TopHistoReader import TopHistoReader, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow

### Input and output
path = {
  2016 : '/nfs/fanae/user/juanr/legacy/PAFnanoAOD/histograms/2016/btag/',
  2017 : '/nfs/fanae/user/juanr/legacy/PAFnanoAOD/histograms/2017/btag/',
  2018 : '/nfs/fanae/user/juanr/legacy/PAFnanoAOD/histograms/2018/btag/',
}
ttfile = {
  2016 : 'TT',
  2017 : 'TTTo2L2Nu',
  2018 : 'TTTo2L2Nu'
}

def GetUnc(year = 2017, tag = 'DeepCSV', unc = 'Btag', ch = 'ElMu', level = '1btag'):
  fname = path[year]+ttfile[year]+'_'+tag+'.root'
  if not os.path.isfile(fname): return -999
  t = TopHistoReader(path[year], ttfile[year]+'_'+tag)
  t.SetLevel(level)
  t.SetChan(ch)
  t.SetHistoNamePrefix('H')
  y = t.GetUnc(s=unc)*100
  return y


for year in [2016,2017,2018]:
  for tag in ['CSVv2', 'DeepCSV', 'DeepFlav']:
    btagunc = GetUnc(year, tag)
    misunc  = GetUnc(year, tag, 'Mistag')
    if btagunc != -999:
      print 'Btag   unc [%i] [%s] : %1.2f %s'%(year, tag, btagunc, '%')
      print 'Mistag unc [%i] [%s] : %1.2f %s'%(year, tag, btagunc, '%')
