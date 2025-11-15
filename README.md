# Training API for semi-advanced Python courses

Hi. I teach Python! And the problem with Python is, after you get past the basics, there's all sorts of things you can do with it! Makes for a great language, obviously, but also means designing a course that goes beyond is... tricky. But I think I've finally managed to distill things down to what semi-advanced students want. And to that end, I've written this little thing that I'm going to be tutoring on. Did I succeed? We'll see!

## How do I run this?

Same as you would your usual poetry-backed FastAPI thing:

```shell
$ poetry run uvicorn training_api.main:app --reload
```

Then, go to [the usual place for the docs](http://localhost:8000/docs) to see what you can do.