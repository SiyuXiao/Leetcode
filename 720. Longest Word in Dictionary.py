#这哥们的算法感觉很巧妙
def longestWord(words):
    words.sort()
    words_set, longest_word = set(['']), ''
    for word in words:
        if word[:-1] in words_set:
            words_set.add(word)
            if len(word) > len(longest_word):
                longest_word = word
    return longest_word
result = longestWord(["a", "banana", "app", "appl", "ap", "apply", "apple"])
print(result)