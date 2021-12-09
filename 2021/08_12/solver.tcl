variable input [read [open "./testerinput.txt" "r"]]

proc part1 {} \
{
	variable input
	variable count 0

	for {set i 0} {$i < 200} {incr i} {
		set offset [expr $i * 15]
		for {set index 11} {$index < 15} {incr index} {
			set item [split [lindex $input [expr $index + $offset]] {} ]
			set length [llength $item]
			
			if {$length == 2 || $length == 3 || $length == 4 || $length == 7} {
				incr count
			}
		}
	}

	puts "Part1: [set count]"
}


proc part2 {} {
	variable input
	variable output 0
	variable decoded [list 0 0 0 0 0 0 0 0 0 0]

	set subset [get_subset 0]
	puts $subset
	set nums [list]
	for {set i 0} {$i < 10} {incr i} {
		lappend nums [lindex $subset $i]
	}

	set decoded [find_easy $nums]
	lset decoded 3 [find3 $nums [lindex $decoded 1]]
	set fives [findfives $nums [lindex $decoded 7] [lindex $decoded 4] [lindex $decoded 3]]
	lset decoded 2 [lindex $fives 0]
	lset decoded 5 [lindex $fives 1]
	lset decoded 0 [findzero $nums [lindex $decoded 2] [lindex $decoded 7] [lindex $decoded 4]]
	lset decoded 9 [findnine $nums [lindex $decoded 1] [lindex $decoded 0]]
	lset decoded 6 [findsix $nums $decoded]

	puts $decoded
}

proc get_subset {num} {
	variable input
	set subset [list]
	set offset [expr $num * 15]
	for {set index $offset} {$index < [expr $offset + 15]} {incr index} {

		set item [lindex $input $index]
		if {$item == "|"} {
			continue
		}
		lappend subset $item
	}
	return $subset
} 

proc find_easy {liste} {
	set temp_decode [list 0 0 0 0 0 0 0 0 0 0]
	foreach element $liste {
		puts $element
		if {[string length $element] == 2} {
			lset temp_decode 1 $element
		}
		if {[string length $element] == 4} {
			lset temp_decode 4 $element
		}
		if {[string length $element] == 3} {
			lset temp_decode 7 $element
		}
		if {[string length $element] == 7} {
			lset temp_decode 8 $element
		}
	}

	return $temp_decode
}

proc find3 {liste one} {
	set chars_one [split $one {}]
	foreach element $liste {
		if {[string length $element] == 5} {
			set chars [split $element {}]
			if {[lsearch $chars [lindex $chars_one 0]] != -1 && [lsearch $chars [lindex $chars_one 1]] != -1} {
				return $element
			}
		}
	}
}

proc findfives {liste seven four three} {
	set ret_vals [list]
	set fives [list]
	foreach element $liste {
		if {[string length $element] == 5 && $element != $three} {
			lappend fives $element
		}
	}

	set first [lindex $fives 0]
	set second [lindex $fives 1]
	set chars [split $first {}]
	set chars_seven [split $seven {}]
	foreach char $chars_seven {
		set index [lsearch $chars $char]
		set chars [lreplace $chars $index $index]
	}

	set foundcount 0
	set chars_four [split $four {}]

	foreach char $chars_four {
		if {[lsearch $chars $char] != -1} {
			incr foundcount
		}
	}

	puts $foundcount

	if {$foundcount == 1} {
		lappend ret_vals $first
		lappend ret_vals $second
	} else {
		lappend ret_vals $second
		lappend ret_vals $first
	}
	return $ret_vals
}

proc findzero {liste two seven four} {
	set chars_two [split $two {}]
	set chars_four [split $four {}]
	set chars_seven [split $seven {}]

	foreach char $chars_seven {
		set index [lsearch $chars_two $chars_two]
		set chars_two [lreplace $chars_two $index $index]
	}

	set cross 0
	foreach char $chars_four {
		set index [lsearch $chars_two $char]
		if {$index != -1} {
		 	set cross $char
		 } 
	}

	foreach element $liste {
		set element_split [split $element {}]
		if {[lsearch $element_split $cross] == -1 && [llength $element_split] == 6} {
			return $element	
		}
	}
}

proc findnine {liste one zero} {
	set chars_one [split $one {}]
	
	foreach element $liste {
		if {[string length $element] == 6 && $element != $zero} {
			set element_split [split $element {}]
			if {[lsearch $element_split [lindex $chars_one 0]] != -1 && [lsearch $element_split [lindex $chars_one 1]] != -1} {
				return $element
			}
		}
	}
}

proc findsix {liste foundlist} {
	foreach element $liste {
		if {[lsearch $foundlist $element] == -1} {
			return $element
		}
	}
}