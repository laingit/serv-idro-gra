import os
import csv

INPUT_CSV = os.path.join(os.path.join(r'C:\Users\alai\PycharmProjects\serv-idro-gra', 'stazioni_annali.csv'))
OUTPUT_DIR = r'e:\_stazioni2014_outputdir'


def read_file():
    my_file = INPUT_CSV
    lista = []
    with open(my_file, newline='') as data_file:  # Error on Windows add encoding='utf-8'
        for entry in csv.reader(data_file, delimiter=";"):
            lista.append(entry)
    return lista


def trasforma_da_lista_static_tuple(lista):
    codice, nome = tuple(lista)
    return (codice,
            nome.strip(),
            )


def specifico_stazioni_csv():
    contenuto = read_file()
    return [trasforma_da_lista_static_tuple(c) for c in contenuto]


def print_stazioni():
    for codice, nome in specifico_stazioni_csv():
        nomedir = "{0}_{1}".format(codice, nome)
        dir_stazione = os.path.join(OUTPUT_DIR, nomedir)
        dir_stazione_2014 = os.path.join(dir_stazione, '2014')
        print(dir_stazione)
        print(dir_stazione_2014)


def mkdir_stazioni_e_2014():
    for codice, nome in specifico_stazioni_csv():
        nomedir = "{0}_{1}".format(codice, nome)
        dir_stazione = os.path.join(OUTPUT_DIR, nomedir)
        dir_stazione_2014 = os.path.join(dir_stazione, '2014')
        os.mkdir(dir_stazione)
        os.mkdir(dir_stazione_2014)


print_stazioni()
# mkdir_stazioni_e_2014()
