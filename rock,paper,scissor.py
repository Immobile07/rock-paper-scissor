import random
import sys
point_pc=0
point_user=0
user_name=input("Enter your name:")
while True:
    user_=input("rock,paper,scissor or press F to exit:")
    pc_=random.randint(1,3)
    if(pc_==1):
        pc_='rock'
    elif(pc_==2):
        pc_='paper'
    else:
        pc_='scissor'
    
    if(user_=='F' or user_=='f'):
        break
    elif(user_=='rock' and pc_=='scissor'):
        point_user+=1
        print(f"{user_name} wins this round")
        print("points of pc:",point_pc)
        print(f"points of {user_name}:",point_user)
    elif (user_=='rock' and pc_=='paper'):
        point_pc+=1
        print('pc wins this round')
        print("points of pc:",point_pc)
        print(f"points of {user_name}:",point_user)
    elif(user_=='paper' and pc_=='rock'):
        point_user+=1
        print(f"{user_name} wins this round")
        print("points of pc:",point_pc)
        print(f"points of {user_name}:",point_user)
    elif(user_=='paper' and pc_=='scissor'):
        
        point_pc+=1
        print('pc wins this round')
        print("points of pc:",point_pc)
        print(f"points of {user_name}:",point_user)
    elif (user_=='scissor' and pc_=='paper'):
        point_user+=1
        print(f"{user_name} wins this round")
        print("points of pc:",point_pc)
        print(f"points of {user_name}:",point_user)
    elif (user_=='scissor' and pc_=='rock'):
        point_pc+=1
        print('pc wins this round')
        print("points of pc:",point_pc)
        print(f"points of {user_name}:",point_user)
    else: print('It\'s a draw')
if(point_pc>point_user):
    print("Winner is pc.")
elif(point_user>point_pc):
    print(f"Winner is {user_name}")
else:
    print('It\'s a draw')
sys.exit()