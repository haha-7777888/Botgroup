FROM python:3.10-slim

WORKDIR /app

# kurigram နှင့် အခြား library များအတွက် လိုအပ်သော git နှင့် tools များ ထည့်သွင်းခြင်း
RUN apt-get update && apt-get install -y --no-install-recommends \
    git \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
