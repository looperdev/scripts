# CREATE DIRECTORY STRUCTURE
mkdir -p changed_files/add/sw/dcp

mkdir -p changed_files/add/sw/om
mkdir -p changed_files/add/sw/rtc

mkdir -p changed_files/add/sw/elmg_mgen
mkdir -p changed_files/add/sw/adapt

mkdir -p changed_files/add/packages/1config/data
mkdir -p changed_files/add/packages/1config/scripts
mkdir -p changed_files/add/packages/glg/glg

mkdir -p changed_files/add/tools/misc/shadow/sl1/adapt/

##################################################################
# MAIN - DCP
cp checkout/m2-dcp/main_source/DOMN_MAIN.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/main_source/GOMN_MAIN.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/main_source/RXRM_MAIN.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/main_source/RXRD_MAIN.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/main_source/DFFD_MAIN.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/main_source/DFAC_MAIN.c changed_files/add/sw/dcp/

# MAIN - OM
cp checkout/m2-dcp/main_source/CDI3_MAIN.c changed_files/add/sw/om/
cp checkout/m2-dcp/main_source/CDIN_MAIN.c changed_files/add/sw/om/

# MAIN - RTC
cp checkout/m2-dcp/main_source/DMMR_MAIN.c changed_files/add/sw/rtc/

##################################################################
# LIB - DCP

# CHANGED DCP FILES
cp checkout/m2-dcp/lib_source/RXRI.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXRL.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXR1.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXR3.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXRS.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXRI_rcvr_cmds.h changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXHC.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXGP.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXDV.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXGE.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RX_RXRM_interface.h   changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RX_RXRM_types.h   changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RX_G3_logs.h  changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RX_RXRD_interface.h changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RX_RXRD_types.h   changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXDV_recording.h  changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DC_AC_RX_status.h changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DC_rcv_fault_data.h   changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DC_osp.h  changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DODS.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DOMS.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DFFD_DCP_LRU_conditions.h changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/DO_DODS_message_handling.h changed_files/add/sw/dcp/   
cp checkout/m2-dcp/lib_source/DO_DOMS_mode_switch.h changed_files/add/sw/dcp/  
cp checkout/m2-dcp/lib_source/DOSS_lru_fault_text.c changed_files/add/sw/dcp/  
cp checkout/m2-dcp/lib_source/DO_xOMN_display_data.h changed_files/add/sw/dcp/  
cp checkout/m2-dcp/lib_source/xOMN_display_data.c changed_files/add/sw/dcp/  

# NEW DCP FILES
cp checkout/m2-dcp/lib_source/RXRI_rcvr_cmds.h changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RXGB.c changed_files/add/sw/dcp/
cp checkout/m2-dcp/lib_source/RX_RXGB_interface.h changed_files/add/sw/dcp/

# LIB - OM
cp checkout/m2-dcp/lib_source/CDWS.c changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/MWSE_lru.c changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/MWSE_wrefaults.dat changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/MWTC.c changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/MWTO_subsystem.c changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/OM_cd_types.h changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/MWTO_top_level.c changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/MWIN_mode_switch.c changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/CD_cdp3.h  changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/CDP3.c  changed_files/add/sw/om/
cp checkout/m2-dcp/lib_source/CDWS.c  changed_files/add/sw/om/

# LIB - WAAS
cp checkout/m2-dcp/lib_source/WAAS_rcv_status_types.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_dcp_msgs.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_dcp_ssp.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_LxUT_types.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_capacities.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_equipment.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_RXRD_message_ids.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_DODS_message_ids.h changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_CDI3_message_ids.h  changed_files/add/sw/waas/
cp checkout/m2-dcp/lib_source/WAAS_CDIN_message_ids.h  changed_files/add/sw/waas/

##################################################################
# ADAPT DATA
cp checkout/m2-dcp/shadow/sl1/adgen/OSP_DCP.add changed_files/add/sw/adapt/


cp checkout/m2-dcp/shadow/sl1/adgen/NSC_NSCwaas_wzfwwrs1c1.add changed_files/add/tools/misc/shadow/sl1/adapt/
cp checkout/m2-dcp/shadow/sl1/adgen/SC_SCSwaas_wzfwwrs1c1.add changed_files/add/tools/misc/shadow/sl1/adapt/
cp checkout/m2-dcp/shadow/sl1/adgen/NSC_NSCwaas_wzfwwrs2c1.add changed_files/add/tools/misc/shadow/sl1/adapt/
cp checkout/m2-dcp/shadow/sl1/adgen/SC_SCSwaas_wzfwwrs2c1.add changed_files/add/tools/misc/shadow/sl1/adapt/
cp checkout/m2-dcp/shadow/sl1/adgen/NSC_NSCwaas_wzfwwrs3c1.add changed_files/add/tools/misc/shadow/sl1/adapt/
cp checkout/m2-dcp/shadow/sl1/adgen/SC_SCSwaas_wzfwwrs3c1.add changed_files/add/tools/misc/shadow/sl1/adapt/

##################################################################

cp /checkout/m2-dcp/elmg/DC_status.txt changed_files/add/sw/elmg_mgen

##################################################################
# PACKAGES
cp /checkout/m2-dcp/packages/1config/1config.rev changed_files/add/packages/1config/
cp /checkout/m2-dcp/packages/1config/data/ether.dat changed_files/add/packages/1config/data/
cp /checkout/m2-dcp/packages/1config/scripts/do_machine_id.ksh changed_files/add/packages/1config/scripts/

cp /checkout/m2-dcp/packages/glg/glg/MWTO_logical_map.g changed_files/add/packages/glg/glg/
cp /checkout/m2-dcp/packages/glg/glg/MWTO_wrs_map.g changed_files/add/packages/glg/glg/
cp /checkout/m2-dcp/packages/glg/glg.config changed_files/add/packages/glg/
cp /checkout/m2-dcp/packages/glg/glg.rev changed_files/add/packages/glg/
