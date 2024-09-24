import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

# Reactor volume for CSTR
def cstr_volume(F0, r, C0, X):
    return F0 * X / (-r) 

# Reactor volume for PFR
def pfr_volume(F0, r, C0, X):
    return F0 / (-r * C0) * (-np.log(1 - X))

# Plot the conversion profile for PFR
def plot_pfr_profile(F0, r, C0, X_target):
    X_values = np.linspace(0, X_target, 100)
    V_values = pfr_volume(F0, r, C0, X_values)
    
    # plt.plot(V_values, X_values, label='PFR Conversion Profile')
    plt.xlabel('Reactor Volume (L)')
    plt.ylabel('Conversion X')
    # plt.title('PFR Conversion Profile')
    # plt.grid(True)
    # plt.legend()
    # st.pyplot(plt.gcf())

# Plot the conversion as a function of reactor volume for CSTR
def plot_cstr_profile(F0, r, C0, X_target):
    X_values = np.linspace(0.01, X_target, 100)
    V_values = cstr_volume(F0, r, C0, X_values)
    
    plt.plot(V_values, X_values, label='CSTR Conversion Profile', color='orange')
    plt.xlabel('Reactor Volume (L)')
    plt.ylabel('Conversion X')
    plt.title('CSTR Conversion Profile')
    plt.grid(True)
    plt.legend()
    st.pyplot(plt.gcf())

# Streamlit UI
st.title('Chemical Reactor Calculator: CSTR vs PFR')

# User inputs
F0 = st.number_input('Molar Flow Rate (mol/s)', min_value=0.1, value=1.0)
r = st.number_input('Reaction Rate Constant (1/s)', min_value=0.0001, value=0.1)
C0 = st.number_input('Initial Concentration (mol/L)', min_value=0.1, value=1.0)
X_target = st.slider('Target Conversion (X)', min_value=0.01, max_value=0.99, value=0.8, step=0.01)

# Calculating reactor volumes
V_cstr = cstr_volume(F0, r, C0, X_target)
V_pfr = pfr_volume(F0, r, C0, X_target)

st.subheader('Reactor Volume Calculations')
st.write(f'CSTR Volume: {V_cstr:.2f} L')
st.write(f'PFR Volume: {V_pfr:.2f} L')

# Plotting conversion profiles
st.subheader('Conversion Profiles')
plot_pfr_profile(F0, r, C0, X_target)
plot_cstr_profile(F0, r, C0, X_target)

# Conclusion
st.subheader('Comparison of CSTR and PFR')
if V_cstr > V_pfr:
    st.write('PFR is more efficient (requires less volume) than CSTR for the same conversion.')
else:
    st.write('CSTR is more efficient (requires less volume) than PFR for the same conversion.')
