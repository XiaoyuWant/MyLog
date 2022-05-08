import requests


class Logger(object): 
    # url means server ip:port/method
    def __init__(self,url,logFileName="mylog.txt"):
        self.url=url
        self.logFileName=logFileName

    def log(self,msg):
        url=self.url
        file=self.logFileName
        data = {
            "msg": msg 
        }
        with open(file,"a") as f:
            f.write(msg+"\n")
            
        try:
            r=requests.post(url=url,data=data)
            print(r)
        except:
            return