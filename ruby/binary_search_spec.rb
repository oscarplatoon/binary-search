require_relative 'binary_search'

test_array = [1,2,3,4,5]

puts binary_search(1, test_array) == 0
puts binary_search(2, test_array) == 1
puts binary_search(3, test_array) == 2
puts binary_search(4, test_array) == 3
puts binary_search(5, test_array) == 4


super_big_array = [1,5,7,2,3,8,4,9]
puts binary_search(7, super_big_array) == 5
