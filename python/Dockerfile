FROM python:3.11
COPY --from=datadog/serverless-init /datadog-init /app/datadog-init
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt app.py /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV DD_SERVICE=datadog-demo-run-python
ENV DD_ENV=datadog-demo
ENV DD_VERSION=1

ENTRYPOINT ["/app/datadog-init"]
CMD ["ddtrace-run", "python", "app.py"]
