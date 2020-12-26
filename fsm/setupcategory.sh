#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# copia il file originale e assegna stati fsm non ottimizzata
cp ${SCRIPTDIR}/controllore.blif ${SCRIPTDIR}/controllore.blif.orig
sis -c "state_minimize stamina;state_assign jedi;write_blif ${SCRIPTDIR}/controllore.blif" ${SCRIPTDIR}/controllore.blif
