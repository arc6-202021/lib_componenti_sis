#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# rimuovi la porta xnor in questa cartella
rm $SCRIPTDIR/../xnor.blif

# rimuovi la porta xor in questa cartella
rm $SCRIPTDIR/../xor.blif

# rimuovi la porta not in questa cartella
rm $SCRIPTDIR/../not.blif