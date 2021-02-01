set input [open "./input.txt" "r"]

set ans_count 0
set ans_list [list]
set reset 0

while {1} {
	gets $input line
	if {[eof $input]} {
		incr ans_count [llength $ans_list]
		#puts $ans_list
		break
	}
	if {$line == ""} {
		incr ans_count [llength $ans_list]
		#puts $ans_list
		set ans_list [list]
		set reset 0
		continue
	}


	if {[lindex $ans_list 0] == "" && $reset == 0} {
		set split_line [split $line {}]
		foreach element $split_line {
			lappend ans_list $element
		}
		#puts "liste war leer"
		#puts $ans_list
		set reset 1
		continue
	}



	set split_line [split $line {}]
	set temp_list [list]
	foreach letter $split_line {
		set result [lsearch $ans_list $letter]
		if {$result != -1} {
			lappend temp_list $letter
			#puts "Buchstabe [set letter] war vorhanden"
		}
	}
	set ans_list $temp_list

}

puts "Ans-Count :"
puts $ans_count