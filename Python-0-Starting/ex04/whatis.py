# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    whatis.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/28 17:32:31 by tchartie          #+#    #+#              #
#    Updated: 2026/01/28 17:47:04 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import sys

def main():
	if (len(sys.argv) <= 1):
		print()
		return(1)
	elif (len(sys.argv) > 2):
		print("AssertionError: more than one argument is provided")
		return(1)

	try:
		arg : int = int(sys.argv[1])
	except:
		print("AssertionError: argument is not an integer")
		return(1)

	if (arg % 2 == 0):
		print("I'm Even.")
	else:
		print("I'm Odd.")
		
	return(0)

if __name__ == "__main__":
	main()
