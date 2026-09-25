FROM quay.io/jupyter/base-notebook:x86_64-python-3.13

USER root

# Install system dependencies
RUN apt-get update && apt-get install -y \
  git \
  wget \
  build-essential \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

# Hugging Face cache shared by the image/runtime.
ENV HF_HOME=/opt/huggingface
ENV HF_HUB_CACHE=/opt/huggingface/hub

RUN mkdir -p ${HF_HUB_CACHE} \
    && chown -R ${NB_UID}:${NB_GID} /opt/huggingface

USER ${NB_UID}

# Copy requirements and install Python packages
COPY --chown=${NB_UID}:${NB_GID} requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Download the model snapshots while building the image.
COPY --chown=${NB_UID}:${NB_GID} download_models.py /tmp/download_models.py

RUN python /tmp/download_models.py \
    && rm /tmp/download_models.py

# Expose Jupyter port
EXPOSE 8888
