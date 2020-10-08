# Curve-Grader
Determines letter grades for a list of exam scores based on number of standard deviations from the mean.

Assignment Instructions

First, The first step involves reading the list of exam scores from the input. Here, all exam grades will be entered in a single line separated by commas. 
  This means that the string obtained from input() needs to be converted to a list with the split() method. 
  However, the split() method yields a list of strings and we want to use the exam scores as integer numbers. 
  Therefore, we have to do an additional type conversion. The int() function only works on single strings and not on a whole list, 
  so you will need to use a loop to convert all the numbers entered by the user to a list.
  
Second, In statistics, the mean and the standard deviation are used to describe a collection of numbers.
  The mean is the average value of the sequence while the standard deviation describe how much variation the numbers have with regards to the mean. 
  Given a list of numbers, there are different ways of calculating the mean and the standard deviation in Python. 
  Later in the class, we will see how Python modules such as numPy offer this functionality as a function.
  There are efficient algorithms to calculate both the mean and the standard deviation at the same time but a simpler solution would be to first calculate the mean by using an accumulating loop or the sum() function. 
  Then, use the mean in a second loop to sum up the individual components for each element in the list until you finally divide the accumulated value by n and take the square root to get the standard deviation.
  
 Third, For the last part, you should go over the list of exam scores again, using a for loop, and for each, decide what letter grade the score should be assigned. 
  Essentially, if the score is better than the sum of the mean and one and a half times the standard deviation, then that student should be assigned an A, 
  if the score is less than that but still higher than the mean plus half a standard deviation, then the student should get a B and so on. 
  Finally, you should print the grades all in one line separated by commas. 
  
    Example Interaction:
     > Enter Exam Scores:
      < 52,63,54,77,65,36,46,27
     > Mean: 52.50 StdDev: 15.14
     > Grades: C,B,C,A,B,D,C,F
