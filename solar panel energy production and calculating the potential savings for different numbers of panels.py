import pandas as pd
import pvlib
import time
import os

from prices_aux import panels_iguais_df
from AC_helper import yearly_consum_Wh
from CONSUMPTION_FUNC import profile

def sm(num):
    start_time = time.time()

    native_times = pd.date_range(start='1999-01-01', end='2019-01-01', freq='1h')
    timezone = 'Etc/GMT-5'
    latitude = 41.1496100
    longitude = -8.6109900
    City = 'Porto'

    newpath = f'C:\\Users\\Diogo Sá\\Desktop\\perkier tech\\Energy\\Final_Calcs\\{City}'
    os.makedirs(newpath, exist_ok=True)  # This will create the directory if it doesn't exist

    altitude = 7

    # Retrieve module data
    sandia_modules = pvlib.pvsystem.retrieve_sam('SandiaMod')

    # Initialize dictionaries
    module = {}
    system = {}

    for i in range(len(panels_iguais_df)):
        module[i] = sandia_modules[panels_iguais_df.iloc[i]['Sandia_Name']]
        system[i] = {'module': module[i], 'inverter': inverter}

    # Define system parameters
    system['surface_tilt'] = latitude
    system['surface_azimuth'] = 180

    # Calculate solar position
    times = native_times.tz_localize(timezone)
    solpos = pvlib.solarposition.get_solarposition(times, latitude, longitude)

    # Calculate irradiance
    dni_extra = pvlib.irradiance.get_extra_radiation(times)
    airmass = pvlib.atmosphere.get_relative_airmass(solpos['apparent_zenith'])
    pressure = pvlib.atmosphere.alt2pres(altitude)
    am_abs = pvlib.atmosphere.get_absolute_airmass(airmass, pressure)
    tl = 2
    cs = pvlib.clearsky.ineichen(solpos['apparent_zenith'], am_abs, tl,
                                 dni_extra=dni_extra, altitude=altitude)

    # Calculate total irradiance
    aoi = pvlib.irradiance.aoi(system['surface_tilt'], system['surface_azimuth'],
                               solpos['apparent_zenith'], solpos['azimuth'])
    total_irrad = pvlib.irradiance.get_total_irradiance(system['surface_tilt'], system['surface_azimuth'],
                                                        solpos['apparent_zenith'], solpos['azimuth'], cs['dni'],
                                                        cs['ghi'], cs['dhi'],
                                                        dni_extra=dni_extra, model='haydavies')

    # Calculate temperatures
    temps = pvlib.pvsystem.sapm_celltemp(total_irrad['poa_global'], wind_speed, temp_air)

    # Initialize result dictionaries
    annual_energy = {}
    recommended_panels = {}
    savings_array = {}
    savings_array_more = {}
    Price_euro_kWh = 0.2284

    for i in range(len(module)):
        effective_irradiance = pvlib.pvsystem.sapm_effective_irradiance(total_irrad['poa_direct'],
                                                                        total_irrad['poa_diffuse'], am_abs, aoi, module[i])

        dc = pvlib.pvsystem.sapm(effective_irradiance, temps['temp_cell'], module[i])
        ac = pvlib.pvsystem.snlinverter(dc['v_mp'], dc['p_mp'], inverter)

        annual_energy[i] = ac.sum() / 20
        recommended_panels[i] = int(yearly_consum_Wh / annual_energy[i]) + num
        savings_array[i] = ac.sum() * Price_euro_kWh / 1000 - panels_iguais_df.iloc[i]['Price']
        savings_array_more[i] = (ac.sum() * recommended_panels[i] * Price_euro_kWh / 1000) - \
                                (panels_iguais_df.iloc[i]['Price'] * recommended_panels[i])

    # Create DataFrame for results
    energ_pd = pd.DataFrame({'Module': panels_iguais_df['Panel_Name'],
                             'Sandia_Name': panels_iguais_df['Sandia_Name'],
                             'Module_Price': panels_iguais_df['Price'],
                             'Power': panels_iguais_df['Power'],
                             'Yearly Prod. (W hr)': pd.Series(annual_energy),
                             'Savings': pd.Series(savings_array),
                             'Recomended_Panels': pd.Series(recommended_panels),
                             'Recom_Panels_Savings': pd.Series(savings_array_more)})

    # Sort DataFrame by recommended panels savings
    energ_pd = energ_pd.sort_values(by='Recom_Panels_Savings', ascending=False).reset_index(drop=True)

    print(energ_pd)

    # Calculate execution time
    print("--- %s seconds ---" % (time.time() - start_time))

    # Write results to CSV
    profile_bill = profile['Bill']
    energ_pd.to_csv(f'C:\\Users\\Diogo Sá\\Desktop\\perkier tech\\Energy\\Final_Calcs\\{City}\\{profile_bill}euro__panels_{num}.csv', index=False, header=True)

# Call the function with different values of 'num'
sm(-1)
sm(0)
sm(1)
