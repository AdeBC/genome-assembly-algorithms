"""
1.2 The String Reconstruction Problem
2 out of 10 steps passed
0 out of 5 points  received
Code Challenge: Solve the String Composition Problem.
     Input: An integer k and a string Text.
     Output: Compositionk(Text) (the k-mers can be provided in any order).
"""


def k_mers(input_text):
    k = int(input_text[0])
    print(k)
    seq = input_text[1]
    k_mers = [seq[i:i + k] for i in range(len(seq) - k)]
    print(k_mers)
    return '\r'.join(k_mers)


def construct_string(input_text):
    k_mers = input_text
    n = len(k_mers)
    k = len(k_mers[0])
    seq = k_mers[0]
    for k_mer in k_mers[1:]:
        tail = seq[len(seq) - k + 1:len(seq)]
        head = k_mer[0:k - 1]
        if tail == head:
            seq += k_mer[-1]
    print(n + k - 1)
    print(len(seq))
    assert n + k - 1 == len(seq)
    return seq