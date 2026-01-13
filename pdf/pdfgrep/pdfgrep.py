import fitz
import re
import datetime
import argparse
import os
import pandas as pd
import pdb
import sys

sys.stdout.reconfigure(encoding='utf-8')

'''

KNOWN BUGS:

* Doesn't handle headings properly that have Unicode Character “→” (U+2192)

'''

def search_by_word(page, regex, color_str):
    # doc = fitz.open(file_path)
    # doc.get_toc()

    # found = 0

    matches = []

    # for page in doc:
    wlist = page.get_text("words", delimiters=None)
   

    for word in wlist:
        # if re.search(regex_str, word[4]):
        if regex.search(word[4]):
            matches.append(word[4])
            #print(word[4])
            # found += 1
            r = fitz.Rect(word[:4])
            annot = page.add_highlight_annot(r)
            annot.set_colors(stroke=fitz.pdfcolor[color_str])
            annot.update()
    
    return matches


def search_by_line(page, list_regex_objs, color_str,highlight=False):
    # doc = fitz.open(file_path)
    # doc.get_toc()

    # found = 0

    # shift for zero index first page is 1
    page_number = page.number + 1 
    matches = []

    # for page in doc:
    dict_page = page.get_text('dict')
    blocks = dict_page['blocks']

    line_count = 0

    line_strs = []
    
    # pdb.set_trace()

    # print(list_regex_objs[0].pattern)

    for block in blocks:

        if 'lines' in block:

            lines = block['lines']

            for line in lines:
                line_str = line['spans'][0]['text']
                line_rect = fitz.Rect(line['spans'][0]['bbox'])
                regex_matches = []

                for regex in list_regex_objs:
                    if regex.search(line_str):
                        regex_str = regex.pattern
                        regex_matches.append(regex_str)
                
                if len(regex_matches) > 0:
                    #print(str_text)
                    #pdb.set_trace()
                    
                   # only match 

                    # unwind regex_matches into a delimited string
                    regex_matches_str = ", ".join(regex_matches)

                    line_strs.append(((page_number,line_count),page_number,line_count,regex_matches_str,line_str))

                    if highlight:
                        annot = page.add_highlight_annot(line_rect)
                        annot.set_colors(stroke=fitz.pdfcolor[color_str])
                        info_annot = dict([('page_number',page_number),('line_count',line_count),('regex_matches_str',regex_matches_str),('line_str',line_str)])
                        #annot.set_info(info=info_annot, content=line_str)
                        #annot.set_info(content=line_str)
                        info_list = [str(page_number), str(line_count), regex_matches_str, line_str]

                        # Use ascii record seperator as a delimiter
                        info_str = '\|'.join(info_list)

                        annot.set_info(content=info_str)
                        #annot.set_info(info=info_annot)
                        annot.update()

                line_count+=1

    return line_strs

    # for word in wlist:
    #     # if re.search(regex_str, word[4]):
    #     if regex.search(word[4]):
    #         matches.append(word[4])
    #         #print(word[4])
    #         # found += 1
    #         r = fitz.Rect(word[:4])
    #         annot = page.add_highlight_annot(r)
    #         annot.set_colors(stroke=fitz.pdfcolor[color_str])
    #         annot.update()
    
    # return matches

def get_toc_name(single_toc):
    return single_toc[1]

def process_data2(fname, 
                highlighted_fname, 
                list_regex_objs):

    doc = fitz.open(fname)

    toc = doc.get_toc()

    toc_names = map(get_toc_name, toc)

    new_doc = False  # indicator if anything found at all

    all_matches = [] # A list to store rows that match

    for page in doc:
        pg_matches = search_by_line(page, list_regex_objs, 'green', highlight=True)

        all_matches += pg_matches
    
    if len(all_matches) > 0:
        new_doc = True
    
    if new_doc:
        doc.save(highlighted_fname)

    df = pd.DataFrame(all_matches,columns = ['PAGE_AND_LINE_TUP','PAGE_NO','LINE_NO','REGEX_MATCHES','TEXT'])
    # df.to_excel(results_fname)
    return df

