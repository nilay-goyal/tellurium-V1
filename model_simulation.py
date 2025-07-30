import tellurium as te

antimony_str = '''
model kinetic_model_2025
  // Compartment
  compartment TestTube = 1;

  // Species with initial concentrations (mostly 0)
  species rGO in TestTube, Aptaprimer in TestTube, CXCL9 in TestTube;
  species rGO_Aptaprimer in TestTube, CXCL9_Aptaprimer in TestTube;
  species Circle_Template in TestTube, RCA_Complex in TestTube;
  species phi29_polymerase in TestTube, RCA_product in TestTube;

  rGO = 0;
  Aptaprimer = 0;
  CXCL9 = 0;
  rGO_Aptaprimer = 0;
  CXCL9_Aptaprimer = 0;
  Circle_Template = 0;
  RCA_Complex = 0;
  phi29_polymerase = 0;
  RCA_product = 0;

  // Parameters (rate constants)
  kf = 1;
  kf_1 = 1;
  kf_2 = 1;
  kf_3 = 1;

  // Reactions
  // 1) rGO + Aptaprimer -> rGO_Aptaprimer
  J1: rGO + Aptaprimer -> rGO_Aptaprimer; kf * rGO * Aptaprimer;

  // 2) CXCL9 + rGO_Aptaprimer -> CXCL9_Aptaprimer + rGO
  J2: CXCL9 + rGO_Aptaprimer -> CXCL9_Aptaprimer + rGO; kf_1 * CXCL9 * rGO_Aptaprimer;

  // 3) Circle_Template + CXCL9_Aptaprimer -> RCA_Complex
  J3: Circle_Template + CXCL9_Aptaprimer -> RCA_Complex; kf_2 * Circle_Template * CXCL9_Aptaprimer;

  // 4) phi29_polymerase + RCA_Complex -> RCA_product
  J4: phi29_polymerase + RCA_Complex -> RCA_product; kf_3 * phi29_polymerase * RCA_Complex;
end
'''

# Load the model into tellurium
rr = te.loadAntimonyModel(antimony_str)

# Optional: Set some initial concentrations if you want to test simulation
rr['rGO'] = 10
rr['Aptaprimer'] = 5
rr['CXCL9'] = 7
rr['Circle_Template'] = 3
rr['phi29_polymerase'] = 4

# Simulate from 0 to 50 time units, 100 steps
result = rr.simulate(0, 50, 100)

# Plot all species concentrations
rr.plot(title="Kinetic Model 2025 Simulation", xlabel="Time", ylabel="Concentration")

plt.show()  # <--- Add this line to display the plot window
