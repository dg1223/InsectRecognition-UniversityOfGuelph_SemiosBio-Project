## Training Set: Run 2

In [4]: len(img_list)
Out[4]: 129

In [5]: all_match
Out[5]: array([9, 9, 8, 7, 5, 3, 1, 0, 0, 0])

In [6]: all_FPPI
Out[6]: array([20, 20, 21, 22, 24, 26, 28, 29, 29, 29])

In [7]: all_FNPI
Out[7]: array([ 2,  2,  2,  3,  6,  8, 10, 11, 11, 11])

In [9]: log_avg_array
Out[9]: 
array([       -inf,        -inf,        -inf,        -inf,        -inf,
              -inf,        -inf, -0.03088688, -0.00336839,  0.        ])

In [10]: mr_array[0]
Out[10]: 
array([ 0.8       ,  0.4       ,  0.2       ,  0.        ,  0.        ,
        0.16666667,  0.16666667,  0.3       ,  0.27272727,  0.09090909,
        0.16666667,  0.        ,  0.08333333,  0.25      ,  0.30769231,
        0.30769231,  0.23076923,  0.38461538,  0.07692308,  0.15384615,
        0.15384615,  0.07692308,  0.15384615,  0.23076923,  0.15384615,
        0.07692308,  0.23076923,  0.30769231,  0.46153846,  0.15384615,
        0.23076923,  0.07692308,  0.33333333,  0.15384615,  0.07692308,
        0.15384615,  0.15384615,  0.30769231,  0.15384615,  0.23076923,
        0.07692308,  0.30769231,  0.92307692,  0.25      ,  0.15384615,
        0.14285714,  0.07142857,  0.07142857,  0.13333333,  0.0625    ,
        0.23529412,  0.17647059,  0.17647059,  0.11764706,  0.17647059,
        0.17647059,  0.23529412,  0.29411765,  0.17647059,  0.29411765,
        0.16666667,  0.        ,  1.        ,  0.42857143,  0.25      ,
        0.25      ,  0.625     ,  0.        ,  0.16666667,  0.25      ,
        0.        ,  0.        ,  0.33333333,  0.21052632,  0.10526316,
        0.19047619,  0.        ,  0.        ,  0.54545455,  0.9       ,
        0.        ,  0.125     ,  0.25      ,  0.33333333,  0.        ,
        0.1       ,  0.1       ,  0.1       ,  0.5       ,  0.3       ,
        0.3       ,  0.4       ,  0.2       ,  0.3       ,  0.        ,
        0.33333333,  0.44444444,  0.2       ,  0.5       ,  0.95      ,
        0.25      ,  0.        ,  0.33333333,  0.25      ,  0.        ,
        0.1       ,  0.08333333,  0.125     ,  0.19047619,  0.25      ,
        0.        ,  0.26315789,  0.45454545,  1.        ,  0.11111111,
        0.08333333,  0.35      ,  0.15      ,  0.07142857,  0.        ,
        0.23809524,  0.5       ,  0.        ,  0.42857143,  0.18181818,
        0.2       ,  0.16666667,  0.31578947,  0.11111111])

In [11]: mr_array[1]
Out[11]: 
array([ 0.8       ,  0.4       ,  0.4       ,  0.        ,  0.        ,
        0.16666667,  0.16666667,  0.3       ,  0.27272727,  0.09090909,
        0.16666667,  0.        ,  0.08333333,  0.25      ,  0.30769231,
        0.30769231,  0.23076923,  0.38461538,  0.07692308,  0.15384615,
        0.15384615,  0.15384615,  0.15384615,  0.23076923,  0.15384615,
        0.07692308,  0.23076923,  0.30769231,  0.46153846,  0.15384615,
        0.23076923,  0.07692308,  0.33333333,  0.15384615,  0.07692308,
        0.15384615,  0.15384615,  0.30769231,  0.15384615,  0.23076923,
        0.07692308,  0.30769231,  0.92307692,  0.25      ,  0.15384615,
        0.14285714,  0.07142857,  0.07142857,  0.13333333,  0.0625    ,
        0.23529412,  0.17647059,  0.17647059,  0.11764706,  0.17647059,
        0.17647059,  0.23529412,  0.29411765,  0.17647059,  0.29411765,
        0.16666667,  0.        ,  1.        ,  0.42857143,  0.25      ,
        0.25      ,  0.625     ,  0.        ,  0.16666667,  0.25      ,
        0.        ,  0.        ,  0.33333333,  0.21052632,  0.10526316,
        0.19047619,  0.        ,  0.        ,  0.54545455,  0.9       ,
        0.        ,  0.125     ,  0.25      ,  0.33333333,  0.        ,
        0.1       ,  0.1       ,  0.1       ,  0.5       ,  0.3       ,
        0.3       ,  0.5       ,  0.2       ,  0.3       ,  0.        ,
        0.33333333,  0.44444444,  0.2       ,  0.5       ,  0.95      ,
        0.25      ,  0.        ,  0.33333333,  0.25      ,  0.        ,
        0.1       ,  0.125     ,  0.125     ,  0.19047619,  0.25      ,
        0.        ,  0.26315789,  0.45454545,  1.        ,  0.11111111,
        0.08333333,  0.35      ,  0.15      ,  0.14285714,  0.        ,
        0.23809524,  0.5       ,  0.        ,  0.42857143,  0.27272727,
        0.2       ,  0.25      ,  0.31578947,  0.11111111])

