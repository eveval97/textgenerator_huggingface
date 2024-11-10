#para ejecutar: cd webapp  --> uvicorn --host 0.0.0.0 main:app
#va a cargar el link: http://localhost:8000
#ponerle así para ver el Swagger UI http://localhost:8000/docs

para construir el Dockerfile(en el venv): docker build -t huggingface:local . 
para correr el Dockerfile: docker run -i -p 8000:8000 huggingface:local

