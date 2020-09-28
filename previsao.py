#-*- coding: utf-8 -*-
#!/usr/bin/env python3

#Import bibliotecas
import os
import ftplib
import zipfile
import glob
import time
import threading

#import scripts auxiliares
import temporizador
from temporizador import IntervalRunner
#import import_data
from import_data import automation


def previsao():
    automation()

#Rodando de tempo e tempo
interval_monitor = IntervalRunner(86400.0,previsao)
interval_monitor.start()
threading.Event().wait()