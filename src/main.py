from converter import asp2excel

test_input = "assigned(matthias,d1) assigned(matthias,d2) assigned(matthias,d7) assigned(matthias,d8) assigned(matthias,d11) assigned(matthias,d19) assigned(matthias,d21) assigned(matthias,d22) assigned(fabian,d1) assigned(fabian,d3) assigned(fabian,d5) assigned(fabian,d9) assigned(fabian,d10) assigned(fabian,d11) assigned(fabian,d13) assigned(fabian,d16) assigned(fabian,d18) assigned(fabian,d19) assigned(fabian,d20) assigned(fabian,d23) assigned(fabian,d25) assigned(fabian,d26) assigned(michelle,d2) assigned(michelle,d3) assigned(michelle,d4) assigned(michelle,d6) assigned(michelle,d9) assigned(michelle,d10) assigned(michelle,d12) assigned(michelle,d14) assigned(michelle,d15) assigned(michelle,d16) assigned(michelle,d17) assigned(michelle,d20) assigned(michelle,d26) assigned(michelle,d31) assigned(oliver,d12) assigned(oliver,d14) assigned(oliver,d18) assigned(oliver,d21) assigned(oliver,d22) assigned(oliver,d23) assigned(oliver,d25) assigned(philine,d4) assigned(philine,d6) assigned(philine,d7) assigned(philine,d8) assigned(philine,d13) assigned(alissia,d15) assigned(alissia,d17) assigned(alissia,d27) assigned(alissia,d29) assigned(alissia,d30) assigned(monika,d5) assigned(monika,d24) assigned(monika,d28) assigned(monika,d30) assigned(laura,d24) assigned(laura,d27) assigned(laura,d28) assigned(laura,d29) assigned(laura,d31)"

asp2excel(test_input, 12, "December_2024_Calendar.xlsx", "output/")