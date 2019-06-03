import glob
import os
import subprocess
#import time
import argparse


#start_time=time.time()
ADDRESS_LXPLUS='root://eoscms.cern.ch/'
ADDRESS_KISTI='root://cms-xrdr.sdfarm.kr:1094/'
#TARGETDIR='/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/'
def get_list(TARGETDIR):

    rootfiles=subprocess.check_output('find '+TARGETDIR+' -name *.root',shell=True)

    #print rootfiles

    FILE_LIST=rootfiles.split('\n')
    #print str(len(FILE_LIST))
    return FILE_LIST



def get_size(ADDRESS,PATH):

    Size='-1'
    PREFIX=''
    if 'eoscms' in ADDRESS: PREFIX='/eos/cms/'
    if 'sdfarm.kr' in ADDRESS: PREFIX='/xrd/'
    sampleinfo=''
    try:
        sampleinfo=subprocess.check_output('xrdfs '+ADDRESS+' stat '+PREFIX+PATH,shell=True)
        for line in sampleinfo.split('\n'):
            if 'Size' in line:
                Size=line.replace('Size:','').strip()
    except subprocess.CalledProcessError as e:
        Size='-1'


    return Size


    #if __name__ == '__main__':
    #lxplusfile= get_size(ADDRESS_LXPLUS,'/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_Run2016B_RemAOD/lepSel__EpTCorr__TrigMakerData__cleanTauData__fakeSel__hadd/latino_DoubleEG_Run2016B-03Feb2017_ver2-v2.root')
    #kistifile=get_size(ADDRESS_KISTI,'/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_Run2016B_RemAOD/lepSel__EpTCorr__TrigMakerData__cleanTauData__fakeSel__hadd/latino_DoubleEG_Run2016B-03Feb2017_ver2-v2.root')
    
    #print lxplusfile==kistifile
def make_fail_list(TARGETDIR,OUTTXT):    
    print "TARGETDIR="+TARGETDIR
    print "OUTTXT="+OUTTXT
    SAVEDIR='list_files/'
    os.system('mkdir -p '+SAVEDIR)
    fw=open(SAVEDIR+'/'+OUTTXT,'w')
    #fw.write("#START#")
    #TARGETDIR='/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/'
    LIST=get_list(TARGETDIR)
    #pool=multiprocessing.Pool(processes=10)
    #pool.map
    n=0
    NFile=len(LIST)
    print "---NFile="+str(NFile)
    for f in LIST:
        #print f
        if n%10==0:
            print "["+OUTTXT+"]"+"----"+str(n)+"/"+str(NFile)+"-----"
        #    print "TIME->"+str(time.time()-start_time)
        if len(f)==0:continue
        ##f ===> all root files
        f=f.replace('/eos/cms/','/')
        lxplusfile= get_size(ADDRESS_LXPLUS,f)
        kistifile= get_size(ADDRESS_KISTI,f)
        if lxplusfile!=kistifile:
            #print "NOT MATCH"
            #print f
            fw.write(f+"\n")
        n=n+1
    fw.close()
    print OUTTXT+" created"

#TARGETDIR='/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_Run2016B_RemAOD/lepSel__EpTCorr__TrigMakerData__cleanTauData__fakeSel__hadd/'    

parser = argparse.ArgumentParser()
####Set options###                                                                                                                             

parser.add_argument("--target", help="targetdir")
parser.add_argument("--output", help="output textfile")
args = parser.parse_args()

#TARGETDIR='/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/'
TARGETDIR=args.target
OUTTXT=args.output
make_fail_list(TARGETDIR,OUTTXT)
os.system(' echo '+TARGETDIR+' | mail -s JOB_FINISHED soarnsoar@gmail.com')
print "DONE."


#end_time=time.time()

