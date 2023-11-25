def solution(a, b, c, d):
    # 각 등장 숫자 세기
    dice = [a, b, c, d]
    counts = [dice.count(i) for i in dice]
    
    # 같은 수 4개
    if max(counts) == 4:
        return 1111 * a
    
    # 같은 수 3개
    elif max(counts) == 3:
        return (10 * dice[counts.index(3)] + dice[counts.index(1)]) ** 2
    
    # 같은 수 2개
    elif max(counts) == 2:
        # 2개 2개
        if min(counts) == 2:
            # a = b, c = d
            if a == b:
                return (a + c) * abs(a - c)
            else:
                return (a + b) * abs(a - b)
        # 2개 1개 1개
        else:
            return (a * b * c * d) / (dice[counts.index(2)] ** 2)
        
    # 다 다름
    else:
        return min(dice)
