# 1️⃣ Base Python image
FROM python:3.11-slim

# 2️⃣ Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 3️⃣ Set working directory
WORKDIR /app

# 4️⃣ Copy project files
COPY . /app

# 5️⃣ Install Python dependencies
# If you have a requirements.txt, this installs them.
# If not, we install FastAPI + Uvicorn + requests + python-multipart
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt


# 6️⃣ Expose API port
EXPOSE 8000

# 7️⃣ Start FastAPI with Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
