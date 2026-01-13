'''
Setup and convert the 
'''
import subprocess
import os
import csv

HOME_DIR = "/home/jlooper"
FILES_CHANGED_CSV = os.path.join(HOME_DIR,"build_to_source_map.csv")

REPO_NAME = "m2-dcp"
BRANCH = "E1_OM_dual_rx"

GIT_REPO_CHECKOUT_DIR=os.path.join(HOME_DIR,"temp","checkout")
CHANGED_FILES_DIR=os.path.join(HOME_DIR,"temp","changed_files")

# Read in the files that changed
csv_reader = csv.DictReader(open(FILES_CHANGED_CSV))

# Updated rows
updated_data = []

source_basenames = []

for row in csv_reader:
    source_basenames.append(os.path.basename(row['source_path']).strip())
    # name_split = row['source_path'].split('/')
    # name = name_split[-1]
    # source_dir = '/'.join(name_split[0:-1]) + '/'

os.chdir(os.path.join(GIT_REPO_CHECKOUT_DIR,REPO_NAME))

build_pathnames = []


# with open(FILES_CHANGED_CSV) as f:
#     csv_reader = csv.reader(f)
#     for row in csv_reader:
#         print(row)

# result = subprocess.run(["mkdir","-p", CHANGED_FILES_DIR], capture_output=True, text=True)
print("Create Dirs\n")
os.makedirs(GIT_REPO_CHECKOUT_DIR, exist_ok=True)
os.makedirs(CHANGED_FILES_DIR, exist_ok=True)

# Clone repo and checkout branch
os.chdir(GIT_REPO_CHECKOUT_DIR)
full_repo_path = "ssh://git@git.faa.gov:7999/waas/" + REPO_NAME + ".git"

result = subprocess.run(["git","clone",full_repo_path])
os.chdir(os.path.join(GIT_REPO_CHECKOUT_DIR,REPO_NAME))

print("Checkout branch " + BRANCH)
result = subprocess.run(["git","checkout",BRANCH])
result = subprocess.run(["git","status"])

# Build the original file location

# print("Files that changed between E1_OM_dual_rx and master")
# result = subprocess.run(["git","diff","--name-only", BRANCH, "master"])
# print(result.stdout)

# CHANGED_FILES=($(git diff --name-only E1_OM_dual_rx f9386508a17))



# # Loop through the array and print each file name
# for file in "${CHANGED_FILES[@]}"; do
#     echo "Changed file: $file"
#     NEW_NAME=$(grep SCCS "$file" | awk -F'[@@]' '{print $2}' | awk -F'WAAS_OPS_sw' '{print $2}')
#     echo "New Name: $NEW_NAME"
# done

# echo "Copying packages"
# mkdir -p $CHANGED_FILES_DIR/add/packages/1config
# mkdir -p $CHANGED_FILES_DIR/add/packages/glg

# cp 


# Package updates



# */change_files/add/packages/1config
#     packages/1config1config.rev
    
# */change_files/add/packages/1config/data/
#     packages/1config/data/ether.dat







# */change_files/add/sw/dcp/
#     main_source/RX* DF* *MN* DMMR* CDI3* CDI1*



#     lib_sourceRXR* RXHC* RXGP* RXDV* RXGE* *RXGB* RX_RXRM* *RXRD* RX_G3* DC_AC_RX* DC_rcv* DC_osp* DODS* DOMS* DO_DODS* DO_DOMS* DO_xOMN* xOMN* WAAS_rcv* WAAS_dcp* WAAS_LxUT* WAAS_DODS* CDWS* *DFFD* DOSS_lru* MWTC* MWTO_subsystem.c MWTO_top_level.c OM_cd_types*  WAAS_equipment* MWIN_mode_switch* MWSE_lru* DFFD_DCP_LRU_conditions.h WAAS_CDI3* WAAS_PIM1* CD_cdp3.h CDP3.c WAAS_cv_horn_data.h WAAS_capacities.h

# */change_files/add/sw/elmg_mgen
#     elmg/DC_status.txt
    
# */change_files/add/sw/adapt
#     adgen/*zfw*.add OSP_DCP.add
    
# */change_files/add/sw/om
#     waas_monitor_waas/MWSE_wrefaults.dat
    


# */change_files/add/packages/1config/scripts/
#     packages/1config/scripts/do_machine_id.ksh
                                    
