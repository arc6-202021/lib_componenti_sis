"""
BLIF_TESTER:
Simulates all the .blif files by executing simulation scripts 
(files that have a filename that ends with .script).
Each simulation output is put against a correct output (file that ends with correct_output.txt)

> This script was inspired by the script https://github.com/JackHack96/Analyzer-SIS
>
> Modifications:
> * modified the regex pattern
> * added the possibility to specify a different .blif filename
> * with os.listdir() it is possible to test more than one .blif file

"""

__author__ = "Zenaro Stefano"
__version__ = "2020-12-15 01_01"

import os
import sys
import re
import subprocess
import time
import configparser

boold = False
success = True  # used to make the CI fail when success == False


def simulate(test_directory, blif_file, sis_simulation_input, sis_simulation_output):
    """
    Simulate the circuit with SIS.

    First a "exec_test.txt" file is created.
    Its job is to execute the command that
    reads the blif file, sources the simulation script,
    reads and maps the circuit using a library and print statistics.

    The function then navigates into the tests directory and executes
    SIS by passing the "exec_test.txt" file as a parameter.
    This allows SIS to execute the commands in the "exec_test.txt" file.

    :param str test_directory: The directory containing the SIS files
    :param str blif_file: path to the .blif file
    :param str sis_simulation_input: The input file to be simulated (contains simulate commands)
    :param str sis_simulation_output: Path to save the outputs of the simulation
    :return: 0 if everything is ok, otherwise -1
    :rtype: int
    """
    
    sis_script = test_directory + "/exec_test.txt"
    sis_simulation_script = "set sisout " + sis_simulation_output + "\n" + \
                            "read_blif " + blif_file + "\n" + \
                            "source " + sis_simulation_input + "\n" + \
                            "read_library synch.genlib\n" + \
                            "map -m 0 -W\n" + \
                            "print_map_stats\n" + \
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


def compare(sis_simulation_output, sis_correct_outputs, config_path, t_flog):
    """
    Compares a circuit's output with the correct one.
    First the correct output are collected from the file that contains
    the correct outputs.
    Then the function opens up the file containing the output of the simulation
    and checks if the outputs are correct.
    While it reads the file the function also collects the area, most negative slack and total gates
    of the simulated circuit.
    
    Lastly the function returns a score of output correctness as a percentage
    and the rest of the collected data.
    :param str sis_simulation_output: File containing the simulated outputs
    :param str sis_correct_outputs: File containing the correct outputs
    :return: Tuple containing percentage of correctness, circuit area, most negative slack and total gates,otherwise -1
    """
    # correct_outputs = []
    # correct_currentstates = []
    # correct_nextstates = []
    correct_data = []

    output_pattern = re.compile(r"Outputs:(\s)?([0-1]+)")
    currentstate_pattern = re.compile(r"Network state:(\s)?([0-1]+)")
    nextstate_pattern = re.compile(r"Next state:(\s)?([0-1]+)")

    compare_result = {"success": True}

    try:
        # ottieni impostazioni del file configurazione
        configs = parse_config(config_path)

        if configs["correct"]:
            # apri il file con gli output corretti, recupera gli output 
            # (righe che iniziano con "Outputs:") e salvali in correct_outputs
            with open(sis_correct_outputs, "r") as infile:
                for line in infile:
                    if output_pattern.match(line) and configs["check_output"]:
                        correct_data.append(line.lstrip("Outputs: ").replace(" ", "").strip())
                    
                    elif currentstate_pattern.match(line) and configs["check_currentstate"]:
                        correct_data.append(line.lstrip("Network state: ").replace(" ", "").strip())
                    
                    elif nextstate_pattern.match(line) and configs["check_nextstate"]:
                        correct_data.append(line.lstrip("Next state: ").replace(" ", "").strip())
            
            match = 0
            i = 0
            area = 0
            slack = 0
            gate_count = 0
            # correct_data = correct_outputs[:] + correct_currentstates[:] + correct_nextstates[:]

            # apri l'output della simulazione e confronta
            with open(sis_simulation_output, "r") as infile:
                for line in infile:
                    if output_pattern.match(line) and configs["check_output"]:
                        if line.lstrip("Outputs: ").replace(" ", "").strip() == correct_data[i]:
                            match += 1
                        i += 1
                    
                    elif currentstate_pattern.match(line) and configs["check_currentstate"]:
                        if line.lstrip("Network state: ").replace(" ", "").strip() == correct_data[i]:
                            match += 1
                        i += 1

                    elif nextstate_pattern.match(line) and configs["check_nextstate"]:
                        if line.lstrip("Next state: ").replace(" ", "").strip() == correct_data[i]:
                            match += 1
                        i += 1

                    elif line.startswith("Total Area"):
                        area = float(line.split('=')[1].strip())
                    elif line.startswith("Most Negative Slack"):
                        slack = -(float(line.split('-')[1].strip()))
                    elif line.startswith("Gate Count"):
                        gate_count = int(line.split('=')[1].strip())
            
            # restituisci correttezza, ...
            compare_result["correctness"] = float(match) / float(i) * 100.0
            compare_result["area"] = area
            compare_result["slack"] = slack
            compare_result["total_gate"] = gate_count
        
        else:
            compare_result["success"] = False

            for error in configs["errors"]:
                printlog("[ERRORE] " + error, t_flog)

    except IndexError as e:
        compare_result["success"] = False
        printlog("[ERRORE] ({}), probabilmente il file con il risultato atteso non ha tutte le informazioni necessarie".format(type(e).__name__) + str(e), t_flog)

    except IOError as e:
        compare_result["success"] = False
        printlog("[ERRORE] ({}) ".format(type(e).__name__) + str(e), t_flog)

    except ZeroDivisionError as e:
        compare_result["success"] = False
        printlog("[ERRORE] ({}), probabilmente il file con gli output corretti e/o il file con gli output di simulazione e' vuoto".format(type(e).__name__) + str(e), t_flog)
        
    return compare_result


