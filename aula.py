import math

heigth_weight_age = [
  170,
  70,
  40
]

grades = [
  95,
  90,
  75,
  62
]


def vector_add (v, w):
  #v = [1, 2, 3]
  #w = [4, 5, 6]
  #zip (v, w) = [(1, 4), (2, 5), (3, 6)]
  return [v_i + w_i for v_i, w_i in zip (v, w)]

def vector_add_test ():
  v = [5, 4]
  w = [2, 1]
  r = vector_add (v, w)
  print (r)

def vector_subtract (v, w):
  return [v_i - w_i for v_i, w_i in zip (v, w)]

def vector_subtract_test ():
  v = [5, 4]
  w = [2, 1]
  r = vector_subtract (v, w)
  print (r)

def vector_sum (vectors):
  result = vectors[0]
  for vector in vectors[1:]:
    result = vector_add (result, vector)
  return result

def vector_sum_test ():
  v1 = [1, 2, 5, 6]
  v2 = [4, 3, 2, 1]
  v3 = [1, 1, 1, 1]
  r = vector_sum ([v1, v2, v3])
  print (r)

def scalar_multiply (c, v):
  return [c * v_i for v_i in v]

def scalar_multiply_test ():
  c = 5
  v = [4, 1, 2, 5]
  r = scalar_multiply (c, v)
  print (r)

def vector_mean (vectors):
  n = len (vectors)
  return scalar_multiply (1 / n, vector_sum(vectors))

def vector_mean_test ():
  v1 = [1, 2, 5, 6]
  v2 = [4, 3, 2, 1]
  v3 = [1, 1, 1, 1]
  r = vector_mean ([v1, v2, v3])
  print (r)

def dot (v, w):
  #v = [1, 2, 5]
  #w = [3, 2, 1]
  #dot (v, w) = 1 * 3 + 2 * 2 + 5 * 1 = 12
  return sum([v_i * w_i for v_i, w_i in zip (v, w)])

def dot_test ():
  v = [1, 2, 5]
  w = [3, 2, 1]
  r = dot (v, w)
  print (r)

def sum_of_squares (v):
  #v = [1, 2, 3]
  #sum_of_squares(v) = 1 * 1 + 2 * 2 + 3 * 3 = 1 + 4 + 9 = 14
  return dot (v, v)

def sum_of_squares_test ():
  v = [1, 2, 3]
  r = sum_of_squares(v)
  print (r)


def magnitude(v):
  return math.sqrt(sum_of_squares(v))


def magnitude_test ():
  v = [1, 2, 3]
  r = magnitude (v)
  print (r)

def squared_distance (v, w):
  #v = [1, 2]
  #w = [3, 5]
  #vector_subtract(v, w) = [-2, -3]
  #sum_of_squares(vector_subtract(v,w)) = (-2 * -2) + (-3 * -3) = 4 + 9 = 13
  return sum_of_squares(vector_subtract (v, w))

def squared_distance_test ():
  v = [1, 2]
  w = [3, 5]
  r = squared_distance (v, w)
  print (r)

def distance (v, w):
  return math.sqrt(squared_distance(v, w))

def distance_test ():
  v = [1, 2]
  w = [3, 5]
  r = distance (v, w)
  print (r)

def distance_test2 ():
  u1 = [27, 80, 180]
  u2 = [58, 100, 198]
  u3 = [29, 79, 179]
  print (f'u1 vs u2: {distance (u1, u2)}')
  print(f'u1 vs u3: {distance (u1, u3)}')
  print(f'u2 vs u3: {distance (u2, u3)}')


def qtde_amigos_minutos_passados ():
  return ([1, 10, 50, 2, 150], [5, 200, 350, 17, 1])


def variance (v):
  mean = sum(v) / len(v)
  return[v_i - mean for v_i in v]

def variance_test():
  v = [1, 2, 3]
  r = variance (v)
  print (r)

def covariance (x, y):
  n = len(x)
  return dot (variance(x), variance(y)) / (n - 1)

def covariance_test ():
  x = [3, 12, 3]
  y = [1, 7, 4]
  print (f'covariancia: {covariance(x, y)}')

def correlation (x, y):
  desvio_padrao_x = math.sqrt (sum_of_squares (variance(x)) / (len(x) - 1))
  desvio_padrao_y = math.sqrt(sum_of_squares(variance(y)) / (len(y) - 1))
  if desvio_padrao_x > 0 and desvio_padrao_y > 0:
    return covariance(x, y) / desvio_padrao_y / desvio_padrao_x
  else:
    return 0

def correlation_test ():
  x = [3, 12, 3]
  y = [1, 7, 4]
  print (f'correlation: {correlation(x, y)}')
  x = [-1, 8, 11]
  y = [8, 2, 24]
  print(f'correlation: {correlation(x, y)}')
  x = [8, 6, 4]
  y = [2, 6, 4]
  print(f'correlation: {correlation(x, y)}')


def correlation_test_with_outlier():
  data = qtde_amigos_minutos_passados()
  resultado = correlation(data[0], data[1])
  print(resultado)

def correlation_test_without_outlier ():
  data = qtde_amigos_minutos_passados()
  resultado = correlation(data[0][:len(data[0])-1], data[1][:len(data[1])-1])
  print (resultado)

def main():
  print (correlation_test_without_outlier())
  #correlation_test_with_outlier()
  #correlation_test()
  #covariance_test()
  #variance_test()
  #distance_test2()
  # distance_test()
  #squared_distance_test()
  #print (magnitude_test())
  #sum_of_squares_test()
  #dot_test()
  #vector_mean_test()
  #scalar_multiply_test()
  #vector_sum_test()
  #vector_subtract_test()
  #vector_add_test()




main()
