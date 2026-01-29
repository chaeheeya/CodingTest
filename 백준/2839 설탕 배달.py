'''
상근이는 요즘 설탕공장에서 설탕을 배달하고 있다. 상근이는 지금 사탕가게에 설탕을 정확하게 N킬로그램을 배달해야 한다.
설탕공장에서 만드는 설탕은 봉지에 담겨져 있다. 봉지는 3킬로그램 봉지와 5킬로그램 봉지가 있다.

상근이는 귀찮기 때문에, 최대한 적은 봉지를 들고 가려고 한다.
예를 들어, 18킬로그램 설탕을 배달해야 할 때, 3킬로그램 봉지 6개를 가져가도 되지만, 5킬로그램 3개와 3킬로그램 1개를 배달하면, 더 적은 개수의 봉지를 배달할 수 있다.

상근이가 설탕을 정확하게 N킬로그램 배달해야 할 때, 봉지 몇 개를 가져가면 되는지 그 수를 구하는 프로그램을 작성하시오.

[입력]
첫째 줄에 N이 주어진다. (3 <= N <= 5000)

[출력]
상근이가 배달하는 봉지의 최소 개수를 출력한다. 만약, 정확하게 N킬로그램을 만들 수 없다면 -1을 출력한다.
'''

# N = int(input())
N = 17

max_5 = N // 5
remain_5 = N - (max_5 *5)
# print("최대로 가능한 5개: ",max_5, "나머지: ", remain_5)

if remain_5 == 0: # 5kg으로 모두 해결 가능한 경우
    print(max_5)
elif max_5 == 0: # 5보다 숫자가 작은 경우
    count_3 = N // 3
    remain_3 = N - (count_3 * 3)
    if remain_3 != 0:
        print(-1)
    else:
        print(count_3)
else:
    is_success = False
    for i in range(max_5, -1, -1):
        # print(i)
        count_3 = (N-(i*5)) // 3
        # print(count_3)
        remain = N - (i*5) - (count_3 * 3)
        # print("5개: ", i, "3개: ", count_3, "remain: ", remain)
        # print('------------------------------------')
        if remain == 0:
            is_success = True
            print(i+count_3)
            break
    if is_success == False:
        print(-1)




for i in range(max_5, -1, -1):
    count_5 = i
    remain_5 = N - (i*5)

    if remain_5 == 0:
        print(count_5)
        break
    else:
        count_3 = remain_5 // 3
        remain_3 = remain_5 = (count_3 * 3)
        if remain_3 == 0:
            print(count_3 + count_5)
        else:
            print(-1)
