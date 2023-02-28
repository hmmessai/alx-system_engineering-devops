# Regular Expressions

A regular expression, commonly called a “regexp”, is a sequence of characters that define a search pattern.  It is mainly for use in pattern matching with strings, or string matching (i.e. it operates like a “find and replace” command). While it is a very powerful tool, it is also very dangerous because of its complexity.

In this project I worked through some problems that need to use regexp's assistance to solve. All the files are built for the Oniguruma library.

1. [0-simply_match_school](./0-simply_match_school.rb): matches any string with the "School" sequence in it.
2. [1-repetition_token_0](./1-repetition_token_0.rb): matches a 'hbtn' string which has a repetition of the 't' char 2 to 5 times.
3. [2-repetition_token_1](./2-repetition_token_1.rb): matches a 'hbtn' string which has no or one 'b' character.
4. [3-repetition_token_2](./3-repetition_token_2.rb): matches a 'hbtn' string which has one or more 't' character.
5. [4-repetition_token_3](./4-repetition_token_3.rb): matches a 'hbtn' string which doesn't allow other character in between and have no or more 't' character.
6. [5-beginnning_and_end](./5-beginning_and_end.rb): matches any string that starts with 'h' ends with 'n' and can have any single character in between.
7. [6-phone_number](./6-phone_number.rb): matches a 10 digit phone number.
8. [7-OMG_WHY_ARE_YOU_SHOUTING](./7-OMG_WHY_ARE_YOU_SHOUTING.rb): matches only capital letters.
9. [100-textme](./100-textme.rb): extracts the sender, reciever, flags from a TextMe app transactions log file.
