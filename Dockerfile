# Gunakan image Python yang valid sebagai base
FROM python:3.11-slim

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file dari host ke container
COPY . /app

# Instal dependensi aplikasi
RUN pip install --no-cache-dir -r requirements.txt

# Mengekspos port aplikasi
EXPOSE 5000

# Menentukan perintah yang akan dijalankan saat container berjalan
CMD ["python", "app.py"]