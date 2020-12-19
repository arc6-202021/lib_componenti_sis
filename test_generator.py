"""
TEST_GENERATOR:
Genera file di test
"""

__author__ = "Zenaro Stefano"
__version__ = "2020-12-15 01_01"

import math
import argparse

bit = 17
boold = False


def n_bits(n, start=0, endbefore=None):
    """
    Generatore di combinazioni di n bit.

    Esempio:
    >>> for combination in n_bits(2):
            print(combination)
    00
    01
    10
    11

    :param int n: numero di bit
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    range_combs = range(start, 2**n)
    if endbefore:
        if endbefore < 2**n:
            range_combs = range(start, endbefore)

    for i in range_combs:
        binary = str(bin(i))
        str_bin = binnotation2bits(binary, n)
            
        yield str_bin


def binnotation2bits(binary, n, ispositive=True):
    """
    Converte numero binario in stringa.
    :param binary: numero binario
    :param int n: numero di cifre
    :param bool ispositive: True indica che il numero e' positivo (altrimenti si fa padding con '1')
    :return str str_bin: stringa con il numero binario
    """
    str_bin = str(binary).lstrip("-").lstrip("0b")
    while len(str_bin) < n:
        if ispositive:
            str_bin = "0" + str_bin
        else:
            str_bin = "1" + str_bin
    
    return str_bin


def add_spaces_between(v):
    """
    Restituisce una lista con gli elementi
    della lista/stringa v separati fra di loro da uno spazio " ".
    :param (list/str) v: stringa o lista
    :return list res: lista con gli elementi di v separati da elementi di spazio (" ")
    """
    res = []
    for el in v:
        res.append(el)
        res.append(" ")

    return res


def v_to_str(v):
    """
    Restituisce una stringa data dalla concatenazione
    degli elementi della lista v.
    :param list v: lista
    :return str string: stringa con elementi di v concatenati
    """
    string = ""
    for el in v:
        string += str(el)

    return string


def gen_simulations(n, print_state=True, start=0, endbefore=None):
    """
    Generatore di comandi simulate e print_state per tutte le combinazioni di n bit.

    Esempio:
    >>> for combination in gen_simulations(2):
            print(combination)

    simulate 0 0
    print_state

    simulate 0 1
    print_state

    simulate 1 0
    print_state

    simulate 1 1
    print_state

    :param int n: numero di bit
    :param bool print_state: True restituisce il comando per visualizzare lo stato attuale
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for i in n_bits(n, start, endbefore):
        cmd_simulate = "simulate " + v_to_str(add_spaces_between(i)) + "\n"
        cmd_print_state = "print_state\n\n"

        command_combination = cmd_simulate
        
        if print_state:
            command_combination += cmd_print_state
        
        yield command_combination


def gen_registry_networkstate(n, start=0, endbefore=None):
    """
    Generatore di stati attuali esatti per i registri.

    Esempio:
    >>> for combination in gen_registry_networkstate(2):
            print(combination)

    # 00
    Network state: 00

    # 01
    Network state: 01

    # 10
    Network state: 10

    # 11
    Network state: 11

    :param int n: numero di bit
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for i in n_bits(n, start, endbefore):
        comment = "# " + i
        network_state = "\nNetwork state: " + i

        command_combination = comment + network_state + "\n\n"
        yield command_combination


def gen_adder_output(nbit, start=0, endbefore=None):
    """
    Generatore di output esatto per i sommatori fulladder.
    :param int nbit: numero di bit totali in ingresso
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for combination in n_bits(nbit, start, endbefore):
        # 110 -> cin = 0, a = 1 b = 1
        cin = combination[-1]
        input_len = int((len(combination)-1)/2)
        a = combination[0:input_len]
        b = combination[input_len:-1]
        
        if boold:
            print("ingresso a, b, cin: ", a, b, cin)

        int_cin = int(cin, 2)
        int_a = int(a, 2)
        int_b = int(b, 2)

        sum_res = int_cin + int_a + int_b
        bin_sumres = bin(sum_res)

        bin_sumres = binnotation2bits(bin_sumres, input_len + 1)

        if boold:
            print("risultato somma:", bin_sumres)

        cout = bin_sumres[0]
        o = bin_sumres[1:]
        
        sim_out = o + cout

        comment = f"# {a} + {b} + {cin} = {o}, riporto {cout} \n"
        netssim = "Network simulation:\n"
        outputs = "Outputs: " + v_to_str(add_spaces_between(sim_out)) + "\n"
        nxstate= "Next state:\n"

        fulloutput = comment + netssim + outputs + nxstate
        yield fulloutput


