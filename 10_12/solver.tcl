variable input [read [open "./input.txt" "r"]]

set sum 0
set ones 0
set threes 0

set input [lsort -integer $input]

foreach element $input {
	set diff [expr $element - $sum]
	if {$diff == 1} {
		incr ones
	}
	if {$diff == 3} {
		incr threes
	}
	incr sum [set diff]
}

#Adapter is 3 higer than highest
incr threes

puts "Ending"
puts "Ones: [set ones]"
puts "Threes : [set threes]"
puts "Mult is: [expr $ones * $threes]"