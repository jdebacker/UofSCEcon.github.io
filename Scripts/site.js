document.addEventListener("DOMContentLoaded", () => {
  const year = document.getElementById("year");
  if (year) {
    year.textContent = new Date().getFullYear();
  }

  const offCanvasWrap = document.querySelector(".off-canvas-wrap");
  const menuToggle = document.querySelector(".right-off-canvas-toggle");
  const exitOffCanvas = document.querySelector(".exit-off-canvas");

  const setMenuState = (open) => {
    if (!offCanvasWrap) {
      return;
    }

    offCanvasWrap.classList.toggle("move-left", open);
    if (menuToggle) {
      menuToggle.setAttribute("aria-expanded", String(open));
    }
    if (exitOffCanvas) {
      exitOffCanvas.hidden = !open;
    }
    document.body.classList.toggle("off-canvas-open", open);
  };

  if (menuToggle && offCanvasWrap) {
    menuToggle.setAttribute("aria-expanded", "false");
    menuToggle.setAttribute("aria-controls", "site-navigation");
    menuToggle.addEventListener("click", (event) => {
      event.preventDefault();
      setMenuState(!offCanvasWrap.classList.contains("move-left"));
    });
  }

  if (exitOffCanvas) {
    exitOffCanvas.hidden = true;
    exitOffCanvas.addEventListener("click", (event) => {
      event.preventDefault();
      setMenuState(false);
    });
  }

  document.querySelectorAll(".off-canvas-submenu-call").forEach((trigger) => {
    const parentItem = trigger.parentElement;
    const submenu = trigger.parentElement?.querySelector(":scope > .off-canvas-submenu");
    if (!parentItem || !submenu) {
      return;
    }

    const isOpen = parentItem.classList.contains("open");
    submenu.hidden = !isOpen;
    trigger.setAttribute("aria-expanded", String(isOpen));

    trigger.addEventListener("click", (event) => {
      event.preventDefault();
      const nextOpen = !parentItem.classList.contains("open");
      parentItem.classList.toggle("open", nextOpen);
      parentItem.classList.toggle("closed", !nextOpen);
      submenu.hidden = !nextOpen;
      trigger.setAttribute("aria-expanded", String(nextOpen));
    });
  });

  document.querySelectorAll(".active").forEach((activeItem) => {
    activeItem.closest(".off-canvas-submenu")?.removeAttribute("hidden");
  });

  document.querySelectorAll('.profile-content a[href^="#"]:not([href="#"])').forEach((link) => {
    link.addEventListener("click", (event) => {
      const anchorName = link.getAttribute("href")?.slice(1);
      if (!anchorName) {
        return;
      }

      const target = document.querySelector(`a[name="${CSS.escape(anchorName)}"]`);
      if (!target) {
        return;
      }

      event.preventDefault();
      target.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  });
});
