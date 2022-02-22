from collections import deque
import sys
input = sys.stdin.readline

def index_check(spell: str):
    for i, li in enumerate(map):
        if spell in li:
            j = li.index(spell)
            break
    return [i, j]

left, right = map(str, input().split())
word = input().strip()
map = [['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
       ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
       ['z', 'x', 'c', 'v', 'b', 'n', 'm']]

vowel = ['b', 'n', 'm', 'h', 'j', 'k', 'l', 'y', 'u', 'i', 'o', 'p']
queue = deque(word)
time = 0
while queue:
    spell = queue.popleft()
    if spell in vowel:
        spell_index = index_check(spell)
        right_index = index_check(right)
        right_go = abs(right_index[0] - spell_index[0]) + abs(right_index[1] - spell_index[1])
        time += right_go + 1
        right = spell
    else:
        spell_index = index_check(spell)
        left_index = index_check(left)
        left_go = abs(left_index[0] - spell_index[0]) + abs(left_index[1] - spell_index[1])
        time += left_go + 1
        left = spell
print(time)