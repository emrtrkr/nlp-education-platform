# Python 3.9 slim image kullan
FROM python:3.9-slim

# Çalışma dizinini ayarla
WORKDIR /app

# Sistem paketlerini güncelle ve gerekli paketleri yükle
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Python requirements'ı kopyala ve yükle
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Uygulama dosyalarını kopyala
COPY . .

# Streamlit konfigürasyonu
RUN mkdir -p /root/.streamlit
RUN echo "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml

RUN echo "\
[server]\n\
headless = true\n\
enableCORS = false\n\
port = 7860\n\
" > /root/.streamlit/config.toml

# Port 7860'ı expose et (HuggingFace Spaces standardı)
EXPOSE 7860

# Health check ekle
HEALTHCHECK CMD curl --fail http://localhost:7860/_stcore/health

# Uygulamayı başlat
ENTRYPOINT ["streamlit", "run", "main.py", "--server.port=7860", "--server.address=0.0.0.0"]