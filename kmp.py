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
            prefix_func[second_symbol_iterator] = 0
            second_symbol_iterator += 1

    return prefix_func


def kmp(text: str, pattern: str):
    pattern_len = len(pattern)
    text_len = len(text)
    matches = []

    if (text_len <= 0) or (pattern_len > text_len):
        return matches

    text_iterator = 0
    pattern_iterator = 0
    prefix_func = get_prefix_func(pattern)

    while text_iterator < text_len and pattern_iterator < pattern_len:

        # if match - we increment iterators for next checks
        if text[text_iterator] == pattern[pattern_iterator]:
            pattern_iterator += 1
            text_iterator += 1

        # if pattern_iterator == pattern_len (yes, it is possible, because we have incremented it before)
        # then we have found a match
        if pattern_iterator == pattern_len:
            matches.append((text_iterator - pattern_len, text_iterator - 1))
            pattern_iterator = prefix_func[pattern_iterator - 1]

        # if mismatch and we are not out of text_len range
        # then we have two cases
        elif text[text_iterator] != pattern[pattern_iterator] and text_iterator < text_len:

            # if we received a mismatch at once
            # then increment text_iterator, to check next symbol of text with first symbol of pattern
            if pattern_iterator == 0:
                text_iterator += 1

            # if we had matches before, but now received a mismatch
            # then we start comparing a text starting from prefix_func[pattern_iterator - 1],
            # because we had a match before
            else:
                pattern_iterator = prefix_func[pattern_iterator - 1]

    return matches
