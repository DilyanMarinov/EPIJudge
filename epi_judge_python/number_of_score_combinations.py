from test_framework import generic_test


def num_combinations_for_final_score(final_score, individual_play_scores):
    dp = [[0 if y > 0 else 1 for y in range(final_score + 1)] for x in range(len(individual_play_scores) + 1)]
    for i in range(1, len(individual_play_scores) + 1):
        for j in range(1, final_score + 1):
            cur = j - individual_play_scores[i - 1]
            dp[i][j] += dp[i - 1][j]
            if  cur >= 0:
                dp[i][j] += dp[i][cur]
    return dp[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_score_combinations.py",
                                       "number_of_score_combinations.tsv",
                                       num_combinations_for_final_score))
