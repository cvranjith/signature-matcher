# Base image with Python and PyTorch + torchvision + timm
FROM python:3.11-slim

# Avoid interactive prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Install system dependencies for OpenCV
RUN apt-get update && apt-get install -y \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir \
    torch torchvision timm \
    flask opencv-python scikit-learn

# Expose Flask default port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
