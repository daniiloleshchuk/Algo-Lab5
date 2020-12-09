def get_prefix_func(pattern: str):
    string_len = len(pattern)
    prefix_func = [0 for _ in range(string_len)]
    first_symbol_iterator = 0
    second_symbol_iterator = 1

    while second_symbol_iterator < string_len:

        if pattern[first_symbol_iterator] == pattern[second_symbol_iterator]:
            prefix_func[second_symbol_iterator] = first_symbol_iterator + 1
            first_symbol_iterator += 1
            second_symbol_iterator += 1

        elif first_symbol_iterator > 0:
            first_symbol_iterator = prefix_func[first_symbol_iterator - 1]

        else:  # first_symbol_iterator == 0
            second_symbol_iterator += 1

    return prefix_func


def kmp(text: str, pattern: str):
    pattern_len = len(pattern)
    text_len = len(text)
    matches = []
    text_iterator = 0
    pattern_iterator = 0

    if (text_len <= 0) or (pattern_len > text_len):
        return matches

    prefix_func = get_prefix_func(pattern)

    while text_iterator < text_len and pattern_iterator < pattern_len:

        if text[text_iterator] == pattern[pattern_iterator]:

            # if symbols are equal and pattern iterator equal len of pattern-1 (iterator started from 0)
            # then we have found a match
            if pattern_iterator == pattern_len - 1:
                matches.append((text_iterator - pattern_len + 1, text_iterator))
                pattern_iterator = 0

            # if symbols are equal but pattern iterator not equal len of pattern-1
            # the we increment iterators and check again
            else:
                pattern_iterator += 1

            text_iterator += 1

        # if symbols are not equal at the very start (start of pattern),
        # then we have to increment text_iterator and check again
        elif pattern_iterator == 0:
            text_iterator += 1

        # if till now symbols were equal, but now they are not,
        # then we have to move our "prefix" to point were we had "suffix" till now
        else:
            pattern_iterator = prefix_func[pattern_iterator - 1]

    return matches
