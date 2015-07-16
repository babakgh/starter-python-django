FROM python:{{.Version}}

RUN apt-get update -qq && apt-get install -y build-essential {{.Packages.ToList " "}} \
		mysql-client libmysqlclient-dev \
		postgresql-client libpq-dev \
		sqlite3
		
ENV APP_HOME /app
RUN mkdir $APP_HOME 
WORKDIR $APP_HOME

ADD . $APP_HOME
RUN pip install --no-cache-dir -r {{.RequirementsTxt}}
