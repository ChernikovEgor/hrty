from datetime import datetime


nowYear = datetime.now().year
oldYear = 1900
rng = nowYear - oldYear
for i in range(rng+1):
    print(oldYear + i)