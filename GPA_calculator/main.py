from data import main_score, all_weight, not_main_score, expected_score


def cal_single_gpa(x, mode):
    if mode == 1:
        return 4 - 3 * (100 - x) * (100 - x) / 1600
    else:
        if x == 90:
            return 4
        elif x == 80:
            return 3.5
        else:
            print("error!")
            return 0


def get_add_gpa():
    return 0.174 * 0.2 + (0.0232 + 0.0087 * 2) * 0.2 + 0.0696 * 0.5


if __name__ == '__main__':
    all_gpa_score = 0
    all_point = 0
    mode = 1
    all_score = dict(list(main_score.items()) + list(not_main_score.items()))

    for name, score in main_score.items():
        if "博雅" in name:
            mode = 2
        else:
            mode = 1
        weight = all_weight[name]
        single_gpa = cal_single_gpa(score, mode)
        all_gpa_score += single_gpa * weight
        all_point += weight

    gpa = all_gpa_score / all_point + get_add_gpa()
    print(gpa)
