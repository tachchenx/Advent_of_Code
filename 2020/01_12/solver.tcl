set temp [open "./input.txt" "r"]
set eingabe [read $temp]
foreach o_element $eingabe {
	foreach i_element $eingabe {
		foreach 3_element $eingabe {
			if {[expr $o_element + $i_element + $3_element] == 2020} {
				puts "Product"
				puts [expr $o_element * $i_element * $3_element]
				return
			}
		}
	}
}
