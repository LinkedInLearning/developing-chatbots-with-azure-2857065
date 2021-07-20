# Developing Chatbots with Azure
This is the repository for the LinkedIn Learning course Developing Chatbots with Azure. The full course is available from [LinkedIn Learning][lil-course-url].

![Developing Chatbots with Azure][lil-thumbnail-url] 
What exactly is a chatbot? How does it differ from a bot, how can you develop one, and how can you use it, once it is developed? Instructor Bhavani Ravi walks you through learning about chatbots and developing your first one. Bhavani begins by describing what a chatbot is, what types of chatbots exist today, and how a chatbot differs from bots and applications. She goes over the components of a chatbot system and discusses the natural language processing (NLP) that allows chatbots to understand requests in human language. She steps through designing a chatbot, then shows you the “brain” of a chatbot: ML models. Bhavani shows you how to use ML models to train your chatbot, challenges you to write your own chatbot, then concludes with some projects that you can work on and submit to GitHub.

## Instructions
This repository has branches for each of the videos in the course. You can use the branch pop up menu in github to switch to a specific branch and take a look at the course at that stage, or you can add `/tree/BRANCH_NAME` to the URL to go to the branch you want to access.

## Branches
The branches are structured to correspond to the videos in the course. The naming convention is `CHAPTER#_MOVIE#`. As an example, the branch named `02_03` corresponds to the second chapter and the third video in that chapter. 
Some branches will have a beginning and an end state. These are marked with the letters `b` for "beginning" and `e` for "end". The `b` branch contains the code as it is at the beginning of the movie. The `e` branch contains the code as it is at the end of the movie. The `main` branch holds the final state of the code when in the course.

When switching from one exercise files branch to the next after making changes to the files, you may get a message like this:

    error: Your local changes to the following files would be overwritten by checkout:        [files]
    Please commit your changes or stash them before you switch branches.
    Aborting

To resolve this issue:
	
    Add changes to git using this command: git add .
	Commit changes using this command: git commit -m "some message"


### Instructor

**Bhavani Ravi**

_Back-End Engineer, Speaker, and Community Leader_

Check out my instructor page on [LinkedIn Learning](https://www.linkedin.com/learning/instructors/bhavani-ravi).

[lil-course-url]: https://www.linkedin.com/learning/developing-chatbots-with-azure
[lil-thumbnail-url]: https://cdn.lynda.com/course/2857065/2857065-1611696629473-16x9.jpg
