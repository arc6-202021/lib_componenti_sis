"""
TEST_GENERATOR:
Genera file di test
"""

__author__ = "Zenaro Stefano"
__version__ = "2020-12-15 01_01"

bit = 17
boold = False


def n_bits(n):
    """
    Generatore di combinazioni di n bit.

    Esempio:
    >>> for combination in n_bits(2):
            print(combination)
    00
    01
    10
    11

    """
    for i in range(2**n):
        binary = str(bin(i))
        str_bin = binnotation2bits(binary, n)
            
        yield str_bin


def binnotation2bits(binary, n):
    str_bin = str(binary).lstrip("0b")
    while len(str_bin) < n:
        str_bin = "0" + str_bin
    
    return str_bin

def add_spaces_between(v):
    """
    Restituisce una lista con gli elementi
    della lista/stringa v separati fra di loro da uno spazio " ".
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
    """
    string = ""
    for el in v:
        string += str(el)

    return string


def gen_simulations(n, print_state=True):
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
    """
    for i in n_bits(n):
        cmd_simulate = "simulate " + v_to_str(add_spaces_between(i))
        cmd_print_state = "\nprint_state\n\n"

        command_combination = cmd_simulate
        
        if print_state:
            command_combination += cmd_print_state
        
        yield command_combination


def gen_networkstate(n):
    """
    Generatore di stati attuali esatti per i registri.

    Esempio:
    >>> for combination in gen_simulations(2):
            print(combination)

    # 00
    Network state: 00

    # 01
    Network state: 01

    # 10
    Network state: 10

    # 11
    Network state: 11
    """
    for i in n_bits(n):
        comment = "# " + i
        network_state = "\nNetwork state: " + i

        command_combination = comment + network_state + "\n\n"
        yield command_combination


def gen_adder_output(bit):
    for combination in n_bits(bit):
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


if __name__ == "__main__":

    #print("Prova per {} bit:".format(bit))
    #for i in n_bits(bit):
    #    print(i)
    
    #print("simulate per {} bit:".format(bit))
    #for combination in gen_simulations(bit, False):
    #    print(combination)
    
    #print("stato corretto per registri a {} bit:".format(bit))
    #for combination in gen_networkstate(bit):
    #    print(combination)
    
    #print("output corretto per gli adder con bit a + bit b + cin = {} bit".format(bit))
    with open("s", "w") as f:
        for combination in gen_adder_output(bit):
            f.write(combination + "\n")
