#goes through a list of sequence titles (here, the match_OTUs_to_sequences.py script) and
#matches the to the original FASTA file (here, VAMPS pyrotag sequences), outputs the matching
#sequences to a separate outfile
#this one is formatted to only take the name of the fasta

import sys
# from sets import Set

titlefile = sys.argv[1]
fastafile = sys.argv[2]
rika = open(titlefile)
infile_titlelist = rika.read()
titlefilename = titlefile.rstrip('.txt')
outfile = open(titlefilename + '.fasta', 'a')

title_list = [] #makes an empty list to later compare to the fasta file
read_titles = infile_titlelist.split('\n')
for read_title in read_titles:
	title_list.append(read_title)
#print title_list

seqs = []
D = {}

readfile = open(fastafile).read()
fastas = readfile.split('>') #splits into fastas
for fasta in fastas: #iterates through each of the sequences
	lines = fasta.split('\n')
	titleline = lines[0]
	words = titleline.split(' ')
	title = words[0]
	D[title] = fasta #makes a dictionary such that the title corresponds to the whole sequence
	seqs.append(title) #makes a list of the sequence titles
#print virome_reads

#these sets allow me to see if an element in one list is present in the other
set1 = set(title_list)
print(set1)
set2 = set(seqs)
#print set2 #D4ZHLFP1:63:C33P7ACXX:3:1105:8866:78230
matches = list(set1.intersection(set2))
print(matches)
for match in matches:
	outfile.write('>' + D[match] + '\n')

rika.close()
outfile.close()
