proc getAdjacent {y x} {
	variable sizeY
	variable sizeX

	set adjCoords [list]

	for {set y_off -1} {$y_off <= 1} {incr y_off} {
		for {set x_off -1} {$x_off <= 1} {incr x_off} {
			set new_y [expr $y + $y_off]
			set new_x [expr $x + $x_off]

			if {$new_y < 0 || $new_x < 0} {
				continue
			}
			if {$new_y == $y && $new_x == $x} {
				continue
			}

			lappend adjCoords [list $new_y $new_x]
		}
	}
	return $adjCoords
}

proc lincr {liste} {
	for {set y 0} {$y < [llength $liste]} {incr y} {
		for {set x 0} {$x < [llength [lindex $liste 0]]} {incr x} {
			lset liste $y $x [expr [lindex $liste $y $x] + 1]
		}
	}
	return $liste
}

proc putsMat {liste} {
	foreach line $liste {
		puts $line
	}
}

proc reset {liste} {
	for {set row 0} {$row < 10} {incr row} {
		lset liste $row [list 0 0 0 0 0 0 0 0 0 0]
	}
	return $liste
}