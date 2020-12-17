# LIBRERIA COMPONENTI SIS

Questo repository contiene file blif
con componenti pronti per essere simulati su SIS.

Il repository contiene anche script e file di test.

## Descrizione

Nel repository ci sono...

... le cartelle:
* .github adesso contiene solo un file per controllare le dipendenze, 
> che per ora non ne abbiamo.

> Possiamo usarla per automatizzare i test con github actions quando facciamo push di commit

* porte_logiche con le 7 porte logiche + script di test e output corretti
* registri contiene registri + script di test e output corretti
* sommatori contiene fulladder + script di test e output corretti
* sottrattori mancano gli script di test e i file di output corretti

... gli script python:
* **blif_tester.py**: entra nelle cartelle e cerca i file blif e una cartella "tests".
Quando trova file blif cerca nella cartella tests
il file di test dei singoli file blif (chiamati ```test_<nomefileblif>.script```)
e l'output atteso dalla simulazione (chiamati ```test_<nomefileblif>_correct_output.txt```)

* **test_generator.py**: contiene funzioni che possono automatizzare la creazione dei
file ```*correct_output.txt```