# Enter your code here. Read input from STDIN. Print output to STDOUT
n = gets.to_i

def prime?(number)
    if number == 1
        return false
    end
    top = Math.sqrt(number).to_int
    (2..top).each do |x|
        if number % x == 0
            return false
        end
    end
    return true
end

def palindrome?(number)
    s = number.to_s
    return s == s.reverse
end

print 2.upto(Float::INFINITY).lazy.select{ |x| prime?(x) && palindrome?(x) }.take(n).to_a
