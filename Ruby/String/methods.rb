# def process_text(arr)
#     arr.map{ |str| str.strip }.join(' ')
# end
def process_text(arr)
    arr.map(&:strip).join(' ')
end
