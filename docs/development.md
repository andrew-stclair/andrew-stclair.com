# Development

To develop and preview the site locally:

1. **Install dependencies** (if you haven't already):

   ```bash
   npm install
   ```

2. **Start the development server**:

   ```bash
   npx @11ty/eleventy --input=src --output=build --config=src/.eleventy.js --serve --port=8081
   ```
   Or use the VS Code task: **11ty: Serve**

3. **Edit source files** in `src/`. The site will automatically rebuild and reload in the browser when files change.

4. **Build for production**:

   ```bash
   npx @11ty/eleventy --input=src --output=build --config=src/.eleventy.js
   ```
   Or use the VS Code task: **11ty: Build**

## Additional Tips

- Use the `css/` directory for custom stylesheets.
- Use the `_includes/` directory for reusable template components.
- Use the `_data/` directory for global data files.
- For security, see the `SECURITY.md` file and the signed `security.txt`.