In [12]: mr_array[2]
Out[12]: 
array([ 0.8       ,  0.6       ,  0.4       ,  0.        ,  0.        ,
        0.16666667,  0.33333333,  0.4       ,  0.27272727,  0.09090909,
        0.16666667,  0.08333333,  0.16666667,  0.25      ,  0.30769231,
        0.30769231,  0.30769231,  0.38461538,  0.07692308,  0.15384615,
        0.15384615,  0.23076923,  0.15384615,  0.30769231,  0.23076923,
        0.15384615,  0.23076923,  0.38461538,  0.53846154,  0.15384615,
        0.23076923,  0.07692308,  0.33333333,  0.15384615,  0.15384615,
        0.15384615,  0.15384615,  0.30769231,  0.23076923,  0.23076923,
        0.07692308,  0.30769231,  0.92307692,  0.25      ,  0.15384615,
        0.14285714,  0.07142857,  0.07142857,  0.2       ,  0.125     ,
        0.23529412,  0.29411765,  0.17647059,  0.11764706,  0.17647059,
        0.17647059,  0.23529412,  0.29411765,  0.17647059,  0.29411765,
        0.22222222,  0.        ,  1.        ,  0.42857143,  0.375     ,
        0.25      ,  0.625     ,  0.09090909,  0.16666667,  0.25      ,
        0.        ,  0.        ,  0.61111111,  0.21052632,  0.10526316,
        0.23809524,  0.        ,  0.        ,  0.54545455,  0.9       ,
        0.        ,  0.125     ,  0.25      ,  0.33333333,  0.        ,
        0.1       ,  0.2       ,  0.1       ,  0.5       ,  0.4       ,
        0.3       ,  0.6       ,  0.2       ,  0.4       ,  0.        ,
        0.33333333,  0.44444444,  0.26666667,  0.5       ,  0.95      ,
        0.25      ,  0.        ,  0.33333333,  0.25      ,  0.        ,
        0.1       ,  0.125     ,  0.20833333,  0.23809524,  0.25      ,
        0.        ,  0.26315789,  0.45454545,  1.        ,  0.22222222,
        0.08333333,  0.35      ,  0.2       ,  0.14285714,  0.        ,
        0.23809524,  0.5       ,  0.        ,  0.42857143,  0.36363636,
        0.2       ,  0.33333333,  0.31578947,  0.11111111])

In [13]: mr_array[3]
Out[13]: 
array([ 0.8       ,  0.8       ,  0.6       ,  0.4       ,  0.4       ,
        0.16666667,  0.5       ,  0.5       ,  0.27272727,  0.18181818,
        0.25      ,  0.08333333,  0.33333333,  0.25      ,  0.30769231,
        0.30769231,  0.53846154,  0.38461538,  0.15384615,  0.30769231,
        0.23076923,  0.30769231,  0.23076923,  0.38461538,  0.23076923,
        0.23076923,  0.38461538,  0.38461538,  0.53846154,  0.23076923,
        0.23076923,  0.15384615,  0.33333333,  0.30769231,  0.30769231,
        0.23076923,  0.15384615,  0.30769231,  0.23076923,  0.53846154,
        0.15384615,  0.38461538,  0.92307692,  0.41666667,  0.23076923,
        0.14285714,  0.07142857,  0.07142857,  0.2       ,  0.3125    ,
        0.23529412,  0.52941176,  0.41176471,  0.17647059,  0.17647059,
        0.17647059,  0.29411765,  0.35294118,  0.41176471,  0.41176471,
        0.33333333,  0.        ,  1.        ,  0.71428571,  0.375     ,
        0.375     ,  0.625     ,  0.09090909,  0.16666667,  0.25      ,
        0.09090909,  0.        ,  0.77777778,  0.31578947,  0.15789474,
        0.33333333,  0.        ,  0.        ,  0.54545455,  0.9       ,
        0.25      ,  0.5       ,  0.5       ,  0.66666667,  0.1       ,
        0.2       ,  0.5       ,  0.1       ,  0.7       ,  0.4       ,
        0.3       ,  0.7       ,  0.2       ,  0.5       ,  0.5       ,
        0.5       ,  0.44444444,  0.26666667,  0.5       ,  0.95      ,
        0.25      ,  0.        ,  0.33333333,  0.25      ,  0.25      ,
        0.2       ,  0.29166667,  0.29166667,  0.23809524,  0.25      ,
        0.14285714,  0.26315789,  0.45454545,  1.        ,  0.22222222,
        0.25      ,  0.375     ,  0.2       ,  0.21428571,  0.        ,
        0.23809524,  0.5       ,  0.        ,  0.57142857,  0.36363636,
        0.2       ,  0.33333333,  0.36842105,  0.16666667])

