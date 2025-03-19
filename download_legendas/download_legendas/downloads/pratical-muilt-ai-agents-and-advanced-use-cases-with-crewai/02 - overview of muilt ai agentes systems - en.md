In this lesson, we're going to do an overview of multi-AI agent systems.

We're going to talk about how the building blocks that goes into building these AI agents.

We're going to talking about agents themselves but also tasks and crews and all the different things that makes these agents work.

Things like caching, memory, guardrails and everything in between.

This is going to be great to catch you up on everything that you need to know to start your journey with AI agent systems.

So let's dive into the lesson.

What you learn in this course.

You'll learned so much.

We will talk about Multi agentic automation in the real world.

What that means is that you're going to get your hands dirty and you're going to build so many different projects that are going to allow you to understand how to build this automations out there for any different use case you might have.

You're going to build an automated project planning using crews and multi agents.

You're going to also build a project monitoring use case in the lead qualification and scoring.

And there's so much more.

We're going to talk about analysis and report on support data about custom content creation and scale in many other use cases.

So stick around because this is going to be a lot of fun.

So before we start talking about this, let's check a quick example on how powerful those systems can be and what kind of automations you can actually get out from them.

So let's start by watching this quick example.

In here, you can see that I'm about to jump into a call with the CEO of Zendesk.

So I want to have some sales materials.

I just put his email in there in we start by doing a research on Tom.

We learned that he has a background in sales and marketing and leadership.

And we also learned a lot about Zendesk.

We know that Zendesk is founded in 2007.

And all this data was research done by agents.

And now these agents put together this landing page slash PDF that we can export and actually send to Tom.

And this PDF is going over CrewAI, but from Zendesk's perspective.

It's talking all about Zendesk culture, and how they're trying to make complexity simpler.

It's a very cool use case where you can see these agents not only doing research, but actually producing a full report that can assist us on coming out of a call, for example.

And there's so many other use cases out there.

We can see a lot of operational automations.

And there is many sales use cases in there as well.

We also see a lot of marketing use cases, code development, research, education, support.

There's a lot of different use cases going over so many different verticals.

And the thing is, independently of what vertical you're building use cases for, we're definitely see a common pattern.

There is kind of like a long tail distribution of what these agents in this automation are trying to do.

It's usually start with you pulling data out of existing systems.

Sometimes those systems are going to be ERP or CRM or a database or whatever it might be.

Once you extract this data from there, there's usually a step of research, and research here you can be researching in documents or on the internet or other systems that you might have.

But after that, you go through a process of analysis.

And analysis can be comparing this data or extracting specific data, or even inferring new data that you didn't have before.

After some analysis, most of use cases go through a process of summarization, where you want to extract learnings and plot charts, or building like specific executive summaries, and then by the end of it, you can go for reporting.

And sometimes you want this report as a PDF or as a json, so then you can push that into another system or as a markdown.

The thing is that by the end of this, you probably will want to push this into an existing system.

So independently of what is the vertical, if it's sales, if it's marketing, if it's H.R., whatever it might be.

Most of the use cases usually go around some of this process of research and analysis, summarization and reporting.

Not necessarily all of them and not necessarily always in this series of steps.

But these is the bulk of the use cases that we see out there.

There's of course, companies that are pushing this to the cutting edge in trying to do very innovative things by using video models and image models and so much more.

And we're going to talk about some of that as well.

So, quick recap.

If this is your first time getting to know multi-agent systems and CrewAI, I want to talk about what are them and how to build them.

So there is a difference between regular apps that we have building as engineers throughout the years in this new kind of AI apps.

If you think about regular apps, it usually is very strong typed.

What I mean by that, is that you have a very good understanding of what is the data that's coming into your application, and you also have a great understanding of what are the transformations that this data is going to go through in order to give you your expected output.

So a good example of this would be a system where you're getting inputs from a lead form, and you will understand that you have a series of conditions that depending on these answers, you're going to have a series of automations or outputs.

But then if you look at these new apps, what I'm calling here, AI apps, they're extremely different.

Because now they're way more fuzzy.

That means that you don't have a good understanding on what are the data that is coming in to this.

