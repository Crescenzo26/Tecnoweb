[README.md](https://github.com/user-attachments/files/25470963/README.md)
# PW17 – Pagina web per download report di sostenibilità (Gruppo BF)

Questo progetto consiste in una semplice pagina web statica che consente il download dei report di sostenibilità del Gruppo BF.
È stato affiancato da alcuni script Python per garantire la generazione automatica dei metadati e la verifica dell’integrità dei documenti (hash SHA-256).

Il progetto è stato testato in locale utilizzando Python 3 e browser Chrome/Edge.

---

## Struttura del progetto

- `site/`
  - `index.html` → pagina principale
  - `assets/` → CSS e JavaScript
  - `data/manifest.json` → metadati dei documenti (generato automaticamente)
  - `reports/` → file PDF scaricabili (nel pacchetto è incluso un report di esempio)

- `scripts/`
  - `build_manifest.py` → genera/aggiorna il manifest con hash e metadati
  - `serve_local.py` → avvia un server locale per test
  - `verify_checksums.py` → verifica l’integrità dei file

---

## Requisiti

- Python 3.x  
Non sono necessarie librerie esterne.

---

## Utilizzo

1. Generare o aggiornare il manifest:

    python scripts/build_manifest.py

2. Avviare il server locale:

    python scripts/serve_local.py

3. Aprire il browser su:

    http://127.0.0.1:8000

---

## Verifica integrità

Per controllare che i file PDF non siano stati modificati:

    python scripts/verify_checksums.py

---

L’elenco dei documenti mostrato nella pagina viene generato leggendo il file `manifest.json`.
I link ai PDF sono relativi alla cartella `site/reports/`, così da funzionare correttamente anche in ambienti diversi dal server locale.
