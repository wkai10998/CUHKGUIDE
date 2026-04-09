(function () {
  const modal = document.getElementById("login-modal");
  if (!modal) return;

  const tabButtons = Array.from(modal.querySelectorAll("[data-auth-tab]"));
  const tabPanels = Array.from(modal.querySelectorAll("[data-auth-panel]"));
  const openTriggers = Array.from(document.querySelectorAll("[data-open-login]"));
  const closeTriggers = Array.from(modal.querySelectorAll("[data-close-login]"));

  function setTab(tabName) {
    const targetTab = tabName === "register" ? "register" : "login";

    tabButtons.forEach(function (button) {
      const isActive = button.dataset.authTab === targetTab;
      button.classList.toggle("bg-brand-600", isActive);
      button.classList.toggle("text-white", isActive);
      button.classList.toggle("text-ink-700", !isActive);
    });

    tabPanels.forEach(function (panel) {
      panel.classList.toggle("hidden", panel.dataset.authPanel !== targetTab);
    });
  }

  function openModal(tabName) {
    setTab(tabName);
    modal.classList.remove("hidden");
    modal.classList.add("flex");
    document.body.classList.add("overflow-hidden");
  }

  function closeModal() {
    modal.classList.add("hidden");
    modal.classList.remove("flex");
    document.body.classList.remove("overflow-hidden");
  }

  tabButtons.forEach(function (button) {
    button.addEventListener("click", function () {
      setTab(button.dataset.authTab);
    });
  });

  openTriggers.forEach(function (trigger) {
    trigger.addEventListener("click", function (event) {
      event.preventDefault();
      openModal(trigger.dataset.authTab || "login");
    });
  });

  closeTriggers.forEach(function (trigger) {
    trigger.addEventListener("click", function () {
      closeModal();
    });
  });

  modal.addEventListener("click", function (event) {
    if (event.target === modal) {
      closeModal();
    }
  });

  document.addEventListener("keydown", function (event) {
    if (event.key === "Escape" && !modal.classList.contains("hidden")) {
      closeModal();
    }
  });

  if (modal.dataset.autoOpen === "1") {
    openModal(modal.dataset.autoTab || "login");
  } else {
    setTab("login");
  }

  window.openLoginModal = openModal;
})();
