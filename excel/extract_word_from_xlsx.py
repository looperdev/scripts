import zipfile
filename = 'CHIA_matrix.xlsm'
prefix = filename.split('.xlsx')[0]

fd = zipfile.ZipFile(filename, 'r')

for a_zipinfo in fd.infolist():
    if a_zipinfo.filename.startswith('xl/embeddings/Microsoft_Word'):
        fd.extract(a_zipinfo)

# Join the word docs together if there are multiple ones


# Build a program that will create snapshots of each CHIA and then create the design review slides.