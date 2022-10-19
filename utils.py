# Script to store labels and cut definitions

labels = {
          #'h1_mass' : 'm(H1)', 
          #'h2_mass' : 'm(H2)', 
          #'h3_mass' : 'm(H3)', 

          #'h1_pt' : 'p_{T}(H1)', 
          #'h2_pt' : 'p_{T}(H2)', 
          #'h3_pt' : 'p_{T}(H3)', 

          #'h1_eta' : '#eta(H1)', 
          #'h2_eta' : '#eta(H2)', 
          #'h3_eta' : '#eta(H3)', 

          #'h1_phi' : '#phi(H1)', 
          #'h2_phi' : '#phi(H2)', 
          #'h3_phi' : '#phi(H3)', 

          #'h1_t2_mass' : 'm(H1)', 
          #'h2_t2_mass' : 'm(H2)', 
          #'h3_t2_mass' : 'm(H3)', 

          'h1_t3_mass' : 'm(H1)', 
          'h2_t3_mass' : 'm(H2)', 
          'h3_t3_mass' : 'm(H3)', 


          'h_fit_mass' : 'm(H) fitted', 

          #'h1_t2_pt' : 'p_{T}(H1)', 
          #'h2_t2_pt' : 'p_{T}(H2)', 
          #'h3_t2_pt' : 'p_{T}(H3)', 

          #'h1_t2_eta' : '#eta(H1)', 
          #'h2_t2_eta' : '#eta(H2)', 
          #'h3_t2_eta' : '#eta(H3)', 

          #'h1_t2_phi' : '#phi(H1)', 
          #'h2_t2_phi' : '#phi(H2)', 
          #'h3_t2_phi' : '#phi(H3)', 

          #'h1_t2_match' : 'H1 truth matched', 
          #'h2_t2_match' : 'H2 truth matched', 
          #'h3_t2_match' : 'H3 truth matched', 

          #'h1_t2_dRjets' : '#Delta R(j1,j2) H1', 
          #'h2_t2_dRjets' : '#Delta R(j3,j4) H2', 
          #'h3_t2_dRjets' : '#Delta R(j5,j6) H3', 

          'h1_t3_pt' : 'p_{T}(H1)', 
          'h2_t3_pt' : 'p_{T}(H2)', 
          'h3_t3_pt' : 'p_{T}(H3)', 

          'h1_t3_eta' : '#eta(H1)', 
          'h2_t3_eta' : '#eta(H2)', 
          'h3_t3_eta' : '#eta(H3)', 

          'h1_t3_phi' : '#phi(H1)', 
          'h2_t3_phi' : '#phi(H2)', 
          'h3_t3_phi' : '#phi(H3)', 

          'h1_t3_dRjets' : '#Delta R(j1,j2) H1', 
          'h2_t3_dRjets' : '#Delta R(j3,j4) H2', 
          'h3_t3_dRjets' : '#Delta R(j5,j6) H3', 

          'h1_t3_match' : 'H1 truth matched', 
          'h2_t3_match' : 'H2 truth matched', 
          'h3_t3_match' : 'H3 truth matched', 

          #'h1_match' : 'H1 truth matched', 
          #'h2_match' : 'H2 truth matched', 
          #'h3_match' : 'H3 truth matched', 

          'bcand1Pt' : 'Jet 1 p_{T}', 
          'bcand2Pt' : 'Jet 2 p_{T}', 
          'bcand3Pt' : 'Jet 3 p_{T}', 
          'bcand4Pt' : 'Jet 4 p_{T}', 
          'bcand5Pt' : 'Jet 5 p_{T}', 
          'bcand6Pt' : 'Jet 6 p_{T}', 

          'bcand1Eta' : 'Jet 1 #eta', 
          'bcand2Eta' : 'Jet 2 #eta', 
          'bcand3Eta' : 'Jet 3 #eta', 
          'bcand4Eta' : 'Jet 4 #eta', 
          'bcand5Eta' : 'Jet 5 #eta', 
          'bcand6Eta' : 'Jet 6 #eta', 

          'bcand1Phi' : 'Jet 1 #phi', 
          'bcand2Phi' : 'Jet 2 #phi', 
          'bcand3Phi' : 'Jet 3 #phi', 
          'bcand4Phi' : 'Jet 4 #phi', 
          'bcand5Phi' : 'Jet 5 #phi', 
          'bcand6Phi' : 'Jet 6 #phi', 

          #'bcand1DeepFlavB' : 'Jet 1 b-tag score', 
          #'bcand2DeepFlavB' : 'Jet 2 b-tag score', 
          #'bcand3DeepFlavB' : 'Jet 3 b-tag score', 
          #'bcand4DeepFlavB' : 'Jet 4 b-tag score', 
          #'bcand5DeepFlavB' : 'Jet 5 b-tag score', 
          #'bcand6DeepFlavB' : 'Jet 6 b-tag score', 

          'bcand1HiggsMatched' : 'Jet 1 truth matched', 
          'bcand2HiggsMatched' : 'Jet 2 truth matched', 
          'bcand3HiggsMatched' : 'Jet 3 truth matched', 
          'bcand4HiggsMatched' : 'Jet 4 truth matched', 
          'bcand5HiggsMatched' : 'Jet 5 truth matched', 
          'bcand6HiggsMatched' : 'Jet 6 truth matched', 

          #'fatJet1Mass' : 'm(H1)', 
          #'fatJet2Mass' : 'm(H2)', 
          #'fatJet3Mass' : 'm(H3)', 

          #'fatJet1Pt' : 'p_{T}(H1)', 
          #'fatJet2Pt' : 'p_{T}(H2)', 
          #'fatJet3Pt' : 'p_{T}(H3)', 

          #'fatJet1Eta' : '#eta(H1)', 
          #'fatJet2Eta' : '#eta(H2)', 
          #'fatJet3Eta' : '#eta(H3)', 

          #'fatJet1Phi' : '#phi(H1)', 
          #'fatJet2Phi' : '#phi(H2)', 
          #'fatJet3Phi' : '#phi(H3)', 

          #'fatJet1PNetXbb' : 'PNet Xbb(H1)', 
          #'fatJet2PNetXbb' : 'PNet Xbb(H2)', 
          #'fatJet3PNetXbb' : 'PNet Xbb(H3)', 

          #'fatJet1PNetXjj' : 'PNet Xjj(H1)', 
          #'fatJet2PNetXjj' : 'PNet Xjj(H2)', 
          #'fatJet3PNetXjj' : 'PNet Xjj(H3)', 

          #'fatJet1PNetQCD' : 'PNet QCD(H1)', 
          #'fatJet2PNetQCD' : 'PNet QCD(H2)', 
          #'fatJet3PNetQCD' : 'PNet QCD(H3)', 

          #'hhh_resolved_mass': 'm(HHH)',
          #'hhh_resolved_pt': 'p_{T}(HHH)',
          'hhh_t3_pt': 'p_{T}(HHH)',

          #'hhh_mass': 'm(HHH)',
          #'hhh_pt': 'p_{T}(HHH)',

          'nfatjets' : 'N fat-jets',
          'nbtags' : 'N b-tags',

          'ht' : 'Event HT [GeV]',
          'met' : 'E_{T}^{miss} [GeV]',
          'bdt' : 'BDT output score',

          'jet1DeepFlavB' : 'jet 1 DeepJet b-score',
          'jet2DeepFlavB' : 'jet 2 DeepJet b-score',
          'jet3DeepFlavB' : 'jet 3 DeepJet b-score',
          'jet4DeepFlavB' : 'jet 4 DeepJet b-score',
          'jet5DeepFlavB' : 'jet 5 DeepJet b-score',
          'jet6DeepFlavB' : 'jet 6 DeepJet b-score',

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

          'h1_match' : '(2,0,2)', 
          'h2_match' : '(2,0,2)', 
          'h3_match' : '(2,0,2)', 

          'h_fit_mass' : '(30,0,300)', 

          'h1_t2_mass' : '(30,0,300)', 
          'h2_t2_mass' : '(30,0,300)', 
          'h3_t2_mass' : '(30,0,300)', 

          'h1_t2_pt' : '(50,0,500)', 
          'h2_t2_pt' : '(50,0,500)', 
          'h3_t2_pt' : '(50,0,500)', 

          'h1_t2_eta' : '(50,-5,5)', 
          'h2_t2_eta' : '(50,-5,5)', 
          'h3_t2_eta' : '(50,-5,5)', 

          'h1_t2_phi' : '(60,-3.2,3.2)', 
          'h2_t2_phi' : '(60,-3.2,3.2)', 
          'h3_t2_phi' : '(60,-3.2,3.2)', 

          'h1_t2_match' : '(2,0,2)', 
          'h2_t2_match' : '(2,0,2)', 
          'h3_t2_match' : '(2,0,2)', 

          'h1_t2_dRjets' : '(40,0,4)', 
          'h2_t2_dRjets' : '(40,0,4)', 
          'h3_t2_dRjets' : '(40,0,4)', 

          'h1_t3_dRjets' : '(40,0,4)', 
          'h2_t3_dRjets' : '(40,0,4)', 
          'h3_t3_dRjets' : '(40,0,4)', 

          'h1_t3_mass' : '(30,0,300)', 
          'h2_t3_mass' : '(30,0,300)', 
          'h3_t3_mass' : '(30,0,300)', 

          'h1_t3_pt' : '(50,0,500)', 
          'h2_t3_pt' : '(50,0,500)', 
          'h3_t3_pt' : '(50,0,500)', 

          'h1_t3_eta' : '(50,-5,5)', 
          'h2_t3_eta' : '(50,-5,5)', 
          'h3_t3_eta' : '(50,-5,5)', 

          'h1_t3_phi' : '(60,-3.2,3.2)', 
          'h2_t3_phi' : '(60,-3.2,3.2)', 
          'h3_t3_phi' : '(60,-3.2,3.2)', 

          'h1_t3_match' : '(2,0,2)', 
          'h2_t3_match' : '(2,0,2)', 
          'h3_t3_match' : '(2,0,2)', 



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

          'bcand1Pt' : '(85,0,500)', 
          'bcand2Pt' : '(85,0,500)', 
          'bcand3Pt' : '(85,0,500)', 
          'bcand4Pt' : '(85,0,500)', 
          'bcand5Pt' : '(85,0,500)', 
          'bcand6Pt' : '(85,0,500)', 

          'bcand1Eta' : '(50,-5,5)', 
          'bcand2Eta' : '(50,-5,5)', 
          'bcand3Eta' : '(50,-5,5)', 
          'bcand4Eta' : '(50,-5,5)', 
          'bcand5Eta' : '(50,-5,5)', 
          'bcand6Eta' : '(50,-5,5)', 

          'bcand1Phi' : '(60,-3.2,3.2)', 
          'bcand2Phi' : '(60,-3.2,3.2)', 
          'bcand3Phi' : '(60,-3.2,3.2)', 
          'bcand4Phi' : '(60,-3.2,3.2)', 
          'bcand5Phi' : '(60,-3.2,3.2)', 
          'bcand6Phi' : '(60,-3.2,3.2)', 

          'bcand1DeepFlavB' : '(40,-1,1)', 
          'bcand2DeepFlavB' : '(40,-1,1)', 
          'bcand3DeepFlavB' : '(40,-1,1)', 
          'bcand4DeepFlavB' : '(40,-1,1)', 
          'bcand5DeepFlavB' : '(40,-1,1)', 
          'bcand6DeepFlavB' : '(40,-1,1)', 


          'bcand1HiggsMatched' : '(2,0,2)', 
          'bcand2HiggsMatched' : '(2,0,2)', 
          'bcand3HiggsMatched' : '(2,0,2)', 
          'bcand4HiggsMatched' : '(2,0,2)', 
          'bcand5HiggsMatched' : '(2,0,2)', 
          'bcand6HiggsMatched' : '(2,0,2)', 

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
          'hhh_t3_pt': '(80,0,800)',

          'hhh_mass': '(155,400,3500)',
          'hhh_pt': '(80,0,800)',
 
          'nfatjets' : '(5,0,5)',
          'nbtags' : '(10,0,10)',

          'ht' : '(200,0,2000)',
          'met' : '(150,0,1500)',
          'bdt' : '(20,-1,1)',

          'jet1DeepFlavB' : '(20,0,1)',
          'jet2DeepFlavB' : '(20,0,1)',
          'jet3DeepFlavB' : '(20,0,1)',
          'jet4DeepFlavB' : '(20,0,1)',
          'jet5DeepFlavB' : '(20,0,1)',
          'jet6DeepFlavB' : '(20,0,1)',

        }

