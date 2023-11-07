#!/usr/bin/python3
def multiple_returns(sentence):
    if isinstance(sentence, str):
        count = len(sentence)
        l_sentence = list(sentence)
        if len(l_sentence) >= 1:
            res_tuple = (count, l_sentence[0])
        else:
            res_tuple = (count, None)

        return res_tuple
