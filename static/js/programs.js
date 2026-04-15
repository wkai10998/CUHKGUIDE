(function () {
  const input = document.getElementById("program-search");
  const collegeFilter = document.getElementById("program-college-filter");
  const list = document.getElementById("program-list");
  if (!input || !list || !collegeFilter) return;

  const items = Array.from(list.querySelectorAll(".program-item"));

  function applyFilters() {
    const keyword = input.value.trim().toLowerCase();
    const selectedCollege = collegeFilter.value;

    items.forEach(function (item) {
      const name = (item.dataset.name || "").toLowerCase();
      const nameZh = (item.dataset.nameZh || "").toLowerCase();
      const nameEn = (item.dataset.nameEn || "").toLowerCase();
      const school = (item.dataset.school || "").toLowerCase();
      const college = item.dataset.college || "";
      const focus = (item.dataset.focus || "").toLowerCase();

      const keywordMatched =
        !keyword ||
        name.includes(keyword) ||
        nameZh.includes(keyword) ||
        nameEn.includes(keyword) ||
        school.includes(keyword) ||
        focus.includes(keyword);
      const collegeMatched = selectedCollege === "全部" || college === selectedCollege;
      const matched = keywordMatched && collegeMatched;

      item.style.display = matched ? "" : "none";
    });
  }

  input.addEventListener("input", applyFilters);
  collegeFilter.addEventListener("change", applyFilters);
  applyFilters();
})();
