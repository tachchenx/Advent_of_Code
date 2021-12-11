variable input [read [open "./input.txt" "r"]]

interp alias {} push {} lappend


proc part1 {} {
	variable input
	variable stack [list]
	variable score 0

	foreach line $input {
		set line [split $line {}]
		set stack [list]

		for {set index 0} {$index < [llength $line]} {incr index} {
			set item [lindex $line $index]
			switch $item {
				"a" {
					push stack "b"
				}
				"c"	{
					push stack "d"
				}
				"e"	{
					push stack "f"
				}
				"g"	{
					push stack "h"
				}
				default {
					set expec [pop stack]
					if {$expec != $item} {
						puts "Expected [set expec], but found [set item] instead"
						switch $item {
							"b" {
								incr score 3
							}
							"d" {
								incr score 57
							}
							"f" {
								incr score 1197
							}
							"h" {
								incr score 25137
							}
						}
					}
				}
			}
		}
	}
	puts "Score: [set score]"
}

proc part2 {} {
	variable input
	variable stack [list]
	variable score 0
	variable scores [list]
	set round 0

	foreach line $input {
		set line [split $line {}]
		set stack [list]
		set score 0
		set corrupt 0

		for {set index 0} {$index < [llength $line]} {incr index} {
			set item [lindex $line $index]
			switch $item {
				"a" {
					push stack "b"
				}
				"c"	{
					push stack "d"
				}
				"e"	{
					push stack "f"
				}
				"g"	{
					push stack "h"
				}
				default {
					set expec [pop stack]
					if {$expec != $item} {
						#corrupted line -> Escape
						#puts "Corrupted line [set round]"
						set corrupt 1
						break
					}
				}
			}
		}
		if {$corrupt == 0} {
			#puts "Incomplete line [set round]"
			#puts "Line incomplete with [set stack]"
			# line not corrupted -> come here
			while {[llength $stack] > 0} {
				set element [pop stack]
				set score [expr $score * 5]
				switch $element {
					"b" {
						incr score 1
					}
					"d" {
						incr score 2
					}
					"f" {
						incr score 3
					}
					"h" {
						incr score 4
					}
				}
			}
			lappend scores $score
			#puts "Appended score [set score]"
			incr round	
		}
		
	}

	set scores [lsort -integer $scores]
	set index [expr [llength $scores] /2]

	puts "Middle Score is [lindex $scores $index]"
}


################################################################
################################################################
proc pop name {
    upvar 1 $name stack
    set res [lindex $stack end] 
    set stack [lreplace $stack end end]
    return $res
 }