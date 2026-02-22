async function loadReports() {
  const container = document.getElementById("reports");
  const kpi = document.getElementById("kpi-count");

  try {
    const response = await fetch("data/manifest.json", { cache: "no-store" });
    if (!response.ok) throw new Error("manifest.json non trovato");

    const data = await response.json();
    const items = data.items || [];

    if (kpi) kpi.textContent = String(items.length);

    if (items.length === 0) {
      container.innerHTML = `<p class="meta">Nessun report disponibile nel manifest.</p>`;
      return;
    }

    container.innerHTML = "";

    items.forEach(r => {
      const div = document.createElement("div");
      div.className = "report";

      // Percorso PDF: supporta sia "/reports/.." sia "../reports/.."
      const pdfPath = (r.local_path || "").startsWith("../reports/")
        ? r.local_path.replace("../reports/", "/reports/")
        : r.local_path;

      const shaShort = (r.sha256 || "").slice(0, 12);

      div.innerHTML = `
        <h3>${escapeHtml(r.title || "")}</h3>
        <p class="meta">${escapeHtml(r.description || "")}</p>

        <div class="chips">
          <span class="chip">Anno: ${escapeHtml(String(r.year || ""))}</span>
          <span class="chip">Tipo: ${escapeHtml(r.type || "")}</span>
          ${shaShort ? `<span class="chip">SHA256: ${escapeHtml(shaShort)}…</span>` : ``}
        </div>

        <a class="btn" href="${escapeAttr(pdfPath)}" download>Download PDF</a>
      `;

      container.appendChild(div);
    });

  } catch (err) {
    container.innerHTML = `<p class="meta">Errore caricamento dati: ${escapeHtml(err.message)}</p>`;
    if (kpi) kpi.textContent = "0";
  }
}

function escapeHtml(s) {
  return String(s).replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#039;'}[c]));
}
function escapeAttr(s){ return escapeHtml(s); }

document.getElementById("btn-refresh")?.addEventListener("click", loadReports);
loadReports();
