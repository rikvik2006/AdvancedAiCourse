# Creare i virtual enviroment

Ho creato 2 virtual env al interno della cartella `.venv`. I due virtual env sono per le due seguenti versioni di python:

-   Python 3.10
-   Python 3.13

Prima di tutto installiamo `virtualenv` con il seguente comando:

```bash
python310 -m pip install virtualenv
python313 -m pip install virtualenv
```

Per creare i virtual env ho usato il seguente comando:

```bash
python310 -m virtualenv .venv/python310
python313 -m virtualenv .venv/python313
```

Per attivare i virtual env ho usato il seguente comando:

```bash
.venv/python310/bin/activate
.venv/python313/bin/activate
```

# Risoluzine problemi

In caso di problemi nella selezione del virtual env su visual studio code, al posto di utilizzare lo script `virtualenv` utilizzare `venv`.

```bash
python310 -m venv .venv/python310
python313 -m venv .venv/python313
```

# Link al notebook di jupyter salvato sul mio github gist per avviare i modelli con ollama

[Notebook](https://colab.research.google.com/gist/rikvik2006/9832bad19649ed47de85b0eedc04b7db/ollama-ngrok-corso-ai-2425-itispininfarina.ipynb)
