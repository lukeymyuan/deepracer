def reward_function(params):
    
    # Read input parameters
    distance_from_center = params['distance_from_center']
    track_width = params['track_width']
    steering = abs(params['steering_angle']) # Only need the absolute steering angle
    all_wheels_on_track = params['all_wheels_on_track']
    speed = params['speed']

    # Calculate 3 markers that are at varying distances away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the agent is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.5
    elif distance_from_center <= marker_2:
        reward = 0.75
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track


    # Penalize reward if the agent is steering too much
    ABS_STEERING_THRESHOLD = 20
    if steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8
    
    # Penalize if the car goes too slow
    SPEED_THRESHOLD = 1.0
    if speed < SPEED_THRESHOLD:
        reward *= 0.8
    
    # Penalize if the car goes off track
    if not all_wheels_on_track:
        reward = 1e-3

    return float(reward)
