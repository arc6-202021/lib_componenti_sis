# LIBRERIA COMPONENTI SIS

![BLIF tester](https://github.com/arc6-202021/lib_componenti_sis/workflows/BLIF%20tester/badge.svg)

Questo repository contiene file blif
con componenti pronti per essere simulati su SIS.

Il repository contiene anche script e file di test.

## Descrizione

Nel repository ci sono...

... le cartelle:
* **.github** contiene file yml per controllare le dipendenze di github actions
e una workflow per eseguire lo script Python blif_tester.py
    > Il workflow scarica il repository, installa SIS e Python e infine esegue lo script python di test
* **porte_logiche** con le 7 porte logiche + script di test e output corretti
* **registri** contiene registri + script di test e output corretti
* **sommatori** contiene fulladder + script di test e output corretti
* **sottrattori** mancano gli script di test e i file di output corretti

... gli script python:
* **blif_tester.py**: entra nelle cartelle e cerca i file blif e una cartella "tests".
Quando trova file blif cerca nella cartella tests
il file di test dei singoli file blif (chiamati ```test_<nomefileblif>.script```)
e l'output atteso dalla simulazione (chiamati ```test_<nomefileblif>_correct_output.txt```)
> Nelle cartelle sono presenti anche i file ```blif_tester_conf.ini``` 
> (usati per definire cosa occorre testare per ogni sottogruppo di componenti) 
> e i file ```setup.sh``` e ```teardown.sh```, script bash che vengono eseguiti
> rispettivamente prima e dopo ogni test di un file blif

* **test_generator.py**: contiene funzioni che possono automatizzare la creazione dei
file ```*correct_output.txt```