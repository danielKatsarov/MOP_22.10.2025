import streamlit as st
import statistics
import matplotlib.pyplot as plt

grades = [5, 6, 4, 6, 3, 5, 4, 6]

avg = statistics.mean(grades)

med = statistics.median(grades)

mode = statistics.mode(grades)

print("Средна стойност:", avg)
print("Медиана:", med)
print("Мода:", mode)

lowest = min(grades)
highest = max(grades)

print("Най-висока оценка:", highest)
print("Най-ниска оценка:", lowest)

count_above_avg = sum(1 for grade in grades if grade > avg)
print("Брой ученици с успех над средния:", count_above_avg)

if (avg >= 5):
    print("Отличен")
elif (avg >= 4):
    print("Много добър")
else:
    print("Трябва повече старание")

st.pyplot(fig)
