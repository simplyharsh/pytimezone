#pytimezone

Determine timezone from offset or lat/long

## Usage

```python
>>> from pytimezone import pytimezone
>>> pyt = pytimezone()
Reading json input file: /Users/Harsh/.Environments/pro/lib/python2.7/site-packages/pytimezone/tz_world_compact.json
>>> pyt.timezone_at(21.00000, 78.00000)
u'Asia/Kolkata'
>>> pyt.timezone_from_offset(300)
'Canada/Eastern'
>>>
```

## RPC

pytimezone is based on [https://github.com/mattbornski/tzwhere](tzwhere) module and imports timezone and location data from `tz_world_compact.json`. It makes sense to use it as separate process. I use it as RPC using Pyro4.

### Start the Pyro4 RPC Server

```bash
$ python tzlatlng/pyro_server.py

Reading json input file: /Users/Harsh/pytimezone/tz_world_compact.json
Ready. Object uri = PYRO:obj_ca05e9be8f84401ba093603e12c9b7dc@localhost:51098
```

### Connect pyro_server

```python
>>> import Pyro4
>>> pyt = Pyro4.Proxy('PYRO:obj_ca05e9be8f84401ba093603e12c9b7dc@localhost:51098')
>>> pyt.timezone_at(21.00000, 78.00000)
u'Asia/Kolkata'
>>> pyt.timezone_from_offset(300)
u'Canada/Eastern'
>>>
```
