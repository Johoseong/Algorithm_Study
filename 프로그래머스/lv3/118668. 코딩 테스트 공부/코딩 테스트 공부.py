def solution(alp, cop, problems):
    alp_max, cop_max = alp, cop
    for p in problems:
        alp_max = max(alp_max, p[0])
        cop_max = max(cop_max, p[1])

    dp = [[10 ** 10] * (cop_max + 1) for _ in range(alp_max + 1)]
    dp[alp][cop] = 0


    for a in range(alp, alp_max + 1):
        for c in range(cop, cop_max + 1):
            if a < alp_max: dp[a + 1][c] = min(dp[a][c] + 1, dp[a + 1][c])
            if c < cop_max: dp[a][c + 1] = min(dp[a][c] + 1, dp[a][c + 1])

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a < alp_req or c < cop_req: continue
                alp_next = min(alp_max, a + alp_rwd)
                cop_next = min(cop_max, c + cop_rwd)
                dp[alp_next][cop_next] = min(dp[a][c] + cost, dp[alp_next][cop_next])

    
    return dp[alp_max][cop_max]