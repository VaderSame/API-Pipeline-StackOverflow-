# ---- 1. Base image ----
FROM python:3.10-slim-buster

# ---- 2. Set work directory ----
WORKDIR /app

# ---- 3. Copy requirements ----
COPY requirements.txt .

# ---- 4. Install dependencies ----
RUN pip install --no-cache-dir -r requirements.txt

# ---- 5. Copy project files ----
COPY . .

# ---- 6. Expose Flask port ----
EXPOSE 5000

# ---- 7. Run the Flask app ----
CMD ["python", "run.py"]
