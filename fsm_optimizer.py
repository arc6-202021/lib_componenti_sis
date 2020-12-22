"""
FSM_OPTIMIZER:
ottimizza un file blif con la macchina a stati finiti.

Il programma copia il file originale per n_copies volte,
poi esegue l'ottimizzazione su queste copie.
A fine ottimizzazione vengono memorizzati
i file blif ottimizzati e viene rieseguita la ottimizzazione.

Questo processo continua per n_layer volte.

A fine programma la macchina a stati finiti
con l'area minore viene salvata nel file
controllore_ottimizzato.blif
"""

__author__ = "Zenaro Stefano"
__version__ = "2020-12-22 01_01"

import os
import shutil
import subprocess
import sys
import time

boold = False

starttime = int(time.time())                               # timestamp inizio programma
current_dir = os.path.dirname(os.path.realpath(__file__))  # cartella script attuale
fsm_dir = os.path.join(current_dir, "fsm")                 # cartella con FSM
fsm_path = os.path.join(fsm_dir, "controllore.blif")       # file FSM da ottimizzare

n_layer = 10   # numero strati di ottimizzazione
n_copies = 10  # numero di copie ottimizzate per strato


def copyntimes(t_file, t_n, t_layer):
    """
    Copia il file t_file per t_n volte con il nome:
    <nome_file>_L<t_layer>_<i>.<estensione>

    Dove:
    * <nome_file> e' il nome del file t_file senza estensione,
    * <t_layer> indica in che strato di ottimizzazione si trova il file
    * <i> e' un numero che va da 1 a <t_n>+1
    * <estensione> e' la estensione del file t_file e delle sue copie

    :param str t_file: percorso file da copiare
    :param int t_n: numero di copie
    :param int t_layer: usato nel nome della copia per indicare strato di ottimizzazione
    """
    # recupera percorso, nome e estensione del file
    file_path = os.path.dirname(t_file)
    file_nameext = os.path.basename(t_file)
    file_name, file_ext = os.path.splitext(file_nameext)

    # per t_n volte (da 1 a t_n1+) copia il file
    for i in range(1, t_n+1):
        copy_path = os.path.join(file_path, file_name + "_L" + str(t_layer) + "_" + str(i) + file_ext)
        shutil.copyfile(t_file, copy_path)


def optimize(blif_file, test_directory, output, optimized_blif):
    """
    Esegue SIS importando lo script di ottimizzazione.

    :param str blif_file: percorso file da ottimizzare
    :param str test_directory: cartella in cui si trova il file e in cui verra' memorizzato script temporaneo
    :param str output: percorso del file output della simulazione
    :param str optimized_blif: percorso file blif_file ottimizzato
    """
    sis_script = os.path.join(test_directory, "exec_test.txt")

    optimizer_script = os.path.join(current_dir, "_optimizer_scripts", "optimize_fsm.script")
    
    sis_simulation_script = "set sisout " + output + "\n" + \
                            "read_blif " + blif_file + "\n" + \
                            "source " + optimizer_script + "\n" + \
                            "write_blif " + optimized_blif + "\n" + \
                            "quit"
    try:
        # crea file con script per eseguire script di simulazione
        with open(sis_script, "w") as s:
            s.write(sis_simulation_script)
        
        # vai nella cartella dei test e esegui lo script che esegue lo script di simulazione
        sis_command = "(cd " + test_directory + "; sis -t pla -f exec_test.txt -x)"
        subprocess.Popen(sis_command, stdout=subprocess.PIPE, shell=True).communicate()  # Launch SIS subprocess
    except IOError:
        return -1
    return 0


