class CurrentEventData:
    def __init__(self, answer):
        self.word_is_unsecreted = False
        self.game_is_going = True
        self.answer = answer
        self.count_strings = 0
        self.last_words = []
        self.current_word = []
