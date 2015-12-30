import numpy

class Carnival_bot:
    def __init__(self,corpus,max_message_length = 10):
        self.corpus = corpus
        self.max_message_length = max_message_length
        
    def compose_message(self,seed):
        cur_word = seed
        cur_message = [seed]
        for i in range(max_message_length-1):
            next_word = corpus.get_random_next(cur_word)
            cur_message.append(next_word)
            cur_word = next_word

        return " ".join(cur_message)


        


