def max_sum_circular_subarray(input:list):
   total = curr_max = max_sum = curr_min = min_sum = input [0]

   for i in range(1, len(input)):
      curr_max = max(input[i], (curr_max + input[i]))
      max_sum = max(curr_max, max_sum)

      curr_min = min(input[i], (curr_min + input[i]))
      min_sum = min(curr_min, min_sum)

      total += input[i]
   if max_sum < 0:
      return max_sum
   else:
      return max(max_sum, total - min_sum)


if __name__ == '__main__':
   input = [1, -2, 3, -2]
   print(max_sum_circular_subarray(input)) 