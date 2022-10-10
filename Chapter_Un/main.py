import re
import long_responses as long 

def message_probability(user_message, recognised_words, single_response=False, required_words=[]) :
    message_certainty = 0
    has_necessary_words = True

    #Counts how many acceptable words are present in each message
    for word in user_message :
        if word in recognised_words :
            message_certainty += 1

    #Get the percentage of acceptable words
    the_value = float(message_certainty) / float(len(recognised_words))

    #Checks if acceptable words are in the string
    for word in user_message :
        if word not in user_message :
            has_necessary_words = False
            break
    
    if required_words or single_response :
        return int(message_certainty*100)
    else :
        return 0

def check_all_messages(message) :
    highest_prob_list = {}

    def response(bot_response, list_of_words, single_response=False, required_words=[]) :
        nonlocal highest_prob_list
        highest_prob_list[bot_response] = message_probability(message, list_of_words, single_response, required_words)

    #responses -------------------
    response('Hello!', ['Hello', 'hi', 'sup', 'heya', 'heyo' 'hey'], single_response=True)
    response('I\'m doing fine, what do you need?', ['How', 'Are', 'you', 'doing'], required_words=['how'])

    best_match = max(highest_prob_list, key=highest_prob_list.get)
    print(highest_prob_list)

    return long.unknown() if highest_prob_list[best_match] < 1 else best_match


def get_responses(user_input):
    split_message = re.split(r'\s+|[,;?!.-]\s*', user_input.lower())
    answer = check_all_messages(split_message)
    return answer

#Testing of the reply
while True :
    print('Bot : ' + get_responses(input("you : ")))