FROM python:3.9-slim

RUN pip install pipenv

WORKDIR /app

COPY ["Pipfile.lock", "Pipfile", "./"]

RUN pipenv install --system --deploy
RUN pip install scikit-learn==0.24.2

COPY ["predict.py", "./"]
COPY ["./Trained_Models/model_selected_1d.bin", "./Trained_Models/"]
COPY ["./Trained_Models/model_selected_7d.bin", "./Trained_Models/"]

EXPOSE 9696

ENTRYPOINT ["waitress-serve", "--listen=0.0.0.0:9696", "predict:app"]