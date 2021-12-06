variable input [read [open "./testinput.txt" "r"]]
variable digits [split $input ","]

#puts "Initial state: [set digits]"

# for {set day 1} {$day <= 256} {incr day} {
# 	set runs [llength $digits]
# 	for {set i 0} {$i < $runs} {incr i} {
# 		set num [lindex $digits $i]

# 		if {$num == 0} {
# 			lappend digits 8
# 			lset digits $i 6
# 		} else {
# 			lset digits $i [expr $num - 1]
# 		}
# 	}

# puts "After day [set day]: [set digits]"
# puts [llength $digits]
# }

# puts "Fishes: [llength $digits]"


variable counts [list 0 0 0 0 0 0 0 0 0]

foreach element $digits {
	lset counts $element [expr [lindex $counts $element] + 1]
}

# puts "Initial state: [set digits]"
# puts "Initial state count: [set counts]"


for {set day 1} {$day <= 256} {incr day} {
	set temp_counts [list 0 0 0 0 0 0 0 0 0]

	lset temp_counts 8 [lindex $counts 0]

	for {set index 0} {$index < 8} {incr index} {
		lset temp_counts $index [lindex $counts [expr $index +1]]
	}

	lset temp_counts 6 [expr [lindex $temp_counts 6] + [lindex $counts 0]]

	set counts $temp_counts
	# puts $temp_counts
	# puts $counts
}

set sum 0
foreach element $counts {
	incr sum $element
}

puts "Fishes: [set sum]"