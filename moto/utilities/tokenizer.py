class GenericTokenizer:
    """
    Tokenizer for a KeyConditionExpression. Should be used as an iterator.
    The final character to be returned will be an empty string, to notify the caller that we've reached the end.
    """

    def __init__(self, expression):
        self.expression = expression
        self.token_pos = 0

    def __iter__(self):
        return self

    def is_eof(self):
        return self.peek() == ""

    def peek(self, length=1):
        """
        Peek the next character without changing the position
        """
        try:
            return self.expression[self.token_pos : self.token_pos + length]
        except IndexError:
            return ""

    def __next__(self):
        """
        Returns the next character, or an empty string if we've reached the end of the string.
        Calling this method again will result in a StopIterator
        """
        try:
            result = self.expression[self.token_pos]
            self.token_pos += 1
            return result
        except IndexError:
            if self.token_pos == len(self.expression):
                self.token_pos += 1
                return ""
            raise StopIteration

    def skip_characters(self, phrase, case_sensitive=False) -> None:
        """
        Skip the characters in the supplied phrase.
        If any other character is encountered instead, this will fail.
        If we've already reached the end of the iterator, this will fail.
        """
        for ch in phrase:
            if case_sensitive:
                assert self.expression[self.token_pos] == ch
            else:
                assert self.expression[self.token_pos] in [ch.lower(), ch.upper()]
            self.token_pos += 1

    def skip_white_space(self):
        """
        Skip any whitespace characters that are coming up
        """
        try:
            while self.peek() == " ":
                self.token_pos += 1
        except IndexError:
            pass
