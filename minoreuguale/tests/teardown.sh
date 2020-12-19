#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# rimuovi tutti i fulladder in questa cartella
rm $SCRIPTDIR/../fulladder*.blif

# rimuovi la porta not in questa cartella
rm $SCRIPTDIR/../not.blif