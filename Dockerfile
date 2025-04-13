FROM python:3.10-slim
#Working directry in the container to app
WORKDIR /app
#copy directory content to app container
COPY . .
#install requirements
RUN pip install -r requirements.txt
#Expose port 80
EXPOSE 80
#Enviroment variable
ENV NAME World
#run main.py when container launched
CMD ["python", "main.py"]