FROM nginx:stable-alpine3.24

# Replace the image's default virtual host with this lab's static-site config.
COPY nginx.conf /etc/nginx/conf.d/default.conf

# The official image serves site files from this document root.
COPY website/ /usr/share/nginx/html/

EXPOSE 80

# Keep the server in the foreground so it remains the container's main process.
CMD ["nginx", "-g", "daemon off;"]
