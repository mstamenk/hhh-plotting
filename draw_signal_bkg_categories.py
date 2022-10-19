# Script to plot data / mc from processed files 

import os, ROOT
import tdrstyle,CMS_lumi

ROOT.gROOT.SetBatch(ROOT.kTRUE)

tdrstyle.setTDRStyle()

CMS_lumi.lumi_7TeV = "4.8 fb^{-1}"
CMS_lumi.lumi_8TeV = "18.3 fb^{-1}"
CMS_lumi.writeExtraText = 1
CMS_lumi.extraText = "Internal"

labels = {
          'h1_mass' : 'm(H1)', 
          'h2_mass' : 'm(H2)', 
          'h3_mass' : 'm(H3)', 

          'h1_pt' : 'p_{T}(H1)', 
          'h2_pt' : 'p_{T}(H2)', 
          'h3_pt' : 'p_{T}(H3)', 

          'h1_eta' : '#eta(H1)', 
          'h2_eta' : '#eta(H2)', 
          'h3_eta' : '#eta(H3)', 

          'h1_phi' : '#phi(H1)', 
          'h2_phi' : '#phi(H2)', 
          'h3_phi' : '#phi(H3)', 

          'fatJet1Mass' : 'm(H1)', 
          'fatJet2Mass' : 'm(H2)', 
          'fatJet3Mass' : 'm(H3)', 

          'fatJet1Pt' : 'p_{T}(H1)', 
          'fatJet2Pt' : 'p_{T}(H2)', 
          'fatJet3Pt' : 'p_{T}(H3)', 

          'fatJet1Eta' : '#eta(H1)', 
          'fatJet2Eta' : '#eta(H2)', 
          'fatJet3Eta' : '#eta(H3)', 

          'fatJet1Phi' : '#phi(H1)', 
          'fatJet2Phi' : '#phi(H2)', 
          'fatJet3Phi' : '#phi(H3)', 

          'fatJet1PNetXbb' : 'PNet Xbb(H1)', 
          'fatJet2PNetXbb' : 'PNet Xbb(H2)', 
          'fatJet3PNetXbb' : 'PNet Xbb(H3)', 

          'fatJet1PNetXjj' : 'PNet Xjj(H1)', 
          'fatJet2PNetXjj' : 'PNet Xjj(H2)', 
          'fatJet3PNetXjj' : 'PNet Xjj(H3)', 

          'fatJet1PNetQCD' : 'PNet QCD(H1)', 
          'fatJet2PNetQCD' : 'PNet QCD(H2)', 
          'fatJet3PNetQCD' : 'PNet QCD(H3)', 

          'hhh_resolved_mass': 'm(HHH)',
          'hhh_resolved_pt': 'p_{T}(HHH)',

          'hhh_mass': 'm(HHH)',
          'hhh_pt': 'p_{T}(HHH)',

          'nfatjets' : 'N fat-jets',
          'nbtags' : 'N b-tags',

        }

binnings = {
          'h1_mass' : '(30,0,300)', 
          'h2_mass' : '(30,0,300)', 
          'h3_mass' : '(30,0,300)', 

          'h1_pt' : '(50,0,500)', 
          'h2_pt' : '(50,0,500)', 
          'h3_pt' : '(50,0,500)', 

          'h1_eta' : '(50,-5,5)', 
          'h2_eta' : '(50,-5,5)', 
          'h3_eta' : '(50,-5,5)', 

          'h1_phi' : '(60,-3.2,3.2)', 
          'h2_phi' : '(60,-3.2,3.2)', 
          'h3_phi' : '(60,-3.2,3.2)', 

          'fatJet1Mass' : '(30,0,300)', 
          'fatJet2Mass' : '(30,0,300)', 
          'fatJet3Mass' : '(30,0,300)', 

          'fatJet1Pt' : '(85,150,1000)', 
          'fatJet2Pt' : '(85,150,1000)', 
          'fatJet3Pt' : '(85,150,1000)', 

          'fatJet1Eta' : '(50,-5,5)', 
          'fatJet2Eta' : '(50,-5,5)', 
          'fatJet3Eta' : '(50,-5,5)', 

          'fatJet1Phi' : '(60,-3.2,3.2)', 
          'fatJet2Phi' : '(60,-3.2,3.2)', 
          'fatJet3Phi' : '(60,-3.2,3.2)', 

          'fatJet1PNetXbb' : '(20,0,1)', 
          'fatJet2PNetXbb' : '(20,0,1)', 
          'fatJet3PNetXbb' : '(20,0,1)', 

          'fatJet1PNetXjj' : '(20,0,1)', 
          'fatJet2PNetXjj' : '(20,0,1)', 
          'fatJet3PNetXjj' : '(20,0,1)', 

          'fatJet1PNetQCD' : '(20,0,1)', 
          'fatJet2PNetQCD' : '(20,0,1)', 
          'fatJet3PNetQCD' : '(20,0,1)', 

          'hhh_resolved_mass': '(80,0,1600)',
          'hhh_resolved_pt': '(80,0,800)',

          'hhh_mass': '(155,400,3500)',
          'hhh_pt': '(80,0,800)',
 
          'nfatjets' : '(5,0,5)',
          'nbtags' : '(10,0,10)',

        }



