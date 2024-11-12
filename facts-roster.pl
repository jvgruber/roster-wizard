% Define days to be scheduled.
day(d1; d2; d3; d4; d5; d6; d7; d8; d9; d10; d11; d12; d13; d14; d15; d16; d17; d18; d19; d20; d21; d22; d23; d24; d25; d26; d27; d28; d29; d30; d31).

% Define employees and their required work days.
employee(matthias, 8).
employee(fabian, 14).
employee(michelle, 14).
employee(oliver, 7).
employee(philine, 5).
employee(alissia, 5).
employee(monika, 4).
employee(laura, 5).


% Matthias unavailability
-available(matthias, d4).
-available(matthias, d5).
-available(matthias, d6).
-available(matthias, d12).
-available(matthias, d23).
-available(matthias, d24).
-available(matthias, d25).
-available(matthias, d26).
-available(matthias, d31).

% Fabian unavailability
-available(fabian, d7).
-available(fabian, d8).
-available(fabian, d14).
-available(fabian, d15).
-available(fabian, d21).
-available(fabian, d22).
-available(fabian, d24).
-available(fabian, d27).
-available(fabian, d28).
-available(fabian, d29).
-available(fabian, d30).

% Michelle unavailability
-available(michelle, d1).
-available(michelle, d7).
-available(michelle, d8).
-available(michelle, d19).
-available(michelle, d21).
-available(michelle, d22).
-available(michelle, d23).
-available(michelle, d24).
-available(michelle, d25).

% Oliver unavailability
-available(oliver, d1).
-available(oliver, d2).
-available(oliver, d3).
-available(oliver, d4).
-available(oliver, d5).
-available(oliver, d6).
-available(oliver, d7).
-available(oliver, d8).

% Philine unavailability
-available(philine, d1).
-available(philine, d2).
-available(philine, d3).
-available(philine, d5).
-available(philine, d9).
-available(philine, d10).
-available(philine, d12).
-available(philine, d17).
-available(philine, d18).
-available(philine, d19).
-available(philine, d20).
-available(philine, d21).
-available(philine, d22).
-available(philine, d23).
-available(philine, d24).
-available(philine, d25).
-available(philine, d26).
-available(philine, d27).

% Alissia unavailability
-available(alissia, d2).
-available(alissia, d4).
-available(alissia, d5).
-available(alissia, d6).
-available(alissia, d9).
-available(alissia, d11).
-available(alissia, d12).
-available(alissia, d13).
-available(alissia, d16).
-available(alissia, d18).
-available(alissia, d19).
-available(alissia, d20).
-available(alissia, d23).
-available(alissia, d24).
-available(alissia, d26).

% Monika unavailability
-available(monika, d7).
-available(monika, d8).
-available(monika, d14).
-available(monika, d15).
-available(monika, d21).
-available(monika, d22).