def extract_matches_from_highlighted_pdf(highlighted_fname):
    doc = fitz.open(highlighted_fname)

    line_strs = []

    for page in doc:
        for annot in page.annots():
            data = annot.info['content']
            page_number, line_count, regex_matches_str, line_str = data.split('\|')

            page_number = int(page_number)
            line_count = int(line_count)

            page_count_tuple = (page_number, line_count)

            line_strs.append(((page_number,line_count),page_number,line_count,regex_matches_str,line_str))
    
    df = pd.DataFrame(line_strs,columns = ['PAGE_AND_LINE_TUP','PAGE_NO','LINE_NO','REGEX_MATCHES','TEXT'])
    return df


def get_headings_Dataframe(fname):

    doc = fitz.open(fname)
    toc = doc.get_toc()

    all_headings_data = []

    # pdb.set_trace()

    for heading in toc:
        page_number = heading[2]
        page = doc[page_number-1]

        heading_name = heading[1]

        # Split only at the first space i.e. '2.1.1.1.2 Message Size' is split into ['2.1.1.1.2', 'Message Size']
        heading_split = heading_name.split(' ',1)

        # if (heading_split[0] == '3.1.1.2.1.5.13'):
        #     pdb.set_trace()
        
        if(len(heading_split) > 1):
            heading_number = heading_split[0] + ' '
        else:
            heading_number = heading_split[0]

        #pdb.set_trace()
        #print(heading_name)
        # results = search_by_line(page,[re.compile(heading_name)], 'green',highlight=False)

        matches = []

        # for page in doc:
        dict_page = page.get_text('dict')
        blocks = dict_page['blocks']

        line_count = 0

        line_strs = []
        
        for block in blocks:

            if 'lines' in block:

                lines = block['lines']

                for line in lines:
                    line_str = line['spans'][0]['text']
                    # print(line_str)

                    if line_str.startswith(heading_number):
                        # if (heading_split[0] == '3.1.1.2.1.5.13'):
                        #     pdb.set_trace()
                        # line_strs.append(((page_number,line_count),page_number,line_count,heading_number,line_str))
                        line_strs.append(((page_number,line_count),page_number,line_count,heading_number,heading_name))

                    line_count += 1

        all_headings_data += line_strs


    df = pd.DataFrame(all_headings_data,columns = ['PAGE_AND_LINE_TUP','PAGE_NO','LINE_NO','NUMBER','SECTION_NAME'])
    return df


def find_heading(match_page, match_line, headings_df):

    headings_before = headings_df[headings_df.PAGE_AND_LINE_TUP < (match_page,match_line)]

    heading_match = ""

    if len(headings_before) == 0:
        heading_match = ""
    else:
        # Get heading name from last row
        heading_match = headings_before['SECTION_NAME'].values[-1]

    return heading_match


def combine_headings_and_matches(matches_df, headings_df):

    for index, row in matches_df.iterrows():
        page_number = row['PAGE_NO']

        
        # Compare with the headings_df

    return []

