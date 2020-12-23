# SIMULATES

Questa cartella contiene i file per la
simulazione dei circuiti.

Il nome del file indica quanti sono i bit che andranno in input al circuito.

Ad esempio il file ```simulate5b.script``` eseguira' il comando
```simulate``` con tutte le combinazioni possibili utilizzando 5 bit.
> Tutte le 2**5 = 32 combinazioni.

Se il nome del file contiene ```_printstate```
vuol dire che lo script, oltre ad eseguire i comandi di simulazione,
esegue anche i comandi per visualizzare lo stato attuale dopo aver eseguito
ogni comando di simulate.

Se il nome contiene un certo numero x, ad esempio ```1milione```,
significa che le combinazioni erano troppe e quindi verranno
testate x combinazioni.
> Se esiste anche lo stesso script per un numero y superiore di x, ad esempio ```2milioni```,
> vuol dire che il secondo script eseguira' il test per le combinazioni da x a y.