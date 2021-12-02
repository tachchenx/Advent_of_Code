variable input [read [open "./input.txt" "r"]]

proc part1 {} \
{
	variable input

	set y 0
	set forward 0

	for {set i 0} {$i < [llength $input]} {incr i 2} \
	{
		set code [lindex $input $i]
		if {$code == "up"} \
		{
			set y [expr $y - [lindex $input [expr $i +1]]]
		}

		if {$code == "down"} \
		{
			set y [expr $y + [lindex $input [expr $i +1]]]
		}

		if {$code == "forward"}	\
		{
			set forward [expr $forward + [lindex $input [expr $i +1]]]
		}
	}

	puts [expr $y * $forward]
}

proc part2 {} \
{
	variable input

	set aim 0
	set y 0
	set forward 0

	for {set i 0} {$i < [llength $input]} {incr i 2} \
	{
		set code [lindex $input $i]
		if {$code == "up"} \
		{
			set aim [expr $aim - [lindex $input [expr $i +1]]]
		}

		if {$code == "down"} \
		{
			set aim [expr $aim + [lindex $input [expr $i +1]]]
		}

		if {$code == "forward"}	\
		{
			set forward [expr $forward + [lindex $input [expr $i +1]]]
			set y [expr $y + [lindex $input [expr $i +1]] * $aim]
		}
	}

	puts [expr $y * $forward]
}