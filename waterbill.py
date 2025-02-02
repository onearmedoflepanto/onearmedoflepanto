T_input = int(input())

for T in range(1,T_input+1):
    case1_perliter, case2_base, case2_baselimit, case2_perliter, myliter=map(int, input().split())

    case1_total=myliter*case1_perliter

    case2_total=case2_base

    if case2_base+case2_perliter*(myliter-case2_baselimit) < case2_base:
        case2_total=case2_base
    else:
        case2_total=case2_base+case2_perliter*(myliter-case2_baselimit)

    print(f"#{T} {min(case1_total, case2_total)}")