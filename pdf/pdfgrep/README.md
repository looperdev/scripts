
# Grep O&M Docs  

## Specs

Examine the following documents and return:  

* list of document  
* section number  

Documents

•	O&M SRS – WID_SD_SRS_106  
•	O&M SDD – WID_SD_SDD_104  
•	ICD for O&M – WID_SD_ICD_909  
•	Software ICD Addendum – WID_SD_ICD_910  

Return any of the following terms that are referenced or used.  

Search Terms

•	PCU  
•	Power  
•	Conditioner  
•	Control  
•	SNMP  

If your search turns up possible additional search terms, please include those as well.  


## False Positives

* Some of the matches are very general SNMP and Power Matches and may not relate to PDU. 
* "Control" is such a general term it is found everywhere.
* "Power" that does not relate to PCU is probably in the document.  

## Other Tools  

* https://github.com/mrabarnett/mrab-regex  
* ugrep  
* pdfgrep  
* https://docs.python.org/3.8/library/re.html  


## TODO  
TODO: Try using ugrep


TODO: Create a better test dataset to verify the code is working.  

TODO: Include false positives in the list  

TODO: Write a config that allows:
        - Page Ranges
        - Highlight options
        - Regex options

## Procedure

Main Steps:

1. Use ripgrep-all (rga) <https://github.com/phiresky/ripgrep-all> to find all occurrences of:  
   
   * "PCU[^T]", "Power", "Conditioner", "SNMP"