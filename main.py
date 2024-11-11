import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns

# Generate synthetic data for students
np.random.seed(0)
data = {
    'Student_ID': [f'S{i}' for i in range(1, 21)],
    'Attendance': np.random.randint(30, 100, size=20),
    'Assignments_Completed': np.random.randint(3, 11, size=20),
    'Quiz_Avg_Score': np.random.randint(35, 95, size=20),
    'Exam_Score': np.random.randint(40, 95, size=20),
    'Participation_Score': np.random.randint(2, 11, size=20)
}

# Create DataFrame
df = pd.DataFrame(data)

# Show basic statistics for context
print("Basic Statistics:\n", df.describe())

# Preprocess data
features = ['Attendance', 'Assignments_Completed', 'Quiz_Avg_Score', 'Exam_Score', 'Participation_Score']
X = df[features]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Apply KMeans clustering
kmeans = KMeans(n_clusters=3, random_state=0)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Summarize each cluster
cluster_summary = df.groupby('Cluster').mean(numeric_only=True)[features]
print("\nCluster Summary:\n", cluster_summary)

# Visualize clusters for two selected features, e.g., Attendance and Exam Score
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Attendance', y='Exam_Score', hue='Cluster', data=df, palette='viridis', s=100)
plt.title('Student Clusters based on Attendance and Exam Score')
plt.xlabel('Attendance')
plt.ylabel('Exam Score')
plt.legend(title='Cluster')
plt.show()

# Analyze and print insights about each cluster
for cluster in cluster_summary.index:
    print(f"\nCluster {cluster} Analysis:")
    avg_attendance = cluster_summary.loc[cluster, 'Attendance']
    avg_exam_score = cluster_summary.loc[cluster, 'Exam_Score']
    
    if avg_attendance < 50:
        print("- Low attendance, these students may need extra support to stay engaged.")
    elif avg_exam_score < 60:
        print("- Lower exam scores, students in this cluster may benefit from targeted teaching support.")
    else:
        print("- This cluster shows better engagement and performance.")
    
    print(f"Average Attendance: {avg_attendance:.2f}")
    print(f"Average Exam Score: {avg_exam_score:.2f}")
