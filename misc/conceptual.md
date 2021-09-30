### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python uses indentation to wrap around code instead of curly brackets.
Python uses dunder methods but Javascript does not
Python uses the keyword 'self' in OO programming wheras Javascript uses the keyword 'this'.

- Given a dictionary like `{"a": 1, "b": 2}`: , list two ways you
  can try to get a missing key (like "c") _without_ your programming
  crashing.

printing it with a get function should result back with None instead of error.

In [1]: test1
Out[1]: {'a': 1, 'b': 2}

In [2]: print(test1.get('c'))
None

Another way is to set a default value.

In [3]: test1.setdefault('c', None)

In [4]: print(test1['c'])
None

- What is a unit test?

A test that specifically checks for one small unit such as one function.
This does not test how the whole application application or how the current function interacts with another function.

- What is an integration test?

A test that checks how functions work together.
Usually up to only 2 functions.
This is checking for function interactions.

- What is the role of web application framework, like Flask?

The role of Flask is to provide code to create a server.
This helps define which requests will be made and how they respond.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

The route URL seems more like a link to a new page with something a server would respond to
The URL query param is normally assoicated with the return and submission included from a form to do something like a POST request.

- How do you collect data from a URL placeholder parameter using Flask?

You use <name_of_placeholder> and then name_of_placeholder as a parameter in your route function.

- How do you collect data from the query string using Flask?

request.args['name_of_data']

- How do you collect data from the body of the request using Flask?

request.args.get('id_of_data')

- What is a cookie and what kinds of things are they commonly used for?

A cookie is a name and string value pair and its used to store small information on a particular user.

- What is the session object in Flask?

A session object is a signed encrypted data type that contains info for current browser.

- What does Flask's `jsonify()` do?

jsonify() wraps data around in a JSON format to provide JSON formatted return when called upon.
