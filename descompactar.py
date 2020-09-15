#!/usr/bin/env python3

import os
import glob
#pip install glob2==0.4.1
import zipfile

dir_name_base = os.path.dirname(os.path.realpath(__file__))
#print(dir_name_base)

#Descompactar arquivo
def unzipefile():
    dir_name_base = os.path.dirname(os.path.realpath(__file__))
    for arc_name in glob.iglob(os.path.join(dir_name_base, "*.zip")):
        try:
            arc_dir_name = os.path.splitext(os.path.basename(arc_name))[0]
            zf = zipfile.ZipFile(arc_name)
            #Exporta o tif dentro de uma pasta
            #zf.extractall(path=os.path.join(dir_name_base, arc_dir_name))
            #Exporta o tif na pasta raiz
            zf.extractall(path=os.path.join(dir_name_base, dir_name_base))
            zf.close() # close file after extraction is completed'''
            arquivo=str(arc_dir_name)
            print("vou printar")
            print(arquivo)
            permissao = 755
            os.chmod(arquivo,permissao)
        except:
            os.remove(os.path.join(dir_name_base, arc_name))
            continue

unzipefile()








