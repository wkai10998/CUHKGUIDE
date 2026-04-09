(function () {
  const input = document.getElementById("qa-search");
  const list = document.getElementById("qa-list");
  if (!input || !list) return;

  const items = Array.from(list.querySelectorAll(".qa-item"));

  input.addEventListener("input", () => {
    const keyword = input.value.trim().toLowerCase();

    items.forEach((item) => {
      const title = (item.dataset.title || "").toLowerCase();
      const category = (item.dataset.category || "").toLowerCase();
      const matched = !keyword || title.includes(keyword) || category.includes(keyword);
      item.style.display = matched ? "block" : "none";
    });
  });
})();
