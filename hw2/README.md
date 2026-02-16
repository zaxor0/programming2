# State vs Strategy Pattern

## Part 1: Code Analysis:
1. What are the design problems with ChatClient?
    - When we need to add any new ways of sending a messages, we have to add another if statement inside the send method.
2. Why does the use of conditionals make the code hard to extend and maintain?
    - 

## Part 2: Pattern Decision
Which pattern is more appropriate, Strategy or State? Answer the following questions:
1. Does the behavior change because the *client configures it*, or because the object *changes over time*?
    - The behavior changes becuase the client selected the method of sending the messaging.
2. Who is responsible for switching the behavior: the client or the object itself?
    - the client does this, it has a `set_mode` method.
3. Based on your answers, which pattern is the correct choice and why?
    - it seems that the strategy pattern is best here, we would not have to have so many IF statements

## Part 3: Refactoring
If you choose Strategy:
- Extract the message-processing logic into a separate strategy classes
- Remove all conditional logic from the ChatClient
If you choose state:
- Represent each mode as a separate state class
- Allow the client to transition between staes through method calls

Your final ChatClient should delegate *behavior* rather than implement it directly.

## Part 4: UML Diagram
Provide a UML class diagram that clearly shows:
- The contect class (ChatClient)
- The abstract strategy or the state interface
- All concrete strategy or state classes
- The relationship type used, composition or association


