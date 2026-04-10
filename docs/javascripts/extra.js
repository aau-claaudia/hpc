function parseDdMm(value, year) {
  const match = value.match(/^(\d{1,2})\/(\d{1,2})$/);
  if (!match) return null;
  const day = Number(match[1]);
  const month = Number(match[2]);
  if (!Number.isInteger(day) || !Number.isInteger(month)) return null;
  return new Date(year, month - 1, day);
}

function styleServiceWindowTable(table) {
  const headerCells = Array.from(table.querySelectorAll("thead th"));
  if (headerCells.length === 0) return;

  const years = headerCells.map((th) => {
    const value = Number((th.textContent || "").trim());
    return Number.isInteger(value) && value >= 2000 && value <= 2100 ? value : null;
  });

  // Only process schedule tables with year columns.
  if (years.every((year) => year === null)) return;

  const today = new Date();
  today.setHours(0, 0, 0, 0);

  const candidates = [];
  const cells = Array.from(table.querySelectorAll("tbody td"));

  cells.forEach((cell, colIndex) => {
    if (!cell.dataset.rawDateValue) {
      cell.dataset.rawDateValue = (cell.textContent || "").trim();
    }

    const raw = cell.dataset.rawDateValue.trim();
    const year = years[colIndex % years.length];

    // Reset to raw before applying new style.
    cell.textContent = raw;

    if (!year || raw === "-") return;

    const date = parseDdMm(raw, year);
    if (!date || Number.isNaN(date.getTime())) return;

    candidates.push({ cell, raw, date });
  });

  if (candidates.length === 0) return;

  let nextUpcoming = null;
  candidates.forEach((entry) => {
    if (entry.date >= today && (!nextUpcoming || entry.date < nextUpcoming.date)) {
      nextUpcoming = entry;
    }
  });

  candidates.forEach((entry) => {
    if (entry.date < today) {
      entry.cell.innerHTML = `<s>${entry.raw}</s>`;
    } else if (nextUpcoming && entry.cell === nextUpcoming.cell) {
      entry.cell.innerHTML = `<span class="service-window-next-date">${entry.raw}</span>`;
    } else {
      entry.cell.textContent = entry.raw;
    }
  });
}

function updateServiceWindowDates() {
  if (!window.location.pathname.includes("/service-windows/")) return;
  const tables = document.querySelectorAll(".md-typeset table");
  tables.forEach(styleServiceWindowTable);
}

document.addEventListener("DOMContentLoaded", updateServiceWindowDates);
if (window.document$?.subscribe) {
  window.document$.subscribe(updateServiceWindowDates);
}
