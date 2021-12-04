variable rands 	[read [open "./nums.txt" "r"]]
variable fields [open "./fields.txt" "r"]

variable nums [split $rands ","]
#puts $nums
#puts "\n"
variable theFields [list]
variable singleField [list]

while {![eof $fields]} {
	set current [gets $fields]
	if {$current == ""} {
		set current [gets $fields]
	}
	lappend singleField $current

	if {[llength $singleField] == 5} {
		lappend theFields $singleField
		set singleField [list]

		# foreach var $theFields {
		# 	foreach element $var {
		# 		puts $element
		# 	}
		# 	puts ""
		# }
	}
}

variable found_index [llength $theFields]
variable num_count [llength $nums]
variable lookup_store [list]

# Gehe alle Bingo-Felder durch
for {set i 0} {$i < [llength $theFields]} {incr i} {
 	
 	#Reset-en des Truth-Table
	set table [list]
	for {set j 0} {$j < 5} {incr j} {
		lappend table [list 0 0 0 0 0]
	}
	set current_field [lindex $theFields $i]

	#Alle Nummern durchgehen
	for {set num_ind 0} {$num_ind < [llength $nums]} {incr num_ind} {
		set current_num [lindex $nums $num_ind]
		#puts "Currrent Num: [set current_num]"

		for {set row 0} {$row < 5} {incr row} {
			for {set col 0} {$col < 5} {incr col} {
				set looking [lindex $current_field $row $col]
				#puts "Looking at: [set looking]"

				if {$looking == $current_num} {
					lset table $row $col 1
					#puts "FOUND [set current_num]!"
					# foreach element $table {
					# 	puts $element
					# }
				}
			}
		}

		set hor 0
		for {set row 0} {$row < 5} {incr row} {
			set hor 0
			for {set col 0} {$col < 5} {incr col} {
				if {[lindex $table $col $row] == 1} {
					incr hor

					if {$hor == 5} {
				
						if {$num_count > $num_ind} {
							set num_count $num_ind
							set found_index $i
							#puts "Found 5 horizontal"
							set lookup_store $table
							break
						}
					}
				}
			}
		}

		set ver 0
		for {set col 0} {$col < 5} {incr col} {
			set ver 0
			for {set row 0} {$row < 5} {incr row} {
				if {[lindex $table $col $row] == 1} {
					incr ver

					if {$ver == 5} {
				
						if {$num_count > $num_ind} {
							set num_count $num_ind
							set found_index $i
							#puts "Found 5 vertical"
							set lookup_store $table
							break
						}
					}
				}
			}
		}

	}

} 

puts "#######"
puts "Fastest Field: [set found_index]"
puts "With Number [lindex $nums $num_count] at Index [set num_count]"
foreach element $lookup_store {
	puts $element
}


variable sum 0
for {set row 0} {$row < 5} {incr row} {
	for {set col 0} {$col < 5} {incr col} {
		if {[lindex $lookup_store $col $row] == 0} {
			incr sum [lindex $theFields $found_index $col $row]
		}
	}
}

puts "Sum is : [set sum]"

variable final [expr $sum * [lindex $nums $num_count]]

puts "Final: [set final]"