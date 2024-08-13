def calculate_dose(start, stop, end_interval, amount):
    '''
    This function calculates the complete dose of a medication or fluid in the
    interval start - stop. If stop > end_interval, the dose of the interval
    start - end_interval is calculated. Complete dose is given in ml for fluids
    and in microgram for norepinephrine. In case of stop < end_interval, the
    complete dose should equal the corresponding value of the "fluidin" row
    (fluids) or the "administered" row (norepinephrine). In case of stop >
    end_interval, the complete dose will be smaller than the corresponding
    value of the "fluidin" or "administered" row.

    start: Timestamp of the beginning of infusion in ms
    stop: Timestamp of stop of infusion in ms
    end_interval: End of interval in ms
    amount: value from the "fluidin" or "administered" row
    '''
    try:
        int(start)
        int(stop)
        int(end_interval)
        float(amount)
    except ValueError as exc:
        raise ValueError("All input values must be numbers") from exc

    # Dose is given before end of timeframe or
    # over the end of timeframe or
    # after the timeframe:
    if start < end_interval:
        if stop <= end_interval:
            return amount
        if stop > end_interval:
            return round((end_interval - start) / (stop - start) * amount, 2)
    return 0.0
