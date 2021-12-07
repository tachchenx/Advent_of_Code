variable input [read [open "./input.txt" "r"]]
variable single [split $input ","]

puts $single
set single [lsort -integer $single]

proc part1 {} {
	variable single
	set fuel 0

	for {set i [lindex $single 0]} {$i < [lindex [expr [llength $single] - 1]]} {incr i} {
		set tmp_fuel 0
		foreach element $single {
			set used [expr $element - $i]
			if {$used < 0} {
				set used [expr $used * -1]
			}
			incr tmp_fuel $used
		}

		if {$fuel == 0 || $fuel > $tmp_fuel} {
			set fuel $tmp_fuel
		}
	}
	puts "Minimum Fuel (Part 1): [set fuel]"
}


proc part2 {} {
	variable single
	set fuel 0

	for {set i [lindex $single 0]} {$i < [lindex [expr [llength $single] - 1]]} {incr i} {
		set tmp_fuel 0
		foreach element $single {
			set used 0
			set dist [expr $element - $i]
			if {$dist < 0} {
				set dist [expr $dist * -1]
			}
			for {set j 1} {$j <= $dist} {incr j} {
				incr used $j
			}
			incr tmp_fuel $used
		}

		if {$fuel == 0 || $fuel > $tmp_fuel} {
			set fuel $tmp_fuel
		}
	}
	puts "Minimum Fuel (Part 2): [set fuel]"
}
