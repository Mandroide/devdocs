# Generate a noisy signal to be filtered:

from scipy import signal
import matplotlib.pyplot as plt
rng = np.random.default_rng()
t = np.linspace(-1, 1, 201)
x = (np.sin(2*np.pi*0.75*t*(1-t) + 2.1) +
     0.1*np.sin(2*np.pi*1.25*t + 1) +
     0.18*np.cos(2*np.pi*3.85*t))
xn = x + rng.standard_normal(len(t)) * 0.08

# Create an order 3 lowpass butterworth filter:

b, a = signal.butter(3, 0.05)

# Apply the filter to xn.  Use lfilter_zi to choose the initial condition of
# the filter:

zi = signal.lfilter_zi(b, a)
z, _ = signal.lfilter(b, a, xn, zi=zi*xn[0])

# Apply the filter again, to have a result filtered at an order the same as
# filtfilt:

z2, _ = signal.lfilter(b, a, z, zi=zi*z[0])

# Use filtfilt to apply the filter:

y = signal.filtfilt(b, a, xn)

# Plot the original signal and the various filtered versions:

plt.figure
plt.plot(t, xn, 'b', alpha=0.75)
plt.plot(t, z, 'r--', t, z2, 'r', t, y, 'k')
plt.legend(('noisy signal', 'lfilter, once', 'lfilter, twice',
            'filtfilt'), loc='best')
plt.grid(True)
plt.show()
