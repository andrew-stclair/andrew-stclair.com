# Creating Blog Posts

Blog posts are stored in the `src/blog-posts/` directory. Each post can be written in Nunjucks (`.njk`) or Markdown (`.md`) format. To create a new blog post:

1. **Create a new file** in `src/blog-posts/`, e.g., `my-new-post.njk` or `my-new-post.md`.
2. **Add front matter** at the top of the file:

   ```yaml
   ---
   title: "My New Post"
   date: 2025-06-17
   description: "A short summary of my new post."
   tags: [blog, update]
   ---
   ```

3. **Write your content** below the front matter using Markdown or Nunjucks syntax.
4. **Save the file**. The post will be included automatically in the blog listing after the next build.

You can use custom fields in the front matter as needed. Posts are typically sorted by date.
