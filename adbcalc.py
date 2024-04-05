def calculate_dose(start, stop, end_interval, dose, intake_type):
    '''
    This function calculates the complete dose of a medication or fluid in the
    interval start - stop. If stop > end_interval, the dose of the interval
    start - end_interval ist calculated. Complete dose is given in ml for
    fluids and in microgram for norepinephrine. In case of stop < end_interval,
    the complete dose should equal the corresponding value of the
    "administered" row. In case of stop > end_interval, the complete dose will
    be smaller than the corresponding value of the "administered" row.

    start: Timestamp of the beginning of infusion in ms
    stop: Timestamp of stop of infusion in ms
    end_interval: End of interval in ms
    dose: value from the "dose" row
    intake_type: 1 - Norepinephrine (mg / h)
                 2 - FLuids (ml / h)
    '''

    try:
        int(start)
    except ValueError as exc:
        raise ValueError("start must be a number") from exc

    try:
        int(stop)
    except ValueError as exc:
        raise ValueError("stop must be a number") from exc

    try:
        int(end_interval)
    except ValueError as exc:
        raise ValueError("end_interval must be a number") from exc

    try:
        int(dose)
    except ValueError as exc:
        raise ValueError("dose must be a number") from exc

    try:
        int(intake_type)
    except ValueError as exc:
        raise ValueError("intake_type must be a number") from exc

    # Select divisor
    #
    # 3600 for norepinephrine (mg per hour to microgram)
    # 3600000 for fluids (ml per hour to mililiters)
    divisor = int

    if intake_type == 1:
        divisor = 3600
    elif intake_type == 2:
        divisor = 3600000

    # Dose is given before end of timeframe or
    # over the end of timeframe or
    # after the timeframe:
    if start < end_interval:
        if stop <= end_interval:
            return round((stop - start) / divisor * dose, 2)
        if stop > end_interval:
            return round((end_interval - start) / divisor * dose, 2)
    return 0.0
