def prime?(number)
    return false if number == 1
    top = Math.sqrt(number).to_int
    for x in (2..top)
        if number % x == 0
            return false
        end
    end
    return true
end
