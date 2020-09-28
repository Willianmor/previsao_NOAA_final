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
            name = str(arc_dir_name + ".tif")
            if os.path.isfile(name):
                print("O Arquivo já existe na pasta")
                continue
            else:
                print("O Arquivo não existe na pasta e vai descompactar")
                #Exporta o tif dentro de uma pasta
                #zf.extractall(path=os.path.join(dir_name_base, arc_dir_name))
                #Exporta o tif na pasta raiz
                zf.extractall(path=os.path.join(dir_name_base, dir_name_base))
                zf.close() # close file after extraction is completed'''
                arquivo=str(arc_dir_name)
                print(arquivo)
                permissao = 755
                os.chmod(arquivo,permissao)
        except:
            #Tratamento o nome
            #print("_______________#######_____________________")
            nome = str(arc_dir_name + ".zip")
            tamanho = os.stat(nome).st_size/1024
            if (tamanho<300):
                print("O arquivo existe, mas está corrompido. Vai deletar!")
                os.remove(os.path.join(dir_name_base, arc_name))
                continue
            else:
                print("O Arquivo já existe na pasta")
                continue
            

unzipefile()








