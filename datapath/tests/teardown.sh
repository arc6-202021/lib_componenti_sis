#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# rimuovi mux 2 ingressi da 1 bit
rm $SCRIPTDIR/../mux2i1b.blif

# rimuovi mux 2 ingressi da 10 bit
rm $SCRIPTDIR/../mux2i10b.blif

# rimuovi mux 2 ingressi da 16 bit
rm $SCRIPTDIR/../mux2i16b.blif

# rimuovi shifter sx da 16 bit
rm $SCRIPTDIR/../shiftersx16b.blif

# rimuovi porta logica xor
rm $SCRIPTDIR/../xor.blif

# rimuovi circuito con funzione maggiore con due ingressi da 16 bit
rm $SCRIPTDIR/../maggiore16.blif

# rimuovi circuito con funzione minore uguale con due ingressi da 16 bit
rm $SCRIPTDIR/../minoreuguale16.blif

# rimuovi porta logica not
rm $SCRIPTDIR/../not.blif

# rimuovi porta logica xnor
rm $SCRIPTDIR/../xnor.blif

# rimuovi comparatore con due ingressi da 16 bit
rm $SCRIPTDIR/../comparatore16.blif
