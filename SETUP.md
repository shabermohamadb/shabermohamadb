# SHABER — THE ANIMATED DEVELOPER IDENTITY
## GitHub Profile Portfolio Setup & Architecture Guide

Welcome to the **Animated Developer Identity** for **SHABER MOHAMAD B**.

This repository is engineered to transform your GitHub profile into an extraordinary, cinematic, motion-graphics developer portfolio leveraging pure, sanitization-safe GitHub README capabilities and self-contained animated SVGs.

---

## 🌌 Repository Architecture

```text
shabermohamadb/
├── .github/
│   └── workflows/
│       └── snake.yml                      # GitHub Actions automated contribution grid snake
├── assets/
│   ├── hero-cinematic.svg                 # SECTION 01: Perspective cyber grid, typewriter, laser beam, HUD
│   ├── profile-timeline.svg               # SECTION 02: Holographic dossier & animated vertical timeline
│   ├── tech-constellation.svg             # SECTION 03: Cosmic neural constellation with counter-rotating orbits
│   ├── project-featured-collabspace.svg   # SECTION 04: Flagship visual with live bidirectional packet network
│   ├── project-floz-commerce.svg          # SECTION 04: Commercial food commerce & dispatch pipeline
│   ├── project-hidden-number.svg          # SECTION 04: 3D WebGL isometric wireframe rotating cube
│   ├── project-al-ameen.svg               # SECTION 04: Automated enterprise document synthesis laser scan
│   ├── project-circuitx.svg               # SECTION 04: Desktop EDA schematic routing & circuit traces
│   ├── project-oggy-3d.svg                # SECTION 04: Interactive WebGL camera viewport reticle
│   ├── analytics-telemetry.svg            # SECTION 05: Cyber telemetry header with ECG Git pulse wave
│   ├── code-in-motion.svg                 # SECTION 06: Full-stack 5-stage architecture pipeline with packet flows
│   ├── terminal-matrix.svg                # SECTION 07: Obsidian CLI terminal with JSON initiative reveal
│   ├── footer-cyber.svg                   # SECTION 08: Receding cyber grid horizon & sweeping radar arm
│   ├── divider-cyber.svg                  # Animated divider: Scanning laser glint & HUD reticle
│   ├── divider-quantum.svg                # Animated divider: Pulsing energy diamond
│   └── divider-matrix.svg                 # Animated divider: High-speed data bus conduit
├── README.md                              # Production GitHub Profile README
├── SETUP.md                               # This documentation guide
└── validate_profile.py                    # Verification suite for SVGs and external URLs
```

---

## 🎨 Visual Identity & Color System

- **Obsidian Space Foundation**: `#020306`, `#04060a`, `#080d1a`, `#070c18`
- **Electric Cyan Primary Accent**: `#00f0ff` (Glow: `rgba(0, 240, 255, 0.4)`)
- **Neon Azure & Blue Highlights**: `#38bdf8`, `#0070f3`, `#0284c7`, `#1d4ed8`
- **White Editorial Typography**: `#ffffff`, `#f8fafc`, `#e2e8f0`
- **Technical Telemetry Slate**: `#64748b`, `#94a3b8`, `#1e293b`
- **System Online Emerald**: `#10b981`

---

## ⚙️ The 15-Point Animation System

Every animation is written in native CSS `@keyframes` inside standard SVG `<defs><style>` blocks or responsive vector paths, rendering reliably in GitHub's Camo proxy:

1. **SVG Stroke Drawing**: `stroke-dasharray` and `stroke-dashoffset` keyframes carve out the main typography `SHABER MOHAMAD B` in `hero-cinematic.svg`.
2. **SVG Path Flow Animation**: Data packets traverse bidirectional conduits between User A, User B, Broker, and AI daemon in `project-featured-collabspace.svg`.
3. **Animated Text Reveals**: Opacity and vertical translation cycle through 3 professional identities in the hero typewriter console.
4. **Typing Effects & Blinking Cursor**: Stepped terminal block cursor `_` blinking in `hero-cinematic.svg` and `terminal-matrix.svg`.
5. **Moving Particle Systems**: 16+ floating cyber motes drifting upwards with staggered keyframe delays and opacities in `hero-cinematic.svg`.
6. **Rotating Technical Diagrams**: Dual counter-rotating orbital rings (15s and 20s) in `tech-constellation.svg` and holographic measurement rings in `profile-timeline.svg`.
7. **Animated Grid Patterns**: Perspective 3D cyber grid lines converging toward the horizon in `hero-cinematic.svg` and `footer-cyber.svg`.
8. **Scanning Beam Effects**: High-precision horizontal laser beam sweeping vertically from `y=0` to `y=480` in `hero-cinematic.svg`.
9. **Animated Gradient Strokes**: Shifting linear gradient highlights traversing across dividers and conduits.
10. **Orbiting Technology Icons**: Satellites traveling along elliptical orbits around the central full-stack AI core.
11. **Animated Separators**: Three distinct dividers (`divider-cyber.svg`, `divider-quantum.svg`, `divider-matrix.svg`) with unique kinetic motifs.
12. **Contribution Snake**: Automatically generated via GitHub Actions (`.github/workflows/snake.yml`) with the Electric Cyan palette.
13. **ECG Git Pulse Monitor**: Oscillating heartbeat waveform in `analytics-telemetry.svg` representing continuous commit velocity.
14. **Audio / Frequency Equalizer**: Bouncing telemetry frequency bars in the hero top HUD.
15. **Custom Looping Wireframes**: 3D rotating isometric cube in `project-hidden-number.svg` and rotating radar scanner arms in `footer-cyber.svg`.

---

## 🚀 How to Deploy / Push Changes to GitHub

Your local repository is set up at:
`/home/shaber/.gemini/antigravity/scratch/shabermohamadb`

To push the new profile to your GitHub account:

```bash
cd /home/shaber/.gemini/antigravity/scratch/shabermohamadb

# 1. Review status
git status

# 2. Stage all updated assets and documentation
git add README.md SETUP.md .github/ assets/

# 3. Commit with a cinematic message
git commit -m "feat: launch animated developer identity with 15-point motion system, tech constellation, and telemetry"

# 4. Push to main branch
git push origin main
```

---

## 🐍 GitHub Contribution Snake Automation

The GitHub Action in `.github/workflows/snake.yml` runs automatically:
- Every 12 hours via cron (`0 */12 * * *`)
- On every push to the `main` branch
- Manually via the **Actions** tab in GitHub (`workflow_dispatch`)

It generates:
- `dist/github-contribution-grid-snake.svg`
- `dist/github-contribution-grid-snake-dark.svg` (customized with `#00f0ff` snake and dark cyan grid dots)
and commits them directly to the `output` branch.

---

## 🧪 Verification & Health Check

You can run the built-in validation script at any time to verify XML integrity and external link availability:

```bash
python3 validate_profile.py
```
