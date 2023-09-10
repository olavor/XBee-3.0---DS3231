from datetime import datetime, timedelta
three_hours = timedelta(hours=3)
import json,csv,time,requests
from datetime import datetime
import pandas as pd 
credenciais = ('X', 'Y')
values = [] ;timestamps = [];luz = [];bat = [];start_time = time.time()
responses = [requests.get(f"http://developer.idigi.com/ws/v1/streams/history/00000000-00000000-0004F3FF-FF182C15/corrente/[00:13:A2:00:42:11:B3:AB]!/current?start_time=2023-09-04T{str(i).zfill(2)}:00:00.000%2D03:00&end_time=2023-09-04T{str(i+1).zfill(2)}:00:00.000%2D03:00", auth=credenciais) for i in range(4, 18)]
data = [response.json()['list'] for response in responses]
values.extend([item['value'] for sublist in data for item in sublist]) 
timestamps.extend([item['timestamp'] for sublist in data for item in sublist]) 
responses = [requests.get(f"http://developer.idigi.com/ws/v1/streams/history/00000000-00000000-0004F3FF-FF182C15/solar/[00:13:A2:00:42:11:B3:AB]!/iluminacao?start_time=2023-09-04T{str(i).zfill(2)}:00:00.000%2D03:00&end_time=2023-09-04T{str(i+1).zfill(2)}:00:00.000%2D03:00", auth=credenciais) for i in range(4, 18)]
data = [response.json()['list'] for response in responses]
luz.extend([item['value'] for sublist in data for item in sublist]) 
responses = [requests.get(f"http://developer.idigi.com/ws/v1/streams/history/00000000-00000000-0004F3FF-FF182C15/bateria/[00:13:A2:00:42:11:B3:AB]!/batery?start_time=2023-09-04T{str(i).zfill(2)}:00:00.000%2D03:00&end_time=2023-09-04T{str(i+1).zfill(2)}:00:00.000%2D03:00", auth=credenciais) for i in range(4, 18)]
data = [response.json()['list'] for response in responses]
bat.extend([item['value'] for sublist in data for item in sublist])
timestamps = [datetime.strptime(ts, "%Y-%m-%dT%H:%M:%S.%fZ") for ts in timestamps] 
timestamps = [ts - three_hours for ts in timestamps]
timestamps = [ts.strftime("%d.%m.%Y %H:%M:%S") for ts in timestamps] 
df = pd.DataFrame({"timestamp": timestamps, "value": values, "luz": luz, "bat":bat})
df.to_csv("foo.csv", index=False)        
end_time = time.time()
print(f"O tempo final de compilação foi de {end_time - start_time} segundos.") 
