# DATAPATH

Questa cartella contiene il datapath
specifico dell'elaborato di architettura degli elaboratori.

![Datapath](images/datapath.svg)

Output del datapath:
* se ```CASH_RICHIESTO * 4 < CASH_DISPONIBILE``` allora ```CASH_OK = 1``` e ```CASH_DA_EROGARE = CASH_RICHIESTO```
* altrimenti ```CASH_DA_EROGARE (10 bit) = 0000000000``` e ```CASH_OK = 0```

> Nota 1: il controllo avviene solo quando CHECK_DISPONIBILITA = 1

> Nota 2: il warning ```"Warning: network `datapath', node "IGNORE" does not fanout"``` e' normale,
> appare perche' l'ultimo bit in uscita dal primo shifter a sinistra (quello che moltiplica CASH_RICHIESTO * 2)
> viene ignorato. Ignorarlo non porta a risultati sbagliati perche' e' sempre uguale a 0.

<div style="background-color: white; padding: 20px;">

![Datapath blackbox](images/datapath_blackbox.svg)

</div>

## Requisiti
Questo circuito richiede come dipendenze diversi sotto-circuiti.

Prima di eseguire il comando ```read_blif datapath.blif``` su SIS,
eseguire lo script ```setup.sh``` (presente nella cartella ```tests```) che copiera' dalle altre
cartelle i file blif necessari per far funzionare il datapath.