(function () {
  const form = document.getElementById("assistant-chat-form");
  const input = document.getElementById("assistant-chat-input");
  const sendButton = document.getElementById("assistant-chat-send");
  const chatLog = document.getElementById("assistant-chat-log");
  const statusNode = document.getElementById("assistant-chat-status");
  const chips = Array.from(document.querySelectorAll("[data-question-chip]"));

  if (!form || !input || !sendButton || !chatLog || !statusNode) return;

  const endpoint = form.dataset.endpoint || "/assistant/message";
  let pending = false;
  let phaseTimer = null;

  function safeLink(href) {
    if (typeof href !== "string") return "#";
    if (href.startsWith("/")) return href;
    return "#";
  }

  function setStatus(text) {
    statusNode.textContent = text;
  }

  function setPending(isPending) {
    pending = isPending;
    input.disabled = isPending;
    sendButton.disabled = isPending;
    sendButton.classList.toggle("opacity-70", isPending);
    sendButton.classList.toggle("cursor-not-allowed", isPending);
  }

  function scrollToBottom() {
    chatLog.scrollTop = chatLog.scrollHeight;
  }

  function renderSources(parent, sources) {
    if (!Array.isArray(sources) || sources.length === 0) return;

    const title = document.createElement("p");
    title.className = "mt-3 text-xs font-semibold text-ink-700";
    title.textContent = "引用来源";
    parent.appendChild(title);

    const list = document.createElement("ul");
    list.className = "mt-1 space-y-1";

    sources.slice(0, 3).forEach((item) => {
      const source = item && typeof item.source === "string" ? item.source : "来源";
      const link = item && typeof item.link === "string" ? item.link : "#";

      const li = document.createElement("li");
      const a = document.createElement("a");
      a.href = safeLink(link);
      a.className = "text-xs text-brand-700 hover:text-brand-600";
      a.textContent = source;
      li.appendChild(a);
      list.appendChild(li);
    });

    parent.appendChild(list);
  }

  function appendMessage(role, text, meta) {
    const row = document.createElement("article");
    row.className = role === "user" ? "flex justify-end" : "flex justify-start";

    const bubble = document.createElement("div");
    if (role === "user") {
      bubble.className =
        "max-w-[85%] md:max-w-[75%] rounded-2xl rounded-br-md bg-brand-600 text-white px-4 py-3 text-sm leading-7 shadow-soft-card";
    } else {
      bubble.className =
        "max-w-[90%] md:max-w-[80%] rounded-2xl rounded-bl-md border border-brand-100 bg-paper-25 px-4 py-3 text-sm leading-7 text-ink-900";
    }

    const textNode = document.createElement("p");
    textNode.className = "whitespace-pre-wrap";
    textNode.textContent = text;
    bubble.appendChild(textNode);

    if (role === "assistant" && meta && Array.isArray(meta.sources)) {
      renderSources(bubble, meta.sources);
    }

    if (role === "assistant" && meta && typeof meta.elapsedMs === "number") {
      const timing = document.createElement("p");
      timing.className = "mt-2 text-[11px] text-ink-700";
      timing.textContent = "响应耗时 " + (meta.elapsedMs / 1000).toFixed(2) + "s";
      bubble.appendChild(timing);
    }

    row.appendChild(bubble);
    chatLog.appendChild(row);
    scrollToBottom();
  }

  async function submitQuestion(question) {
    const normalized = (question || "").trim();
    if (pending || normalized.length < 2) {
      if (normalized.length > 0 && normalized.length < 2) {
        setStatus("问题太短，请至少输入 2 个字。");
      }
      return;
    }

    appendMessage("user", normalized);
    input.value = "";
    setPending(true);
    setStatus("正在检索资料...");
    phaseTimer = window.setTimeout(function () {
      setStatus("正在生成回答...");
    }, 450);

    try {
      const response = await fetch(endpoint, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: normalized }),
      });
      const data = await response.json();

      if (!response.ok || !data.ok) {
        throw new Error((data && data.error) || "当前服务繁忙，请稍后重试。");
      }

      appendMessage("assistant", data.answer || "暂未获得回答。", {
        sources: data.sources || [],
        elapsedMs: Number(data.elapsed_ms) || 0,
      });
      setStatus("已完成，你可以继续追问。");
    } catch (error) {
      appendMessage("assistant", "本次回答暂时失败：" + (error.message || "请稍后重试。"), {
        sources: [],
      });
      setStatus("本次请求未完成，请重试或换个问法。");
    } finally {
      if (phaseTimer !== null) {
        window.clearTimeout(phaseTimer);
        phaseTimer = null;
      }
      setPending(false);
      input.focus();
    }
  }

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    void submitQuestion(input.value);
  });

  input.addEventListener("keydown", function (event) {
    if (event.key !== "Enter" || event.shiftKey || event.isComposing) return;
    event.preventDefault();
    void submitQuestion(input.value);
  });

  chips.forEach(function (chip) {
    chip.addEventListener("click", function () {
      const preset = chip.dataset.questionChip || "";
      input.value = preset;
      input.focus();
      void submitQuestion(preset);
    });
  });
})();
