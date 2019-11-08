import json
import os
from urllib.request import urlopen
import matplotlib.pyplot as plt

x=input("enter the city name")
apikey="36e3a13f50023446732adf2f0eea6903"
url="http://api.openweathermap.org/data/2.5/forecast?q="+x+"&APPID="+apikey

with urlopen(url) as response:
    source=response.read()
tpoint=[]       #temperature value to be ploted
dpoint=[]       #date and time against the temperature point
data=json.loads(source)
#print(json.dumps(data,indent=2))
print("date and time","\t","\t",'temperature')
for mval in data['list']:
    print(mval['dt_txt'],"\t",mval['main']['temp'])
    tpoint.append(float(mval['main']['temp']))
    dpoint.append(mval['dt_txt'])


xline=np.linspace(0,40,40)

plt.figure(figsize=(15,15))
plt.xlabel("dates",fontsize=20)
plt.ylabel("temeprature",fontsize=20)
plt.title("temperature graph of "+x ,fontsize=20)

plt.xticks(xline,dpoint)

plt.xticks(rotation=60)

plt.plot(xline,tpoint,'ro-')
name=x+"figure.png"
#plt.savefig(name)

plt.show()

