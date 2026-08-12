Here, I have compiled the notes for the Programming Paradigms chapter in BICP 306, a course taken during my 6th semester of BSc Bioinformatics.

# Programming Paradigms
Programming paradigm is basically a philosophy of writing computer programs. It is problem solving style that tells us **how code should be structured** and **how logic should be expressed.**

> A paradigm gives a programmer a mental model for solving problems. It helps programmers to choose a suitable approach for a specific task.

### 📍Importance of Programming Paradigms
- They help structure thinking before writing code.
- They improve code organization, readability and problem solving.
- They support modularity and reusability of code.
- They help reduce confusion in large programs / codebases.
> Without a paradigm , code can become a random collection of instructions.

There are many programming paradigms, but the common ones are:
1. Functional Programming Paradigm 
2. Procedural Programming Paradigm
3. Imperative Programming Paradigm
4. Declarative Programming Paradigm
5. Object-Oriented Programming Paradigm etc.


```markdown
Q.) Why multiple paradigms exist, why one paradigm is not enough?

-> Different problems require different ways of thinking and different approaches to solve them.
No single paradigm is perfect for every problem. Some paradigm / style are:

    a. Very clear but less flexible.
    b. Very fast but hard to maintain.
    c. Very expressive but slow or hard to optimize, etc.

Thus, different problems require different styles, so multiple paradigms exist.
Programmers can choose the most suitable paradigm for a specific problem or even combine paradigms to leverage their strengths.
```
>These paradigms differ mainy in :  
    **a. How they view a problem    
    b. How they solve problems**


## 1. Imperative Programming Paradigm
> Think of imperative programming as giving a computer a set of instructions to follow, step by step, to achieve a desired outcome. It focuses on **how** to perform tasks.

- It is a programming approach where the programmers tells the computer how to do something step by step.
- The program is written as a sequence of instructions that **change the program's state as execution moves forward**.

### 📍Main Idea of Imperative Paradigm
- Focus on steps and commands.
- The programmer controls the order of execution and the flow of the program.
- The program updates variables as it runs.
- Logic is expressed through **explicit instructions** and control structures (like loops and conditionals).

### 📍Key Features of Imperative Paradigm
- Uses variables to store and update values / data.
- Uses assignments to change values during execution.
- Uses control structures such as :
    - Loops (for, while) to repeat actions.
    - Conditionals (if, else) to make decisions.

```python
seq = "TATATAGCGCATTAGCGATAA"
gc_count = 0
at_count = 0
for nucleotide in seq:
    
    if nucleotide in "GC":
        gc_count += 1

    elif nucleotide in "AT":
        at_count += 1

print(f"GC count: {gc_count}")
print(f"AT count :{at_count}")
```

Why is this imperative?

- `gc_count` and `at_count` are initialized to 0.
- The program goes through the DNA sequence one nucleotide at a time.
- An `if` statement checks each nucleotide.
- `gc_count` and `at_count` are changed using += 1. [**State Modification**]
- The instructions are executed in a specific sequence.(**Step-by-step**)



## 2. Procedural Programming Paradigm
- Procedural paradigm is the structured form of imperative programming  where the step by step instructions (or code) are organized into **procedures** / **functions**.
- Instead of writing everything in one long sequence, the program is divided into smaller reusable blocks.
- Procedural paradigm still follows the imperative(step by step) style, but in a **cleaner structure** as it emphasizes **modularity** and **code reuse**.
- Function call & return are central to Procedural style. 

```markdown
**Think of it this way**

Imperative is the broader category:
"Tell the computer what to do, step by step."

Procedural is a style within imperative programming:
"Organize those step-by-step instructions into procedures/functions."
```
```python
# Procedural Programming Example : We have put the same logic as above into a function.
def count_bases(seq):
    gc_count = 0
    at_count = 0

    for nucleotide in seq:
        if nucleotide in "GC":
            gc_count += 1
        elif nucleotide in "AT":
            at_count += 1

    return gc_count, at_count
```
### 📍Main Idea of Procedural Paradigm :
 - The program is split into procedures / functions.
 - Each procedure performs a specific task.
 - The main program calls these procedures in needed order.

> Procedural paradigm is better or useful than a single long block of instructions because:
> - makes program modular and reduces repition.
> - improves readability.
> - makes debugging easier as logics are separated into parts.

## 3. Functional Programming Paradigm
```
      Input                       Output
        x ------> [Function] -----> y
- x is transformed into y.
- Transformation of data happens through function.
```

- Functional Paradigm is the programming approach based on the concept of **'chain of transformation.'**
- It is built by combining functions that transform the data from one form to another.
- It uses **pure functions** and prefers **immutability** of data. It avoids changing state and mutable data.
- Functional Paradigm is used when the solution to problems are **predictable** and can be expressed as a series of transformations on data.


> **Pure Function:**    
> A function is said to be pure if it:
> 1. always produces the same output for the same input & 
> 2. *does not have any side effects* (like modifying a global variable or changing the state of an object).  
>  
> **Pure functions make programs more predictable and easier to test.**


## 4. Declarative Programming Paradigm
- Declarative = expressing / declaring what should happen.
- It is the approach where the programmer focuses on **what result is wanted** and **not the exact steps to achieve it** .
- The language / framework handles the process behind the scenes.
- Focuses on **what** (i.e Result) , not **how** (i.e Process).
> Declarative paradigm is  good for Query Languages, example : SQL.

### 📍Main Idea of Declerative Paradigm
- We state the goal, conditions or result.
- We do not describe every low-level step to achieve the result.
- The underlying system or framework takes care of the implementation details.


## Summary
| Paradigm | Main Focus | Style of thinking | Common Strength|
| :--- | :--- | :--- | :--- |
| Imperative | How to solve the problem | Step-by-step | Direct Control |
| Procedural | How, using functions | Broken into procedures | Modular Code |
| Functional | Data transformation via functions | Function chains | Predictability |
| Declarative | What result is needed | Specific result & constraints | Simplicity of intent |
