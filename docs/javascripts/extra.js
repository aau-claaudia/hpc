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

/**
 * Open external (other-origin) http(s) links in a new tab. Skips links that
 * already have a target, anchors, mailto, tel, and javascript URLs.
 */
function setExternalLinksNewTab() {
  const originHost = window.location.hostname;
  document.querySelectorAll('a[href]:not([target])').forEach((anchor) => {
    const href = anchor.getAttribute("href");
    if (!href || href.startsWith("#")) return;
    let url;
    try {
      url = new URL(href, window.location.origin);
    } catch {
      return;
    }
    if (url.protocol !== "http:" && url.protocol !== "https:") return;
    if (url.hostname === originHost) return;
    anchor.target = "_blank";
    const extra = "noopener noreferrer";
    const existing = (anchor.getAttribute("rel") || "").trim();
    anchor.setAttribute("rel", existing ? `${existing} ${extra}` : extra);
  });
}

document.addEventListener("DOMContentLoaded", setExternalLinksNewTab);
if (window.document$?.subscribe) {
  window.document$.subscribe(setExternalLinksNewTab);
}

function updateHomeNewsCards() {
  const isHomePage =
    window.location.pathname === "/" ||
    window.location.pathname.endsWith("/index.html");
  if (!isHomePage) return;

  const target = document.getElementById("home-news-cards");
  if (!target) return;

  fetch("/news/")
    .then((response) => {
      if (!response.ok) throw new Error("Failed to load news page");
      return response.text();
    })
    .then((html) => {
      const parser = new DOMParser();
      const doc = parser.parseFromString(html, "text/html");
      const allNewsCards = Array.from(doc.querySelectorAll(".grid.cards.three ul > li"));
      const newestThreeCards = allNewsCards.slice(0, 3);

      if (newestThreeCards.length === 0) {
        target.innerHTML = "No news items found.";
        return;
      }

      const wrapper = document.createElement("div");
      wrapper.className = "grid cards three";

      const list = document.createElement("ul");
      newestThreeCards.forEach((card) => {
        list.appendChild(card.cloneNode(true));
      });

      wrapper.appendChild(list);
      target.innerHTML = "";
      target.appendChild(wrapper);
      setExternalLinksNewTab();
    })
    .catch(() => {
      target.innerHTML = "Unable to load latest news right now.";
    });
}

document.addEventListener("DOMContentLoaded", updateHomeNewsCards);
if (window.document$?.subscribe) {
  window.document$.subscribe(updateHomeNewsCards);
}
