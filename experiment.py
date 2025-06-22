import plotly.graph_objects as go
import random
from plotly.subplots import make_subplots

def experiment():
    # Trials without gaps
    n_trials = 1000
    rolls = [randint(1,6) for _ in range(n_trials)]
    running_averages = [sum(rolls[:i])/i for i in range(1, n_trials+1)]
    
    rolls2 = [randint(1,6) for _ in range(n_trials)]
    running_averages2 = [sum(rolls2[:i])/i for i in range(1, n_trials+1)]
    
    # Insert None between each pair of elements
    with_gaps = []
    for i, val in enumerate(running_averages2):
        with_gaps.append(val)
        if i < len(running_averages2) - 1:
            for _ in range(30):
                with_gaps.append(None)
    
    running_averages2 = with_gaps

    # Create Plotly figure
    fig = go.Figure()
    
    # Add running average line
    fig.add_trace(go.Scatter(y=running_averages, mode='markers', name='Average of rolls'))
    
    # Add average while there are gaps
    fig.add_trace(go.Scatter(y=running_averages2[:n_trials], mode='markers', name='Average of rolls'))
    
    # Add expected value line
    fig.add_trace(go.Scatter(y=[3.5]*n_trials, mode='lines', name='Expected value (3.5)', line=dict(dash='dash', color='red')))
    
    # Update layout
    fig.update_layout(
        title="Convergence of Dice Roll Averages to Expected Value",
        xaxis_title="Number of Rolls",
        yaxis_title="Average",
        hovermode="x unified"
    )
    
    # Show interactive plot
    fig.show()
    fig.write_html("experiment_3.html")

experiment()