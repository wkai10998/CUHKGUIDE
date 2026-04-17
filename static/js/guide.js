(function () {
  function setupCompleteToggle() {
    const button = document.getElementById("toggle-complete");
    const label = document.getElementById("complete-label");
    const hint = document.getElementById("complete-hint");
    if (!button || !label || !hint) return;

    button.addEventListener("click", async function () {
      const api = button.dataset.api;
      if (!api) return;

      button.disabled = true;

      try {
        const response = await fetch(api, { method: "POST" });
        if (!response.ok) {
          throw new Error("request failed");
        }

        const payload = await response.json();
        const completed = Boolean(payload.completed);

        label.textContent = completed ? "已完成" : "标记为已完成";
        hint.textContent = "已完成步骤数：" + String(payload.completed_count || 0);

        button.classList.remove("bg-brand-600", "hover:bg-brand-700", "bg-emerald-600", "hover:bg-emerald-700");
        if (completed) {
          button.classList.add("bg-emerald-600", "hover:bg-emerald-700");
        } else {
          button.classList.add("bg-brand-600", "hover:bg-brand-700");
        }
      } catch (_error) {
        window.alert("状态更新失败，请稍后重试。");
      } finally {
        button.disabled = false;
      }
    });
  }

  function renderComment(comment) {
    const wrapper = document.createElement("div");
    wrapper.className = "rounded-md border border-brand-100 bg-white p-3";

    const userName = String(comment.user_name || "游客");
    const createdAt = String(comment.created_at || "");
    const content = String(comment.content || "");

    wrapper.innerHTML =
      '<div class="flex items-center gap-2 mb-2">' +
      '<span class="w-7 h-7 rounded-full text-white text-xs font-semibold flex items-center justify-center bg-brand-600">' +
      userName.slice(0, 1) +
      "</span>" +
      '<span class="text-sm font-medium text-ink-900"></span>' +
      '<span class="text-xs text-ink-700"></span>' +
      "</div>" +
      '<p class="text-sm text-ink-700 leading-7"></p>';

    const spans = wrapper.querySelectorAll("span");
    const contentNode = wrapper.querySelector("p");
    if (spans[1]) spans[1].textContent = userName;
    if (spans[2]) spans[2].textContent = createdAt;
    if (contentNode) contentNode.textContent = content;

    return wrapper;
  }

  async function loadComments() {
    const container = document.getElementById("guide-comments");
    if (!container) return;

    const api = container.dataset.commentsApi;
    if (!api) return;

    try {
      const response = await fetch(api);
      if (!response.ok) {
        throw new Error("request failed");
      }

      const payload = await response.json();
      const comments = Array.isArray(payload.comments) ? payload.comments : [];

      container.innerHTML = "";
      if (!comments.length) {
        container.innerHTML = '<p class="text-sm text-ink-700">还没有评论，来发第一条吧。</p>';
        return;
      }

      comments.forEach(function (comment) {
        container.appendChild(renderComment(comment));
      });
    } catch (_error) {
      container.innerHTML = '<p class="text-sm text-ink-700">评论加载失败，请稍后刷新重试。</p>';
    }
  }

  setupCompleteToggle();
  loadComments();
})();
