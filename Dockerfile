FROM python:3.10.6
RUN apt-get update
RUN apt-get install -y git
RUN pip install --upgrade pip
RUN pip install aiogram==2.25.1
RUN git clone https://github.com/bukhantcev/BeautyServant.git
WORKDIR /BeautyServant
ENV TOKEN="6587552734:AAG079fkf6vVV8P6l8RIxeUcbpwyfECfT1U"
RUN echo "git pull && python3 main.py" > start.sh
CMD [ "bash", "start.sh" ]