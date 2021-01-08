# LIBRERIA COMPONENTI SIS


Questo repository contiene file blif
con componenti pronti per essere simulati su SIS.
> Sono presenti anche file specifici dell'elaborato
> di architettura degli elaboratori.

Il repository contiene anche script e file di test.

## Test

|Badge test|Descrizione|
|-----|-----------|
|![Tester comparatori](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20comparatori/badge.svg)|testa i comparatori: verificano se due dati sono uguali o diversi<br><blockquote><p>richiedono la porta logica xnor (che a sua volta dipende dalla porta not e dalla porta nor)</p></blockquote>|
|![Tester funzione maggiore](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20funzione%20maggiore/badge.svg)|testa funzione maggiore: indica se il primo dato e' maggiore del secondo dato<br><blockquote><p>richiedono la porta logica xor</p></blockquote>|
|![Tester funzione minore uguale](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20funzione%20minore%20uguale/badge.svg)|testa funzione minore uguale: indica se il primo dato e' minore uguale del secondo dato<br><blockquote><p>richiedono la funzione complementare (maggiore) e le loro dipendenze (porta logica xor)</p></blockquote>|
|![Tester multiplexer](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20multiplexer/badge.svg)|testa multiplexer: permettono di selezionare uno dei dati in ingresso e ritrasmetterli in uscita |
|![Tester porte logiche](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20porte%20logiche/badge.svg)|testa porte not, or, and, ...|
|![Tester registri](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20registri/badge.svg)|testa registri che si occupano di memorizzare dati|
|![Tester shifter a sinistra](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20shifter%20a%20sinistra/badge.svg)|testa shifter a sinistra: permettono di moltiplicare un numero per 2 |
|![Tester sommatori](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20sommatori/badge.svg)|testa i sommatori: sommano due ingressi (e eventuale riporto in ingresso) e mette in uscita il risultato con eventuale riporto|
|![Tester sottrattori](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20sottrattori/badge.svg)|testa i sottrattori: effettuano la differenza tra due ingressi e restituiscono il risultato <br> <blockquote><p>il bit meno siginificativo in uscita e' sempre 1. Questo bit non fa parte del risultato ed e' necessario per evitare warning di fanout di SIS</p></blockquote><blockquote><p>i sottrattori necessitano della porta not e del sommatore fulladder a 2 bit</p></blockquote>|

Test specifici dell'elaborato:

|Badge test|Descrizione|
|-----|-----------|
|![Tester FSM](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20FSM/badge.svg)|testa la macchina a stati finiti|
|![Ottimizzatore FSM](https://github.com/arc6-202021/lib_componenti_sis/workflows/Ottimizzatore%20FSM/badge.svg)|ottimizza automaticamente la macchina a stati finiti|
|![Tester datapath](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20datapath/badge.svg)|testa il datapath|
|![Tester FSMD](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20FSMD/badge.svg)|testa la FSMD|
|![Ottimizzatore FSMD](https://github.com/arc6-202021/lib_componenti_sis/workflows/Ottimizzatore%20FSMD/badge.svg)|ottimizza automaticamente la FSMD|
|![Tester progetto completo](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20progetto%20completo/badge.svg)|testa i file finali del progetto|
|![Tester uguaglianza file](https://github.com/arc6-202021/lib_componenti_sis/workflows/Tester%20uguaglianza%20file/badge.svg)|si assicura che i file finali del progetto sono uguali a quelli delle altre sottocartelle|

## Descrizione

Nel repository ci sono...

... le cartelle:
* **_optimizer_scripts**: contiene script di ottimizzazione che possono essere importati da SIS
* **_simulates**: contiene script che eseguono i comandi simulate per simulare le diverse combinazioni degli ingressi di un circuito
* **.github** contiene file yml per controllare le dipendenze di github actions
e diverse workflow per eseguire gli script Python blif_tester.py e fsm_optimizer.py
    > I workflow che eseguono blif_tester.py scaricano il repository, installano SIS e Python e infine eseguono lo script Python di test
    > per controntare i risultati ottenuti dalle simulazioni con i risultati attesi

    > Il workflow che esegue fsm_optimizer.py scarica il repository, installa Python e SIS, esegue lo script e infine carica
    > come artifact il file di log e il file blif ottimizzato della fsm
* **comparatori**: contiene i comparatori e output attesi dai test
* **datapath**: contiene il file del datapath specifico dell'elaborato
* **fsm**: contiene il file della macchina a stati finiti specifica dell'elaborato e la fsm ottimizzata
* **fsmd**: contiene il file della macchina a stati finiti specifica dell'elaborato
* **maggiore**: contiene circuiti che verificano se il primo ingresso e' maggiore del secondo e i relativi output attesi dai test
* **minoreuguale**: contiene circuiti che verificano se il primo ingresso e' minore uguale del secondo e i relativi output corretti
* **multiplexer**: contiene multiplexer e output corretti
* **porte_logiche** contiene le 7 porte logiche e output corretti
* **registri** contiene registri e output corretti
* **shiftersx**: contiene shifter che moltiplicano per due l'ingresso eseguendo uno shift a sinistra dei bit
* **sis**: contiene tutti i file del progetto finito per l'elaborato
* **sommatori** contiene fulladder e output corretti
* **sottrattori** contiene sottrattori e i file di output corretti

... gli script python:
* **blif_tester.py**: di default entra nelle cartelle e cerca i file blif e una cartella "tests".
Quando trova file blif cerca nella cartella tests
il file di test dei singoli file blif (chiamati ```test_<nomefileblif>.script```)
e l'output atteso dalla simulazione (chiamati ```test_<nomefileblif>_correct_output.txt```)
oppure un file di configurazione chiamato ```blif_tester_conf.ini``` (questo ha priorita' sui file ```.script```)
    > Nelle cartelle sono presenti anche i file ```blif_tester_conf.ini```.
    > Sono usati per definire cosa occorre testare per ogni componente appartenente a quella categoria di componenti
    > e, opzionalmente, per indicare il percorso degli script di simulate e di output corretto.
    > 
    > Se entrambe i percorsi non vengono specificati verra' cercati i file ```test_<nomefileblif>.script```
    > e ```test_<nomefileblif>_correct_output.txt```.
    >
    > Combinazioni ibride (file di simulate e percorso in configurazione del file di output atteso o viceversa )
    > non sono permesse.

    > Nelle cartelle sono presenti anche i file ```setup.sh``` e ```teardown.sh```, script bash che vengono eseguiti
    > rispettivamente prima e dopo ogni test di un file blif.

    > Nelle cartelle sono presenti anche i file ```setupcategory.sh``` e ```teardowncategory.sh```, script bash che
    > vengono eseguiti rispettivamente all'inizio e alla fine dei test di quella categoria di componenti.

* **fsm_optimizer.py**: si occupa di ottimizzare la macchina a stati finiti contenuta nella cartella ```fsm```
    > Lo script copia il file blif diverse volte, esegue ottimizzazioni medianti SIS e lo script nella cartella ```_optimizer_scripts```
    > sulle copie e sulle copie delle copie (questo passaggio viene eseguito piu' volte) e infine sceglie la macchina a stati finiti piu' ottimizzata per area.

* **test_generator.py**: contiene funzioni che possono automatizzare la creazione dei
file ```*correct_output.txt```

... lo script bash:
* **git_chmod_bash.sh**: si occupa di cercare tutti gli script bash nelle sottocartelle e ad indicare
a git che i file sono eseguibili.
