% Define days to be scheduled.
day(d1; d2; d3; d4; d5; d6; d7; d8; d9; d10; d11; d12; d13; d14; d15; d16; d17; d18; d19; d20; d21; d22; d23; d24; d25; d26; d27; d28; d29; d30; d31).

% Define employees and their required work days.
employee(matthias, 8).
employee(fabian, 14).
employee(michelle, 15).
employee(oliver, 6).
employee(philine, 5).
employee(alissia, 5).
employee(monika, 4).
employee(laura, 5).

% Matthias unavailability
-available(matthias, d1).
-available(matthias, d2).
-available(matthias, d8).
-available(matthias, d9).
-available(matthias, d10).
-available(matthias, d11).
-available(matthias, d12).

% Fabian unavailability
-available(fabian, d2).
-available(fabian, d3).
-available(fabian, d4).
-available(fabian, d5).

% Michelle unavailability
-available(michelle, d9).
-available(michelle, d10).
-available(michelle, d19).
-available(michelle, d20).

% Oliver unavailability
-available(oliver, d1).
-available(oliver, d9).
-available(oliver, d17).
-available(oliver, d26).

% Philine unavailability
-available(philine, d7).
-available(philine, d13).
-available(philine, d14).
-available(philine, d18).
-available(philine, d20).
-available(philine, d21).
-available(philine, d25).
-available(philine, d28).

% Alissia unavailability

% Monika unavailability
-available(monika, d3).
-available(monika, d4).
-available(monika, d5).

% Laura unavailability

