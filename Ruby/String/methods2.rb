def strike(str)
    "<strike>#{str}</strike>"
end

# def mask_article(str, words)
#     words.each do |word|
#         str.gsub!(word, strike(word))
#     end
#     return str
# end

def mask_article(text, words)
    pattern = words.join("|")
    text.gsub(/#{pattern}/) {|match| strike(match)}
end
