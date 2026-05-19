const navToggle = document.querySelector(".nav-toggle");
const navLinks = document.querySelector(".nav-links");
const contactForm = document.querySelector(".contact-form");
const formStatus = document.querySelector(".form-status");

if (navToggle && navLinks) {
    navToggle.addEventListener("click", () => {
        const isOpen = navLinks.classList.toggle("open");
        navToggle.setAttribute("aria-expanded", String(isOpen));
    });

    navLinks.querySelectorAll("a").forEach((link) => {
        link.addEventListener("click", () => {
            navLinks.classList.remove("open");
            navToggle.setAttribute("aria-expanded", "false");
        });
    });
}

if (contactForm && formStatus) {
    contactForm.addEventListener("submit", (event) => {
        event.preventDefault();
        formStatus.textContent = "Thanks! This demo form is ready to connect to a Django view.";
        contactForm.reset();
    });
}
