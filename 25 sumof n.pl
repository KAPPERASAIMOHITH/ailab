% Knowledge base
subject(math).
subject(science).
subject(history).
subject(english).

teacher(mr_smith, math).
teacher(mr_jones, science).
teacher(mrs_davis, history).
teacher(miss_adams, english).

student(john, math).
student(sarah, science).
student(emma, history).
student(ryan, english).

code(math, m101).
code(science, s202).
code(history, h303).
code(english, e404).

% Generate questions
generate_question(Question) :-
    subject(Subject),
    teacher(Teacher, Subject),
    student(Student, Subject),
    code(Subject, Code),
    format(atom(Question), 'Who teaches ~w to ~w, which has code ~w, and is taken by ~w?', [Subject, Student, Code, Teacher]).

% Example query to generate a question
% ?- generate_question(Question).