def printlog(t_text, t_file):
    """
    Prints and logs text. (with timestamp)

    :param str t_text: string with text to write to file and print
    :param IO t_file: Opened log file
    """
    print("[{}]".format(int(time.time())) + t_text)
    t_file.write("[{}]".format(int(time.time())) + t_text + "\n")


def parse_config(t_file, t_blif_file=None):
    """
    Parses blif_tester_conf.ini files.

    ini file content should be:
    
    ```
    [CHECK]
    output = true/false
    nextstate = true/false
    currentstate = true/false
    ```
    
    :param str t_file: file to parse
    :param (None, str) t_blif_file: blif file that needs to be tested (checks if test section corresponds to a blif file)
    :return dict parsed: dictionary with correct file status, errors and or what to check during the tests
    """
    config = configparser.ConfigParser()

    parsed = {"correct": True, "errors": []}

    try:
        read = config.read(t_file)

        if len(read) > 0:
            output = config['CHECK']['output']
            nextstate = config['CHECK']['nextstate']
            currentstate = config['CHECK']['currentstate']

            if output == "false":
                parsed["check_output"] = False
            elif output == "true":
                parsed["check_output"] = True
            else:
                parsed["errors"].append("'output' setting in '{}' should be 'true' or 'false'".format(t_file))
                parsed["correct"] = False

            if nextstate == "false":
                parsed["check_nextstate"] = False
            elif nextstate == "true":
                parsed["check_nextstate"] = True
            else:
                parsed["errors"].append("'nextstate' setting in '{}' should be 'true' or 'false'".format(t_file))
                parsed["correct"] = False

            if currentstate == "false":
                parsed["check_currentstate"] = False
            elif currentstate == "true":
                parsed["check_currentstate"] = True
            else:
                parsed["errors"].append("'currentstate' setting in '{}' should be 'true' or 'false'".format(t_file))
                parsed["correct"] = False
            
            if not (parsed["check_output"] or parsed["check_nextstate"] or parsed["check_currentstate"]):
                parsed["errors"].append("At least one check (check_output/check_nextstate/check_currentstate) should be set to true in ini file ('{}')".format(t_file))
                parsed["correct"] = False
            
            # controlla se ci sono dettagli di simulazione
            configfile_path = os.path.dirname(os.path.realpath(t_file))
            blifs_path = os.path.realpath(os.path.join(configfile_path, ".."))
            root_path = os.path.realpath(os.path.join(blifs_path, ".."))
            testconfigs = []

            for section in config.keys():
                #print(section)
                if section.startswith("test "):
                    bliffile = section.replace("test ", "")
                    blifpath = os.path.realpath(os.path.join(configfile_path, "..", bliffile + ".blif"))
                    #print(bliffile, " ", configfile_path, " ", blifpath, " ", t_blif_file)
                    if os.path.isfile(blifpath) and t_blif_file == blifpath:
                        for i in range(1, 10):
                            #print(i)
                            simulatefile = None
                            correctoutput = None
                            try:
                                #print(section)
                                simulatefile = config[section]["simulatefile{}".format(i)]
                                correctoutput = config[section]["correctoutput{}".format(i)]
                            except KeyError:
                                if simulatefile:
                                    parsed["correct"] = False
                                    parsed["errors"].append("Configurazione nel file ini del test '{}' incompleta".format(bliffile))
                                    simulatefile = None
                            
                            #print(simulatefile, " ", correctoutput)
                            if simulatefile and correctoutput:
                                simulatefile = simulatefile.replace(r"{{testspath}}", configfile_path)
                                correctoutput = correctoutput.replace(r"{{testspath}}", configfile_path)
                                simulatefile = simulatefile.replace(r"{{blifspath}}", blifs_path)
                                correctoutput = correctoutput.replace(r"{{blifspath}}", blifs_path)
                                simulatefile = simulatefile.replace(r"{{root}}", root_path)
                                correctoutput = correctoutput.replace(r"{{root}}", root_path)
                                simulatefile = os.path.realpath(simulatefile)
                                correctoutput = os.path.realpath(correctoutput)
                                
                                if not os.path.isfile(simulatefile):
                                    parsed["correct"] = False
                                    parsed["errors"].append("Configurazione nel file ini del test '{}' errata, il file '{}' non esiste".format(bliffile, simulatefile))
                                if not os.path.isfile(correctoutput):
                                    parsed["correct"] = False
                                    parsed["errors"].append("Configurazione nel file ini del test '{}' errata, il file '{}' non esiste".format(bliffile, correctoutput))

                                testconfigs.append({"simulatefile": simulatefile, "correctoutput": correctoutput})
                        
                        break
            
            parsed["testconfigs"] = testconfigs
                    
        else:
            parsed["correct"] = False
            parsed["errors"].append("can't read ini file '{}'".format(t_file))

    except KeyError:
        parsed["correct"] = False
        parsed["errors"].append("({}) prop '{}' doesn't exist".format(type(e).__name__, str(e)))

    except Exception as e:
        parsed["correct"] = False
        parsed["errors"].append("({}) ".format(type(e).__name__) + str(e))

    return parsed


