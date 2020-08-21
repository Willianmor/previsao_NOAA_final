#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Import bibliotecas
import os
import ftplib
import zipfile
import glob
import time
from threading import Thread
from time import sleep

#import scripts auxiliares
import temporizador
from temporizador import IntervalRunner
from log import log,logerro
from descompactar import unzipefile

def automation(*args):
    try:

        log()
        #Acessando a classe FTP da biblioteca ftplib
        from ftplib import FTP

        #Criando uma variável com 
        ftp = FTP('ftp.cpc.ncep.noaa.gov')     # connect to host, default port

        #Login do ftp
        ftp.login()

        #Avaliando diretórios
        #ftp.dir()

        #Entrando no diretório dos dados
        ftp.cwd("/GIS/GRADS_GIS/GeoTIFF/PREC_FORECAST/")
        #ftp.retrlines('LIST')

        #Lista todos os arquivos do diretório
        dirs = ftp.nlst()

        #Imprimindo 
        #[print(str(i)+' '+j) for i,j in enumerate(dirs)]

        #Criando uma descrição para os arquivos
        description_files = [i for i in dirs if len(i.split('.'))>1]
        #Percorrendo os elementos listados, baixando os dados não existentes na pasta e descompactando os dados.
        for file in description_files:
            if os.path.isfile(file):
                print('already downloaded file: '+file)
                continue
            with open(file, 'wb') as fp:
                ftp.retrbinary('RETR '+file, fp.write) # save non-directory files (readme, etc.)
        ftp.close() # close ftp connection
        unzipefile()

    except Exception as e:
        print(e)
        logerro()

#Rodando de tempo e tempo
interval_monitor = IntervalRunner(86400.0,automation)
interval_monitor.start()


resposta = input('Começou...\n')


