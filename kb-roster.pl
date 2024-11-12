%% CONSTRAINTS
% Rule to assign two employees to each day.
% 2 { assigned(E, D) : employee(E, _) } 2 :- day(D).

% Allow up to 2 employees per day.
0 { assigned(E, D) : employee(E, _) } 2 :- day(D).

% Reward solutions with more employees per day.
#maximize { 1, E, D : assigned(E, D) }.

% Employees can only work on days they are available.
:- assigned(E, D), -available(E, D).

% Each employee must work exactly their required number of days.
:- employee(E, N), N != #count { day(D) : assigned(E, D) }.


#show assigned/2.