For example, if you think about ChatGPT, you don't know if the text that user's putting there is a recipe or a PhD thesis or whatever it might be, it's fuzzy.

And then this data goes through a model that is a black box, and that then goes into a fuzzy output because you don't know what the output will be.

It really depend heavily on the input and the model.

So you can think about Multi-AI agents as a kind of AI app that is way more fuzzy.

But because of that, it allows you to build automations that were just not possible before, because now you don't need to treat for every single edge case out there.

You can basically let your agents decide on real time how they're going to react to specific data and deciding what tools to use in order to achieve the task that you want it to do.

And when you look at these agents, what are their anatomy? Well, it starts pretty simple.

You have an LLM in the center, and this LLM can have access to some tools.

And once you give this LLM a task, it's going to find a way to use these tools in order to provide you a final answer.

And when you go one step higher, what you see is actually this multi-agent systems where now you just don't have one agent, but you have two, three or many more.

And now these agents can not only use tools themselves, but they can delegated work to each other, and they can ask questions to each other in order to accomplish whatever is the final outcome that you want it to.

And it starts usually pretty simple, but once that you start to bring this automation into a production setting, what do you realize is there's so many needs you're going to have to learn that you're going to need a caching layer.

So whatever tools your agents are using, they're not consuming and necessary credits.

And using these tools over and over and over again.

You also want to make sure that they have a memory layer, so they remember what they have done in the past, and they share their memory with each other.

So if they ever have come across this same data point again, they will remember and how they handle it in the last time.

There's also training data, something that we're going to talk in this specific lesson.

And I'm so excited about that.

There's also guardrails and how you're going to protect these agents from going into crazy hallucinations and so much more.

And not only all these features, but once that you have these agents working together, you really to think through how you want to orchestrate them.

Sometimes you just want them to do their work sequentially.

Other times, you want to have a manager agent that is going to delegate work and review the output, but you can go crazy on that.

So you can have a hybrid approach where some tasks are going to be performed in parallel, and other tasks are going to wait for multiple tasks to finish before moving on.

And you're going to create an example like this as well.

Others are going to be complete in parallel and others may be completely asynchronous.

So there are so many different use cases.

And also, you can get even more complex if you want to by doing multi-crews.

And you're going to use a feature that we call flows.

Where you're able to hook one crew result with another.

All right.

So you just learned about AI agents, how they work, what are their anatomy, and how you can put them to work together.

Well, what are the main building blocks for building these multi-AI agent systems? Well, everything starts with agents.

But then you also need to make sure that you have the tasks.

In this use case, you can see that we have more tasks than agents.

And that is not a problem because one agent could be doing multiple tasks.

And we're going to see some examples of that.

In order for these agents to be able to accomplish these tasks, we're going to need to give them tools.

So you can either give your agents tools, so they can use data when performing any tasks, or you can give your tasks tools, so your agents know what tools to use in order to accomplish that task.

Once that you have that, you basically have a crew.

A crew is a combination of multi agents and their tasks.

And once that you have all of these agents and tasks, CrewAI comes in time and gives you all the features that you need to run this things in production by adding guardrails to avoid your agents to hallucinate, but also testing so that you can measure the quality of your agents and tasks.

Also allows delegations where your agents can automatically delegate and ask questions to each other, and then training data so you can train these agents even further in the memory.

So these agents get it better over time.

There's so much that we're going to talk about make sure to stick around.

So let's look at these agents and tasks.

Every agent and CrewAI needs to have a role a goal and a backstory.

And every task needs to have a description, an expected output and an agent.

So now these agents are actually defined as Yaml files.

You're going to go over it on our lessons where you can easily see how these agents have their role that goes and their backstory set and their tasks as well with their descriptions and their expected outputs.

This makes extra easy for non-technical people to be able to contribute to these agents and tasks by just having to update Yaml files instead of having to update any code.

All right.

So now that we know that we can create agents and tasks using Yaml files, why do we get our hands dirty? And we built our first crew.

This is going to be so exciting.

Let's go to our next step where we're going to dive into a Jupyter notebook.

And we're going to put together our first crew together.

I'll see you there in a second.