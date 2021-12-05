variable input [read [open "./input.txt" "r"]]

variable size 1000

variable c_inp [list]
variable map [list]

for {set row 0} {$row < $size} {incr row} {
	set line [list]
	for {set col 0} {$col < $size} {incr col} {
		lappend line 0
	}
	lappend map $line
}

for {set i 0} {$i < [llength $input]} {incr i} {
	if {[lindex $input $i] == "->"} {
		continue
	}
	lappend c_inp [lindex $input $i]
}

#puts $c_inp

for {set i 0} {$i < [llength $c_inp]} {incr i} {
	#puts "I is: [set i]"
	set Xer [list]
	set Yer [list]
	set pair [split [lindex $c_inp $i] ","]
	lappend Xer [lindex $pair 0]
	lappend Yer [lindex $pair 1]

	incr i

	set pair [split [lindex $c_inp $i] ","]
	lappend Xer [lindex $pair 0]
	lappend Yer [lindex $pair 1]

	# puts "Pair 1 is X: [lindex $Xer 0] Y: [lindex $Yer 0]"
	# puts "Pair 2 is X: [lindex $Xer 1] Y: [lindex $Yer 1]"


	if {[lindex $Xer 0] == [lindex $Xer 1] || [lindex $Yer 0] == [lindex $Yer 1]} {
		set Xer [lsort -integer $Xer]
		set Yer [lsort -integer $Yer]
		for {set row [lindex $Yer 0]} {$row <= [lindex $Yer 1]} {incr row} {
			for {set col [lindex $Xer 0]} {$col <= [lindex $Xer 1]} {incr col} {
				set val [lindex $map $row $col]
				lset map $row $col [incr val]
			}
		}	
	} else {
		variable length [expr [lindex $Xer 0] - [lindex $Xer 1]]
		if {$length < 0} {
			set length [expr $length * -1]
		}

		#puts "Length is: [set length]"

		variable x_pos [lindex $Xer 0]
		variable y_pos [lindex $Yer 0]

		variable x_step 1
		if {[lindex $Xer 0] > [lindex $Xer 1]} {
			set x_step -1
		}

		variable y_step 1
		if {[lindex $Yer 0] > [lindex $Yer 1]} {
			set y_step -1
		}

			set t_x_pos 0
			set t_y_pos 0
		for {set diag 0} {$diag <= $length} {incr diag} {
			set t_x_pos [expr $x_pos + $diag * $x_step]
			set t_y_pos [expr $y_pos + $diag * $y_step]
			#puts "XPos is: [set t_x_pos]"
			#puts "YPos is: [set t_y_pos]"
			#puts "+++++++++"

			set val [lindex $map $t_y_pos $t_x_pos]
			#puts $val
			lset map $t_y_pos $t_x_pos [incr val]
		}
		# puts "Map:"
		# foreach var $map {
		# 	puts $var
		# }
	}

	#puts "###############################"
}

# puts "Map:"
# foreach var $map {
# 	puts $var
# }

puts "##########################################################"

puts "Size: [set size]"

variable cross_count 0
for {set row 0} {$row < $size} {incr row} {
	for {set col 0} {$col < $size} {incr col} {
		set val [lindex $map $row $col]
		if {$val > 1} {

			incr cross_count
		}
	}
}

puts "There are [set cross_count] crosspoints"