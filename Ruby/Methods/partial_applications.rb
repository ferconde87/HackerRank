def fact(x)
    result = 1
    (2..x).each do |x|
      result *= x
    end
    result
end

combination = -> (n) do
    -> (r) do
        fact(n) / (fact(n-r) * fact(r))
    end
end

n = gets.to_i
r = gets.to_i
nCr = combination.(n)
puts nCr.(r)