if __name__ == "__main__":



    # # Testing data for "power"
    # input_dir = './test/test_pages/'
    # input_fnames = ['Power_Test_Pages_WID_SD_ICD_909_V11.pdf']

    input_dir = '/mnt/c/work/04_Projects/WPR00129344_SNMP_and_OM_CY25/docs/'
    input_fnames = ['WID_SD_ICD_909_V11.pdf',
                    'WID_SD_ICD_910_V8.pdf',
                    'WID_SD_SDD_104_V8.pdf',
                    'WID_SD_SRS_106_V21.pdf']


    input_fnames = list(map(lambda fname: os.path.join(input_dir,fname), input_fnames))

    output_dir = 'test_output'

    try:
        os.mkdir(output_dir)
    except FileExistsError:
        pass # same as mkdir -p 
        #print("output dir already exists\n")

    # # Test regex variations
    # regex_strs = ["PCU[^T]"]
    # regex_strs = ["conditioner","conditioners","conditioning","power.control","power.conditioner"]
    # regex_strs = ['Power']

    '''
    •	PCU  
    •	Power  
    •	Conditioner  
    •	Control  
    •	SNMP  
    '''

    regex_strs = []
    regex_strs += ["PCU[^T]","pcutrap","pcu trap","pc_trap","pcupoll","pcu controller","pcu receptacle",]
    regex_strs += ["Power.Conditioner", "Conditioner", "Power.Conditioning", "PWR.COND", "Receptacle", "Recepticle", ]
    regex_strs += ["Power.Control","Control.Power.Command", "PCCP", "Control.Power"]
    regex_strs += ["SNMP","SNMP.Power"]
    

    list_regex_objs = []

    for a_str in regex_strs:
        list_regex_objs.append(re.compile(a_str,flags=re.IGNORECASE))
    
    for fname in input_fnames:

        print("Processing file: " + fname)

        all_matches = []

        base_fname = os.path.basename(fname)
        base_fname = os.path.splitext(base_fname)[0]

        highlighted_fname = os.path.join(output_dir, base_fname + "_hl.pdf")

        results_fname = os.path.basename(fname)
        results_fname = os.path.join(output_dir, os.path.splitext(results_fname)[0] + "_grep.xlsx")

        matches_df = process_data2(fname, highlighted_fname, list_regex_objs)


        heading_fname = os.path.basename(fname)
        heading_fname = os.path.join(output_dir, os.path.splitext(heading_fname)[0] + '_grep.xlsx')

        #headings_df = get_heading_page_and_line_no(fname)
        #headings_df.to_excel(heading_fname)
        headings_df = get_headings_Dataframe(fname)

        headings_list = []

        for index, row in matches_df.iterrows():
            headings_list.append(find_heading(row['PAGE_NO'], row['LINE_NO'], headings_df))

        matches_df['SECTION_NAME'] = headings_list
        matches_df.to_excel(results_fname)

        matches_uniq_headings = list(matches_df['SECTION_NAME'].unique())

        section_summary = []

        #Create a summary for each section's REGEX_MATCHES
        for uniq_heading in matches_uniq_headings:
            # Get info about heading
            heading_info_row = headings_df[headings_df['SECTION_NAME'] == uniq_heading]

            # Handles case where no heading exists (i.e. matches in the table of contents of the file)
            if heading_info_row.empty:
                heading_pg_no = -1
            else:
                heading_pg_no = heading_info_row['PAGE_NO'].values[-1]

            section_matches_df = matches_df[matches_df['SECTION_NAME'] == uniq_heading]
            section_matches_df['REGEX_MATCHES']

            #all_matches = section_matches_df['REGEX_MATCHES'].to_list()
            #uniq_matches = set(all_matches)
            #uniq_matches = list(uniq_matches)
            #uniq_matches.sort()
            uniq_matches = section_matches_df['REGEX_MATCHES'].unique().tolist()

            values = []

            for a_match in uniq_matches:
                split_values = a_match.split(',')
                clean_values = map(lambda x: x.strip(), split_values) # strip whitespace
                clean_values = list(clean_values)
                values += clean_values
            
            # pdb.set_trace()

            uniq_matches = set(values)
            uniq_matches = list(uniq_matches)
            uniq_matches.sort()

            # pdb.set_trace()
            uniq_matches.sort()
            uniq_matches_str = ', '.join(uniq_matches)

            section_summary.append((heading_pg_no, uniq_heading, uniq_matches_str))
        
        section_summary_df = pd.DataFrame(section_summary,columns = ['PAGE_NO','SECTION_NAME','REGEX_MATCHES'])

        section_summary_fname = os.path.basename(fname)
        section_summary_fname = os.path.join(output_dir, os.path.splitext(section_summary_fname)[0] + '_section_summary.xlsx')
        section_summary_df.to_excel(section_summary_fname)

