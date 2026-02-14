import os
import json
import hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MANIFEST_PATH = os.path.join(ROOT, "site", "data", "manifest.json")
REPORTS_DIR = os.path.join(ROOT, "site", "reports")


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def main() -> None:
    if not os.path.exists(MANIFEST_PATH):
        print("Errore: manifest.json non trovato.")
        return

    with open(MANIFEST_PATH, "r", encoding="utf-8") as f:
        manifest = json.load(f)

    items = manifest.get("items", [])
    if not items:
        print("Nessun documento da verificare.")
        return

    print("Verifica integrità dei documenti (SHA-256):\n")

    ok = 0
    checked = 0

    for item in items:
        filename = item.get("filename")
        expected_hash = item.get("sha256")

        if not filename or not expected_hash:
            print("[SKIP] Metadati incompleti per un elemento.")
            continue

        file_path = os.path.join(REPORTS_DIR, filename)
        if not os.path.exists(file_path):
            print(f"[ERRORE] File non trovato: {filename}")
            checked += 1
            continue

        current_hash = sha256_file(file_path)
        checked += 1

        if current_hash.lower() == expected_hash.lower():
            print(f"[OK]   {filename}")
            ok += 1
        else:
            print(f"[FAIL] {filename} (hash diverso)")

    print(f"\nRisultato: {ok}/{checked} file verificati correttamente.")


if __name__ == "__main__":
    main()
