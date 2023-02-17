FROM continuumio/miniconda3:latest

# Set up the environment
ENV MICROMAMBA_CHANNEL_PRIORITY strict
ENV MICROMAMBA_ROOT_PREFIX /opt/micromamba
ENV PATH /opt/micromamba/bin:$PATH
ENV JUPYTER_ENABLE_LAB yes

RUN wget -qO- https://micromamba.snakepit.net/api/micromamba/linux-64/latest | tar -xvj bin/micromamba && \
    ./bin/micromamba shell init -s bash -p /opt/micromamba && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Copy environment.yml file and create conda environment
COPY environment.yml /app
RUN micromamba env create -f /app/environment.yml && \
    micromamba clean --all --yes

# Activate the new conda environment and install additional packages
SHELL ["conda", "run", "-n", "my_env", "/bin/bash", "-c"]
RUN conda install -y jupyterlab pandas matplotlib && \
    conda clean --all --yes



# Expose the Jupyter port
EXPOSE 8888

# Start Jupyter
CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser"]
