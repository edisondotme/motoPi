## How to get starting working on motoPi

### Cloning the project

```
git clone https://github.com/edisondotme/motoPi.git
```

### Creating the virtual environment
Run the virtualenv command to create a virtual environment wherever you keep your virtual environments:

Be sure to use python3
```
virtualenv --python=python3 motoPi_venv
```

Activate the virtual environment with `source motoPi_venv/bin/activate`

### Installing dependencies
From the project root, run:
```
pip install -r requirements/requirements.txt
```

If you encounter the error: `include python.h compilation terminated` error, then run

```
sudo apt-get install python3-dev
```