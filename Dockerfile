FROM python:3
WORKDIR /

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN git clone https://github.com/ethicalhack3r/DVWA /var/www

COPY . .
