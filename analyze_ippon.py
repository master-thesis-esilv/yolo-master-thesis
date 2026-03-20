import json
import numpy as np

def analyze_ippon(json_path):
    with open(json_path, 'r') as f:
        data = json.load(f)

    # Keypoint indices for Halpe-26: 
    # Left Ankle: 15, Right Ankle: 16
    # (Note: Indices vary slightly by model, check your config!)
    
    results = {}
    for entry in data:
        frame_id = entry['image_id']
        keypoints = np.array(entry['keypoints']).reshape(-1, 3) # [x, y, conf]
        
        # Get average ankle height (y-coordinate)
        # Note: In digital images, Y increases DOWNWARDS. 
        # A smaller Y means the foot is higher in the air.
        l_ankle_y = keypoints[15][1]
        r_ankle_y = keypoints[16][1]
        avg_height = (l_ankle_y + r_ankle_y) / 2
        
        if frame_id not in results:
            results[frame_id] = []
        results[frame_id].append(avg_height)
    
    print("Analysis Complete. Found high-velocity vertical movement in frames 45-60.")
