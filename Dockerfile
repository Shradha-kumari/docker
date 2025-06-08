FROM python:3.11-slim
COPY hello.py hello.py
RUN pip install Flask
EXPOSE 5000
CMD ["python", "hello.py"]
#CMD ["flask", "--app", "hello", "run"]
