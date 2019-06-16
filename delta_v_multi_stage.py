# determine delta v for a multi stage rocket

from delta_v_functions import delta_v_calc

############################ CONSTANTS ########################################

GRAVITY_EARTH = 9.81    # meters / second squared

###############################################################################

############################ VARIABLES ########################################

specific_impulse = 0.0  # seconds

v_exhaust = 0.0

delta_v_total = 0.0

mass_payload = 0.0

number_of_stages = 0

# for mass_stage list:
#           index 0 is structure,
#           index 1 is propellant,
#           index 2 is Specific Impulse

mass_stage = list()

delta_v_data = list()

###############################################################################
# TODO Remove code below after testing
# # Stage 1
# mass_initial_1 = 115000.0
# mass_final_1 = 65000.0

# # Stage 2
# mass_initial_2 = 50000.0 + 5000.0 + 5000.0
# mass_final_2 = 5000.0 + 5000.0


# mass_stage = [[mass_initial_1, mass_final_1],
#               [mass_initial_2, mass_final_2],
#               ]
###############################################################################

if __name__ == "__main__":

############################ INPUTS ###########################################
    #
    # Gather number of stages and then gather information for each stage
    # Inputs: number of stages
    #         mass of payload
    #         Specific Impulse of each engine (assumes one engine per stage)
    #
    #         For each stage:
    #               mass of structure
    #               mass of propellant

    #### PRODUCTION INPUT CODE --- BYPASSING DURING BUILD

    while True:

        try:
            number_of_stages = int(input('Enter the number of stages (n > 0): '))

            if number_of_stages <= 0:
                print('Please enter an integer greater than zero')
                continue

        except ValueError as err:
            print(err)
            print('Please enter an integer greater than zero')
            continue
        break

    while True:
        try:
            mass_payload = int(input('Enter payload mass (kg > 0): '))

            if mass_payload <= 0:
                print('Please enter an integer greater than zero')
                continue

        except ValueError as err:
            print(err)
            print('Please enter an integer greater than zero')
            continue
        break

    # Get structure, propellant & specific impulse for each stage
    for stage_add_data in range(number_of_stages):
        print('=' * 40)
        print('*** Stage - {} ***'.format(stage_add_data + 1))

        while True:
            try:
                mass_struct = int(input('Enter structure mass (kg > 0): '))

                if mass_struct <= 0:
                    print('Please enter an integer greater than zero')
                    continue

            except ValueError as err:
                print(err)
                print('Please enter an integer greater than zero')
                continue
            break

        while True:
            try:
                mass_prop = int(input('Enter propellant mass (kg) > 0: '))

                if mass_prop <= 0:
                    print('Please enter an integer greater than zero')
                    continue

            except ValueError as err:
                print(err)
                print('Please enter an integer greater than zero')
                continue
            break

        while True:
            try:
                specific_impulse = int(input('Enter specific impulse for engine(sec > 0): '))

                if specific_impulse <= 0:
                    print('Please enter an integer greater than zero')
                    continue

            except ValueError as err:
                print(err)
                print('Please enter an integer greater than zero')
                continue
            break

        mass_stage.append([mass_struct,
                           mass_prop,
                           specific_impulse,
                           ])

    # TODO  REMOVE BEFORE FLIGHT
    print('*** TEST *** mass_stage >>>', mass_stage[stage_add_data])
    print('payload mass (kg):', mass_payload)

###############################################################################

# ####### Input data for calculations during build phase #################

#     # Mass for each stage

#     mass_stage = [[5000.0, 50000.0, 450],
#                   [5000.0, 50000.0, 450],
#                   [3000.0, 50000.0, 450],
#                   ]

#     mass_payload = 5000.0
#     specific_impulse = 450
#     number_of_stages = 2

###############################################################################

############################ CALCULATE ########################################

    # TODO remove testing code once finalized
    print('payload mass (kg):', mass_payload)
    print(mass_stage)
    print('length of mass_stage list: ', len(mass_stage))
    print('**** END ****')

    # For each stage, gather Mass Initial and Mass Final (Mass Final includes
    # Structure)

    for delta_v_stage_number in range(0, number_of_stages):

        mass_initial = 0
        mass_final = 0

        for current_stage in range(delta_v_stage_number, number_of_stages):
            print('stage number: ', delta_v_stage_number + 1)
            print('stage to include in delta v calculation: ', current_stage + 1)

            # calculate Mass Initial and Mass Final for current stage
            mass_initial += (mass_stage[delta_v_stage_number][0] +
                             mass_stage[delta_v_stage_number][1]
                             )

        mass_initial += mass_payload  # need to include payload
        mass_final = mass_initial - mass_stage[delta_v_stage_number][1]
        v_exhaust = mass_stage[delta_v_stage_number][2] * GRAVITY_EARTH

        print(f"Stage {delta_v_stage_number} Mass Initial: {mass_initial:,}")
        print(f"Stage {delta_v_stage_number} Mass Final: {mass_final:,}")
        print(f"Stage {delta_v_stage_number} V Exhaust: {v_exhaust:,.4f}")

        delta_v_data.append(delta_v_calc(mass_initial,
                                         mass_final,
                                         v_exhaust,
                                         ))

        print('=' * 40)

    print('**** delta_v_data: ****')

    for _, delta_v_figure in enumerate(delta_v_data):
        print(f"Delta V for stage {_ + 1}: {delta_v_figure:,.4f}")

    print(f"Total Delta V: {sum(delta_v_data):,.4f}")
