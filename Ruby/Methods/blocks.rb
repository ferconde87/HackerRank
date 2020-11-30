def factorial(n)
    result = 1
    for i in 2..n
        result *= i
    end
    puts result
end

n = gets.to_i
factorial(n)

#### not interesting but using yield
# def factorial(x)
#     result = 1
#     for i in 2..x
#         result *= yield(i)
#     end
#     print result
# end

# n = gets.to_i
# factorial(n) do |x|
#     x    
# end
