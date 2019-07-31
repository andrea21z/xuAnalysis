import os, sys
from conf import *
from plotter.TopHistoReader import TopHistoReader, StackPlot, Process
from ROOT.TMath import Sqrt as sqrt
from ROOT import kRed, kOrange,kWhite, kBlue, kTeal, kGreen, kGray, kAzure, kPink, kCyan, kBlack, kSpring, kViolet, kYellow, TCanvas, TLegend



c=TCanvas("c", "canvas", 800, 800);
t = TopHistoReader(path[2016])
t2=TopHistoReader(path[2015])
t.SetLumi(GetLumi(2016)*1000)
t2.SetLumi(GetLumi(2016)*1000)
h = t.GetNamedHisto('H_NJets_Muon_dilepton',process[2016]['DY_2016'])
h2= t.GetNamedHisto('H_NJets_Muon_dilepton',process[2015]['DY_2015'])
h3= t.GetNamedHisto('H_NJets_Muon_dilepton',process[2016]['data_2016'])
h4= t2.GetNamedHisto('H_NJets_Muon_dilepton',process[2015]['data_2015'])
h.SetLineColor(kViolet);
h2.SetLineColor(kAzure)
h3.SetLineColor(kWhite)
h4.SetLineColor(kWhite)
h3.SetMarkerColor(kCyan)
h4.SetMarkerColor(kBlack)   
h3.SetMarkerStyle(20)
h4.SetMarkerStyle(34)


integral = h.Integral() if h.Integral() > 0 else 0
h.Scale(1./(integral if integral != 0 else 1))
integral2 = h2.Integral() if h2.Integral() > 0 else 0
h2.Scale(1./(integral2 if integral2 != 0 else 1))
integral3 = h3.Integral() if h3.Integral() > 0 else 0
h3.Scale(1./(integral3 if integral3 != 0 else 1))
integral4 = h4.Integral() if h4.Integral() > 0 else 0
h4.Scale(1./(integral4 if integral4 != 0 else 1))

h.Draw()
h2.Draw("same")
h3.Draw("same")
h4.Draw("same")
leg=TLegend(0.64, 0.65, 0.95, 0.91);
leg.SetNColumns(2);
leg.SetTextSize(0.015)
leg.AddEntry(h2,"DY TOP-17-001","l");
leg.AddEntry(h,"DY2016", "l");
leg.AddEntry(h3,"data 2016", "p");
leg.AddEntry(h4,"data TOP-17-001", "p");

leg.Draw()
h.SetTitle("N^{o} jets");
h.SetYTitle("Entries");
h.SetXTitle("N^{o} jets");
c.Print("/mnt_pool/ciencias_users/user/andreatf/njets_muon_dilepton_prueba.png",'png');
