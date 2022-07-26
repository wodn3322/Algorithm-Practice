import sys

if __name__ == '__main__':

    test_room=int(input())
    room_person =list(map(int,input().split(" ")))
    oversee_list =list(map(int,input().split(" ")))
    stack_map={}
    sum=0;

    for i in room_person:
        count = 0;
        temp=i
        if i in stack_map:
            sum+=stack_map[i]
            continue
        while i>0 :
            if count==0:
                i=i-oversee_list[0]
                count+=1
            else:
                i=i-oversee_list[1]
                count+=1
        stack_map[temp]=count
        sum+=count

    print(sum)

    # count = int(input())
    # for i in range(count):
    #     string=""
    #     for j in range(count):
    #         if count-1-i>j:
    #             string+=" "
    #         else:
    #             string+="*"
    #     print(string)

    # count=int(input())
    # answer_list=[]
    # for i in range(0,count):
    #     input_arr = list(map(int, sys.stdin.readline().rstrip().split(" ")))
    #     print(sum(input_arr))
    #     answer_list.append([input_arr[0],input_arr[1],input_arr[0]+input_arr[1]])
    # for i in range(0,count):
    #     print("Case #"+str(i+1)+":",answer_list[i][0],"+",answer_list[i][1],"=",answer_list[i][2])


    # first=int(input())
    # second=int(input())
    # hundred=second//100
    # ten=(second%100)//10
    # one=second%10
    # print(first*one)
    # print(first*ten)
    # print(first*hundred)
    # print(first*second)

    # input_arr=list(map(int,input().split(" ")))
    # print((input_arr[0]+input_arr[1])%input_arr[2])
    # print(((input_arr[0]%input_arr[2])+(input_arr[1]%input_arr[2]))%input_arr[2])
    # print((input_arr[0]*input_arr[1])%input_arr[2])
    # print(((input_arr[0]%input_arr[2])*(input_arr[1]%input_arr[2]))%input_arr[2])


    # input_list =list(map(int,input().split(" ")))
    # for i