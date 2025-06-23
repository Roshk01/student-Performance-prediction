# use a base image with python
FROM python:3.10

# set working directory
WORKDIR /app

# copy code
copy . .

# install dependancy
run pip install --upgrade pip
run pip install -r requirements.txt

# streamlit port expose
expose 8501

# run the app
CMD ["streamlit","run","app.py", "--server.port=8501","--server.address=0.0.0.0"]