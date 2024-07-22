# Use the official pgAdmin 4 image as the base
FROM dpage/pgadmin4:latest

# Set environment variables
ENV PGADMIN_DEFAULT_EMAIL=user@example.com
ENV PGADMIN_DEFAULT_PASSWORD=securepassword

# Expose port 80 (default for pgAdmin)
EXPOSE 80
