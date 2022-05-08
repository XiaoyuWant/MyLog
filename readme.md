## Introduction
Send logs to a server with `POST` method.

Situation: Log training results and show on iOS Scriptable widget.

## Install
```
pip install .
```

## Configuration
### 1. Server
Using `Flask` as backend of the server for receiving messages and showing messages.

To activate server: 
```
python logServer.py
```
### 2. iOS widget
import `LogWidget.js` to Scriptable app, and change `URL` to your server's GET address url.
## Usage on Python codes
```python
import MyLog
logger=MyLog.Logger(url="http://H_O_S_T/send")

logger.log("hello world!")
```
