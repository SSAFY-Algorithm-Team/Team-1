def solution(data, ext, val_ext, sort_by):
    answer = []

    if ext == "code":
        index = 0
    elif ext == "date":
        index = 1
    elif ext == "maximum":
        index = 2
    elif ext == "remain":
        index = 3

    if sort_by == "code":
        sort_index = 0
    elif sort_by == "date":
        sort_index = 1
    elif sort_by == "maximum":
        sort_index = 2
    elif sort_by == "remain":
        sort_index = 3

    for i in range(len(data)):
        if data[i][index] < val_ext:
            answer.append(data[i])

    answer = sorted(answer, key=lambda x: x[sort_index])

    return answer