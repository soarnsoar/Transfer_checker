import glob
import os

fnew=open('result_combined.txt','w')
LIST=glob.glob('list_files_190603/*.txt')
DIRLIST=[]
for a in LIST:


    f=open(a,'r')
    lines=f.readlines()
    for line in lines:
        line=line.replace("//","/")
        fnew.write(line)
        DIRLIST.append('/'.join(line.split('/')[:-1])  )
    f.close()


fnew.close()




DIRLIST=list(set(DIRLIST))
os.system('rm dirlist.txt')
os.system('rm dirname.txt')
fdir=open('dirlist.txt','w')
fonly=open('dirname.txt','w')
i=0
for b in DIRLIST:
    if len(b.strip())==0:continue
    print b
    fdir.write('--job'+str(i)+"--- \n")
    #fdir.write(b+"\n")
    fdir.write('gsiftp://eoscmsftp.cern.ch//eos/cms/'+b+" \n")
    fdir.write('gsiftp://cms-se.sdfarm.kr//xrootd/'+b+" \n")
    fdir.write('')
    fonly.write(b+'\n')
    i=i+1    
fdir.close()
fonly.close()    