def twos_complement(val, nbits):
    """
    Restituisci il complemento a due di val (formato intero).
    # > Credits: https://stackoverflow.com/a/37075643

    :param int val: numero di cui calcolare il complemento a due
    :param int n_bits: numero di bit del risultato
    :return int val: numero intero che corrisponde al complemento a due di val
    """
    if val < 0:
        val = (1 << nbits) + val
    else:
        if (val & (1 << (nbits - 1))) != 0:
            # If sign bit is set.
            # compute negative value.
            val = val - (1 << nbits)
    return val


def gen_sub_output(nbit, start=0, endbefore=None):
    """
    Generatore di output esatti per i sottrattori.
    > In outputs viene aggiunto un uno alla fine,
    > l'uscita IGNORE da ignorare.
    > E' stata aggiunta per evitare warning di fanout di SIS

    :param int nbit: numero di bit di tutti gli ingressi
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for combination in n_bits(nbit, start, endbefore):
        # 1110 -> a = 11 b = 10
        input_len = int((len(combination))/2)
        a = combination[0:input_len]
        b = combination[input_len:]
        
        if boold:
            print("ingresso a, b: ", a, b)
        
        # a = 11 -> -1    b = 10 -> -2
        int_a = twos_complement(int(a, 2), input_len)
        int_b = twos_complement(int(b, 2), input_len)

        if boold:
            print("ingresso base 10 a, b: ", int_a, " ", int_b)

        # -1 - (-2) = -1 +2 = 1
        sub_res = int_a - int_b
        of_sub_res = sub_res

        # togli eventuale overflow
        if not (-(2**input_len)/2 <= sub_res <= ((2**input_len)/2)-1):
            while of_sub_res > ((2**input_len)/2)-1:
                of_sub_res -= 2**input_len
                if boold:
                    print("cerco di togliere overflow sottrando {}, risultato: {}".format(2**input_len, of_sub_res))

            while of_sub_res < -(2**input_len)/2:
                of_sub_res += 2**input_len
                if boold:
                    print("cerco di togliere overflow sommando {}, risultato: {}".format(2**input_len, of_sub_res))          

        if boold:
            print("risultato differenza: ", sub_res)
            print("risultato senza overflow: ", of_sub_res)

        # 1 --> 01
        bin_subres = bin(twos_complement(of_sub_res, input_len))
        padded_subres = binnotation2bits(bin_subres, input_len, of_sub_res >= 0)
        
        if boold:
            print("Risultato in complemento a 2: ", bin_subres)
            print("Risultato riscritto con n bit esatti: ", padded_subres)
            print("-"*10)
            print("")

        comment = f"# {a} - {b} = {padded_subres}\n"
        netssim = "Network simulation:\n"
        outputs = "Outputs: " + v_to_str(add_spaces_between(padded_subres)) + "1\n"
        nxstate= "Next state:\n"

        fulloutput = comment + netssim + outputs + nxstate

        yield fulloutput


def divide_per_nels(string, n_el):
    """
    Suddivide una stringa ogni n_el caratteri.

    :param str string: stringa da suddividere
    :param int n_el: numero di elementi per stringa nell'output
    :return list res: lista di stringhe
    """
    res = []
    el_string = ""
    for i, char in enumerate(string, 1):
        if i % n_el == 0:
            el_string += char
            res.append(el_string)
            el_string = ""
        else:
            el_string += char
    
    return res


def invert(bit_string):
    """
    Scambia zero con uno e viceversa.
    :param str bit_string: stringa con bit
    :return str res: stringa con bit invertiti
    """
    res = ""
    for bit in bit_string:
        if bit == "0":
            res += "1"
        else:
            res += "0"
    return res


def gen_mux_output(ninputs, nbit, start=0, endbefore=None):
    """
    Generatore di output esatti per i multiplexer.
    
    Esempio: multiplexer 4 ingressi da 2 bit ciascuno
    
    * ninputs = 4 perche' il multiplexer ha 4 ingressi
    * nbit = 9 perche' 8 sono di dati (4 ingressi X 2 bit ciascuno)
               e 1 e' il bit di selettore

    :param int ninputs: numero di input nel multiplexer
    :param int nbit: numero di bit di tutti gli ingressi
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for combination in n_bits(nbit, start, endbefore):
        # 2 ingressi (e 3 bit) --> 1 bit di selettore
        selector = combination[0:int(math.log2(ninputs))]

        # 2 ingressi e 3 bit --> 1 di selettore, 2 di dato.
        # 2 bit di dato / 2 ingressi = 1 bit di dato per ingresso
        inputs = combination[int(math.log2(ninputs)):]
        input_len = int((nbit - int(math.log2(ninputs))) / ninputs)
        
        if boold:
            print("selettore, inputs, lunghezza per input: ", selector, " ", inputs, " ", input_len)

        v_inputs = divide_per_nels(inputs, input_len)

        if boold:
            print("Input ottenuti:")
            for i in v_inputs:
                print("* " + i)
        
        int_selector = int(selector, 2)
        selected_input = v_inputs[int_selector]

        if boold:
            print("Input selezionato: ", selected_input)

        comment = "\n"
        netssim = "Network simulation:\n"
        outputs = "Outputs: " + v_to_str(add_spaces_between(selected_input)) + "\n"
        nxstate= "Next state:\n"

        fulloutput = comment + netssim + outputs + nxstate
        
        yield fulloutput


