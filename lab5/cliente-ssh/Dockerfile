FROM python:3.11-slim
WORKDIR /app
RUN pip install --no-cache-dir paramiko
COPY cliente-ssh.py .
CMD ["python", "cliente-ssh.py"]
