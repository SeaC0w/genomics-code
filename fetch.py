# by Kerim Celik for genomics final project

def getPhotosynthesisAcc(filename):
    outp = open('accessions.txt', 'w+')
    inp = open(filename, 'r')
    orfFile = inp.read()
    for line in orfFile:
        vals = line.split()
        if ('Photosy' in vals[5]) or ('photosy' in vals[5]):
            outp.write(vals[4] + ' \n')
    inp.close()
    outp.close()
