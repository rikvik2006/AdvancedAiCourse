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
