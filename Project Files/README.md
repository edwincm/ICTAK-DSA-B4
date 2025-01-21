**Presentation**: https://docs.google.com/presentation/d/1AEaI9lVbqU_xhv163zH2GDnIafGNmMkHIycHAjqe0qc/edit?usp=sharing

**Hosting**: https://fifa-player-performance.streamlit.app

**Dataset**: FIFA17_official_data.csv

# Abstract

This project presents a comprehensive implementation of a Football Player Performance Prediction System, leveraging advanced machine learning and interactive tools to deliver actionable insights into player attributes and performance. The system integrates a Random Forest Regressor model trained on real-world football data to predict a player’s overall rating based on key attributes, such as physical, mental, and technical scores.

The project incorporates a Flask-based backend for model hosting and prediction services and a responsive, user-friendly Streamlit front-end interface for interaction. 

Key features include:
- Feature Engineering: Attributes like Physical, Passing, Mental, and Shooting Scores are dynamically computed based on individual metrics, enhancing the model’s interpretability and prediction accuracy.
- Machine Learning Model: The Random Forest Regressor, optimized through cross-validation and hyperparameter tuning, ensures robust and accurate predictions, achieving high R², low Mean Absolute Error (MAE), and low Mean Squared Error (MSE).
- CI/CD Pipeline (Partial): Automated deployment pipelines enable seamless integration, testing, and deployment of updates on platforms like Docker and Google Cloud Platform (GCP).
- Interactive Interface: The Streamlit application allows users to input player attributes and visualize predictions.

This project showcases the potential of AI-driven decision-making tools in enhancing player scouting, team selection, and performance analysis in the football industry. The application is designed to be scalable, modular, and accessible, providing a template for similar predictive analytics projects in other domains.
