def runge_rule(i_h, i_h_div_2, k):
    d = (abs(i_h_div_2-i_h))/(2**k - 1)
    print("Runge rule says: I - I_{h/2} = ", d)
    return
