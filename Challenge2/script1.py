#!/usr/bin/env python
import argparse
import re




parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', dest="file_path", required=True)
args = parser.parse_args()

f = open(args.file_path, "r")
file_text  = f.readlines()
f.close()

bids = []
i = 0
# << read >>
for line in file_text:
    check = line.strip()
    if not check:
        continue
    number = re.findall(r'\d+', line)
    val = int(number[0])
    name = line.replace(number[0], '').strip()
    i = i+1
    if i -1 == 0:
        items = val
        continue
    bids.append((val, name)) 



bids.sort(key=lambda k: (-k[0], k[1]))


# << Write >> 
cnt = 0
res = ['\n', "========= << Result>> ========", '\n']

if len(bids) > items:
    for bid in bids:
        if items > 0 :
            res.append(str(bid[1]) + ' '+ str(bids[cnt+1][0]))
        else:
            res.append(str(bid[1]) + ' Lost')

        cnt = cnt +1
        items = items - 1

if len(bids) == 0:
    res.append(" No Winners ")
if len(bids)!= 0  and len(bids) <= items:
    res.append(" Not Handeled but i think all is Winners :v")

f = open(args.file_path, "a+")
f.writelines(['{} \n'.format(i) for i in res])
f.close()