set input [open "./input.txt" "r"]
set lines [list]
while {![eof $input]} {
	lappend lines [gets $input]
}

##puts $lines
variable accumulator 0
variable pc 0
variable visited [list]
variable exitflag 0
variable replace_line -1

proc execute {command} {
	variable pc
	variable accumulator
	variable exitflag
	variable replace_line
	set cmd [lindex $command 0]
	#puts $command
	#puts $cmd
	#puts $pc

	if {$cmd == "acc"} {
		incr accumulator [lindex $command 1]
		incr pc
	}

	if {$cmd == "jmp"} {
		if {$replace_line == $pc} {
			incr pc 1
		} else {
			incr pc [lindex $command 1]
		}
	}

	if {$cmd == "nop"} {
		if {$replace_line == $cmd} {
			incr pc [lindex $command 1]
		} else {
			incr pc 1
		}
	}

	if {$cmd == "exit"} {
		set exitflag 1
	}
}

proc replace {} {
	variable lines
	variable replace_line
	set counter $replace_line
	incr counter
	#puts $counter

	while {1} {
		set curr_line [lindex $lines $counter]
		set cmd [lindex $curr_line 0]
		#puts $cmd

		if {$cmd == "jmp" || $cmd == "nop"} {
			set replace_line $counter
			puts "New replaceline is:"
			puts $replace_line
			return
		}
		incr counter
	}
}

while {1} {
	if {$exitflag == 0} {
		if {[lsearch $visited $pc] == -1} {
			lappend visited $pc
			execute [lindex $lines $pc]
			##puts $visited
		} else {
			puts "Loop found"
			replace
			set visited [list]
			set pc 0
			set accumulator 0
		}
	} else {
		puts "Exit found"
		puts $accumulator
		return
	}
}