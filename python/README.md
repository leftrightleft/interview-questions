# BaDCOdE
Badcode is an example Python application which is riddled with errors.  There are security errors, logic errors, syntax problems, and general formatting issues.  

The intention is to get a sense of what kinds of issues the candidate will find.

The best approach is to sit with your candidate and have them do a code review with you.  Share the file with them and have them talk through it as though it were a PR.

You're trying to get a sense of how aware they are of these problems; but more so, it's a great opportunity to get a sense of how the candidate communicates!  

Answer some of these questions to yourself as the candidate is reviewing the code:
* Are they asking additional questions about the code? 
* Are they clearly articualte what the issues are and why they are bad?
* Can they elaborate on how to fix the issues?
* Can they give examples of how to prevent these problems?

## The Issues
Among others, this is a list of issues located in 
* General - poorly named module, no docs, docstrings, or logging
* Lines 3-8:  You should never have secrets stored in your code...
* Line 10: There is a mutable object as a default parameter.  More [here](https://florimond.dev/en/posts/2018/08/python-mutable-defaults-are-the-source-of-all-evil/#:~:text=In%20Python%2C%20when%20passing%20a,or%20even%20a%20class%20instance.)
* Line 12: SQL injection - should be parameterizing the query
* Line 10-14: no error handling
* Line 17: Logging sensitive data
* Line 17: using print instead of logging facility
* Line 20: SQL injection
* Line 22: Comparing string values with `is` instead of `==`
* Line 26: Except:pass (terrible error handling)
* Line 31: Not restricting to GET requests
* Line 38: Returning the username and password in clear text in the body
* Line 38: ALWAYS returning a 200 no matter the result of the lookup for the password

