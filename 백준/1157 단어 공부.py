from collections import Counter

### 코드 설명
'''
1. 입력으로 주어지는 문자열을 알파벳으로 슬라이싱하여 'words' 리스트에 저장
2. 'words' 리스트에 저장된 알파벳 각각의 개수를 세어 저장 (1단계에서는 with_count, 2단계에서는 alphabet_with_count)
3. 가장 높은 등장 횟수가 얼마인지 확인하여 (max_count/max_cnt)에 저장 
4. with_count / alphabet_with_count를 하나씩 순회하면서 가장 높은 등장 횟수가 2개 이상인지 확인함
5. 가장 높은 등장 횟수가 2개 이상일 경우 ?를, 아닐 경우, with_count / alphabet_with_count 를 등장 횟수 기준으로 정렬하여 가장 앞쪽에 위치한 알파벳을 출력

'''

## 첫번째 시도
# words = [w for w in input().upper()]
# set_words = set(words)
#
# with_count = []
# for word in set_words:
#     with_count.append((word, words.count(str(word))))
#
# max_count = max([word[1]for word in with_count])
#
# cnt = 0
# for word in with_count:
#     if word[1] == max_count:
#         cnt +=1
#
# if cnt > 1:
#     print('?')
# else:
#     print(sorted(with_count, key=lambda x: x[1], reverse=True)[0][0])


## 2번째: 디버깅하면서 코드 깔끔하게 수정하기
words = [w for w in input().upper()]
alphabet_with_count = sorted(Counter(words).items(), key=lambda x:x[1], reverse=True)
# Counter(words) --> dictionary {key: list의 각각의 요소들, value: list 각각 요소들의 개수}
# Counter(list).items() --> [(list[0], count(list[0])), (), () ...] --> 리스트 안에 튜플 형태

max_cnt = max([alphabet[1] for alphabet in alphabet_with_count])
if len([i for i in alphabet_with_count if i[1] == max_cnt]) > 1:
    print('?')
else:
    print(alphabet_with_count[0][0])
