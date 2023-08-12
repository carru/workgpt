FROM python:3

WORKDIR /workgpt

COPY *.py ./
COPY requirements.txt ./
COPY entrypoint.sh ./
RUN chmod +x ./entrypoint.sh
ADD https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin ./models/

# Streamlit
EXPOSE 8501

# python deps
RUN pip install --no-cache-dir -r requirements.txt

# download embeddings
RUN python3 ./init.py

# persistent vectorstore
VOLUME [ "./db" ]

ENTRYPOINT ["./entrypoint.sh"]