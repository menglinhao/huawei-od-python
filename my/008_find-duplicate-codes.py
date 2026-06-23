
def solve(text1: str, text2: str):
    if not (text1 and text2):
        return ''
    n, m = len(text1), len(text2)
    # dp[i][j] = text1[:i] 与 text2[:j] 结尾的最长公共子串长度
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    max_len = 0
    end_pos = 0  # 最长子串在 text1 中的结束位置
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if text1[i - 1] == text2[j - 1]:
                # 从 dp[i-1][j-1]（左上角）继承：子串要求双方同步推进
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > max_len:
                    max_len = dp[i][j]
                    end_pos = i
    return text1[end_pos - max_len:end_pos]

if __name__ == '__main__':
    assert solve("hello123world", "hello123abc4") == "hello123"
    assert solve("private_void_method", "public_void_method") == "_void_method"
    assert solve("hiworld", "hiweb") == "hiw"

