import pickle

# Assuming rf_model is your trained Random Forest model
with open("rf_model.pkl", "wb") as file:
    pickle.dump(rf_model, file)

print("✅ Model saved successfully as rf_model.pkl")
