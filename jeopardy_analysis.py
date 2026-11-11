import pandas as pd
import numpy as np

jeopardy = pd.read_csv('jeopardy.csv')

# Preview the dataset
print(jeopardy.head(10))

# Filter questions containing both "King" and "England"
filtered = jeopardy[
    jeopardy[' Question'].apply(
        lambda question: all(
            word.lower() in question.lower().split()
            for word in ['King', 'England']
        )
    )
]
print(filtered)

# Convert monetary values to float
jeopardy['Float Values'] = jeopardy[' Value'].apply(
    lambda value: np.nan if value == 'no value'
    else float(value.replace('$', '').replace(',', ''))
)
print(jeopardy['Float Values'].mean())

# Count unique answers
def count_unique_answers(data):
    return data[' Answer'].nunique()

print(count_unique_answers(jeopardy))

# Explore and convert dates
print(jeopardy[' Air Date'].head(10))
print(jeopardy[' Air Date'].dtype)

jeopardy[' Air Date'] = pd.to_datetime(jeopardy[' Air Date'])

print(jeopardy[' Air Date'].dtype)
print(jeopardy[' Air Date'].dt.year.head(10))

# Filter questions by decade
jeopardy_90s = jeopardy[
    (jeopardy[' Air Date'].dt.year >= 1990) &
    (jeopardy[' Air Date'].dt.year <= 1999)
]

jeopardy_2000s = jeopardy[
    (jeopardy[' Air Date'].dt.year >= 2000) &
    (jeopardy[' Air Date'].dt.year <= 2009)
]

# Find questions containing "Computer"
questions_90s = jeopardy_90s[
    jeopardy_90s[' Question'].str.contains('Computer', case=False, na=False)
]

questions_2000s = jeopardy_2000s[
    jeopardy_2000s[' Question'].str.contains('Computer', case=False, na=False)
]

print(questions_90s.shape[0])
print(questions_2000s.shape[0])

# Explore question data
print(questions_90s.head())
print(questions_2000s.head())

# Explore rounds and categories
print(jeopardy[' Round'].value_counts())
print(jeopardy[' Category'].value_counts().head(10))

# Compare categories across Jeopardy rounds
cat_round = jeopardy[
    jeopardy[' Round'] != 'Final Jeopardy!'
]

category_round_table = pd.crosstab(
    cat_round[' Category'],
    cat_round[' Round']
)

print(category_round_table)
print(category_round_table.loc['LITERATURE'])
