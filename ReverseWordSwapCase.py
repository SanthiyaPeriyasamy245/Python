def reverse_words_order_and_swap_cases(sentence):
    # Step 1: Split the sentence into a list of words
    words = sentence.split()  # ['Hello', 'World']

    # Step 2: Reverse the list
    reversed_words = words[::-1]  # ['World', 'Hello']

    # Step 3: Join the words back into a string
    reversed_sentence = " ".join(reversed_words)  # 'World Hello'

    # Step 4: Swap the case of each letter
    result = reversed_sentence.swapcase()  # 'wORLD hELLO'

    return result
