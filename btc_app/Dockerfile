#immagine docker python
FROM python:3.9-slim

#directory di lavoro nel container
WORKDIR /app

#copiare il file nella directory /app
COPY requirements.txt .

#installare le dipendenze presenti nel file .txt
RUN pip install --no-cache-dir -r requirements.txt

#copiare codice rimanente dell'app nella directory
COPY . .

#porta su cui gira l'applicazione
EXPOSE 5000

#comando di partenza dell'app
CMD ["python", "main.py"]

