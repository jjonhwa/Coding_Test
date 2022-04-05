import pandas as pd

def solution(info, query):
    answer = []
    
    lang_list = []
    stack_list = []
    career_list = []
    food_list = []
    score_list = []
    for inf in info :
        lang, stack, career, food, score = inf.split(' ')
        score = int(score)
        lang_list.append(lang)
        stack_list.append(stack)
        career_list.append(career)
        food_list.append(food)
        score_list.append(score)
        
    info_df = pd.DataFrame(data = {'언어' : lang_list,
                              '스택' : stack_list,
                              '경력' : career_list,
                              '소울푸드' : food_list,
                              '점수' : score_list})
    
    for q in query :
        lang, stack, career, food_score = q.split('and')
        lang = lang.strip()
        stack = stack.strip()
        career = career.strip()
        food_score = food_score.strip()
        food = food_score.split(' ')[0]
        score = int(food_score.split(' ')[1])
        
        new_df = info_df[info_df['점수'] >= score]

        if lang == '-' :
            pass
        else :
            new_df = new_df[new_df['언어'] == lang]

        if stack == '-' :
            pass
        else :
            new_df = new_df[new_df['스택'] == stack]

        if career == '-' :
            pass
        else :
            new_df = new_df[new_df['경력'] == career]

        if food == '-' :
            pass
        else :
            new_df = new_df[new_df['소울푸드'] == food]

        answer.append(len(new_df))  
    return answer
