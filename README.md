# Clearwell Dermatology — website

A single-page, animated marketing site for a dermatology clinic.

**Live site:** https://dani2127.github.io/dermatology-clinic/

## Stack
- HTML + custom CSS (glassmorphism, clip-path reveals, blur transitions)
- [Tailwind CSS](https://tailwindcss.com) 3.4.16 via CDN
- Vanilla JavaScript (scroll-driven animation loop, IntersectionObserver reveals)
- [Lenis](https://github.com/darkroomengineering/lenis) 1.1.13 for smooth scrolling
- [Lucide](https://lucide.dev) 0.460.0 icons
- Google Fonts: Plus Jakarta Sans, JetBrains Mono

No backend yet — the booking and newsletter forms only show a confirmation message.

## Structure
```
index.html        # built, self-contained page (images embedded) — what GitHub Pages serves
src/index.html    # editable source; loads images from src/assets/
src/assets/       # photos (AI-generated)
src/build.py      # rebuilds index.html from src/
```

## Editing
1. Edit `src/index.html` (open it directly in a browser to preview).
2. Run `python3 src/build.py` to regenerate the root `index.html`.
3. Commit and push — GitHub Pages redeploys automatically.
