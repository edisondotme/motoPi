Collection of personal notes for this project.

## Starting up
- Run `source ~/.bashrc` to get syntaxt highlighting upon sshing into the pi.
- Run `source ~/.myenvs/django/bin/activate` to activate the virtualenv for django


## Running the development server
### Starting the server

```
python ~/motoPi/manage.py runserver 0.0.0.0:8000
```

### Simulating hardware activity with the sensor worker
```
python ~/motoPi/manage.py readSensor
```

The readSensor command shows up in `python manage.py help` because it is placed in a sub folder of an app `appName/management/commands/`

In the readSensor case, it is `sensorWorker/management/commands/readSensor.py`

## Miscellany

#### Changing filepermissions

For some reason, files created with touch do not have editing permissions. Use `chmod 777 fileName.py` to change the permissions.

#### SMB share
The development raspberry pi serves files via smb so that I can edit them in sublime on my home desktop computer.
There are files that designate the SMB shares somewhere...

