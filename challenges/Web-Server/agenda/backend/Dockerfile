FROM openjdk:11-jdk-stretch AS java-build

WORKDIR /home
ADD . /home
RUN ./gradlew build

FROM openjdk:11-jdk-stretch

RUN apt-get update && apt-get install -y netcat \
    && rm -rf /var/lib/apt/lists/*

COPY scripts/* /usr/local/bin/
COPY --from=java-build /home/build/libs/graphql-demo-service.jar /app/agenda-app.jar

EXPOSE 80

CMD java -jar /app/agenda-app.jar