if __name__ == "__main__":

    current_dir = os.path.dirname(os.path.abspath(__file__))
    category_hasbeen_tested = False

    with open("log.txt", "a") as flog:
        try:
            # controlla i parametri
            if len(sys.argv) == 1:
                # esegui tutti i test
                tests = "all"

            elif len(sys.argv) == 2:
                # esegui solo i test della categoria specificata
                tests = sys.argv[1]
            else:
                raise Exception("[ERROR] Troppi parametri (> 1)")
                    
            printlog("[START] Inizio dei test", flog)
            
            # scorri elementi della cartella src
            for element in os.listdir(current_dir):
                if os.path.isdir(os.path.join(current_dir, element)) and (tests == "all" or tests == element) and (not element.startswith("_")):
                    # specifica che la categoria e' stata trovata
                    category_hasbeen_tested = True

                    # entra nella cartella dei blif
                    if boold:
                        printlog("[DEBUG - SRC] Elemento '{}' e' cartella".format(os.path.join(current_dir, element)), flog)
                    
                    folder = element
                    blif_directory = os.path.join(current_dir, folder)

                    setupcategory_script = os.path.join(blif_directory, "setupcategory.sh")
                    if os.path.isfile(setupcategory_script):
                        printlog("[SETUP CATEGORY] File di setup di questa categoria di componenti trovato, eseguo script per preparare i test", flog)
                        subprocess.Popen("sudo " + setupcategory_script + " " + blif_directory, stdout=subprocess.PIPE, shell=True).communicate()

                    # scorri gli elementi della cartella dei blif
                    for l in os.listdir(blif_directory):
                        if os.path.isfile(os.path.join(blif_directory, l)):
                            # e' un file, controlla estensione
                            if boold:
                                printlog("[DEBUG - BLIFDIR] Elemento '{}' e' un file".format(os.path.join(current_dir, l)), flog)

                            fullpath_filename, fileextension = os.path.splitext(os.path.join(blif_directory, l))
                            filename = os.path.splitext(os.path.basename(fullpath_filename))[0]

                            # se e' un blif...
                            if fileextension == ".blif":
                                blif_file = os.path.join(blif_directory, l)

                                simulation_input = os.path.join(blif_directory, "tests", "test_" + filename + ".script")
                                sim_out_path = os.path.join(blif_directory, "tests", "sim_output.txt")
                                correct_path = os.path.join(blif_directory, "tests", "test_" + filename + "_correct_output.txt")
                                config_path = os.path.join(blif_directory, "tests", "blif_tester_conf.ini")

                                # se esiste la cartella dei test, esiste il file di simulazione e esiste il file di output atteso...
                                if os.path.isdir(os.path.join(blif_directory, "tests")):
                                    
                                    setup_script = os.path.join(blif_directory, "tests", "setup.sh")
                                    if os.path.isfile(setup_script):
                                        printlog("[SETUP] File di setup trovato, eseguo script per preparare i test", flog)
                                        subprocess.Popen("sudo " + setup_script + " " + blif_file, stdout=subprocess.PIPE, shell=True).communicate()

                                    # se nel file di configurazione sono specificati i test, esegui quelli
                                    configs = parse_config(config_path, blif_file)
                                    if len(configs["testconfigs"]) > 0:
                                        printlog(f"[TEST CONFIGURAZIONE] Trovate configurazioni di simulazione", flog)
                                        for testconfig in configs["testconfigs"]:
                                            printlog("[TEST CONFIGURAZIONE] Eseguo simulazione '{}', output atteso '{}'".format(testconfig["simulatefile"], testconfig["correctoutput"]), flog)
                                            # se la esecuzione della simulazione ha successo... 
                                            if simulate(blif_directory, blif_file, testconfig["simulatefile"], sim_out_path) == 0:
                                                # confronta output ottenuto e output atteso, ottieni statistiche
                                                compare_result = compare(sim_out_path, testconfig["correctoutput"], config_path, flog)
                                                    
                                                if compare_result["success"]:
                                                    correctness = compare_result["correctness"]
                                                    area = compare_result["area"]
                                                    slack = compare_result["slack"]
                                                    total_gate = compare_result["total_gate"]

                                                    printlog(f"[SIMULAZIONE] Simulazione file '{filename}.blif' eseguita con successo", flog)
                                                    printlog(f"[SIMULAZIONE - OUTPUT] correctness: {correctness}, area: {area}, slack: {slack}, total_gate: {total_gate}", flog)

                                                    # controlla la correttezza (percentuale di uguaglianza di output atteso e di output ottenuto)
                                                    if correctness == 100.0:
                                                        printlog("[SIMULAZIONE - SUCCESSO] La simulazione ha dato il risultato atteso", flog)
                                                    else:
                                                        printlog("[SIMULAZIONE - FALLIMENTO] La simulazione NON ha dato il risultato atteso", flog)
                                                        success = False
                                                else:
                                                    success = False
                                            else:
                                                printlog("[ERRORE - SIMULAZIONE] Simulazione fallita", flog)
                                                success = False
                                    else:
                                        # nella configurazione non e' specificato il test, controlla se esiste il file di test di default
                                        if os.path.isfile(simulation_input) and os.path.isfile(correct_path):
                                            printlog("[TEST FILE] Trovato file di simulazione nella cartella tests", flog)
                                            # se la esecuzione della simulazione ha successo... 
                                            if simulate(blif_directory, blif_file, simulation_input, sim_out_path) == 0:
                                                # confronta output ottenuto e output atteso, ottieni statistiche
                                                compare_result = compare(sim_out_path, correct_path, config_path, flog)
                                                        
                                                if compare_result["success"]:
                                                    correctness = compare_result["correctness"]
                                                    area = compare_result["area"]
                                                    slack = compare_result["slack"]
                                                    total_gate = compare_result["total_gate"]

                                                    printlog(f"[SIMULAZIONE] Simulazione file '{filename}.blif' eseguita con successo", flog)
                                                    printlog(f"[SIMULAZIONE - OUTPUT] correctness: {correctness}, area: {area}, slack: {slack}, total_gate: {total_gate}", flog)

                                                    # controlla la correttezza (percentuale di uguaglianza di output atteso e di output ottenuto)
                                                    if correctness == 100.0:
                                                        printlog(f"[SIMULAZIONE - SUCCESSO] La simulazione ha dato il risultato atteso", flog)
                                                    else:
                                                        printlog(f"[SIMULAZIONE - FALLIMENTO] La simulazione NON ha dato il risultato atteso", flog)
                                                        success = False
                                                else:
                                                    success = False
                                            else:
                                                printlog("[ERRORE - SIMULAZIONE] Simulazione fallita", flog)
                                                success = False
                                        else:
                                            printlog("[ERRORE] file di simulazione ('{}') e/o file di output ('{}') atteso non esistente/i".format(simulation_input, correct_path), flog)
                                            success = False

                                    teardown_script = os.path.join(blif_directory, "tests", "teardown.sh")
                                    if os.path.isfile(teardown_script):
                                        printlog("[TEARDOWN] File di teardown trovato, eseguo script per chiusura del test", flog)
                                        subprocess.Popen("sudo " + teardown_script + " " + blif_file, stdout=subprocess.PIPE, shell=True).communicate()
                                    
                                else:
                                    printlog("[ERRORE] La cartella tests non esiste in '{}'".format(blif_directory), flog)
                                    success = False
                        else:
                            if boold:
                                printlog("[DEBUG - BLIFDIR] Elemento '{}' non e' un file".format(os.path.join(current_dir, l)), flog)

                    teardowncategory_script = os.path.join(blif_directory, "teardowncategory.sh")
                    if os.path.isfile(teardowncategory_script):
                        printlog("[TEARDOWN CATEGORY] File di teardown di questa categoria di componenti trovato, eseguo script per terminare i test", flog)
                        subprocess.Popen("sudo " + teardowncategory_script + " " + blif_directory, stdout=subprocess.PIPE, shell=True).communicate()

                else:
                    if boold:
                        printlog("[DEBUG] Elemento '{}' non e' cartella".format(os.path.join(current_dir, element)), flog)

            if not category_hasbeen_tested:
                success = False
                printlog("[ERRORE] Categoria di test passata come parametro non trovata", flog)

        except Exception as e:
            printlog("[ERRORE] Errore non previsto '{}' (dettagli: '{}', riga: '{}')".format(type(e).__name__, str(e), sys.exc_info()[-1].tb_lineno), flog)
            success = False
        
        printlog("[END] Fine dei test", flog)
    
    if not success:
        sys.exit(1)