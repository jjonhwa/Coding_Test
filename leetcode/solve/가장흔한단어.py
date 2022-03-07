# 내 풀이
# 속도: 하위 10% / 메모리: 하위 35%
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # make lower
        paragraph = paragraph.lower()
        
        # make word list
        paragraph = [word for word in paragraph.split(',')]
        
        w_1 = []
        for words in paragraph:
            w_1 += words.split()
        
        w_2 = []
        for words in w_1:
            w_2 += words.split('.')
            
        # remove special string
        word_list = []
        for word in w_2:
            word = re.sub('[^a-z]', '', word)
            if word:
                word_list.append(word)
                
        # count word
        counter = collections.Counter(word_list)
        counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)

        # print most counter word which isn't included in banned list 
        for key, values in counter:
            if key not in banned:
                return key
            
# 정규표현식 힌트 본 후 풀이
# 속도: 상위 20% / 메모리: 상위 60%
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # make lower
        paragraph = paragraph.lower()
        
        # remove special string
        paragraph = re.sub('[^\w]', ' ', paragraph)
        
        # make word list
        paragraph = [word for word in paragraph.split()]
        
        # count word
        counter = collections.Counter(paragraph)
        counter = sorted(counter.items(), key = lambda x: x[1], reverse=True)

        # print most counter word which isn't included in banned list 
        for key, values in counter:
            if key not in banned:
                return key
            
        
# 정답 풀이
# 속도: 하위 15% / 메모리: 상위 60%
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        
        # make lower
        paragraph = paragraph.lower()
        
        # remove special string
        paragraph = re.sub('[^\w]', ' ', paragraph)
        
        # make word list
        paragraph = [word for word in paragraph.split() if word not in banned]
        
        # count word
        counter = collections.Counter(paragraph)
        
        return counter.most_common(1)[0][0]
            
        
        
        