def gen_shiftersx_output(leninput, nbit, start=0, endbefore=None):
    """
    Genera output corretti per gli shifter a sinistra.

    :param int leninput: lunghezza dell'input (TODO: rimuovere il parametro, basta usare nbit al suo posto)
    :param int nbit: numero di bit di tutti gli ingressi
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for combination in n_bits(nbit, start, endbefore):
        
        if boold:
            print("input: ", combination)
        
        # se entra 011 di lunghezza 3, entra il numero 3, moltiplica per 2 -> 6
        int_input = int(combination, 2)
        times2_input = int_input * 2
        
        # 6 in binario e' 110, in lunghezza 3+1 -> 0110
        bin_output = binnotation2bits(bin(times2_input), leninput+1)

        if boold:
            print("Output: ", bin_output)

        comment = "# {} * 2 = {}\n".format(int_input, times2_input)
        netssim = "Network simulation:\n"
        outputs = "Outputs: " + v_to_str(add_spaces_between(bin_output)) + "\n"
        nxstate= "Next state:\n\n"

        fulloutput = comment + netssim + outputs + nxstate
        
        yield fulloutput


def gen_comparator_output(nbit, start=0, endbefore=None):
    """
    Generatore di output esatti per i comparatori.

    :param int nbit: numero di bit di tutti gli ingressi
    :param int start: numero che corrisponde alla combinazione iniziale
    :param (None, int) endbefore: numero che indica che la combinazione prima di endbefore e' l'ultima
    """
    for combination in n_bits(nbit, start, endbefore):
        
        if boold:
            print("input: ", combination)
        
        # se entra 011 di lunghezza 3, entra il numero 3, moltiplica per 2 -> 6
        input_len = int(len(combination)/2)
        int_a = int(combination[0:input_len], 2)
        int_b = int(combination[input_len:], 2)
        
        bin_output = "0"
        if int_a == int_b:
            bin_output = "1"

        if boold:
            print("Output: ", bin_output)

        comment = "# {} == {} ?\n".format(int_a, int_b)
        netssim = "Network simulation:\n"
        outputs = "Outputs: " + v_to_str(add_spaces_between(bin_output)) + "\n"
        nxstate= "Next state:\n\n"

        fulloutput = comment + netssim + outputs + nxstate
        
        yield fulloutput


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Automatizza la creazione dei test.')
    parser.add_argument('nbits', metavar='NBITS', type=int, help='numero di bit')
    parser.add_argument('--simulate', action='store_true', default=False, help='indica di creare script di test con comandi simulate')
    parser.add_argument('--noprintstate', action='store_true', default=False, help='NON usare i comandi print_state dopo i comandi simulate (--simulate e\' necessario per usare questo flag)')
    parser.add_argument('--registry', action='store_true', default=False, help='indica di creare output corretti di stati attuali per testare i registri')
    parser.add_argument('--fulladder', action='store_true', default=False, help='indica di creare output corretti per testare i sommatori fulladder')
    parser.add_argument('--subtractor', action='store_true', default=False, help='indica di creare output corretti per testare i sottrattori (nota: l\'ultimo bit e\' sempre 1 e non fa parte del risultato)')
    parser.add_argument('--mux', action='store_true', default=False, help='indica di creare output corretti per testare i multiplexer')
    parser.add_argument('--shiftersx', action='store_true', default=False, help='indica di creare output corretti per testare gli shifter a sinistra')
    parser.add_argument('--comparator', action='store_true', default=False, help='indica di creare output corretti per testare i comparatori')
    parser.add_argument('--ninputs', type=int, help='numero di input nel multiplexer')
    parser.add_argument('--leninput', type=int, help='numero di bit che rappresentano l\'input nei shifter')
    parser.add_argument('--startnum', type=int, default=0, help='numero da cui iniziare le combinazioni')
    parser.add_argument('--endnum', type=int, default=None, help='numero in cui forzare la fine delle combinazioni')
    args = parser.parse_args()
    
    if not (args.simulate or args.registry or args.fulladder or args.subtractor or args.mux or args.shiftersx or args.comparator):
        print("ATTENZIONE: Una flag deve essere vera\n")
        parser.print_help()
    elif (args.simulate + args.registry + args.fulladder + args.subtractor + args.mux + args.shiftersx + args.comparator) > 1:
        print("ATTENZIONE: Solo UNA flag deve essere vera\n")
        parser.print_help()
    else:
        if args.mux and (not args.ninputs):
            print("ATTENZIONE: la flag --mux richiede la flag --ninputs\n")
            parser.print_help()

        elif args.shiftersx and (not args.leninput):
            print("ATTENZIONE: la flag --shiftersx richiede la flag --leninput\n")
            parser.print_help()

        elif args.startnum < 0:
            print("ATTENZIONE: il parametro --startnum deve essere un numero positivo\n")
            parser.print_help()
        
        elif args.endnum is not None and args.endnum < 0:
            print("ATTENZIONE: il parametro --endnum deve essere un numero positivo\n")
            parser.print_help()

        elif args.mux and args.ninputs:
            # ottieni gli output dei multiplexer
            for combination in gen_mux_output(args.ninputs, args.nbits, start=args.startnum, endbefore=args.endnum):
                print(combination, end="")
        
        elif args.shiftersx and args.leninput:
            # ottieni gli output del shifter a sinistra
            for combination in gen_shiftersx_output(args.leninput, args.nbits, start=args.startnum, endbefore=args.endnum):
                print(combination, end="")

        elif args.simulate:
            print_state = not args.noprintstate
            for combination in gen_simulations(args.nbits, print_state=print_state,start=args.startnum, endbefore=args.endnum):
                print(combination, end="")

        elif args.registry:
            for combination in gen_registry_networkstate(args.nbits, start=args.startnum, endbefore=args.endnum):
                print(combination, end="")

        elif args.fulladder:
            for combination in gen_adder_output(args.nbits, start=args.startnum, endbefore=args.endnum):
                print(combination, end="")

        elif args.subtractor:
            for combination in gen_sub_output(args.nbits, start=args.startnum, endbefore=args.endnum):
                print(combination, end="")
        
        elif args.comparator:
            for combination in gen_comparator_output(args.nbits, start=args.startnum, endbefore=args.endnum):
                print(combination, end="")

