# MULTIPLEXER

Questo readme descrive i multiplexer presenti in questa cartella.

I multiplexer hanno una nomenclatura precisa:

    mux<n_ingressi>i<n_bit>b.blif

Dove:
* ```<n_ingressi>``` e' il numero di dati in ingresso
* ```<n_bit>``` e' il numero di bit che rappresentano i dati

Esempio:

    mux2i4b.blif

Significa che il multiplexer permette di selezionare due dati
da 4 bit l'uno.

Il test provera' quindi 2**9 combinazioni diverse.
> Dove 9 = 2*4 + 1. 1 e' il bit di selezione e 8 sono i bit complessivi dei dati (4 per dato)

NOTA: i multiplexer con un numero superiore di 2^20 combinazioni non sono testati
con tutte le combinazioni possibili
> ```mux2i10b```, ```mux2i16b```, ```mux4i8b```, ```mux8i4b``` e ```mux8i8b``` non sono testati completamente