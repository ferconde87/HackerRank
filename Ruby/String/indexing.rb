#format SSS-XX.XX-YY.YY
def serial_average(str)
    return "#{str[0,4]}#{((str[4,5].to_f+str[10,5].to_f)/2.0).round(2)}"
end
