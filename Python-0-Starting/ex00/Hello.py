# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Hello.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: tchartie <tchartie@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/27 14:03:58 by tchartie          #+#    #+#              #
#    Updated: 2026/01/27 14:16:10 by tchartie         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

#your code here
ft_list[1] = "World!"

ft_tmp_tuple = list(ft_tuple)
ft_tmp_tuple[1] = "France!"
ft_tuple = tuple(ft_tmp_tuple)

ft_set.remove("tutu!")
ft_set.add("Angoulême!")

ft_dict["Hello"] = "42Angoulême"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