hist_properties = {'JetHT' : [ROOT.kBlack, 0.2, 2, 'Data', True] , # [color, marker size, line size, legend label , add in legend]
                   'QCD'   : [ROOT.kOrange, 0, 2, 'QCD', True], 
                   'QCD6B'   : [ROOT.kOrange, 0, 2, 'QCD', True], 
                   'ZJetsToQQ'   : [ROOT.kCyan, 0, 2, 'V+jets', True], 
                   'WJetsToQQ'   : [ROOT.kCyan + 1, 0, 2, 'V+jets', True], 
                   'ZZTo4Q' : [ROOT.kGray, 0, 2, 'VV', True], 
                   'WWTo4Q' : [ROOT.kGray, 0, 2, 'VV', False], 
                   'ZZZ' : [ROOT.kRed, 0, 2, 'VVV', True], 
                   'WWW' : [ROOT.kRed+1, 0, 2, 'VVV', True], 
                   'WZZ' : [ROOT.kRed+2, 0, 2, 'VVV', True], 
                   'WWZ' : [ROOT.kRed+3, 0, 2, 'VVV', True], 
                   'TT' : [ROOT.kBlue, 0,2, 't#bar{t}', True],
                   'GluGluToHHHTo6B_SM' : [ROOT.kRed, 0,2, 'SM HHH', True],
        } 


iPos = 11
if( iPos==0 ): CMS_lumi.relPosX = 0.12

iPeriod = 0
version = 'v13-6jets'
typename = 'allHLT'

