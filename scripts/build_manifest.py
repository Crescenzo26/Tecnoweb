import os
import json
import hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS_DIR = os.path.join(ROOT, "site", "reports")
MANIFEST_PATH = os.path.join(ROOT, "site", "data", "manifest.json")

REPORTS = [
    {
        "id": "bf_dnf_2023",
        "title": "Dichiarazione Non Finanziaria",
        "year": 2023,
        "type": "DNF (D.Lgs. 254/2016)",
        "filename": "gruppobfdnf2023.pdf",
        "description": "Dichiarazione Non Finanziaria 2023 del Gruppo BF."
    }
]


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    items = []

    for r in REPORTS:
        file_path = os.path.join(REPORTS_DIR, r["filename"])
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File non trovato: {file_path}")

        items.append({
            "id": r["id"],
            "title": r["title"],
            "year": r["year"],
            "type": r["type"],
            "description": r["description"],
            "filename": r["filename"],
            "local_path": f"/reports/{r['filename']}",
            "sha256": sha256_file(file_path)
        })

    manifest = {
        "project": "PW17 – Tecnologia web per la sostenibilità d’impresa",
        "company": "Gruppo BF – settore primario",
        "items": items
    }

    with open(MANIFEST_PATH, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print("Manifest generato correttamente:", MANIFEST_PATH)


if __name__ == "__main__":
    main()
