# Practice_Questions
#QUESTION_1
<p>
  A website requires the users to input username and password to register. Write a program to check the validity of password input by users.
Following are the criteria for checking the password:
1. At least 1 letter between [a-z]
2. At least 1 number between [0-9]
1. At least 1 letter between [A-Z]
3. At least 1 character from [$#@]
4. Minimum length of transaction password: 6
5. Maximum length of transaction password: 12
Your program should accept a sequence of comma separated passwords and will check them according to the above criteria. Passwords that match the criteria are to be printed, each separated by a comma.


Example
</br>If the following passwords are given as input to the program:
</br>ABd1234@1,a F1#,2w3E*,2We3345
Then, the output of the program should be:
</br>ABd1234@1
</p>


</br>

#QUESTION_2

<p>
  A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. The trace of robot movement is shown as the following:
</br>UP 5
</br>DOWN 3
</br>LEFT 3
</br>RIGHT 2
The numbers after the direction are steps. Please write a program to compute the distance from current position after a sequence of movement and original point. If the distance is a float, then just print the nearest integer.


Example:

Input:
</br>UP 5
</br>DOWN 3
</br>LEFT 3
</br>RIGHT 2

</br>Output:
</br>2
  </p>
  </br>
  #Question_3
  
  <p>
  You are going to travel to another city that is located 𝑑 miles away from your home city. Your can can travel at most 𝑚 miles on a full tank and you start with a full tank. Along your way, there are gas stations at distances stop1, stop2, . . . , stop𝑛 from your home city. What is the minimum number of refills needed?
Problem Description

Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.

Ouput Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles on a full tank, and there are gas stations at distances stop1 , stop2 , . . . , stop𝑛 along the way, output the minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to reach the destination, output −1.

Constraints. 1≤𝑑≤105.1≤𝑚≤400.1≤𝑛≤300.0<stop1 <stop2 <···<stop𝑛 <𝑚.


Sample 1.
Input:
</br>950
</br>400
</br>4
</br>200 375 550 750
</br>Output:
</br>2

HINT:
The distance between the cities is 950, the car can travel at most 400 miles on a full tank. It suffices to make two refills: at points 375 and 750. This is the minimum number of refills as with a single refill one would only be able to travel at most 800 miles.




Sample 2.
Input:
</br>10
</br>3
</br>4
</br>1 2 5 9
</br>Output:
</br>-1


HINT:
One cannot reach the gas station at point 9 as the previous gas station is too far away.
</p>
  
  
  
  
  
  
  
  
  
  
  
