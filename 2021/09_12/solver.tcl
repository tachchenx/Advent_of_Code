variable input [read [open "./input.txt" "r"]]

for {set i 0} {$i < [llength $input]} {incr i} {
	set line [lindex $input $i]

	lset input $i [split $line {}]
}

proc part1 {} {
	variable input
	variable sum 0

	for {set row 0} {$row < [llength $input]} {incr row} {
		set line [lindex $input $row]

		for {set col 0} {$col < [llength $line]} {incr col} {
			set item [lindex $line $col]

			#drüber
			if {$row >=1} {
				if {[lindex $input [expr $row - 1] $col] <= $item} {
					continue
				}
			}
			#puts "1"

			#drunter
			if {$row <= [expr [llength $input] -2]} {
				if {[lindex $input [expr $row + 1] $col] <= $item} {
					continue
				}
			}
			#puts "2"

			#links
			if {$col >= 1} {
				if {[lindex $input $row [expr $col - 1]] <= $item} {
					continue
				}
			}
			#puts "3"

			#rechts
			if {$col <= [expr [llength $line] -2]} {
				if {[lindex $input $row [expr $col + 1]] <= $item} {
					continue
				}
			}
			#puts "4"
			#puts "FOUND"
			puts "row: [set row] and col [set col]"

			incr sum [expr 1 + $item]
		}
	}

	puts "Sum is [set sum]"
}