# */change_iles/add/tools/misc/shadow/sl1/adapt
#                                             shadow/sl1/adgen/*zfw*.add

# https://usfaa-my.sharepoint.com/:x:/r/personal/xavier_i-ctr_boomershine_faa_gov/_layouts/15/Doc2.aspx?action=edit&sourcedoc=%7B20c0c81a-e294-4e47-931e-e1f89321aaa4%7D&wdOrigin=TEAMS-MAGLEV.teamsSdk_ns.rwc&wdExp=TEAMS-TREATMENT&wdhostclicktime=1747256698560&web=1
# sw/dcp/DOMN_MAIN.c	
# sw/dcp/GOMN_MAIN.c	
# sw/dcp/DFFD_MAIN.c	
# sw/dcp/DFAC_MAIN.c	
# sw/dcp/RXRM_MAIN.c	
# sw/dcp/RXRD_MAIN.c	
# sw/rtc/DMMR_MAIN.c	
# sw/dcp/RXRI.c	
# sw/dcp/RXRL.c	
# sw/dcp/RXR1.c	
# sw/dcp/RXR3.c	
# sw/dcp/RXRS.c	
# sw/dcp/RXHC.c	
# sw/dcp/RXGP.c	
# sw/dcp/RXDV.c	
# sw/dcp/RXGE.c	
# sw/dcp/RXRI_rcvr_cmds.h	
# sw/dcp/RX_RXRM_interface.h	
# sw/dcp/RX_RXRM_types.h	
# sw/dcp/RX_G3_logs.h	
# sw/dcp/RX_RXRD_interface.h	
# sw/dcp/RX_RXRD_types.h	
# sw/dcp/RXDV_recording.h	
# sw/dcp/DC_AC_RX_status.h	
# sw/dcp/DC_rcv_fault_data.h	
# sw/dcp/DC_osp.h	
# sw/dcp/DODS.c	
# sw/dcp/DOMS.c	
# sw/dcp/DFFD_DCP_LRU_conditions.h	
# sw/dcp/DO_DODS_message_handling.h	
# sw/dcp/DO_DOMS_mode_switch.h	
# sw/dcp/DOSS_lru_fault_text.c	
# sw/dcp/DO_xOMN_display_data.h	
# sw/dcp/xOMN_display_data.c	
# sw/waas/WAAS_rcv_status_types.h	
# sw/waas/WAAS_dcp_msgs.h	
# sw/waas/WAAS_dcp_ssp.h	
# sw/waas/WAAS_LxUT_types.h	
# sw/waas/WAAS_capacities.h	
# sw/waas/WAAS_equipment.h	
# sw/waas/WAAS_RXRD_message_ids.h	
# sw/waas/WAAS_DODS_message_ids.h	
# sw/om/CDWS.c	
# sw/om/MWSE_lru.c	
# sw/om/MWSE_wrefaults.dat	
# sw/om/MWTC.c	
# sw/om/MWTO_subsystem.c	
# sw/om/OM_cd_types.h	
# sw/om/MWTO_top_level.c	
# sw/om/MWIN_mode_switch.c	
# sw/elmg_mgen/DC_status.txt	
# sw/adapt/OSP_DCP.add	
# sw/adapt/NSC_NSCwaas_wzfwwrs1c1.add	
# sw/adapt/SC_SCSwaas_wzfwwrs1c1.add	
# sw/adapt/NSC_NSCwaas_wzfwwrs2c1.add	
# sw/adapt/SC_SCSwaas_wzfwwrs2c1.add	
# sw/adapt/NSC_NSCwaas_wzfwwrs3c1.add	
# sw/adapt/SC_SCSwaas_wzfwwrs3c1.add	
# packages/1config/data/ether.dat	
# packages/1config/scripts/do_machine_id.ksh	
# packages/1config/1config.rev	
# om/WAAS_CDI3_message_ids.h	
# om/WAAS_CDIN_message_ids.h	
# om/CD_cdp3.h	
# om/CDP3.c	
# om/CDWS.c	
# om/CDI3_MAIN.c	
# om/CDIN_MAIN.c	
# packages/glg/MWTO_logical_map.g	
# packages/glg/MWTO_wrs_map.g	
# sw/dcp/RXRI_rcvr_cmds.h	
# sw/dcp/RXGB.c	
# sw/dcp/RX_RXGB_interface.h	

os.chdir(HOME_DIR)