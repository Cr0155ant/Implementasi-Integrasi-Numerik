import numpy as np
import time

# Fungsi Yang Diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Metode Integrasi Trapezoid
def trapezoid_integral(f, a, b, n):
    width = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * width)
    return total * width

# Menghitung Galat RMS Trapezoid - Referensi
def rms_error_Trapezoid_Referensi(estimated_pi_trapezoid, reference_pi):
    return np.sqrt(np.mean((estimated_pi_trapezoid - reference_pi)**2))

# Referensi Nilai Pi
pi_ref = 3.14159265358979323846

# Nilai N
N_values = [10, 100, 1000, 10000]

# Plot Testing
for N in N_values:
    start_time = time.time()
    estimated_pi_trapezoid = trapezoid_integral(f, 0, 1, N)
    execution_time = time.time() - start_time
    error_trapezoid_ref = rms_error_Trapezoid_Referensi(estimated_pi_trapezoid, pi_ref)

    print(f"Nilai N = {N}")
    print(f"Estimasi Nilai Pi Trapezoid: {estimated_pi_trapezoid}")
    print(f"RMS Error Trapezoid-Referensi (Galat): {error_trapezoid_ref}")
    print(f"Waktu Eksekusi: {execution_time} Detik")
    print("-" * 50)