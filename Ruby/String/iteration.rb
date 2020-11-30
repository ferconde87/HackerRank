# def count_multibyte_char(str)
#     count = 0
#     str.each_char do |c| 
#         count += 1 if c.bytesize > 1
#     end
#     return count
# end

def count_multibyte_char(str)
    str.each_char.select{ |c| c.bytesize > 1 }.count
end
