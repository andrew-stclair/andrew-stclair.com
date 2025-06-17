# Site Configuration

Site-wide configuration is managed in the following files:

- `src/_data/site.json`: Contains global site metadata such as title, description, author, and social links. Example:

  ```json
  {
    "title": "My Awesome Blog",
    "description": "A blog about awesome things.",
    "author": "Your Name",
    "url": "https://example.com",
    "social": {
      "twitter": "yourhandle",
      "github": "yourhandle"
    }
  }
  ```

- `src/.eleventy.js`: The Eleventy configuration file. Use this to customize input/output directories, add filters, shortcodes, collections, and plugins.

To update site metadata, edit `src/_data/site.json`. To change build behavior or add custom logic, edit `src/.eleventy.js`.
