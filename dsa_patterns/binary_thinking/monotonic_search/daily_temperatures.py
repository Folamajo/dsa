def daily_temperatures(temperatures: list[int])-> list[int]:
   stack = []
   output = [0] * len(temperatures)

   for i in range(len(temperatures)):
      while stack and temperatures[i] > temperatures[stack[-1]]:
         prev = stack.pop()
         output[prev] = i - prev

      stack.append(i)
   return output

if __name__ == "__main__":
   input = [73,74,75,71,69,72,76,73]
   print(daily_temperatures(input))