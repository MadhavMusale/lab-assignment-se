import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Step 1: Collect data from the user
try:
    n = int(input("Enter the number of data points: "))  # Number of readings

    # Collect screen time data
    print("\nEnter screen time readings (in hours):")
    screen_time = []
    for i in range(n):
        value = float(input(f"Screen time for data point {i+1}: "))
        screen_time.append(value)

    # Collect performance data
    print("\nEnter performance readings (e.g., test scores, productivity):")
    performance = []
    for i in range(n):
        value = float(input(f"Performance for data point {i+1}: "))
        performance.append(value)

    # Step 2: Create a DataFrame
    data = {
        "Screen Time (hours)": screen_time,
        "Performance": performance
    }
    df = pd.DataFrame(data)

    # Step 3: Compute the correlation matrix
    correlation_matrix = df.corr()

    # Step 4: Print and visualize the correlation matrix
    print("\nCorrelation Matrix:")
    print(correlation_matrix)

    # Visualize the correlation matrix
    plt.figure(figsize=(6, 4))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title("Correlation Matrix: Screen Time vs Performance")
    plt.show()

except Exception as e:
    print(f"An error occurred: {e}")