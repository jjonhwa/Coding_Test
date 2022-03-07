# 내 풀이
# 속도: 상위 65% / 메모리: 상위 40% 
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # seperate digit logs & letter logs
        string_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                string_logs.append(log)
                
        # sort letter logs
        sorted_string_logs = []
        for string in string_logs:
            string = string.split()
            sorted_string_logs.append((string[0], ' '.join(string[1:])))
        
        sorted_string_logs.sort(key = lambda x: (x[1], x[0]))
        
        # answer
        answer = []
        for letter_log in sorted_string_logs:
            answer.append(' '.join(letter_log))
        
        for digit_log in digit_logs:
            answer.append(digit_log)
        
        return answer
      
# 정답
# 속도: 상위 5% / 메모리: 상위 40%
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        
        # seperate digit logs & letter logs
        string_logs = []
        digit_logs = []
        for log in logs:
            if log.split()[1].isdigit():
                digit_logs.append(log)
            else:
                string_logs.append(log)
                
        # sort letter logs
        string_logs.sort(key = lambda x: (x.split()[1:], x.split()[0]))
        
        return string_logs + digit_logs
        
