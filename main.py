import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# 1. Create a high-resolution function with 1000 points
x_high = np.linspace(0, 10, 1000)
y_high = np.sin(x_high)  # You can replace np.sin with your desired function

# 2. Create a low-resolution function with 10 points
x_low = np.linspace(0, 10, 10)
y_low = np.sin(x_low)  # Same function but with fewer points

# 3. Perform linear interpolation to increase low-resolution function to 1000 points
interp_func = interp1d(x_low, y_low, kind='linear')
y_low_interpolated = interp_func(x_high)

# 4. Calculate errors between the high-resolution and interpolated functions
abs_error = np.abs(y_high - y_low_interpolated)
mae = np.mean(abs_error)  # Mean Absolute Error
mse = np.mean((y_high - y_low_interpolated) ** 2)  # Mean Squared Error
rmse = np.sqrt(mse)  # Root Mean Squared Error
max_error = np.max(abs_error)  # Maximum Error

# 5. Output the error metrics
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"Maximum Error: {max_error}")

# 6. Visualize the original high-resolution function and the interpolated low-resolution function
plt.figure(figsize=(10, 6))
plt.plot(x_high, y_high, label='High Resolution')
plt.plot(x_high, y_low_interpolated, label='Interpolated Low Resolution', linestyle='--')
plt.legend()
plt.title('Function Comparison')
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# 7. Visualize the absolute error between the two functions
plt.figure(figsize=(10, 4))
plt.plot(x_high, abs_error)
plt.title('Absolute Error')
plt.xlabel('x')
plt.ylabel('Error')
plt.show()
