FROM nginx:alpine
COPY ["build", "/usr/share/nginx/html"]
RUN apk update && apk upgrade --no-cache
EXPOSE 80
HEALTHCHECK --interval=10s --timeout=4s CMD curl -f https://localhost/ || exit 1
