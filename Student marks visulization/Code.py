import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv('student_marks_100.csv')
print(df.head())

# Count occurrences of each (Gender, Grade) combination
gg_count = df[['Gender', 'Grade']].value_counts().reset_index(name='Count')

# Create labels for x-axis like "Male-A", "Female-B"
labels = gg_count['Gender'] + '-' + gg_count['Grade']

# Plot bar chart
plt.figure(figsize=(8, 4))
plt.bar(labels, gg_count['Count'], color='orange')
plt.title("Bar chart: Count by Gender and Grade")
plt.xlabel('Gender-Grade')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()

# Save and show the plot
plt.savefig("Gender_Grade_bar.png")
plt.show()

# 📈 Line plots of marks trends

# Subjects to plot
subjects = ['Math', 'Science', 'English', 'History', 'Geography']

# Plot settings
plt.figure(figsize=(12, 6))

# Plot each student's marks as a light-colored line
for i, row in df.iterrows():
    marks = [row[subj] for subj in subjects]
    plt.plot(subjects, marks, color='lightgray', linewidth=1)

# Optional: plot average trend line
average_marks = df[subjects].mean()
plt.plot(subjects, average_marks, color='red', linewidth=3, marker='o', label='Average')

# Final touches
plt.title("📈 Subject-wise Marks Trend for All Students (with Average)", fontsize=14)
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.ylim(0, 100)
plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('Plot_Marks_trends.png')
plt.show()

# 🟢 Scatter plots (compare subject scores)


subject_score = ['Math', 'Science', 'English', 'History', 'Geography']
x_pos = list(range(len(subject_score)))  # [0, 1, 2, 3, 4]

for i, row in df.iterrows():
    marks = [row[subj] for subj in subject_score]
    plt.scatter(x_pos, marks, color='gray', alpha=0.3)

plt.xticks(x_pos, subject_score)  # Replace numbers with subject names
plt.title("🟢 Subject Score Scatter Plot")
plt.xlabel("Subjects")
plt.ylabel("Score")
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('Comapre_subject_score.png')
plt.show()


# 🧮 Group-wise averages (e.g., average marks by gender or grade)

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV
df = pd.read_csv('student_marks_100.csv')

# List of subjects
subjects = ['Math', 'Science', 'English', 'History', 'Geography']

# Group by Gender and calculate mean
avg_by_gender = df.groupby('Gender')[subjects].mean()        # if we want with grade just replace gender

# Plot
avg_by_gender.T.plot(kind='bar', figsize=(8, 5), colormap='Set2')
plt.title("📊 Average Subject Marks by Gender")
plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.ylim(0, 100)
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.savefig('Avg_Marks_Gender.png')
plt.show()

# 🧱 Simport pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("student_marks_100.csv")

# Subjects list
subjects = ['Math', 'Science', 'English', 'History', 'Geography']

# Group by Gender and compute mean
grouped = df.groupby('Gender')[subjects].mean()

# Create subplots (1 row, 5 columns)
fig, axes = plt.subplots(1, len(subjects), figsize=(18, 4), sharey=True)

# Loop through each subject and corresponding subplot
for i, subject in enumerate(subjects):
    axes[i].bar(grouped.index, grouped[subject], color=['skyblue', 'salmon'])
    axes[i].set_title(subject)
    axes[i].set_xlabel("Gender")
    if i == 0:
        axes[i].set_ylabel("Avg Marks")
    axes[i].set_ylim(0, 100)

# General layout and display
plt.suptitle("📊 Subject-wise Average Marks by Gender", fontsize=16)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig('Average Marks by Gender.png')
plt.show()

# this is complete code