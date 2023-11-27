FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9
COPY ./app /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["uvicorn", "weather_app:app", "--host", "0.0.0.0", "--port", "5000"]
