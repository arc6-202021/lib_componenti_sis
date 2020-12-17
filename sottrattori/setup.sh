#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# copia tutti i fulladder in questa cartella
cp $SCRIPTDIR/../sommatori/fulladder*.blif $SCRIPTDIR/.

# copia la porta not in questa cartella
cp $SCRIPTDIR/../porte_logiche/not.blif $SCRIPTDIR/.
