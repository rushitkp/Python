import os
# if(not os.path.exists("data")):
#     os.mkdir("Data")
    
for i in range(0,100):
    # os.mkdir(f"Data/Day{i+1}")    
    os.rename(f"Data/Tutorial{i+1}",f"Data/Tutorial{i+1}")    
