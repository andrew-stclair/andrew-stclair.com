module.exports = function (eleventyConfig) {
    eleventyConfig.addPassthroughCopy("src/css");
    eleventyConfig.addPassthroughCopy("src/.well-known");
    eleventyConfig.addPassthroughCopy("src/robots.txt");
};