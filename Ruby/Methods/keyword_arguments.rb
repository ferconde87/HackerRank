def convert_temp(temp, hash)
    #puts "input_scale = #{hash[:input_scale]}" 
    #puts "output_scale = #{hash[:output_scale]}"
    #puts "temp = #{temp}"
    if !hash.key?(:output_scale)
        return temp
    end
    if hash[:input_scale] == hash[:output_scale]
        return temp
    end

    x = send("#{hash[:input_scale]}_to_#{hash[:output_scale]}", temp).round(2)
    return x
end

public
def celsius_to_kelvin(temp)
    return temp + 273.15
end

def celsius_to_fahrenheit(temp)
    return 32 + temp*(9/5)
end

def kelvin_to_celsius(temp)
    return temp - 273.15
end

def fahrenheit_to_celsius(temp)
    return (temp - 32)*(5.0/9)
end

def fahrenheit_to_kelvin(temp)
    return (temp - 32)*(5.0/9) + 273.15
end

def kelvin_to_fahrenheit(temp)
    return (temp - 273.15)*(9.0/5) + 32
end
