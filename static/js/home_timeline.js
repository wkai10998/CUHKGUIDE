(function () {
  const container = document.getElementById("timeline-flow");
  const svg = document.getElementById("timeline-connector-layer");
  if (!container || !svg) return;

  const svgNS = "http://www.w3.org/2000/svg";
  let rafId = 0;
  let observer = null;

  function isDesktop() {
    return window.matchMedia("(min-width: 768px)").matches;
  }

  function getCards() {
    return Array.from(container.querySelectorAll("[data-stage-card]"));
  }

  function scheduleDraw() {
    if (rafId) {
      window.cancelAnimationFrame(rafId);
    }
    rafId = window.requestAnimationFrame(drawConnectors);
  }

  function drawConnectors() {
    rafId = 0;
    svg.replaceChildren();

    const cards = getCards();
    if (cards.length < 2 || !isDesktop()) return;

    const rootRect = container.getBoundingClientRect();
    const width = Math.max(1, Math.round(rootRect.width));
    const height = Math.max(1, Math.round(rootRect.height));
    svg.setAttribute("viewBox", `0 0 ${width} ${height}`);
    svg.setAttribute("width", String(width));
    svg.setAttribute("height", String(height));

    for (let i = 0; i < cards.length - 1; i += 1) {
      const currentRect = cards[i].getBoundingClientRect();
      const nextRect = cards[i + 1].getBoundingClientRect();

      const currentCenterX = currentRect.left + currentRect.width / 2;
      const nextCenterX = nextRect.left + nextRect.width / 2;
      const toRight = nextCenterX >= currentCenterX;

      const startX = toRight
        ? currentRect.right - rootRect.left - 12
        : currentRect.left - rootRect.left + 12;
      const startY = currentRect.top - rootRect.top + currentRect.height / 2;

      const endX = toRight
        ? nextRect.left - rootRect.left + 12
        : nextRect.right - rootRect.left - 12;
      const endY = nextRect.top - rootRect.top + nextRect.height / 2;

      const baseOffset = Math.abs(endX - startX) * 0.5;
      const controlOffset = Math.max(72, Math.min(180, baseOffset));
      const direction = toRight ? 1 : -1;

      const control1X = startX + controlOffset * direction;
      const control2X = endX - controlOffset * direction;
      const pathData = `M ${startX} ${startY} C ${control1X} ${startY}, ${control2X} ${endY}, ${endX} ${endY}`;

      const path = document.createElementNS(svgNS, "path");
      path.setAttribute("d", pathData);
      path.setAttribute("class", "timeline-flow-path");
      svg.appendChild(path);
    }
  }

  window.addEventListener("resize", scheduleDraw);
  window.addEventListener("orientationchange", scheduleDraw);
  window.addEventListener("load", scheduleDraw);

  if ("ResizeObserver" in window) {
    observer = new ResizeObserver(scheduleDraw);
    observer.observe(container);
    getCards().forEach(function (card) {
      observer.observe(card);
    });
  }

  if (document.fonts && document.fonts.ready) {
    document.fonts.ready.then(scheduleDraw).catch(function () {});
  }

  scheduleDraw();
})();
