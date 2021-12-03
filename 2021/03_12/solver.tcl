variable input [read [open "./input.txt" "r"]]

proc solve {} \
{
	variable input
	set counter_one 	[list 0 0 0 0 0 0 0 0 0 0 0 0]
	set counter_zero	[list 0 0 0 0 0 0 0 0 0 0 0 0]
	set gamma_word 		[list]
	set epsilon_word	[list]
	set gamma 0
	set epsilon 0

	foreach element $input \
	{
		set word [split $element {}]

		for {set i 0} {$i < [llength $word]} {incr i} \
		{
			if {[lindex $word $i] == 1} \
			{
				lset counter_one $i [expr [lindex $counter_one $i] + 1]
			}
			if {[lindex $word $i] == 0} \
			{
				lset counter_zero $i [expr [lindex $counter_zero $i] + 1]
			}
		}

	}

	for {set i 0} {$i < [llength $counter_one]} {incr i} \
	{
		if {[lindex $counter_one $i] > [lindex $counter_zero $i]} {
			lappend gamma_word 1
			lappend epsilon_word 0
		} else {
			lappend gamma_word 0
			lappend epsilon_word 1
		}
	}

	set gamma [join $gamma_word {}]
	set epsilon [join $epsilon_word {}]

	set gamma [expr "0b$gamma"]
	set epsilon [expr "0b$epsilon"]

	puts "Product (Part1): [expr $gamma * $epsilon]"

	set bits [list]
	for {set i 0} {$i < [llength $counter_one]} {incr i} {
		if {[lindex $counter_one $i] > [lindex $counter_zero $i]} {
			lappend bits 1
		} else {
			lappend bits 0
		}
	}

	set ogr $input
	set co2 $input
	set result_A 0
	set result_B 0


	set bitpos 0

	while {$bitpos < 12} {
		set templist [list]
		set 0_count 0
		set 1_count 0
		set bit 0

		foreach element $ogr {
			set word [split $element {}]
			if {[lindex $word $bitpos] == 0} {
				incr 0_count
			} else {
				incr 1_count
			}
		}

		if {$1_count >= $0_count} {
			set bit 1
		}

		foreach element $ogr {
			set word [split $element {}]

			if {[lindex $word $bitpos] == $bit} {
				lappend templist $element
			}
		}

		if {[llength $templist] == 1} {
			set result_A [lindex $templist 0]
			break
		} elseif {[llength $templist] == 0} {
			error "WTF"
		} else {
			set ogr $templist
			puts [llength $templist]
			incr bitpos
		}	
	}

	set bitpos 0

	while {$bitpos < 12} {
		set templist [list]
		set 0_count 0
		set 1_count 0
		set bit 1

		foreach element $co2 {
			set word [split $element {}]
			if {[lindex $word $bitpos] == 0} {
				incr 0_count
			} else {
				incr 1_count
			}
		}

		if {$0_count <= $1_count} {
			set bit 0
		}

		foreach element $co2 {
			set word [split $element {}]

			if {[lindex $word $bitpos] == $bit} {
				lappend templist $element
			}
		}

		if {[llength $templist] == 1} {
			set result_B [lindex $templist 0]
			break
		} elseif {[llength $templist] == 0} {
			error "WTF"
		} else {
			set co2 $templist
			puts [llength $templist]
			incr bitpos
		}	
	}

	puts "A: [set result_A]"
	puts "B: [set result_B]"

	set A [expr "0b$result_A"]
	set B [expr "0b$result_B"]

	puts "FINAL 2 : [expr $A * $B]"
}