import statistics
import pandas as pd
import plotly.figure_factory as  ff
import plotly.graph_objects as go

df = pd.read_csv("properties_of_normal_distribution.csv")

math_scores = df["math score"].tolist()

scores_mean = statistics.mean(math_scores)
scores_std_deviation = statistics.stdev(math_scores)
scores_median = statistics.median(math_scores)
scores_mode = statistics.mode(math_scores)

print("Mean of the data is -> " + format(scores_mean))
print("Median of the data is -> " + format(scores_median))
print("Mode of the data is -> " + format(scores_mode))
print("Stardard Deviation is -> " + format(scores_std_deviation))

#Finding 1 standard deviation start and end values, and 2 standard deviations start and end values
first_std_deviation_start, first_std_deviation_end = scores_mean - scores_std_deviation, scores_mean + scores_std_deviation
second_std_deviation_start, second_std_deviation_end = scores_mean - (2*scores_std_deviation), scores_mean + (2*scores_std_deviation)
third_std_deviation_start, third_std_deviation_end = scores_mean - (3*scores_std_deviation), scores_mean + (3*scores_std_deviation)

#Plotting the chart and lines for mean. 1 standard deviation, and 2 standard deviations
thin_1_std_deviation = [result for result in math_scores if result > first_std_deviation_start and result < first_std_deviation_end]
thin_2_std_deviation = [result for result in math_scores if result > second_std_deviation_start and result < second_std_deviation_end]
thin_3_std_deviation = [result for result in math_scores if result > third_std_deviation_start and result < third_std_deviation_end]

#Finding the percentage of data in the lists
print("{}% of data for math scores lies within 1 standard deviation".format(len(thin_1_std_deviation)*100.0/len(math_scores)))
print("{}% of data for math scores lies within 2 standard deviation".format(len(thin_2_std_deviation)*100.0/len(math_scores)))
print("{}% of data for math scores lies within 3 standard deviation".format(len(thin_3_std_deviation)*100.0/len(math_scores)))

#Plotting the bell curve graph with lines showing standard deviations 
fig = ff.create_distplot([math_scores], ["Math Scores"], show_hist = False)
fig.add_trace(go.Scatter(x=[scores_mean, scores_mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[third_std_deviation_start, third_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[third_std_deviation_end, third_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.show()
