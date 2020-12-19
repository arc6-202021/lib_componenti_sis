#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# rimuovi la porta xor in questa cartella
rm $SCRIPTDIR/../xor.blif