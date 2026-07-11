# Kristina Persall Portfolio Website

A polished multi-page marketing portfolio website for Kristina Persall. The site is designed for recruiters, hiring managers, nonprofit leaders, agency teams, and potential collaborators reviewing Kristina's marketing strategy, branding, communications, resume, and professional development work.

## Project Overview

This is a static portfolio website built with simple HTML and CSS. It does not use React, Next.js, Tailwind, Vite, or a JavaScript framework.

Pages included:

- Home
- About
- Portfolio
- Resume
- Professional Development
- Contact

The visual style is premium, editorial, recruiter-friendly, and professional, with a consistent navy, teal, warm beige, off-white, and charcoal color palette.

## Technologies Used

- HTML5
- CSS3
- Google Fonts
  - Playfair Display
  - Montserrat
  - Inter
- Static assets: PNG, JPG, PDF, MOV

## Project Type

This project is:

**HTML/CSS static website**

It is not:

- Next.js
- React
- Vite
- Tailwind CSS
- A server-rendered application

## Folder Structure

```text
portfolio-site/
├── index.html
├── about.html
├── portfolio.html
├── resume.html
├── professional-development.html
├── contact.html
├── styles.css
├── package.json
├── vercel.json
├── .gitignore
├── README.md
└── assets/
    ├── images
    ├── PDFs
    └── portfolio materials
```

## Installation

No dependency installation is required for the website itself.

If you want to use the included local preview scripts, make sure Python 3 is available on your computer.

```bash
npm install
```

The command above does not install any production dependencies because this is a static site.

## Local Preview

From inside the project folder:

```bash
npm run dev
```

Then open:

```text
http://localhost:3000
```

You can also open `index.html` directly in a browser.

## Build Instructions

The website is static, but the included build command prepares a `public/` folder for hosts that expect a build output directory.

```bash
npm run build
```

After the build runs, the generated `public/` folder contains the HTML pages, stylesheet, and referenced assets.

## Deployment Instructions

### Deploying to Vercel

1. Upload or push this folder to GitHub.
2. Create a new project in Vercel.
3. Select the GitHub repository.
4. Use these settings:
   - Framework Preset: **Other**
   - Build Command: `npm run build`
   - Output Directory: `public`
   - Install Command: `npm install` or leave blank
5. Deploy.

The included `vercel.json` file adds static asset caching and clean URL support.

### Deploying to Netlify or Other Static Hosts

Upload the contents of this folder as a static site.

No server setup or framework configuration is required.

## GitHub Preparation

Recommended GitHub steps:

```bash
git init
git add .
git commit -m "Initial production-ready portfolio website"
git branch -M main
git remote add origin YOUR_REPOSITORY_URL
git push -u origin main
```

## Production Notes

- The site uses static HTML and CSS only.
- All pages share one stylesheet: `styles.css`.
- Internal links have been checked.
- Placeholder copy has been removed from production pages.
- The clean production package should include only website files and referenced assets.
- `.DS_Store`, local ZIP files, Vercel cache files, and dependency folders are ignored by Git.
