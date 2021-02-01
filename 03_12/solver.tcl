variable input [read [open "./input.txt" "r"]]
variable depth [llength $input]
variable width [llength [split [lindex $input 0] {}]]
variable result 1

proc runthrough {right down startval} {
	variable depth
	variable x
	variable input
	variable trees
	variable width

	puts "Performing run with right:[set right] and down:[set down]"

	for {set i $startval} {$i < $depth} {incr i $down} {
		incr x $right
		if {$x >= $width} {
			set x [expr $x - $width]
		}
		puts "x is: [set x] and down is : [set i]"
		set line [split [lindex $input $i] {}]
		if {[lindex $line $x] == "1"} {
			incr trees
			#puts "Found"
		}
	}
	puts $trees
}


variable x 0
variable trees 0
runthrough 1 1 1
set result [expr $result * $trees]
set x 0
set trees 0
runthrough 3 1 1
set result [expr $result * $trees]
set x 0
set trees 0
runthrough 5 1 1
set result [expr $result * $trees]
set x 0
set trees 0
runthrough 7 1 1
set result [expr $result * $trees]
set x 0
set trees 0
runthrough 1 2 2
set result [expr $result * $trees]

puts "RESULT: [set result]"