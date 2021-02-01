set file [open "./input.txt" "r"]
variable current_dataset [list]
variable valid_datasets 0
variable checklist {"byr" "iyr" "eyr" "hgt" "hcl" "ecl" "pid"}
variable eyecolors {"amb" "blu" "brn" "gry" "grn" "hzl" "oth"}

proc check_dataset {} {
	variable current_dataset
	variable checklist
	variable eyecolors
	variable valid_datasets
	set valid 1
	set temp_dataset [list]
	puts $current_dataset
	foreach element $current_dataset {
		lappend temp_dataset [lindex [split $element ":"] 0]
	}

	foreach var $checklist {
		if {[lsearch $temp_dataset $var] == -1} {
			set valid 0
		} 
	}
	
	if {$valid == 1} {
		set current_dataset [join [split $current_dataset ":"]]

		set byr_index [lsearch $current_dataset "byr"]
		puts $byr_index
		set byr_num [lindex $current_dataset [expr $byr_index + 1]]
		if {$byr_num < 1920 || $byr_num > 2002} {
			puts "Byr does not fit"
			set valid 0
		} else {
			puts "Byr fitts"
		}

		set iyr_index [lsearch $current_dataset "iyr"]
		puts $iyr_index
		set iyr_num [lindex $current_dataset [expr $iyr_index + 1]]
		if {$iyr_num < 2010 || $iyr_num > 2020} {
			puts "Iyr does not fit"
			set valid 0
		} else {
			puts "Iyr fitts"
		}

		set eyr_index [lsearch $current_dataset "eyr"]
		puts $eyr_index
		set eyr_num [lindex $current_dataset [expr $eyr_index + 1]]
		if {$eyr_num < 2020 || $eyr_num > 2030} {
			puts "Eyr does not fit"
			set valid 0
		} else {
			puts "Eyr fitts"
		}

		set hgt_index [lsearch $current_dataset "hgt"]
		puts $hgt_index
		set hgt_num [lindex $current_dataset [expr $hgt_index + 1]]
		
		set hgt_num [split $hgt_num {}]
		puts $hgt_num
		puts [llength $hgt_num]
		set identifier [lindex $hgt_num [expr [llength $hgt_num] -1]]
		puts $identifier
		set hgt_num [lreplace $hgt_num end end]
		set hgt_num [lreplace $hgt_num end end]
		set hgt_num_one "[lindex $hgt_num 0][lindex $hgt_num 1][lindex $hgt_num 2]"
		puts $hgt_num_one

		if {$identifier == "m"} {
			if {$hgt_num_one < 150 || $hgt_num_one > 193} {
			puts "Hgt does not fit in cm"
			set valid 0
			} else {
				puts "Hgt fitts in cm"
			}
		}
		if {$identifier == "n"} {
			if {$hgt_num_one < 59 || $hgt_num_one > 76} {
			puts "Hgt does not fit in in"
			set valid 0
			} else {
				puts "Hgt fitts in in"
			}
		}
		if {$identifier != "m" && $identifier != "n"} {
			puts "missing scale"
			set valid 0
		}

		set hcl_index [lsearch $current_dataset "hcl"]
		puts $hcl_index
		set hcl_num [lindex $current_dataset [expr $hcl_index + 1]]		

		if {[string index $hcl_num 0] == "#" && [string length $hcl_num] == 7} {
			set hcl_num [string replace $hcl_num 0 0 ""]
			puts $hcl_num
			if {[string is xdigit $hcl_num] == 1} {
				puts "Hcl fitts"
			} else {
				puts "hcl does not fit"
				set valid 0
			}
		} else {
			puts $hcl_num
			puts "Hcl Wrong start or too short"
			set valid 0
		}

		set ecl_index [lsearch $current_dataset "ecl"]
		puts $ecl_index
		set ecl_num [lindex $current_dataset [expr $ecl_index + 1]]	

		if {[lsearch $eyecolors $ecl_num] == -1} {
			puts $ecl_num
			puts "no valid eyecolor"
			set valid 0
		} else {
			puts "Ecl okay"
		}

		set pid_index [lsearch $current_dataset "pid"]
		puts $pid_index
		set pid_num [lindex $current_dataset [expr $pid_index + 1]]
		if {[string length $pid_num] != 9} {
			puts $pid_num
			puts "pid too short"
			set valid 0
		} else {
			if {[string match {*?[0-9]} $pid_num]} {
				puts $pid_num
				puts "Pid is okay"
			} else {
				puts $pid_num
				puts "Pid is not valid"
				set valid 0
			}
		}
	}





	if {$valid == 1} {
		incr valid_datasets
		puts "Is valid set"
	} else {
		puts "Is no valid set"
	}
	set current_dataset [list]
	puts "#################################################################"
}


while {1} {

	gets $file line
	if {[eof $file]} {
		check_dataset
		break
	}
	if {$line == ""} {
		check_dataset
		continue
	}
	foreach element $line {
		lappend current_dataset $element	
	}
}

puts "Valid dataset count:"
puts $valid_datasets
