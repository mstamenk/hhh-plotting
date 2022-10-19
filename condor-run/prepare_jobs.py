# Scritp to prepare jobs for plotting with make_histograms_rdataframe.py

import os 

#tags = ['0tag','1tag','2tag','3tag','4tag','5tag','6tag','0ptag']
tags = ['0ptag','6tag']
#wps = ['loose','medium','tight']
wps = ['loose','medium','tight']
#regions = ['nFJ0','nFJ1','nFJ2','nFJ3','inclusive']
regions = ['inclusive']
files = ['JetHT','WWTo4Q','WWZ','ZJetsToQQ','ZZZ','QCD','QCD6B','WJetsToQQ','WWW','WZZ','ZZTo4Q','TT','GluGluToHHHTo6B_SM']


script = '/isilon/data/users/mstamenk/hhh-6b-producer/CMSSW_11_1_0_pre5_PY3/src/plottting/make_histograms_rdataframe_selection.py'

jobs_path = 'jobs'


submit="Universe   = vanilla\nrequest_memory = 7900\nExecutable = %s\nArguments  = $(ClusterId) $(ProcId)\nLog        = log/job.$(ClusterId).$(ProcId).log\nOutput     = output/job.$(ClusterId).$(ProcId).out\nError      = error/job.$(ClusterId).$(ProcId).error\nQueue 1"

job_cmd = '#! /bin/bash\nsource /cvmfs/cms.cern.ch/cmsset_default.sh\ncmsrel CMSSW_11_1_0_pre5_PY3\ncd CMSSW_11_1_0_pre5_PY3/src\ncmsenv\nulimit -s unlimited \n%s'


submit_all = 'submit_all.sh'

jobs = []
for tag in tags:
    for wp in wps:
        for region in regions:
            for f_in in files:
                filename = 'job_%s_%s_%s_%s.sh'%(f_in,region,wp,tag)
                cmd = 'python %s --f_in %s --region %s --wp %s --tag %s'%(script,f_in,region,wp,tag)
                print("Writing %s"%filename)
                with open(jobs_path + '/' + filename, 'w') as f:
                    f.write(job_cmd%cmd)

                submit_file = 'submit_%s_%s_%s_%s'%(f_in,region,wp,tag)
                print('Writing %s/%s'%(jobs_path, submit_file))
                with open(jobs_path + '/' + submit_file, 'w') as f:
                    f.write(submit%(jobs_path+'/'+filename))
                jobs.append(submit_file)

                #if 'GluGluToHHHTo6B' in f_in:
                #    for match in ['H1','H2', 'H3']:
                #        filename = 'job_%s_%s_%s_%s_%s.sh'%(f_in,region,wp,tag,match)
                #        cmd = 'python %s --f_in %s --region %s --wp %s --tag %s --match %s --addBDT'%(script,f_in,region,wp,tag,match)
                #        print("Writing %s"%filename)
                #        with open(jobs_path + '/' + filename, 'w') as f:
                #            f.write(job_cmd%cmd)

                #        submit_file = 'submit_%s_%s_%s_%s_%s'%(f_in,region,wp,tag,match)
                #        print('Writing %s/%s'%(jobs_path, submit_file))
                #        with open(jobs_path + '/' + submit_file, 'w') as f:
                #            f.write(submit%(jobs_path+'/'+filename))
                #        jobs.append(submit_file)

cmd = '#!/bin/bash\n'
for j in jobs:
    cmd += 'condor_submit %s/%s \n'%(jobs_path, j)


with open(submit_all, 'w') as f:
    f.write(cmd)




                        
