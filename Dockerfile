# Set basic image data
FROM python:3.12-slim
LABEL org.opencontainers.image.source="https://github.com/PythonVilag/pythonvilag-website"

ENV LANG=C.UTF-8
ENV TZ=Europe/Copenhagen

# Copy files
WORKDIR /workspace
COPY ./requirements.txt ./requirements.txt
COPY ./src/ ./src/

# Install python packages
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

# Run command
EXPOSE 5000
CMD ["python", "src/run.py", "--port", "5000"]
