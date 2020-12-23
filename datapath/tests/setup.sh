#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# copia mux 2 ingressi da 1 bit (dipendenza di mux2i10b)
cp $SCRIPTDIR/../../multiplexer/mux2i1b.blif $SCRIPTDIR/..

# copia mux 2 ingressi da 10 bit
cp $SCRIPTDIR/../../multiplexer/mux2i10b.blif $SCRIPTDIR/..

# copia mux 2 ingressi da 16 bit
cp $SCRIPTDIR/../../multiplexer/mux2i16b.blif $SCRIPTDIR/..

# copia shifter sx da 16 bit
cp $SCRIPTDIR/../../shiftersx/shiftersx16b.blif $SCRIPTDIR/..

# copia porta logica xor (dipendenza di maggiore16.blif)
cp $SCRIPTDIR/../../porte_logiche/xor.blif $SCRIPTDIR/..

# copia circuito con funzione maggiore con due ingressi da 16 bit (dipendenza di minoreuguale16.blif)
cp $SCRIPTDIR/../../maggiore/maggiore16.blif $SCRIPTDIR/..

# copia circuito con funzione minore uguale con due ingressi da 16 bit
cp $SCRIPTDIR/../../minoreuguale/minoreuguale16.blif $SCRIPTDIR/..

# copia porta logica not (dipendenza di xnor.blif)
cp $SCRIPTDIR/../../porte_logiche/not.blif $SCRIPTDIR/..

# copia porta logica xnor (dipendenza di comparatore16.blif)
cp $SCRIPTDIR/../../porte_logiche/xnor.blif $SCRIPTDIR/..

# copia comparatore con due ingressi da 16 bit
cp $SCRIPTDIR/../../comparatori/comparatore16.blif $SCRIPTDIR/..
