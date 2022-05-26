FROM nginx:1.22.0-alpine
COPY ["build", "/usr/share/nginx/html"]
EXPOSE 80
HEALTHCHECK --interval=10s --timeout=4s CMD curl -f https://localhost/ || exit 1
