#!/usr/bin/env bash

SCRIPTDIR=$(dirname $(realpath $0))

# assegna stati fsm non ottimizzata per poterla testare
sis -c "state_minimize stamina;state_assign jedi;write_blif ${SCRIPTDIR}/controllore_src.blif" ${SCRIPTDIR}/controllore_src.blif