def parse_output(output):
    """
    Legge il file in output e restituisce area e numero di gate.

    :param str output: percorso file output della simulazione
    :return float total_area: area del circuito ottimizzato
    :return float gate_count: numero di gate del circuito ottimizzato
    """
    map_stats = False
    str_total_area = "-1"
    str_gate_count = "-1"

    with open(output, "r") as fout:
        line = fout.readline()
        while line != "":
            if "sis>print_map_stats" in line:
                map_stats = True
            
            if map_stats and "Total Area" in line:
                str_total_area = line.replace("Total Area", "").strip().strip("=").strip()
            elif map_stats and "Gate Count" in line:
                str_gate_count = line.replace("Gate Count", "").strip().strip("=").strip()

            line = fout.readline()

    total_area = float(str_total_area)
    gate_count = float(str_gate_count)

    return total_area, gate_count


def printlog(t_text, t_file):
    """
    Prints and logs text. (with timestamp)

    :param str t_text: string with text to write to file and print
    :param IO t_file: Opened log file
    """
    print("[{}]".format(int(time.time())) + t_text)
    t_file.write("[{}]".format(int(time.time())) + t_text + "\n")


if __name__ == "__main__":

    smallest_area = None
    best_fsm = ""
    best_fsm_gates = None

    file_path = os.path.dirname(fsm_path)
    outputs_path = os.path.join(file_path, "outputs")

    file_nameext = os.path.basename(fsm_path)
    file_name, file_ext = os.path.splitext(file_nameext)
    
    # crea la cartella degli output di ottimizzazione (se necessario)
    if not os.path.isdir(outputs_path):
        os.makedirs(outputs_path)

    with open("fsm_optimizer_log.txt", "w") as flog:
        # layer 1 di ottimizzazione
        # copia per n_copies volte il file
        if boold:
            printlog("creo layer 1 di simulazione", flog)
        copyntimes(fsm_path, n_copies, 1)

        # layer di ottimizzazione
        for layer in range(1, n_layer+1):
            if boold:
                printlog("eseguo ottimizzazioni del layer {}".format(layer), flog)
            
            for i in range(1, n_copies+1):
                # percorso della copia da ottimizzare, dell'output di simulazione e del blif ottimizzato
                copy_path = os.path.join(file_path, file_name + "_L" + str(layer) + "_" + str(i) + file_ext)
                output_path = os.path.join(outputs_path, file_name + "_L" + str(layer) + "_" + str(i) + "_optimized_out.txt")
                opt_blif_path = os.path.join(file_path, file_name + "_L" + str(layer+1) + "_" + str(i) + file_ext)

                if boold:
                    printlog("file da ottimizzare: " + copy_path, flog)
                    printlog("output della ottimizzazione: " + output_path, flog)
                    printlog("file ottimizzato: " + opt_blif_path, flog)

                # esegui SIS e ottimizza il file blif
                if optimize(copy_path, file_path, output_path, opt_blif_path) == 0:
                    total_area, gate_count = parse_output(output_path)
                    if boold:
                        printlog("Statistiche della fsm dopo l'ottimizzazione '{}':".format(file_name + "_L" + str(layer) + "_" + str(i)), flog)
                        printlog("* area: {}".format(total_area), flog)
                        printlog("* numero di gate: {}".format(gate_count), flog)

                    # memorizza statistiche della miglior fsm e
                    # il suo percorso
                    if not smallest_area:
                        smallest_area = total_area
                        best_fsm_gates = gate_count
                        best_fsm = opt_blif_path

                    elif total_area < smallest_area:
                        smallest_area = total_area
                        best_fsm_gates = gate_count
                        best_fsm = opt_blif_path
                else:
                    printlog("[ERRORE] Qualcosa e' andato storto", flog)
                    sys.exit(1)
        
        printlog("La miglior fsm e' '{}'".format(best_fsm), flog)
        printlog("* area: {}".format(smallest_area), flog)
        printlog("* numero di gate: {}".format(best_fsm_gates), flog)
        printlog("L'ottimizzazione e' durata {} secondi".format(int(time.time()) - starttime), flog)

        # copia la FSM migliore mettendoci un nome riconoscibile
        shutil.copy(best_fsm, os.path.join(file_path, "controllore_ottimizzato.blif"))