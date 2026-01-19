# PW17 – Pagina web per download report di sostenibilità (Gruppo BF)

Questo pacchetto contiene una pagina web statica (HTML/CSS/JS) e un set di script Python per garantire **replicabilità** e **verifica di integrità** dei documenti.

## Struttura

- `site/` → sito web (pagina + asset + dati + PDF)
  - `index.html` → pagina principale
  - `assets/` → CSS e JavaScript
  - `data/manifest.json` → metadati documenti (generato dagli script)
  - `reports/` → PDF scaricabili
- `scripts/` → script Python (replicabilità)

## Requisiti

- Python 3.x (nessuna libreria esterna necessaria)

## Avvio rapido

1) Genera/aggiorna il manifest (metadati + SHA-256):

```bash
python scripts/build_manifest.py
```

2) Avvia il server locale:

```bash
python scripts/serve_local.py
```

3) Apri il browser su:

- `http://127.0.0.1:8000`

## Verifica integrità (opzionale)

Per verificare che i PDF non siano stati modificati:

```bash
python scripts/verify_checksums.py
```

## Note

- I link ai PDF funzionano perché i report sono collocati in `site/reports/` (cartella servita dal server locale).
- L’elenco dei documenti mostrato nella pagina viene popolato automaticamente leggendo `site/data/manifest.json`.
