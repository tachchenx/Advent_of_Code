set input [read [open "./input.txt" "r"]]
set max_value 0
set id_liste [list]

foreach var $input {
	set singles [split $var {}]

	set lower 0
	set upper 127
	set left 0
	set right 7


	foreach letter $singles {
		if {$letter == "F"} {
			set upper [expr $upper - [expr [expr [expr $upper - $lower] / 2] + 1]]
		}

		if {$letter == "B"} {
			set lower [expr $lower + [expr [expr [expr $upper - $lower] / 2] +1]]
		}

		if {$letter == "L"} {
			set right [expr $right - [expr [expr [expr $right - $left] / 2] + 1]]
		}

		if {$letter == "R"} {
			set left [expr $left + [expr [expr [expr $right - $left] / 2] +1]]
		}
	}

	if {$lower != $upper} {
		error "Lower not equal upper"
	}
	if {$left != $right} {
		error "Lower not equal upper"
	}

	set temp_max [expr [expr $lower * 8] + $left]
	lappend id_liste $temp_max
	if {$temp_max > $max_value} {
		set max_value $temp_max
	}
}

puts "Max Value:"
puts $max_value
puts "########################################"

for {set i 1} {$i <= $max_value} {incr i} {
	if {[lsearch $id_liste $i] == -1} {
		puts $i
	}
}