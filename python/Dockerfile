#FROM --platform=linux/x86_64 python:3.11
FROM python:3.11
COPY --from=datadog/serverless-init /datadog-init /app/datadog-init
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY entrypoint.sh requirements.txt app.py /app/
RUN pip install --no-cache-dir -r requirements.txt

ENV DD_SERVICE=datadog-demo-run-python
ENV DD_ENV=datadog-demo
ENV DD_VERSION=1
ENV DD_TRACE_PROPAGATION_STYLE=datadog
ENV DD_TRACE_ENABLED=true

#ENTRYPOINT ["/app/datadog-init"]
#CMD ["ddtrace-run", "python", "app.py"]
ENTRYPOINT ["/app/entrypoint.sh"]