In [14]: mr_array[4]
Out[14]: 
array([ 0.8       ,  0.8       ,  0.8       ,  0.6       ,  0.6       ,
        0.5       ,  0.83333333,  0.7       ,  0.45454545,  0.45454545,
        0.66666667,  0.58333333,  0.58333333,  0.41666667,  0.30769231,
        0.61538462,  0.61538462,  0.38461538,  0.23076923,  0.30769231,
        0.53846154,  0.46153846,  0.30769231,  0.61538462,  0.53846154,
        0.30769231,  0.46153846,  0.61538462,  0.76923077,  0.23076923,
        0.38461538,  0.15384615,  0.41666667,  0.38461538,  0.30769231,
        0.46153846,  0.46153846,  0.69230769,  0.30769231,  0.61538462,
        0.30769231,  0.61538462,  0.92307692,  0.41666667,  0.30769231,
        0.35714286,  0.42857143,  0.35714286,  0.73333333,  0.625     ,
        0.64705882,  0.88235294,  0.70588235,  0.41176471,  0.52941176,
        0.41176471,  0.41176471,  0.64705882,  0.76470588,  0.76470588,
        0.55555556,  0.        ,  1.        ,  0.85714286,  0.5       ,
        0.5       ,  0.625     ,  0.09090909,  0.25      ,  0.33333333,
        0.36363636,  0.25      ,  0.88888889,  0.63157895,  0.31578947,
        0.71428571,  0.        ,  0.33333333,  0.54545455,  0.9       ,
        0.625     ,  0.75      ,  0.875     ,  0.88888889,  0.5       ,
        0.9       ,  0.7       ,  0.5       ,  0.8       ,  0.8       ,
        0.5       ,  0.9       ,  0.3       ,  0.7       ,  0.5       ,
        0.66666667,  0.77777778,  0.4       ,  0.5       ,  0.95      ,
        0.75      ,  0.        ,  0.66666667,  0.25      ,  0.375     ,
        0.6       ,  0.58333333,  0.58333333,  0.52380952,  0.375     ,
        0.28571429,  0.63157895,  0.45454545,  1.        ,  0.33333333,
        0.25      ,  0.375     ,  0.3       ,  0.42857143,  0.4       ,
        0.28571429,  0.5       ,  0.        ,  0.85714286,  0.63636364,
        0.4       ,  0.5       ,  0.36842105,  0.16666667])

In [15]: mr_array[5]
Out[15]: 
array([ 0.8       ,  1.        ,  1.        ,  0.8       ,  0.8       ,
        0.83333333,  1.        ,  0.7       ,  0.54545455,  0.90909091,
        0.83333333,  0.83333333,  0.83333333,  0.83333333,  0.61538462,
        0.76923077,  1.        ,  0.53846154,  0.61538462,  0.61538462,
        0.69230769,  0.92307692,  0.69230769,  0.84615385,  0.69230769,
        0.61538462,  0.76923077,  0.76923077,  0.92307692,  0.38461538,
        0.46153846,  0.61538462,  0.58333333,  0.84615385,  0.61538462,
        0.84615385,  0.76923077,  0.84615385,  0.46153846,  0.76923077,
        0.61538462,  0.69230769,  1.        ,  0.5       ,  0.61538462,
        0.64285714,  0.71428571,  0.78571429,  0.86666667,  0.875     ,
        0.82352941,  0.94117647,  0.88235294,  0.70588235,  0.76470588,
        0.76470588,  0.76470588,  0.88235294,  1.        ,  0.82352941,
        0.88888889,  0.5       ,  1.        ,  0.85714286,  0.5       ,
        0.5       ,  0.75      ,  0.27272727,  0.41666667,  0.5       ,
        0.81818182,  0.58333333,  1.        ,  0.78947368,  0.52631579,
        0.85714286,  1.        ,  0.33333333,  0.54545455,  0.9       ,
        0.625     ,  0.875     ,  1.        ,  0.88888889,  0.8       ,
        1.        ,  0.9       ,  1.        ,  1.        ,  0.8       ,
        0.6       ,  1.        ,  0.6       ,  1.        ,  1.        ,
        0.83333333,  0.88888889,  0.73333333,  0.66666667,  0.95      ,
        1.        ,  0.        ,  0.66666667,  0.75      ,  0.625     ,
        0.9       ,  0.70833333,  0.75      ,  0.80952381,  0.5       ,
        1.        ,  0.84210526,  0.54545455,  1.        ,  0.55555556,
        0.5       ,  0.55      ,  0.45      ,  0.85714286,  0.6       ,
        0.57142857,  1.        ,  0.5       ,  1.        ,  0.90909091,
        0.6       ,  0.75      ,  0.57894737,  0.38888889])

