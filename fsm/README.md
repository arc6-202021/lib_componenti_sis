# FSM

Questa cartella contiene la macchina a stati finiti
per l'elaborato di architettura degli elaboratori.

![FSM](images/fsm.svg)

> Immagine creata dal programma ```generate-stg``` [scaricabile da qui](https://github.com/bohzio/sis-tools),
> modificato per salvare il grafico come documento svg (il programma esporta in png)

Tabella degli stati della fsm ottimizzata:

|nome abbreviato|nome completo              |codifica|
|---------------|---------------------------|--------|
|S0             |T3_CODICE2_ERRORE / BLOCCO |00110   |
|S1             |INSERIMENTO                |11001   |
|S2             |T1_CODICE1                 |01001   |
|S3             |T1_CODICE1_ERRORE          |10111   |
|S4             |T1_CODICE2                 |11111   |
|S5             |T1_CODICE2_ERRORE          |00101   |
|S6             |T1_CODICE3                 |01101   |
|S7             |T2_CODICE1                 |01010   |
|S8             |RICHIESTA                  |01110   |
|S9             |T2_CODICE1_ERRORE          |10110   |
|S10            |T2_CODICE2                 |11110   |
|S11            |T2_CODICE2_ERRORE          |00011   |
|S12            |T2_CODICE3                 |01011   |
|S13            |T3_CODICE1                 |01100   |
|S14            |T3_CODICE1_ERRORE          |00111   |
|S15            |T3_CODICE2                 |01111   |
|S16            |T3_CODICE3                 |00010   |
|S17            |EROGAZIONE                 |10001   |