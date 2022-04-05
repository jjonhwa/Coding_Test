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

# 시간초과
import pandas as pd

def solution(info, query):
    answer = []
    
    dataframe = pd.DataFrame()
    languages, stacks, careers, foods, scores = [], [], [], [], []
    for information in info: # O(50000)
        language, stack, career, food, score = information.split()
        languages.append(language)
        stacks.append(stack)
        careers.append(career)
        foods.append(food)
        scores.append(int(score))
        
    dataframe['언어'] = languages
    dataframe['직군'] = stacks
    dataframe['경력'] = careers
    dataframe['푸드'] = foods
    dataframe['점수'] = scores
    
    for q in query: # O(100000)
        language, stack, career, food_score = q.split('and')
        food, score = food_score.split()
        
        if language.strip() == '-': language = ''
        if stack.strip() == '-': stack = ''
        if career.strip() == '-': career = ''
        if food.strip() == '-': food = ''
        if score.strip() == '-': score = ''

        d_l = dataframe[dataframe['언어'] == language.strip()] if language else dataframe
        d_s = d_l[d_l['직군'] == stack.strip()] if stack else d_l
        d_c = d_s[d_s['경력'] == career.strip()] if career else d_s
        d_f = d_c[d_c['푸드'] == food.strip()] if food else d_c
        d_ss = d_f[d_f['점수'] >= int(score.strip())] if score else d_f
        answer.append(len(d_ss))
    return answer

# 시간초과
from itertools import product, combinations
import numpy as np

def solution(info, query):
    answer = []
    
    languages = ['cpp', 'java', 'python']
    stacks = ['backend', 'frontend']
    careers = ['junior', 'senior']
    foods = ['chicken', 'pizza']

    combination_dict = {'empty': []}
    for prod in list(product(languages, stacks, careers, foods)):
        for i in range(1, 5):
            for comb in combinations(prod, i):
                combination_dict[comb] = []

    for information in info:
        language, stack, career, food, score = information.split()
        combination_dict['empty'].append(score)
        for i in range(1, 5):
            for comb in combinations([language, stack, career, food], i):
                combination_dict[comb].append(score)

    for q in query:
        language, stack, career, food_score = q.split(' and ')
        food, score = food_score.split()

        name = []
        if language != '-': name.append(language)
        if stack != '-': name.append(stack)
        if career != '-': name.append(career)
        if food != '-': name.append(food)
        name = tuple(name)

        if not name:
            name = 'empty'

        check_score = combination_dict[name]

        check_score = combination_dict[name]
        check_score = list(map(int, check_score))
        check_score = np.array(check_score)
        count = len(check_score[check_score >= int(score)])

        answer.append(count)
        
        # count = 0
        # cnt = [1 if int(s) >= int(score) else 0 for s in check_score ]
        # answer.append(sum(cnt))
        # for s in check_score:
        #     if int(s) >= int(score):
        #         count += 1
        # answer.append(count)
    return answer
