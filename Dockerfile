FROM python
COPY . /app
WORKDIR /app
COPY req.txt .
RUN pip install -r requirements.txt
CMD ["python", "app.py"]