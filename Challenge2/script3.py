#!/usr/bin/env python
import argparse
import re
from queue import PriorityQueue




parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', dest="file_path", required=True)
args = parser.parse_args()

f = open(args.file_path, "r")
file_text  = f.readlines()
f.close()

bids = PriorityQueue()
i = 0
maxi = 0
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
    maxi = val if val > maxi else maxi

    bids.put((maxi-val+1, val, name)) 

cnt = 0
res = ['\n', "========= << Result>> ========", '\n']
bids_list=[]
while not bids.empty():
    bids_list.append(bids.get())


if len(bids_list) > items:
    for bid in bids_list:
        if items > 0 :
            res.append(str(bid[2]) + ' '+ str(bids_list[cnt+1][1]))
        else:
            res.append(str(bid[2]) + ' Lost')

        cnt = cnt +1
        items = items - 1


if len(bids_list) == 0:
    res.append(" No Winners ")
if len(bids_list)!= 0  and len(bids_list) <= items:
    res.append(" Not Handeled but i think all is Winners :v")

f = open(args.file_path, "a+")
f.writelines(['{} \n'.format(i) for i in res])
    