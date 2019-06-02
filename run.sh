#/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/
#/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_Run2016B_RemAOD/lepSel__EpTCorr__TrigMakerData__cleanTauData__fakeSel__hadd/
#   parser.add_argument("--target", help="targetdir")
#    parser.add_argument("--output", help="output textfile")
##DATA##
BASEDIR='/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17'
SUBDIRS=()
SUBDIRS+=(Apr2017_Run2016B_RemAOD)
SUBDIRS+=(Apr2017_Run2016C_RemAOD)
SUBDIRS+=(Apr2017_Run2016D_RemAOD)
SUBDIRS+=(Apr2017_Run2016E_RemAOD)
SUBDIRS+=(Apr2017_Run2016F_RemAOD)
SUBDIRS+=(Apr2017_Run2016G_RemAOD)
SUBDIRS+=(Apr2017_Run2016H_RemAOD)

for subdir in ${SUBDIRS[@]};do
    python make_list.py --target "${BASEDIR}/${subdir}/" --output "${subdir}.txt" &> log_${subdir}.txt&
    continue
done



##MC##
BASEDIR='/eos/cms/store/group/phys_higgs/cmshww/amassiro/Full2016_Apr17/Apr2017_summer16/'
SUBDIRS=($(ls -d ${BASEDIR}/*/))
for subdir in ${SUBDIRS[@]};do
    #echo ${subdir}
    #echo "@"
    #python make_list.py --target "${subdir}" --output "${subdir}.txt" &
    subdir=${subdir#"${BASEDIR}"}
    subdir=${subdir#"/"}
    subdir=${subdir%"/"}
    #echo ${subdir}

    python make_list.py --target "${BASEDIR}/${subdir}" --output "${subdir}.txt" &> log_${subdir}.txt&
done
    
