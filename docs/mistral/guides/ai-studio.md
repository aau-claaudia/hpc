# AI Studio

## What is AI Studio?

AI Studio is the part of Mistral intended for more structured experimentation. It is a better fit than Le Chat when you want to work deliberately with prompts, model behavior, and repeatable AI-assisted workflows.

## When to use AI Studio

AI Studio is especially useful when you want to:

* test several prompt variants against the same task
* compare different model behaviors
* develop reusable prompt structures
* move from casual exploration toward a more repeatable workflow
* prototype AI-assisted tasks before integrating them elsewhere

## A simple workflow

1. Define the task you want to solve.
2. Write a clear prompt or instruction set.
3. Test the prompt on a few representative examples.
4. Adjust the wording until the output becomes more consistent.
5. Document the prompt pattern that works best for your use case.

## Good practices

* Start with a small, representative test case.
* Change one thing at a time when refining prompts.
* Compare outputs across several examples instead of relying on a single result.
* Save successful prompt structures in your own project documentation.
* Make human review part of the workflow from the beginning.

## When Le Chat is enough

If you mainly need quick day-to-day assistance, [Le Chat](/mistral/guides/le-chat/) will often be faster and simpler than AI Studio.

## Important limitations

!!! warning "Avoid sensitive or regulated data"
    Until the rules for the AAU deployment are fully documented, AI Studio should be treated as unsuitable for confidential, personal, or otherwise sensitive information.

!!! info "Document what works"
    AI Studio becomes more valuable when successful prompts, examples, and evaluation criteria are written down so the workflow can be repeated and improved over time.
