import re

print("Starting")
f = open("ERR599078_ORFs.noasterisks.faa.tsv", 'r')
f2 = open("output.txt", 'w+')
scrub = f.read()
scrub = re.sub('\t', ' ', scrub)
f2.write(scrub)
f.close()
f2.close()
