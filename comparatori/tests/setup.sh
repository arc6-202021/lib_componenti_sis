#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# copia la porta xnor in questa cartella
cp $SCRIPTDIR/../../porte_logiche/xnor.blif $SCRIPTDIR/..

# copia la porta xor in questa cartella (dipendenza di xnor)
cp $SCRIPTDIR/../../porte_logiche/xor.blif $SCRIPTDIR/..

# copia la porta not in questa cartella (dipendenza di xnor)
cp $SCRIPTDIR/../../porte_logiche/not.blif $SCRIPTDIR/..