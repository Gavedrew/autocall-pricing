import numpy as np
 
np.random.seed(0)
 
# --- Paramètres ---
S0 = 100
T = 5
dt = 1
sigma = 0.2
r = 0.02
N = 1000
coupon = 0.08
autocall_level = 1.00 * S0
protection_barrier = 0.60 * S0
nominal = 100
 
# --- Fonction : simuler un chemin de prix ---
def simulate_path(S0, T, r, sigma, dt):
    prices = [S0]
    for _ in range(T):
        shock = np.random.normal()
        S = prices[-1] * np.exp((r - 0.5 * sigma**2) * dt + sigma * np.sqrt(dt) * shock)
        prices.append(S)
    return prices
 
# --- Fonction : calculer le payoff ---
def autocall_payoff(path):
    for i in range(1, len(path)):
        if path[i] >= autocall_level:
            return nominal * (1 + coupon * i)   # coupons mémoire
    final = path[-1]
    if final >= protection_barrier:
        return nominal * (1 + coupon * T)
    else:
        return nominal * (final / S0)
 
# --- Simulation Monte Carlo ---
results = []
autocall_count = 0
capital_loss_count = 0   # chemins avec perte en capital
 
for _ in range(N):
    path = simulate_path(S0, T, r, sigma, dt)
    payoff = autocall_payoff(path)
    results.append(payoff)
 
    autocalled = any(p >= autocall_level for p in path[1:])
 
    if autocalled:
        autocall_count += 1
    elif path[-1] < protection_barrier:   # pas autocallé ET barrière cassée
        capital_loss_count += 1
 
# --- Résultats ---
print(f"Average payoff         : {np.mean(results):.2f}")
print(f"Autocall probability   : {autocall_count / N:.1%}")
print(f"Capital loss probability: {capital_loss_count / N:.1%}")
print(f"Worst case payoff      : {min(results):.2f}")
