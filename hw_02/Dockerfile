FROM python:3.8-slim
WORKDIR /app
COPY main.py main.py
RUN mkdir -p /app/artifacts
RUN python3 -m pip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple astprintfib==0.1.1
RUN apt update
RUN apt install -y texlive
RUN apt install -y graphviz

CMD python3 /app/main.py
