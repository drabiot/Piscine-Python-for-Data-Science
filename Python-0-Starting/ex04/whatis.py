# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 17:32:31 by tchartie          #+#    #+#              #
#    Updated: 2026/01/29 17:42:11 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	assert (len(sys.argv) > 1), ""
	assert (len(sys.argv) <= 2), "AssertionError:  more than one argument is provided"
	assert sys.argv[1].isdigit() or (sys.argv[1].startswith(('+', '-')) and sys.argv[1][1:].isdigit()) , "AssertionError: argument is not an integer"

	if (int(sys.argv[1]) % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
		
	return(0)

if __name__ == "__main__":
    try:
        main()
    except AssertionError as error:
        print(error)
