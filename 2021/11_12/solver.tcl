source "helper.tcl"

variable input [read [open "./input.txt" "r"]]

for {set i 0} {$i < [llength $input]} {incr i} {
	lset input $i [split [lindex $input $i] {}]
}

variable flashed [list]
variable sizeY 10
variable sizeX 10

for {set row 0} {$row < 10} {incr row} {
	lappend flashed [list 0 0 0 0 0 0 0 0 0 0]
}

proc part1 {} {
	variable input
	variable flashed
	variable sizeY
	variable sizeX
	variable totalFlashes 0
	variable p2_ans 0
	variable p2_trigger 0

	set simstep 0

	while {$p2_trigger == 0} {
		set stepdone 0
		set flashed [reset $flashed]
		set input [lincr $input]

		while {!$stepdone} {
			#puts "Go with Step [expr [set simstep]+1]"
			for {set y 0} {$y < $sizeY} {incr y} {
				for {set x 0} {$x < $sizeX} {incr x} {
					if {[lindex $input $y $x] > 9 && [lindex $flashed $y $x] == 0} {
						#puts "Flash at \[ [set y], [set x] \]"
						flash $y $x
						incr totalFlashes
					}
				}
			}

			set stepdone 1
			foreach line $input {
				foreach element $line {
					if {!($element < 10)} {
						set stepdone 0
					}
				}
			}

			if {$stepdone == 1} {
				#puts "Done with Step [expr [set simstep]+1]"
				#putsMat $input
				#putsMat $flashed
			}
		}

		set part2 1
		foreach line $flashed {
			foreach element $line {
				if {$element == 0} {
					set part2 0
				}
			}
		}
		if {$part2 == 1 && $p2_trigger == 0} {
			set p2_ans [expr [set simstep] + 1]
			set p2_trigger 1
		}
		incr simstep
	}

	puts "Total flashes: [set totalFlashes]"
	puts "First Fullflash: [set p2_ans]"
}


proc flash {y_pos x_pos} {
	variable flashed
	variable input

	lset flashed $y_pos $x_pos 1
	lset input $y_pos $x_pos 0

	set near [getAdjacent $y_pos $x_pos]
	foreach pair $near {
		set nearY [lindex $pair 0]
		set nearX [lindex $pair 1]
		if {[lindex $flashed $nearY $nearX] == 0} {
			lset input $nearY $nearX [expr [lindex $input $nearY $nearX] + 1]
		}
	}
}