cuts = {#'resolved' : ROOT.TCut('nbtags == 6 && nfatjets == 0 && nbtags > 4',
        #'boosted'  : 'nfatjets == 3 && nbtags > 4',
        'nFJ0'  : 'nfatjets == 0',
        'nFJ1'  : 'nfatjets == 1',
        'nFJ2'  : 'nfatjets == 2',
        'nFJ3'  : 'nfatjets == 3',
        'inclusive' : '1'
        }


# cut loose = 0.0532 = 91%, medium = 0.3040 = 79%, tight = 0.7476 = 61%

wps = { 'loose'  : '0.0532', 
        'medium' : '0.3040',
        'tight'  : '0.7476',
        }


tags = {'5tag' :  'jet1DeepFlavB > %s && jet2DeepFlavB > %s && jet3DeepFlavB > %s && jet4DeepFlavB > %s && jet5DeepFlavB > %s && jet6DeepFlavB < %s  ', 
        '6tag' :  'jet1DeepFlavB > %s && jet2DeepFlavB > %s && jet3DeepFlavB > %s && jet4DeepFlavB > %s && jet5DeepFlavB > %s && jet6DeepFlavB > %s  ',
        '4tag' :  'jet1DeepFlavB > %s && jet2DeepFlavB > %s && jet3DeepFlavB > %s && jet4DeepFlavB > %s && jet5DeepFlavB < %s && jet6DeepFlavB < %s  ',
        '3tag' :  'jet1DeepFlavB > %s && jet2DeepFlavB > %s && jet3DeepFlavB > %s && jet4DeepFlavB < %s && jet5DeepFlavB < %s && jet6DeepFlavB < %s  ',
        '2tag' :  'jet1DeepFlavB > %s && jet2DeepFlavB > %s && jet3DeepFlavB < %s && jet4DeepFlavB < %s && jet5DeepFlavB < %s && jet6DeepFlavB < %s  ',
        '1tag' :  'jet1DeepFlavB > %s && jet2DeepFlavB < %s && jet3DeepFlavB < %s && jet4DeepFlavB < %s && jet5DeepFlavB < %s && jet6DeepFlavB < %s  ',
        '0tag' :  'jet1DeepFlavB < %s && jet2DeepFlavB < %s && jet3DeepFlavB < %s && jet4DeepFlavB < %s && jet5DeepFlavB < %s && jet6DeepFlavB < %s  ',
        '0ptag' :  '1',
        
        }


