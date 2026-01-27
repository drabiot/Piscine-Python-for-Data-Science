# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    format_ft_time.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 14:18:29 by tchartie          #+#    #+#              #
#    Updated: 2026/01/27 15:31:42 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import datetime
import time

def main():
	date = datetime.datetime.now()
	seconds = time.time()
	
	print("Seconds since January 1, 1970:", f"{seconds:,.4f}", "or " f"{seconds:.2e}", "in scientific notation")
	print(date.strftime("%b"), date.day, date.year)

if __name__ == "__main__":
	main()