In [16]: mr_array[6]
Out[16]: 
array([ 0.8       ,  1.        ,  1.        ,  1.        ,  0.8       ,
        0.83333333,  1.        ,  0.8       ,  0.81818182,  1.        ,
        0.91666667,  0.83333333,  0.91666667,  1.        ,  0.92307692,
        1.        ,  1.        ,  0.76923077,  0.69230769,  0.84615385,
        0.92307692,  1.        ,  0.92307692,  0.84615385,  0.92307692,
        0.84615385,  0.92307692,  0.84615385,  1.        ,  0.46153846,
        0.76923077,  0.76923077,  0.66666667,  1.        ,  0.69230769,
        1.        ,  0.92307692,  0.92307692,  0.84615385,  0.92307692,
        0.92307692,  0.92307692,  1.        ,  0.58333333,  0.69230769,
        0.85714286,  0.92857143,  0.92857143,  1.        ,  0.9375    ,
        0.94117647,  1.        ,  0.94117647,  0.88235294,  1.        ,
        0.94117647,  0.94117647,  1.        ,  1.        ,  0.94117647,
        1.        ,  1.        ,  1.        ,  0.85714286,  0.5       ,
        0.625     ,  0.875     ,  0.81818182,  0.83333333,  0.91666667,
        0.90909091,  0.91666667,  1.        ,  0.89473684,  0.78947368,
        0.95238095,  1.        ,  0.66666667,  0.54545455,  0.9       ,
        0.75      ,  1.        ,  1.        ,  1.        ,  0.9       ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        0.8       ,  1.        ,  0.7       ,  1.        ,  1.        ,
        1.        ,  1.        ,  0.86666667,  1.        ,  0.95      ,
        1.        ,  0.        ,  0.83333333,  0.75      ,  0.875     ,
        0.9       ,  0.95833333,  0.95833333,  1.        ,  0.625     ,
        1.        ,  0.89473684,  0.81818182,  1.        ,  0.66666667,
        0.83333333,  0.75      ,  0.65      ,  1.        ,  0.8       ,
        0.76190476,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  0.91666667,  0.73684211,  0.55555556])

In [17]: mr_array[7]
Out[17]: 
array([ 0.8       ,  1.        ,  1.        ,  1.        ,  0.8       ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        0.91666667,  1.        ,  0.91666667,  1.        ,  0.92307692,
        1.        ,  1.        ,  0.92307692,  0.92307692,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  0.92307692,
        1.        ,  1.        ,  1.        ,  1.        ,  0.84615385,
        0.92307692,  0.92307692,  0.83333333,  1.        ,  0.92307692,
        1.        ,  1.        ,  1.        ,  0.92307692,  1.        ,
        1.        ,  1.        ,  1.        ,  0.75      ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  0.85714286,  0.625     ,
        1.        ,  1.        ,  0.90909091,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  0.94736842,  0.94736842,
        1.        ,  1.        ,  1.        ,  0.90909091,  0.9       ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        0.9       ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  0.95      ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  0.77777778,
        1.        ,  0.975     ,  0.85      ,  1.        ,  1.        ,
        0.9047619 ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  0.89473684,  0.77777778])

In [18]: mr_array[8]
Out[18]: 
array([ 0.8       ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  0.92307692,
        1.        ,  1.        ,  1.        ,  1.        ,  0.92307692,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  0.95      ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ,  1.        ,
        1.        ,  1.        ,  1.        ,  1.        ])

In [19]: mr_array[9]
Out[19]: 
array([ 1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,
        1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.,  1.])