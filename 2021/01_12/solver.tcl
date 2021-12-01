variable input [read [open "./input.txt" "r"]]

proc part1 {} \
{
	variable input

	set count 0

	for {set i 1} {$i < [llength $input]} {incr i} \
	{
		if {[lindex $input $i] > [lindex $input [expr $i -1]]} \
		{
			incr count
		}
	}
	puts $count
}

proc part2 {} \
{
	variable input

	set count 0

	for {set i 0} {$i < [expr [llength $input] - 3]} {incr i} \
	{
		set lower [expr [lindex $input [expr $i + 0]] + [lindex $input [expr $i + 1]] + [lindex $input [expr $i + 2]]]
		set upper [expr [lindex $input [expr $i + 1]] + [lindex $input [expr $i + 2]] + [lindex $input [expr $i + 3]]]

		if {$upper > $lower} \
		{
			incr count
		}
	}
	puts $count
}