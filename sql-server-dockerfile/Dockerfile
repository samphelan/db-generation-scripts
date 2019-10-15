FROM lbosqmsft/mssql-python-pyodbc
RUN pip install faker
RUN pip install google-cloud-dataproc
RUN pip install google-cloud-storage
RUN pip install pyyaml
COPY labs-sbx-d9cd32768fe7.json
ENV GOOGLE_APPLICATION_CREDENTIALS="/labs-sbx-d9cd32768fe7.json"