for region in ['inclusive']:
    for wp in ['loose']:
        for tag in ['0ptag']: 

            eos_plots = 'plots_s_vs_b-%s-%s-%s-%s-wp-%s'%(typename,version,region,wp,tag)

            if not os.path.isdir(eos_plots):
                os.mkdir(eos_plots)

            histo_path = 'histo-root-%s-%s-%s-%s-wp-%s'%(typename,version,region,wp,tag)

            # ['JetHT','WWTo4Q','WWZ','ZJetsToQQ','ZZZ','QCD','WJetsToQQ','WWW','WZZ','ZZTo4Q', 'TT']:

            #file_data = ROOT.TFile('histograms_%s.root'%('JetHT'))

            file_signal = ROOT.TFile(histo_path + '/' + 'histograms_%s.root'%('GluGluToHHHTo6B_SM'))
            file_h1 = ROOT.TFile(histo_path + '/' + 'histograms_%s.root'%('GluGluToHHHTo6B_SM_H1Matched'))
            file_h2 = ROOT.TFile(histo_path + '/' + 'histograms_%s.root'%('GluGluToHHHTo6B_SM_H2Matched'))
            file_h3 = ROOT.TFile(histo_path + '/' + 'histograms_%s.root'%('GluGluToHHHTo6B_SM_H3Matched'))

            files_bkg = {}
            for bkg in ['WWTo4Q','WWZ','ZJetsToQQ','ZZZ','QCD','WJetsToQQ','WWW','WZZ','ZZTo4Q', 'TT','JetHT']:
            #for bkg in ['QCD6B']:
                files_bkg[bkg] = ROOT.TFile(histo_path + '/' + 'histograms_%s.root'%bkg)

            var = 'fatJet1PNetXbb_boosted'
            variables = [v.GetName() for v in file_signal.GetListOfKeys()]
            print(variables)

            #for var in ['h1_mass_resolved', 'h2_mass_resolved', 'h3_mass_resolved', 'h1_pt_resolved','h2_pt_resolved', 'h3_pt_resolved', 'fatJet1Mass_boosted', 'fatJet2Mass_boosted', 'fatJet3Mass_boosted', 'fatJet1Pt_boosted', 'fatJet2Pt_boosted', 'fatJet3Pt_boosted', 'fatJet1PNetXbb_boosted', 'fatJet2PNetXbb_boosted', 'fatJet3PNetXbb_boosted']:
            for var in variables:
                legend = ROOT.TLegend(0.6,0.6,.9,0.9)
                legend.SetBorderSize(0)

                #h_data = file_data.Get(var)
                #h_data.SetMarkerColor(hist_properties['JetHT'][0])
                #h_data.SetMarkerSize(hist_properties['JetHT'][1])
                #legend.AddEntry(h_data, hist_properties['JetHT'][3])

                h_signal = file_signal.Get(var)
                h_h1 = file_h1.Get(var)
                h_h2 = file_h2.Get(var)
                h_h3 = file_h3.Get(var)

                for h in [h_signal,h_h1,h_h2,h_h3]:
                    h.SetMarkerColor(hist_properties['GluGluToHHHTo6B_SM'][0])
                    h.SetLineColor(hist_properties['GluGluToHHHTo6B_SM'][0])
                    h.SetMarkerSize(hist_properties['GluGluToHHHTo6B_SM'][1])
                    h.SetLineWidth(hist_properties['GluGluToHHHTo6B_SM'][2])
                    h.SetLineStyle(ROOT.kDashed)


                if h_signal.Integral() > 0:
                    h_h1.Scale(1./h_signal.Integral())
                    h_h2.Scale(1./h_signal.Integral())
                    h_h3.Scale(1./h_signal.Integral())
                    h_signal.Scale(1./h_signal.Integral())
                legend.AddEntry(h_signal, hist_properties['GluGluToHHHTo6B_SM'][3], 'l')
                h_signal.SetLineStyle(ROOT.kDashed)

                h_h1.SetLineColor(ROOT.kBlue + 2)
                h_h2.SetLineColor(ROOT.kGreen + 2)
                h_h3.SetLineColor(ROOT.kViolet+ 2)

                legend.AddEntry(h_h1,'HHH H1 matched ' , 'l')
                legend.AddEntry(h_h2,'HHH H2 matched ' , 'l')
                legend.AddEntry(h_h3,'HHH H3 matched ' , 'l')

                h_bkg = []

                #for bkg in ['QCD','ZJetsToQQ','WJetsToQQ','ZZTo4Q', 'WWTo4Q', 'ZZZ' ,'WWW', 'WZZ', 'WWZ', 'TT','JetHT']:
                for bkg in ['JetHT','QCD']:
                    f_bkg = files_bkg[bkg]
                    h_tmp = f_bkg.Get(var)

                    #h_tmp.SetFillColor(hist_properties[bkg][0])
                    h_tmp.SetLineColor(hist_properties[bkg][0])
                    h_tmp.SetMarkerSize(hist_properties[bkg][1])
                    h_tmp.SetLineWidth(hist_properties[bkg][2])
                    if h_tmp.Integral() > 0 :
                        h_tmp.Scale(1./h_tmp.Integral())
                    if hist_properties[bkg][4]:
                        legend.AddEntry(h_tmp, hist_properties[bkg][3], 'f')
                    h_bkg.append(h_tmp)

                   
                maxi = max(h_signal.GetMaximum(), h_bkg[0].GetMaximum())
                #maxi = 0.3
                h_signal.SetMaximum(1.8 * maxi)
                h_bkg[0].SetMaximum(1.8 * maxi)

                c = ROOT.TCanvas()
                #h_data.Draw('e')

                h_bkg[0].Draw('hist e')
                for h in h_bkg:
                    h.Draw('hist e same')
                h_signal.Draw('hist e same')
                h_h1.Draw('hist e same')
                h_h2.Draw('hist e same')
                h_h3.Draw('hist e same')
                legend.Draw()
                CMS_lumi.CMS_lumi(c, iPeriod, iPos)

                c.Print(eos_plots + '/' + var +  '.pdf')


