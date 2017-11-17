# by Kerim Celik for genomics final project
import sys


def getPhotosynthesisAccs(filename, query):
    outp = open('photoAccessions.txt', 'w+')
    inp = open(filename, 'r')
    orfFile = inp.read()
    added = []
    lines = orfFile.split('\n')
    for line in lines:
        vals = line.split('\t')
        if (len(vals) != 11):
            continue
        # print(vals)
        if (query in vals[5]):
            candidate = vals[4]
            if candidate not in added:
                outp.write(candidate + ' \n')
                added.append(candidate)
    inp.close()
    outp.close()

def getPhotosynthesisAccFuncts(filename, query):
    outp = open('photoAccFuncts.txt', 'w+')
    inp = open(filename, 'r')
    orfFile = inp.read()
    added = []
    lines = orfFile.split('\n')
    for line in lines:
        vals = line.split('\t')
        if (len(vals) != 11):
            continue
        # print(vals)
        if (query in vals[5]):
            candidate = vals[4]
            if candidate not in added:
                outp.write(candidate + '     Function: ' + vals[5] + ' \n')
                added.append(candidate)
    inp.close()
    outp.close()

def getPhotosynthesisContigs(filename, query):
    outp = open('photoContigs.txt', 'w+')
    inp = open(filename, 'r')
    orfFile = inp.read()
    added = []
    lines = orfFile.split('\n')
    for line in lines:
        vals = line.split('\t')
        if (len(vals) != 11):
            continue
        # print(vals)
        if (query in vals[5]):
            candidate = vals[0]
            if candidate not in added:
                outp.write(candidate + ' \n')
                added.append(candidate)
    inp.close()
    outp.close()

def main():
    if len(sys.argv) != 4:
        print("Error! Invalid number of command line arguments.\n Should be 3: scriptName fileName optionNum queryStr.")
        return
    fil = sys.argv[1]
    if sys.argv[2] == '0':
        getPhotosynthesisAccs(fil, sys.argv[3])
    elif sys.argv[2] == '1':
        getPhotosynthesisContigs(fil, sys.argv[3])
    elif sys.argv[2] == '2':
        getPhotosynthesisAccFuncts(fil, sys.argv[3])
    else:
        print("Error! Integer options are 0 for accession numbers or 1 for contigs or 2 for functions.")
        return

if __name__ == '__main__':
    main()
