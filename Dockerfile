# Use Python as base image
FROM python:3.10

# Install Chrome
RUN apt-get update && apt-get install -y wget unzip \
    && wget -q -O /tmp/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && dpkg -i /tmp/chrome.deb || apt-get -fy install \
    && rm /tmp/chrome.deb

# Install dependencies
RUN pip install selenium

# Set environment variables
ENV DISPLAY=:99

# Copy script
COPY visit_website.py /visit_website.py

# Run script
CMD ["python", "/visit_website.py"]
