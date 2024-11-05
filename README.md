This repository hosts a set of Python-based calculators built with Streamlit to help with retirement planning, budgeting, and engineering calculations. Each app provides user-friendly interfaces and dynamic data visualization.
1. Problem 1
- Develop a python based app to calculate the heat exchanger performance using the Log Mean Temperature Difference (LMTD) method, which is a common calculation in chemical engineering for designing heat exchangers.
- Project Description:
  - The calculator will take in the following inputs:
    - Inlet and outlet temperatures of both the hot and cold fluids.
    - Heat transfer coefficient.
    - Heat exchanger area. It will then calculate:
        - Log Mean Temperature Difference (LMTD).
        - Heat duty (Q), which is the rate of heat transfer in the heat exchanger.
- This calculator will help chemical engineers quickly calculate and estimate heat exchanger performance based on fluid temperatures and equipment specifications.
2. Problem 2
One common problem in chemical engineering is the Reynolds number calculation and its relationship with flow regime and pressure drop in a pipe. develop an app that will make it easier to estiate the relationship between flow velocity and Reynolds number.
- The app will allow the user to:
  - Input fluid properties (fluid density, viscosity, and flow rate).
  - Input pipe dimensions (diameter, length).
  - Calculate the Reynolds number to classify the flow as laminar, transitional, or turbulent.
  - Display a graph that shows the relationship between the flow velocity and Reynolds number for different flow regimes. Additionally, we’ll plot how pressure drop varies with Reynolds number using the Darcy-Weisbach equation for a given range of Reynolds numbers.
3. Problem 3
Develop a Streamlit-based calculator for a distillation column, which is commonly used in chemical engineering for the separation of liquid mixtures. The app will calculate the number of theoretical stages using the McCabe-Thiele method and plot a graphical representation of the stages on the equilibrium curve and operating lines.
- Project Description: This distillation column app will:
  - Calculate the minimum number of theoretical stages required for the separation using the McCabe-Thiele method.
  - Plot the equilibrium curve and the operating lines.
  - Show the feed line, rectifying section operating line, and stripping section operating line on the graph.
    - Assumptions:
      - Binary distillation (two-component mixture).
      - You have a constant relative volatility ( 𝛼 α).
      - Feed is a mixture of two components (component A and component B).
4. Problem 4
Develop a Streamlit-based calculator for a chemical engineering iterative process that involves phase diagrams, particularly focusing on Vapor-Liquid Equilibrium (VLE) using Raoult's Law. This app will calculate the composition of vapor and liquid phases iteratively using a flash distillation process.
- Project Description:
The app will allow the user to input:
  - Feed composition of a binary mixture.
  - Temperature and pressure conditions.
  - Vapor-Liquid Equilibrium (VLE) data.
  - The app will use Raoult's Law to iteratively calculate the composition of the liquid and vapor phases and plot the phase diagram showing the equilibrium curve and iterative process.
Assumptions:
- Binary mixture of two components, A and B.
- Ideal vapor-liquid equilibrium (Raoult's Law).
- Constant relative volatility ( 𝛼 α) is used for simplicity.
5. Problem 5
Develop a Streamlit-based calculator for a liquid-liquid extraction process, which is a common separation technique in chemical engineering. The app will calculate the equilibrium compositions of two immiscible phases and plot the distribution curve (also known as the tie-line diagram) for a ternary liquid-liquid system. This process is useful in the separation of compounds based on their different solubilities in two immiscible liquids.
- Project Description:
The app will:
  - Calculate the distribution ratio (D) of a solute between two immiscible solvents.
  - Use a distribution curve to visualize the relationship between the solute concentration in the two phases.
  - Plot a tie-line diagram, showing the equilibrium compositions in both phases across different initial solute concentrations.
6. Problem 6
Develop a Streamlit-based iterative app for a common problem in wastewater treatment: calculating the oxygen transfer rate (OTR) in an aeration tank. This process involves iteratively calculating the dissolved oxygen (DO) levels based on oxygen transfer and consumption rates.
- Project Description:
In wastewater treatment, oxygen is supplied to support biological processes in an aeration tank. The oxygen transfer rate (OTR) is crucial for maintaining sufficient dissolved oxygen (DO) levels to meet biological oxygen demand (BOD). This app will:
    - Simulate the dissolved oxygen (DO) profile over time in the aeration tank.
    - Iteratively calculate DO levels using the oxygen transfer and consumption rates.
    - Allow users to adjust parameters such as oxygen transfer efficiency (OTE), oxygen consumption rate, and initial DO. Plot the DO concentration over time.
