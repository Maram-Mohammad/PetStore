#!/usr/bin/env python
import argparse
import re


parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', dest="file_path", required=True)
args = parser.parse_args()

f = open(args.file_path, "r")
file_text  = f.readlines()
f.close()

bids = {}
vals = []
i = 0
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

    vals.append(val)
    if not bids.get(val):
        bids[val] = [name]
    else:
        names = bids.get(val)
        names.append(name)
        names.sort()
        bids[val] = names


vals.sort(reverse=True)

i=0
res = ['\n', "========= << Result>> ========", '\n']
while i<len(vals) and items < len(vals):
    ones = bids.get(vals[i])
    for one in ones:
        one_val = vals[i+1] if items > 0  else 'Lost'
        res.append(one + ' '+ str(one_val))
        i = i+1
        items = items - 1
if len(vals) == 0:
    res.append(" No Winners ")
if len(vals)!= 0  and len(vals) <= items:
    res.append(" Not Handeled but i think all is Winners :v")

f = open(args.file_path, "a+")
f.writelines(['{} \n'.format(i) for i in res])
f.close()   