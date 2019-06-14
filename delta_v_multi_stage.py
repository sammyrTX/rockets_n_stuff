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

    ##### PRODUCTION INPUT CODE --- BYPASSING DURING BUILD

    # while True:
    #     try:
    #         number_of_stages = int(input('Enter the number of stages: '))
    #         specific_impulse = int(input('Enter the specific impulse (secs): '))

    #     except Exception as e:
    #         raise
    #     else:
    #         pass
    #     finally:
    #         pass

    #     try:
    #         mass_payload = int(input('Enter payload mass (kg): '))

    #     except Exception as e:
    #         raise
    #     else:
    #         pass
    #     finally:
    #         pass

    #     if number_of_stages is None or number_of_stages == '':
    #         break

    #     if mass_payload == 0:
    #         print('Payload mass is zero. Delta V will calculate without a payload')

    #     for stage_add_data in range(number_of_stages):
    #         print('*** Stage - {} ***'.format(stage_add_data + 1))

    #         mass_struct = int(input('Enter structure mass (kg): '))
    #         mass_prop = int(input('Enter propellant mass (kg): '))
            # specific_impulse = int(input('Enter specific impulse for
            #                               engine (sec): '))
    #         mass_stage.append([mass_struct,
    #                            mass_prop,
    #                            specific_impulse,
                               # ])

    #         print('*** TEST *** mass_stage >>>', mass_stage[stage_add_data])

    #     print('payload mass (kg):', mass_payload)
    #     break
    #
    #
###############################################################################

####### Input data for calculations during build phase #################

    # Mass for each stage

    mass_stage = [[5000.0, 50000.0, 450],
                  [5000.0, 50000.0, 450],
                  [3000.0, 50000.0, 450],
                  ]

    mass_payload = 5000.0
    specific_impulse = 450
    number_of_stages = 2

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

        mass_initial = 0.0
        mass_final = 0.0

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

        print('Stage {} Mass Initial: {}'.format(delta_v_stage_number,
                                                 mass_initial))
        print('Stage {} Mass Final: {}'.format(delta_v_stage_number,
                                               mass_final))
        print('Stage {} V Exhaust: {}'.format(delta_v_stage_number,
                                              v_exhaust))

        delta_v_data.append(delta_v_calc(mass_initial,
                                         mass_final,
                                         v_exhaust,
                                         ))

        print('=' * 40)

    print('delta_v_data:')

    stage_ = 1
    for _ in delta_v_data:
        print('Delta V for stage {}: {}'.format(stage_, _))
        stage_ += 1

    print('Total Delta V: {}'.format(sum(delta_v_data)))

    help(delta_v_calc)
