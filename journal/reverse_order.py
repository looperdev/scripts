import re
import itertools

with open('input.md') as f:
    lines = f.readlines()

entries = []

group_id = 0
entries.append([])

for aLine in lines:
    
    if(re.search(r'^# (\d{4}-\d{2}-\d{2})', aLine)):
        entries.append([aLine])
        # print(aLine)
    else:
        entries[-1].append(aLine)

# Sort entries by date descending 
entries.reverse()

reversed_entries = list(itertools.chain(*entries))

with open('output.md','w') as f:
    f.writelines(reversed_entries)


