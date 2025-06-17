# Project Documentation

## Overview

This project is a static site built with [Eleventy (11ty)](https://www.11ty.dev/), a simple and flexible static site generator. The site content, templates, and configuration are organized for easy customization and deployment.

## Project Structure

- `src/` - Main source directory for site content and configuration
  - `blog.njk`, `feed.njk`, `index.njk`, etc. - Nunjucks templates for pages
  - `_data/` - Global data files (e.g., `site.json`)
  - `_includes/` - Reusable template partials (Liquid and Nunjucks)
  - `blog-posts/` - Individual blog post files
  - `css/` - Stylesheets for the site
- `package.json` - Project dependencies and scripts
- `README.md` - Project overview and basic instructions
- `SECURITY.md` - Security policy and contact information

## Documentation Index

- [Creating Blog Posts](creating-blog-posts.md)
- [Site Configuration](site-configuration.md)
- [Development](development.md)

## Getting Started

### Prerequisites

- Node.js (LTS recommended)
- npm (comes with Node.js)

### Install Dependencies

```bash
npm install
```

### Build the Site

```bash
npx @11ty/eleventy --input=src --output=build --config=src/.eleventy.js
```

Or use the VS Code task: **11ty: Build**

### Serve Locally

```bash
npx @11ty/eleventy --input=src --output=build --config=src/.eleventy.js --serve --port=8081
```

Or use the VS Code task: **11ty: Serve**

The site will be available at [http://localhost:8081](http://localhost:8081).

## Eleventy Configuration

The Eleventy configuration file is located at `src/.eleventy.js` (not shown above, but referenced in build commands). It defines input/output directories, template engines, and custom configuration for the build process.

- **Input directory:** `src/`
- **Output directory:** `build/`
- **Config file:** `src/.eleventy.js`

You can customize Eleventy by editing `src/.eleventy.js` to add filters, shortcodes, collections, and more. See the [Eleventy documentation](https://www.11ty.dev/docs/config/) for details.

## Security

- The project includes a `SECURITY.md` file and a signed `security.txt` (see VS Code task: **Sign security.txt**).

## Additional Resources

- [Eleventy Documentation](https://www.11ty.dev/docs/)
- [Nunjucks Templating](https://mozilla.github.io/nunjucks/templating.html)
- [Liquid Templating](https://shopify.github.io/liquid/)

---

For further details, see the `README.md` and `SECURITY.md` files in the project root.
