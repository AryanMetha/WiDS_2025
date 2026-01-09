import matplotlib
matplotlib.use("TkAgg")
from mc_control import mc_control
import numpy as np
import matplotlib.pyplot as plt
from sarsa_lambda import sarsa_lambda
from sarsa_lambda_linear import sarsa_lambda_linear

# ---- Monte Carlo Control ----
def plot_value_function(Q,title):
    dealer = range(1,11)
    player = range(1,22)
    V = np.zeros((21,10))
    for d in dealer:
        for p in player:
            if (d,p) in Q:
                V[p-1,d-1] = max(Q[(d,p)].values())
    plt.figure(figsize=(8,6))
    plt.imshow(V,origin="lower",aspect="auto")
    plt.colorbar(label="V*(s)")
    plt.xlabel("Dealer Showing")
    plt.ylabel("Player Sum")
    plt.title(title)
    plt.show()
print("Running Monte Carlo Control")
Q_mc = mc_control(episodes=200000)
print("Done")
plot_value_function(Q_mc,"Monte-Carlo Optimal Value Function")

# ----SARSA(λ) ----
print("Computing Q* using Monte Carlo")
Q_star = mc_control(200000)
lambdas = np.arange(0,1.1,0.1)
final_mse = []
learning_curves = {}
for lmbda in lambdas:
    print(f"Running SARSA(λ={lmbda})")
    Q,mse_curve = sarsa_lambda(lmbda,Q_star)
    final_mse.append(mse_curve[-1])
    if lmbda == 0 or lmbda == 1:
        learning_curves[lmbda] = mse_curve
plt.figure()
plt.plot(lambdas,final_mse,marker="o")
plt.xlabel("λ")
plt.ylabel("Mean Squared Error")
plt.title("MSE vs λ")
plt.show()
for lmbda in learning_curves:
    plt.figure()
    plt.plot(learning_curves[lmbda])
    plt.xlabel("Episode")
    plt.ylabel("Mean Squared Error")
    plt.title(f"Learning Curve (λ={lmbda})")
    plt.show()

# ---- Linear SARSA(λ) ----
print("Running Linear SARSA(λ)")
final_mse_linear = []
learning_curves_linear = {}
for lmbda in lambdas:
    print(f"Linear SARSA(λ={lmbda})")
    theta,mse_curve = sarsa_lambda_linear(lmbda,Q_star)
    final_mse_linear.append(mse_curve[-1])
    if lmbda == 0 or lmbda == 1:
        learning_curves_linear[lmbda] = mse_curve
plt.figure()
plt.plot(lambdas,final_mse_linear,marker="o")
plt.xlabel("λ")
plt.ylabel("Mean Squared Error")
plt.title("Linear SARSA(λ): MSE vs λ")
plt.show()
for lmbda in learning_curves_linear:
    plt.figure()
    plt.plot(learning_curves_linear[lmbda])
    plt.xlabel("Episode")
    plt.ylabel("Mean Squared Error")
    plt.title(f"Linear SARSA Learning Curve (λ={lmbda})")
    plt.show()