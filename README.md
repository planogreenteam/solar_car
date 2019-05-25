# Local Program Testing
Use the socat command to create two virtual ports to facilitate communication:

```
socat -d -d PTY,raw,echo=0,link=/tmp/vmodem0 PTY,raw,echo=0,link=/tmp/vmodem1
```.

Now `/tmp/vmodem0` and `/tmp/vmodem1` have been established. Expected response should be similar to:

```
socat[939] N PTY is /dev/pts/4
socat[939] N PTY is /dev/pts/5
11:13:26 socat[939] N starting data transfer loop with FDs [5,5] and [7,7]
```

Create two new terminal windows. Connect vedirect.py to /tmp/vmodem1 and vedirectsim.py to /tmp/vmodem0 or use a live recording from test/mppt.dump. Note that these programs are written for Python 2. Also realize that the simulator passes in static data; see code for details.
Commands to run programs are:

```python
python vedirect.py --port /tmp/vmodem1
python vedirectsim.py --port /tmp/vmodem0
```

If you wish to use a dump file, the latter command should be changed to

```
cat test/mppt.dump > /dev/vmodem0
```.

# Run with MPPT Charge Controller

Here no socat command is needed. Hardwire the pi to the MPPT via USB connection. Create an SSH tunnel to the computer to work with the pi (use `ssh pi@<IP>`). Find the desired USB port with the command
`ls /dev/tty* `. Expected port should be similar to `/dev/ttyUSB0`. Now run the program directly into this port:

```python
python vedirect.py --port /dev/ttyUSB0
```.

