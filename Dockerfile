FROM python:3
WORKDIR /app/webtraffic
COPY . /app/webtraffic
RUN pip install -r requirements.txt --trusted-host pypi.org --trusted-host files.pythonhosted.org
CMD python ./app.py