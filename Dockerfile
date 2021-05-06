FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano
ENV STATIC_URL /static
ENV STATIC_PATH /Users/andrewmaclean/Desktop/API/Lantern/Data_Science/Lantern-Flask-Project/Lantern-Flask-Project/static
COPY ./requirements.txt /Users/andrewmaclean/Desktop/API/Lantern/Data_Science/Lantern-Flask-Project/Lantern-Flask-Project/requirements.txt
RUN pip install -r requirements.txt
