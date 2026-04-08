document.addEventListener('DOMContentLoaded', () => {

    // ========================================
    // 1. Theme Toggle
    // ========================================
    const themeToggle = document.getElementById('theme-toggle');

    function getPreferredTheme() {
        const saved = localStorage.getItem('theme');
        if (saved) return saved;
        return window.matchMedia('(prefers-color-scheme: light)').matches ? 'light' : 'dark';
    }

    function setTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem('theme', theme);
    }

    // Listen for system preference changes
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
        if (!localStorage.getItem('theme')) {
            setTheme(e.matches ? 'dark' : 'light');
        }
    });

    if (themeToggle) {
        themeToggle.addEventListener('click', () => {
            const current = document.documentElement.getAttribute('data-theme') || 'dark';
            const next = current === 'dark' ? 'light' : 'dark';
            setTheme(next);
        });
    }


    // ========================================
    // 2. Typing Animation
    // ========================================
    const typedTextSpan = document.querySelector(".typed-text");
    const cursorSpan = document.querySelector(".cursor");

    const textArray = ["Backend Developer", "API Architect", "Python Specialist", "Automation Wizard"];
    const typingDelay = 100;
    const erasingDelay = 50;
    const newTextDelay = 2000;
    let textArrayIndex = 0;
    let charIndex = 0;

    function type() {
        if (charIndex < textArray[textArrayIndex].length) {
            if (!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
            typedTextSpan.textContent += textArray[textArrayIndex].charAt(charIndex);
            charIndex++;
            setTimeout(type, typingDelay);
        } else {
            cursorSpan.classList.remove("typing");
            setTimeout(erase, newTextDelay);
        }
    }

    function erase() {
        if (charIndex > 0) {
            if (!cursorSpan.classList.contains("typing")) cursorSpan.classList.add("typing");
            typedTextSpan.textContent = textArray[textArrayIndex].substring(0, charIndex - 1);
            charIndex--;
            setTimeout(erase, erasingDelay);
        } else {
            cursorSpan.classList.remove("typing");
            textArrayIndex++;
            if (textArrayIndex >= textArray.length) textArrayIndex = 0;
            setTimeout(type, typingDelay + 1100);
        }
    }

    if (textArray.length) setTimeout(type, newTextDelay + 250);


    // ========================================
    // 3. Smooth Scrolling & Active Link
    // ========================================
    const sections = document.querySelectorAll("section");
    const navLinks = document.querySelectorAll(".nav-links a");

    window.addEventListener("scroll", () => {
        let current = "";
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            if (pageYOffset >= sectionTop - 150) {
                current = section.getAttribute("id");
            }
        });

        navLinks.forEach(link => {
            link.classList.remove("active");
            if (link.getAttribute("href").includes(current)) {
                link.classList.add("active");
            }
        });
    });


    // ========================================
    // 4. Contact Form Submission (AJAX)
    // ========================================
    const contactForm = document.getElementById("contact-form");
    const formMessage = document.getElementById("form-message");

    if (contactForm) {
        contactForm.addEventListener("submit", async (e) => {
            e.preventDefault();
            const formData = new FormData(contactForm);

            try {
                const response = await fetch("/contact/submit/", {
                    method: "POST",
                    body: formData,
                    headers: {
                        "X-CSRFToken": formData.get("csrfmiddlewaretoken")
                    }
                });

                const data = await response.json();

                formMessage.textContent = data.message;
                formMessage.className = data.status === "success" ? "success-msg" : "error-msg";
                formMessage.classList.remove("hidden");

                if (data.status === "success") {
                    contactForm.reset();
                }
            } catch (error) {
                console.error("Error:", error);
                formMessage.textContent = "Something went wrong. Please try again later.";
                formMessage.className = "error-msg";
                formMessage.classList.remove("hidden");
            }
        });
    }


    // ========================================
    // 5. Mobile Menu Toggle
    // ========================================
    const menuToggle = document.querySelector(".menu-toggle");
    const navLinksContainer = document.querySelector(".nav-links");

    if (menuToggle) {
        menuToggle.addEventListener("click", () => {
            navLinksContainer.classList.toggle("mobile-active");
            if (navLinksContainer.classList.contains("mobile-active")) {
                navLinksContainer.style.display = "flex";
                navLinksContainer.style.flexDirection = "column";
                navLinksContainer.style.position = "absolute";
                navLinksContainer.style.top = "80px";
                navLinksContainer.style.left = "0";
                navLinksContainer.style.width = "100%";
                navLinksContainer.style.background = "var(--bg-mobile-nav)";
                navLinksContainer.style.padding = "20px";
                navLinksContainer.style.borderBottom = "1px solid var(--border-glass)";
                navLinksContainer.style.zIndex = "999";
            } else {
                navLinksContainer.style.display = "";
                navLinksContainer.style.background = "";
                navLinksContainer.style.borderBottom = "";
                navLinksContainer.style.zIndex = "";
            }
        });
    }


    // ========================================
    // 6. Project Cards — Read More / Show Less
    // ========================================
    function initProjectCards() {
        const wrappers = document.querySelectorAll('.project-content-wrapper');

        wrappers.forEach(wrapper => {
            const content = wrapper.querySelector('.project-content');
            const btn = wrapper.querySelector('.project-read-more-btn');

            if (!content || !btn) return;

            // Measure full content height (uncollapse temporarily)
            content.classList.remove('collapsed');
            const fullHeight = content.scrollHeight;
            content.classList.add('collapsed');

            // Get the collapsed max-height from CSS
            const collapsedMaxHeight = parseFloat(getComputedStyle(content).maxHeight) || (9.5 * 16);

            if (fullHeight <= collapsedMaxHeight + 5) {
                // Content fits — no truncation needed
                wrapper.classList.add('no-truncate');
                return;
            }

            btn.addEventListener('click', () => {
                const isCollapsed = content.classList.contains('collapsed');

                if (isCollapsed) {
                    // Expand
                    content.classList.remove('collapsed');
                    content.classList.add('expanded');
                    wrapper.classList.add('is-expanded');
                    btn.classList.add('active');
                    btn.querySelector('.btn-text').textContent = 'Show Less';
                } else {
                    // Collapse
                    content.classList.remove('expanded');
                    content.classList.add('collapsed');
                    wrapper.classList.remove('is-expanded');
                    btn.classList.remove('active');
                    btn.querySelector('.btn-text').textContent = 'Read More';
                }
            });
        });
    }

    initProjectCards();
});
