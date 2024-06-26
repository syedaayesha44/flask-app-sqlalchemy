import os
import cv2
import numpy as np
from models import Image

def perform_visual_search(uploaded_image, app):
    try:
        # Save the uploaded image temporarily
        temp_image_path = os.path.join(app.config['UPLOAD_FOLDER'], 'temp_image.jpg')
        uploaded_image.save(temp_image_path)

        # Read the uploaded image
        query_image = cv2.imread(temp_image_path, cv2.IMREAD_COLOR)

        if query_image is None:
            raise Exception("Failed to read uploaded image.")

        # Retrieve images from the database
        images = Image.query.all()
        if not images:
            raise Exception("No images found in the database.")

        # Initialize SIFT feature detector
        sift = cv2.SIFT_create()

        # Extract keypoints and descriptors from the query image
        kp1, des1 = sift.detectAndCompute(query_image, None)

        if des1 is None:
            raise Exception("Failed to extract features from the query image.")

        # Initialize list to store similarity scores and corresponding images
        similarities = []

        for img in images:
            # Read image from the database
            db_image_path = os.path.join(app.config['UPLOAD_FOLDER'], img.path)
            db_image = cv2.imread(db_image_path, cv2.IMREAD_COLOR)

            if db_image is None:
                continue

            # Extract keypoints and descriptors from the database image
            kp2, des2 = sift.detectAndCompute(db_image, None)

            if des2 is None:
                continue

            # Match features between query image and database image
            bf = cv2.BFMatcher()
            matches = bf.knnMatch(des1, des2, k=2)

            # Apply ratio test to select good matches
            good_matches = [m for m, n in matches if m.distance < 0.75 * n.distance]

            # Compute similarity score based on the number of good matches
            similarity_score = len(good_matches)
            similarities.append((similarity_score, img))

        # Sort images based on similarity score in descending order
        similarities = sorted(similarities, key=lambda x: x[0], reverse=True)

        # Get the top results (e.g., top 5 most similar images)
        top_results = [(img.path, img.flipkart_url) for score, img in similarities[:5]]

        # Debugging: Print paths of the top results
        print("Top results:")
        for path, url in top_results:
            print(f"Path: {path}, URL: {url}")

        return top_results

    except Exception as e:
        print(f"Error in perform_visual_search: {e}")
        return []
