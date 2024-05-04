# video_processor.py
import cv2
import numpy as np
import hashlib
import secrets
import logging

def get_stream_url(youtube_url):
    import streamlink
    streams = streamlink.streams(youtube_url)
    return streams['best'].url

def setup_background_subtractor():
    return cv2.createBackgroundSubtractorMOG2(history=500, varThreshold=16, detectShadows=True)

def process_video(stream_url):
    cap = cv2.VideoCapture(stream_url)
    if not cap.isOpened():
        return {"error": "Error opening video stream."}, None

    back_sub = setup_background_subtractor()
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
    entropy_pool = bytearray()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        fg_mask = back_sub.apply(gray)
        fg_mask = cv2.morphologyEx(fg_mask, cv2.MORPH_OPEN, kernel)
        
        contours, _ = cv2.findContours(fg_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for contour in contours:
            x, y, w, h = cv2.boundingRect(contour)
            entropy_pool.extend(x.to_bytes(2, 'big'))
            entropy_pool.extend(y.to_bytes(2, 'big'))
            entropy_pool.extend(w.to_bytes(2, 'big'))
            entropy_pool.extend(h.to_bytes(2, 'big'))

        if len(entropy_pool) > 1024:
            random_number = generate_random_number(entropy_pool)
            cap.release()
            cv2.destroyAllWindows()
            return {"random_number": random_number}, random_number

    cap.release()
    cv2.destroyAllWindows()
    return {"error": "No random number generated"}, None

def generate_random_number(entropy_pool):
    hash_digest = hashlib.sha256(entropy_pool).digest()
    seed = int.from_bytes(hash_digest, 'big')
    secrets_generator = secrets.SystemRandom(seed)
    return secrets_generator.randint(0, 100)
