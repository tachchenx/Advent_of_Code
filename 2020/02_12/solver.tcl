proc part_one {} {
	set valid_passwords 0
	set list [read [open "./input.txt" "r"]]

	for {set i 0} {$i < 3000} {incr i} {
		puts "Versuch: [expr $i / 3]"
		set range [split [lindex $list $i] "-"]
		puts $range
		incr i
		set letter [lindex [split [lindex $list $i] {}] 0]
		puts $letter
		incr i
		set pw_to_test [split [lindex $list $i] {}]
		puts $pw_to_test
		set counter 0
		for {set j 0} {$j < [llength $pw_to_test]} {incr j} {
			if {[lindex $pw_to_test $j] == $letter} {
				incr counter
			}
		}
		if {!($counter < [lindex $range 0] || $counter > [lindex $range 1])} {
			incr valid_passwords
			puts "Stimmt"
		} else {
			puts "Nein"
		}
		puts ""
	}

	puts "Anzahl:"
	puts $valid_passwords
}

proc part_two {} {
	set valid_passwords 0
	set list [read [open "./input.txt" "r"]]

	for {set i 0} {$i < 3000} {incr i} {
		puts "Versuch: [expr $i / 3]"
		set indexone_range [split [lindex $list $i] "-"]
		puts $indexone_range
		set range [list [expr [lindex $indexone_range 0] - 1] [expr [lindex $indexone_range 1] -1]]
		puts "Corrected range"
		puts $range
		
		incr i
		set letter [lindex [split [lindex $list $i] {}] 0]
		puts $letter
		incr i
		set pw_to_test [split [lindex $list $i] {}]
		puts $pw_to_test
		
		if {[lindex $pw_to_test [lindex $range 0]] == $letter} {
			if {[lindex $pw_to_test [lindex $range 1]] == $letter} {
				puts "Double occurence"
			} else {
				puts "Single occurence front"
				incr valid_passwords
			}
		} else {
			if {[lindex $pw_to_test [lindex $range 1]] == $letter} {
				puts "Single occurence back"
				incr valid_passwords
			} else {
				puts "No occurence"
			}
		}

	}

	puts "Anzahl:"
	puts $valid_passwords
}