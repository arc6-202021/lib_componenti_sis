# OPTIMIZER SCRIPTS

Questa cartella contiene lo script **optimize_fsm.script** per ottimizzare per area la
macchina a stati finiti.

Lo script visualizza anche statistiche ad ogni comando eseguito.

Per usarlo occorre prima aprire SIS e leggere il file blif con il comando:

    read_blif <fileblif>
> Dove ```<fileblif>``` e' il percorso del file blif.
> Se SIS viene eseguito nella cartella del file blif basta
> specificare nome e estensione del file: non occorre indicare il percorso completo.

Poi e' possibile importare lo script con:

    source <percorso_script>
> Dove ```<percorso_script>``` e' il percorso del file ```optimize_fsm.script```.
> Se copiato nella cartella del file blif basta eseguire ```source optimize_fsm.script```