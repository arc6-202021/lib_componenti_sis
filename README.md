# LIBRERIA COMPONENTI SIS


Questo repository contiene file blif
con componenti pronti per essere simulati su SIS.

Il repository contiene anche script e file di test.

## Test

|Badge|Descrizione|
|-----|-----------|
|![Tester multiplexer](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20multiplexer/badge.svg)|testa multiplexer: permettono di selezionare uno dei dati in ingresso e ritrasmetterli in uscita |
|![Tester porte logiche](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20porte%20logiche/badge.svg)|testa porte not, or, and, ...|
|![Tester registri](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20registri/badge.svg)|testa registri che si occupano di memorizzare dati|
|![Tester shifter a sinistra](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20shifter%20a%20sinistra/badge.svg)|testa shifter a sinistra: permettono di moltiplicare un numero per 2 |
|![Tester sommatori](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20sommatori/badge.svg)|testa i sommatori: sommano due ingressi (e eventuale riporto in ingresso) e mette in uscita il risultato con eventuale riporto|
|![Tester sottrattori](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20sottrattori/badge.svg)|testa i sottrattori: effettuano la differenza tra due ingressi e restituiscono il risultato <br> <blockquote><p>il bit meno siginificativo in uscita e' sempre 1. Questo bit non fa parte del risultato ed e' necessario per evitare warning di fanout di SIS</p></blockquote><blockquote><p>i sottrattori necessitano della porta not e del sommatore fulladder a 2 bit</p></blockquote>|

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