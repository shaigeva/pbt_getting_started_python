# 01 - Initial setup

## What is this?
This is a part of a [getting started](https://propertybasedtesting.com/learning-path-python/) series from [PropertyBasedTesting.com](https://propertybasedtesting.com).

Specifically, this chapter corresponds to [this part of the series](https://propertybasedtesting.com/hello-world-project-setup-python/).

There is a common [README](https://github.com/shaigeva/pbt_getting_started_python) for the repo where you can find setup instructions.

# About this chapter
This chapter is here just to make sure that you're successfully set up technically.

Start with setup described on the common [README](https://github.com/shaigeva/pbt_getting_started_python).

Now `cd` into this directory in terminal and run this:
```sh
./devtools/run_tests_watch.sh
```
This runs the tests in "watch" mode, so they will re-run when you change things.

You're supposed to see something like this:
```

[Thu Feb 24 11:59:30 2022] Running: py.test
======================== test session starts ===================
platform darwin -- Python 3.9.6, pytest-7.0.1, pluggy-1.0.0
rootdir: /Users/username/proj/pbt_getting_started_python/chapters/01_initial_setup
plugins: xdist-2.5.0, forked-1.4.0, hypothesis-6.37.2
collected 2 items

tests/code_test.py ..                                                                                                                                                         [100%]

======================== 2 passed in 0.51s ===================

```

Now edit the code file: `chapters/01_initial_setup/src/code.py` - just add a newline or a comment.<br/>
In the terminal you're expecting to see the tests run again.

Now we'll do the same thing with the tests file: `chapters/01_initial_setup/tests/code_test.py` - again, add a newline or comment and you should see the tests run again.

And last thing, we have an examples file to help you play around with inputs to the test function.<br/>
Terminate the test process, and run this:
```sh
./devtools/print_examples.sh
```

You're expecting to see something like this:
```
sort_func([]) = []
sort_func([1]) = [1]
sort_func([1, 2]) = [1, 2]
sort_func([2, 1]) = [1, 2]
sort_func([1, 1]) = [1, 1]
sort_func([1, 2, 3]) = [1, 2, 3]
sort_func([1, 3, 2]) = [1, 2, 3]
sort_func([2, 1, 3]) = [1, 2, 3]
sort_func([2, 3, 1]) = [1, 2, 3]
sort_func([3, 1, 2]) = [1, 2, 3]
sort_func([3, 2, 1]) = [1, 2, 3]
sort_func([1, 2, 2]) = [1, 2, 2]
sort_func([1, 1, 2]) = [1, 1, 2]
sort_func([1, 1, 1]) = [1, 1, 1]
```
Edit the file `chapters/01_initial_setup/src/print_examples.py` and add another example, then run the script again to make sure you see your new example.

That's it! Everything works and you're ready to start learning about property-based testing!
