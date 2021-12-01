variable input [read [open "./input.txt" "r"]]

variable preamble_size 25

# proc find {it p_current_num} {
# 	variable preamble_size
# 	variable input

# 	for {set j [expr $it - $preamble_size]} {$j < $it} {incr j} {
# 		for {set k [expr $it - $preamble_size]} {$k < $it} {incr k} {
# 			#puts "j is [set j] with value [lindex $input $j] and k is [set k] and value [lindex $input $k]"
# 			set current_val [expr [lindex $input $j] + [lindex $input $k]]
# 			#puts $current_val
# 			if {$current_val == $p_current_num} {
# 				return 1
# 			}
# 		}
# 	}

# 	return 0
# }

# for {set i $preamble_size} {$i < [llength $input]} {incr i} {
# 	#puts "Looked-at value is [lindex $input $i]"
# 	set current_num [lindex $input $i]
# 	if {[find $i $current_num]} {
# 		#puts "Found"
# 	} else {
# 		puts "not found"
# 		puts "Value is :"
# 		puts [lindex $input $i]
# 		return
# 	}	
# }

variable search_key 2089807806
variable val_list [list]
set sum 0

for {set j 0} {$j < [llength $input]} {incr j} {
	puts $j

	for {set k $j} {$k < [llength $input]} {incr k} {
		if {$sum < $search_key} {
			incr sum [lindex $input $k]
			lappend val_list [lindex $input $k]
			#puts $val_list
		}
		if {$sum > $search_key} {
			puts "Abort"
			set val_list [list]
			set sum 0
			break
		}
		if {$sum == $search_key} {
			puts $val_list
			set sorted [lsort -integer $val_list]
			set answer [expr [lindex $sorted 0] + [lindex $sorted end]]
			puts "Answer is [set answer]"
			return
		}
	}
}

return 0