#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# copia mux 2 ingressi da 1 bit (dipendenza di mux2i10b)
cp $SCRIPTDIR/../../multiplexer/mux2i1b.blif $SCRIPTDIR/../mux2i1b.blif

# copia mux 2 ingressi da 10 bit
cp $SCRIPTDIR/../../multiplexer/mux2i10b.blif $SCRIPTDIR/../mux2i10b.blif

# copia mux 2 ingressi da 16 bit
cp $SCRIPTDIR/../../multiplexer/mux2i16b.blif $SCRIPTDIR/../mux2i16b.blif

# copia shifter sx da 16 bit
cp $SCRIPTDIR/../../shiftersx/shiftersx16b.blif $SCRIPTDIR/../shiftersx16b.blif

# copia porta logica xor (dipendenza di maggiore16.blif)
cp $SCRIPTDIR/../../porte_logiche/xor.blif $SCRIPTDIR/../xor.blif

# copia circuito con funzione maggiore con due ingressi da 16 bit (dipendenza di minoreuguale16.blif)
cp $SCRIPTDIR/../../maggiore/maggiore16.blif $SCRIPTDIR/../maggiore16.blif

# copia circuito con funzione minore uguale con due ingressi da 16 bit
cp $SCRIPTDIR/../../minoreuguale/minoreuguale16.blif $SCRIPTDIR/../minoreuguale16.blif

# copia porta logica not (dipendenza di xnor.blif)
cp $SCRIPTDIR/../../porte_logiche/not.blif $SCRIPTDIR/../not.blif

# copia porta logica xnor (dipendenza di comparatore16.blif)
cp $SCRIPTDIR/../../porte_logiche/xnor.blif $SCRIPTDIR/../xnor.blif

# copia comparatore con due ingressi da 16 bit
cp $SCRIPTDIR/../../comparatori/comparatore16.blif $SCRIPTDIR/../comparatore16.blif

# copia datapath
cp $SCRIPTDIR/../../datapath/datapath.blif $SCRIPTDIR/../datapath.blif

# copia fsm
cp $SCRIPTDIR/../../fsm/controllore_ottimizzato.blif $SCRIPTDIR/../controllore.blif