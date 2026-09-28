"""
Hermetic Vacuum Magnetic Drive & Gas Loop Performance Model
Author: Abhishek Singh
Repository: hermetic-vacuum-tribology-drive
"""

import numpy as np

def calculate_heat_extraction(delta_T: float, m_dot: float = 0.28, cp: float = 850.0) -> float:
    """
    Calculates convective heat removal rate (kW) for He-Xe gas loop.
    """
    Q_watts = m_dot * cp * delta_T
    return Q_watts / 1000.0  # Convert to kW

def calculate_eddy_loss(rpm: float, sigma: float = 0.0, B_peak: float = 0.45, 
                        thickness: float = 0.001, volume: float = 5e-6) -> float:
    """
    Calculates induction power loss in containment barrier.
    For Si3N4 ceramic, sigma = 0.0 S/m yielding 0.0 W.
    """
    omega = rpm * (2.0 * np.pi / 60.0)
    P_loss = 0.5 * sigma * ((omega * B_peak * thickness) ** 2) * volume
    return float(P_loss)

if __name__ == "__main__":
    delta_T_test = 200.0  # deg C
    rpm_test = 10000.0
    
    Q_kW = calculate_heat_extraction(delta_T_test)
    P_eddy = calculate_eddy_loss(rpm_test)
    
    print(f"=== HERMETIC VACUUM DRIVE VERIFICATION ===")
    print(f"Heat Extraction Rate (@ Delta T = {delta_T_test} C): {Q_kW:.2f} kW")
    print(f"Si3N4 Ceramic Barrier Eddy Loss (@ {rpm_test:.0f} RPM): {P_eddy:.2f} W")
