# Delta V Functions

import math


def delta_v_calc(mass_initial,
                 mass_final,
                 v_exhaust,
                 ):

    """
    Delta -V is the maximum change of velocity of the rocket (if no other
    external forces act)

    The Delta-V function utilizes the Ideal Rocket Equation:

    Delta V equals Exhaust Velocity times the natural logarithm of Initial
    Mass divided by Final Mass

    where
         - Initial Mass includes the mass of the payload, structure and
           propellant. Final Mass is the Initial Mass less the Propellant Mass

         - Exhaust Velocity equals the Specific Impulse of the Engine times
           the Gravitational Acceleration of Earth (9.81 meters per second
           squared)
    """

    return v_exhaust * math.log(mass_initial / mass_final)
