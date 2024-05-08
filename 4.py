import cv2
def detect_motion(video_path):
    cap = cv2.VideoCapture(video_path)
    motion_detector = cv2.createBackgroundSubtractorMOG2()
    motion_timings = []
    motion_count = 0
    motion_threshold = 500
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        fgmask = motion_detector.apply(frame)
        motion_pixels = cv2.countNonZero(fgmask)
        if motion_pixels > motion_threshold:
            motion_count += 1
            temp = cap.get(cv2.CAP_PROP_POS_MSEC)
            motion_timings.append(temp)

        elif motion_count >= 2:
            break


    cap.release()
    return motion_timings, motion_count

def convert_millis_to_minutes(millis):
    minutes = round((millis / (10)) / 60, 3)
    seconds = round((millis / 1000) % 60, 3)
    return minutes, seconds

video_path = "'E:\\san\\input_video 2.mp4'"
motion_timings, motion_count = detect_motion(video_path)

if len(motion_timings) >= 2:
    print("Motion events detected in the video:")
    for timing in motion_timings:
        minutes, seconds = convert_millis_to_minutes(timing)
        print(f"Output: Motion detected at {minutes} minutes and {seconds} seconds")
else:
    print("Not enough motion events detected in the video.")