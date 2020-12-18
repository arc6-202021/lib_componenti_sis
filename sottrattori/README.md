# SOTTRATTORI
Questo readme descrive i sottrattori presenti in questa cartella.

> Nella cartella ```tests``` sono contenuti gli script di esecuzione simulazione (```*.script```)
> e i file con gli output attesi (```*_correct_output.txt```)

I sottrattori si occupano di fare la sottrazione tra due numeri binari in complemento a 2
e di restituire il risultato.

**ATTENZIONE:** prima di simulare un sottrattore assicurarsi che nella stessa
cartella sia presente una porta not (```porte_logiche/not.blif```) e un fulladder a 2 bit (```sommatori/fulladder2.blif```).
> In fase di test questi file sono copiati automaticamente in questa cartella dallo script ```setup.sh```,
> eseguito da ```blif_tester.py```. Questo processo assicura il fatto di importare sempre componenti aggiornati e testati.

**NOTA:** tutti i sottrattori hanno un bit in output aggiuntivo, chiamato IGNORE,
che e' sempre a livello logico alto. Questo bit, in posizione di bit meno significativo, NON fa parte del risultato.

> Questa uscita e' stata aggiunta per evitare il warning di fanout di SIS
> dovuto al fatto che vengono ignorati gli ultimi riporti dei sommatori usati per
> creare questi componenti.

## SOTTRATTORE 2 BIT
Sottrae due numeri Ax e Bx rappresentati con 2 bit in complemento a 2.

L'uscita Sx, rappresentato con 2 bit, e' il risultato della differenza.
> Il terzo bit in uscita, quello meno significativo, NON fa parte del risultato.

## SOTTRATTORE 4 BIT
Sottrae due numeri Ax e Bx rappresentati con 4 bit in complemento a 2.

L'uscita Sx, rappresentato con 4 bit, e' il risultato della differenza.
> Il quinto bit in uscita, quello meno significativo, NON fa parte del risultato.

## SOTTRATTORE 8 BIT
Sottrae due numeri Ax e Bx rappresentati con 8 bit in complemento a 2.

L'uscita Sx, rappresentato con 8 bit, e' il risultato della differenza.
> Il nono bit in uscita, quello meno significativo, NON fa parte del risultato.