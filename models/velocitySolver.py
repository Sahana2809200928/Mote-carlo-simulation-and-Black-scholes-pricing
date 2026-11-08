from sphereDensityFinder import radius

def appendAB(ABValues, radius, Density):

    fluidDensity = 1261
    viscosity = 1.3
    g = 9.81

    for a, sphereDensity in zip(radius, Density):

        A = g * (1 - fluidDensity / sphereDensity)

        B = (9 * viscosity) / (2 * sphereDensity * a**2)

        ABValues.append((A, B))

    return ABValues


def euler_method(A, B, h, total_time):

    velocity = 0.0
    time = 0.0

    times = [time]
    velocities = [velocity]

    while time < total_time:

        velocity = velocity + h * (A - B * velocity)

        time = time + h

        times.append(time)
        velocities.append(velocity)

    return times, velocities