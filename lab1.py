sample = [585, 136, 578, 619, 133, 740, 1665, 1729,
          930, 1027, 862, 669, 700, 419, 182, 111,
          417, 99, 365, 337, 1909, 1655, 3424, 139,
          3217, 528, 125, 1, 1398, 237, 132, 1852,
          2258, 12, 292, 158, 986, 1675, 1299, 661,
          936, 1888, 657, 321, 287, 845, 2181, 118,
          1633, 870, 1082, 187, 2351, 3622, 288,
          1119, 1187, 928, 367, 66, 359, 960, 53, 271,
          3257, 514, 716, 2051, 1273, 75, 878, 539,
          1147, 294, 751, 1108, 3843, 2513, 495,
          1346, 718, 428, 1180, 748, 134, 1575, 750,
          1367, 1278, 1417, 301, 89, 387, 276, 199,
          37, 256, 1918, 1063, 1448]

y = 0.63
t_probability = 1473
t_intensity = 3335

sample.sort()
n = len(sample)
Tcp = sum(sample) / len(sample)
print("Average value: ", Tcp)

k = 10
h = (sample[-1] - 0) / k

intervals = []
for _ in range(1, k + 1):
    intervals.append(round(_ * h, 1))
# print("Intervals= ", intervals)

Ni = [0] * 10
for i in range(len(sample)):
    for j in range(len(intervals)):
        if intervals[j] >= sample[i]:
            Ni[j] += 1
            continue
N = [Ni[0]]
for i in range(1, len(Ni)):
    N.append(Ni[i] - Ni[i - 1])

f = []
for _ in range(len(intervals)):
    f.append(round(N[_] / (h * n), 6))

# print("f(i)= ", f)

P = [0 for _ in range(k)]
for i in range(k):
    square = 0
    for j in range(i + 1):
        square += (f[j] * h)
    P[i] = round(1 - square, 5)
# print("P(t)= ", P, "\n")

d_01 = round((P[0] - y) / (P[0] - 1), 2)
T_y = round(h - h * d_01, 2)
print("Tγ= ", T_y)


def probability_for_time(time, frequency_arr, intervals):
    number_of_interval = 1
    for i in range(k):
        if intervals[i] <= time <= intervals[i + 1]:
            number_of_interval = i
            break
    square = 0
    for i in range(number_of_interval + 1):
        if i != number_of_interval:
            square += (frequency_arr[i] * h)
        else:
            square += (frequency_arr[i] * (time - intervals[i]))
    p = round(1 - square, 4)
    return p


intervals.insert(0, 0)
pr_tr_op = probability_for_time(t_probability, f, intervals)
print("P= ", round(pr_tr_op, 4))

number_of_interval = 1
for i in range(k):
    if intervals[i] <= t_intensity <= intervals[i + 1]:
        number_of_interval = i
        break
p = probability_for_time(t_intensity, f, intervals)
fail_rate = round(f[number_of_interval] / p, 4)
print("λ= ", fail_rate)
