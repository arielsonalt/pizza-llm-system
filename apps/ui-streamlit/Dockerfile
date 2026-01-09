FROM python:3.11-slim
WORKDIR /app

RUN pip install --no-cache-dir streamlit==1.37.1 requests==2.32.3

COPY packages /app/packages
COPY apps/ui-streamlit/app.py /app/app.py

EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
